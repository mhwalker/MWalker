#include "MWalker/TrackAnalyzer/interface/FindAndMerge.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/eventSetupGetImplementation.h"
#include "FWCore/Framework/interface/TriggerNamesService.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/Common/interface/AssociationMap.h"
#include "DataFormats/Common/interface/OneToOne.h"
#include "SimDataFormats/Track/interface/SimTrackContainer.h"
#include "SimDataFormats/Vertex/interface/SimVertexContainer.h"
#include "SimTracker/TrackAssociation/interface/TrackAssociatorByChi2.h"
#include "SimTracker/TrackAssociation/interface/TrackAssociatorByHits.h"
#include "SimTracker/TrackerHitAssociation/interface/TrackerHitAssociator.h"
#include "SimTracker/Records/interface/TrackAssociatorRecord.h"
#include "SimDataFormats/TrackingAnalysis/interface/TrackingParticle.h"
#include "SimDataFormats/TrackingAnalysis/interface/TrackingVertex.h"
#include "SimDataFormats/TrackingAnalysis/interface/TrackingVertexContainer.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "SimDataFormats/EncodedEventId/interface/EncodedEventId.h"
#include "TrackingTools/TrajectoryState/interface/FreeTrajectoryState.h"
#include "TrackingTools/PatternTools/interface/TSCBLBuilderNoMaterial.h"
#include "TrackingTools/PatternTools/interface/TwoTrackMinimumDistance.h"
#include "TrackingTools/TrajectoryState/interface/TrajectoryStateOnSurface.h"
#include "TrackingTools/TrajectoryState/interface/TrajectoryStateTransform.h"
#include <TrackingTools/PatternTools/interface/TSCPBuilderNoMaterial.h>
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"
#include "DataFormats/TrackCandidate/interface/TrackCandidate.h"

#include <functional>
#include <sstream>
#include <iostream>
using namespace edm;
using namespace reco;

typedef math::XYZTLorentzVectorD LorentzVector;
typedef math::XYZVector Vector;
typedef math::XYZPoint Point;

using namespace std;

MWFindAndMerge::MWFindAndMerge(const edm::ParameterSet& iPara) : merger_(iPara)
{
  m_totalEvents = 0;
  m_outFile = 0;
  m_source = "generalTracks";
  m_associatorName = "TrackAssociatorByHits";
  m_produceDuplicates = true;
  m_minMissingOuterHitsFromInner = 2;
  m_minDeltaR3d = -4.0;
  m_minAvgRho = 15.0;
  m_minBDTG = -0.96;
  //m_simSource = "mergedtruth";
  if(iPara.exists("nMissingOuterFromInner")) m_minMissingOuterHitsFromInner = iPara.getParameter<int>("nMissingOuterFromInner");
  if(iPara.exists("minDeltaR3d"))m_minDeltaR3d = iPara.getParameter<double>("minDeltaR3d");
  if(iPara.exists("minAvgRho"))m_minAvgRho = iPara.getParameter<double>("minAvgRho");
  if(iPara.exists("minBDTG"))m_minBDTG = iPara.getParameter<double>("minBDTG");
  if(iPara.exists("outfile"))m_outFile = new TFile(iPara.getParameter<string>("outfile").c_str(),"RECREATE");
  if(iPara.exists("source"))m_source = iPara.getParameter<string>("source");
  if(iPara.exists("simSource"))m_simSource = iPara.getParameter<InputTag>("simSource");
  if(iPara.exists("associator"))m_associatorName = iPara.getParameter<string>("associator");
  if(iPara.exists("produceDuplicates"))m_produceDuplicates = iPara.getParameter<bool>("produceDuplicates");


  m_duplicatesMerged_eta = new TH1F("duplicate_merged_eta","",300,-3.0,3.0);
  m_combMerged_eta = new TH1F("comb_merged_eta","",300,-3.0,3.0);
  produces<std::vector<TrackCandidate> >("duplicateCandidates"); 
  produces<std::vector<TrackCandidate> >("combinatoricCandidates");
  //produces<std::vector<DuplicateRecord> >("duplicateRecords");
  //produces<std::vector<DuplicateRecord> >("combinatoricRecords");


  m_tmvaReader = new TMVA::Reader("!Color:Silent");
  m_tmvaReader->AddVariable("ddsz:=inner_dsz-outer_dsz",&m_tmva_ddsz);
  m_tmvaReader->AddVariable("ddxy:=inner_dxy-outer_dxy",&m_tmva_ddxy);
  m_tmvaReader->AddVariable("dphi:=inner_phi-outer_phi",&m_tmva_dphi);
  m_tmvaReader->AddVariable("dlambda:=inner_lambda-outer_lambda",&m_tmva_dlambda);
  m_tmvaReader->AddVariable("dqoverp:=inner_qoverp-outer_qoverp",&m_tmva_dqoverp);
  m_tmvaReader->AddVariable("delta3d_r:=sqrt(delta3d_x*delta3d_x+delta3d_y*delta3d_y)",&m_tmva_d3dr);
  m_tmvaReader->AddVariable("delta3d_z",&m_tmva_d3dz);
  m_tmvaReader->AddVariable("outer_nMissingInner",&m_tmva_outer_nMissingInner);
  m_tmvaReader->AddVariable("inner_nMissingOuter",&m_tmva_inner_nMissingOuter);
  m_tmvaReader->BookMVA("BDTG","TRACKSV01/weights/TMVARegression_BDTG.weights.xml");


}
//------------------------------------------------------------
//------------------------------------------------------------
MWFindAndMerge::~MWFindAndMerge()
{
  /* no op */
}
//------------------------------------------------------------
//------------------------------------------------------------
void MWFindAndMerge::beginJob()
{
  m_totalEvents = 0;
  m_nDuplicates = 0;
  m_nDuplicatesGood = 0;
  m_nDuplicatesMerged = 0;
  m_nCombinatorics = 0;
  m_nCombinatoricsGood = 0;
  m_nCombinatoricsMerged = 0;
}

//------------------------------------------------------------
//------------------------------------------------------------
void MWFindAndMerge::endJob()
{
  m_outFile->cd();
  m_duplicatesMerged_eta->Write();
  m_combMerged_eta->Write();
  m_outFile->Close();

  cout<<"agrdl duplicates: "<<m_nDuplicates<<" good: "<<m_nDuplicatesGood<<" merged: "<<m_nDuplicatesMerged<<endl;
  cout<<"agrdl combinatorics: "<<m_nCombinatorics<<" good: "<<m_nCombinatoricsGood<<" merged: "<<m_nCombinatoricsMerged<<endl;
}
//------------------------------------------------------------
//------------------------------------------------------------
void MWFindAndMerge::beginRun(const edm::Run& iRun, const edm::EventSetup& iSetup)
{
  cout<<"find and merge beginrun"<<endl;
}
//------------------------------------------------------------
//------------------------------------------------------------
void MWFindAndMerge::endRun(const edm::Run& iRun, const edm::EventSetup& iSetup)
{
  /* no op */
}
//------------------------------------------------------------
//------------------------------------------------------------
void MWFindAndMerge::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  m_totalEvents++;

  edm::ESHandle<TrackAssociatorBase> theAssociator;
  iSetup.get<TrackAssociatorRecord>().get(m_associatorName,theAssociator);

  m_associator = theAssociator.product();
  iSetup.get<IdealMagneticFieldRecord>().get(m_magfield);


  auto_ptr<vector<TrackCandidate> > out_duplicateCandidates(new vector<TrackCandidate>());
  auto_ptr<vector<TrackCandidate> > out_combinatoricCandidates(new vector<TrackCandidate>());
  //auto_ptr<vector<DuplicateRecord> > out_duplicateRecords(new vector<DuplicateRecord>());
  //auto_ptr<vector<DuplicateRecord> > out_combinatoricRecords(new vector<DuplicateRecord>());
  edm::Handle<View<Track> >handle;
  iEvent.getByLabel(m_source,handle);
  edm::Handle<TrackingParticleCollection>  simTPhandle;
  iEvent.getByLabel(m_simSource,simTPhandle);
  const TrackingParticleCollection simTracks = *(simTPhandle.product());

  reco::RecoToSimCollection recSimColl;
  reco::SimToRecoCollection simRecColl;

  merger_.init(iSetup);

  //recSimColl = m_associator->associateRecoToSim(handle,simTPhandle,&iEvent,&iSetup);


  simRecColl = m_associator->associateSimToReco(handle,simTPhandle,&iEvent,&iSetup);

  TwoTrackMinimumDistance ttmd;
  TSCPBuilderNoMaterial tscpBuilder;
  //TrajectoryStateTransform transformer;
  //AssociationMap<OneToOne<vector<Track>,vector<Track> > > matchedTracks;
  map<Track,Track,trackCompare> matchedTracks;
  for(int i = 0; i < (int)simTracks.size(); i++){
    TrackingParticleRef tpr(simTPhandle, i);
    TrackingParticle* tp=const_cast<TrackingParticle*>(tpr.get());
    if(simRecColl.find(tpr) == simRecColl.end())continue;
    vector<pair<RefToBase<Track>, double> > rt = (std::vector<std::pair<RefToBase<Track>, double> >) simRecColl[tpr];
    if(rt.size() == 0)continue;
    if(tp->p4().Rho() < 1.0)continue;
    int nGoodPt = 0;
    for(int j = 0; j < (int)rt.size(); j++){
      if((rt[j].first)->innerMomentum().Rho() > 1.0)nGoodPt++;
    }

    if(nGoodPt < 2)continue;
    for(int j = 0; j < (int)rt.size(); j++){
      if((rt[j].first)->innerMomentum().Rho() < 1.0)continue;
      for(int k = j+1; k < (int)rt.size(); k++){
	if((rt[k].first)->innerMomentum().Rho() < 1.0)continue;
	
	m_nDuplicates++;
	Track t1,t2;

	
	if((rt[j].first)->outerPosition().Rho() < (rt[k].first)->outerPosition().Rho()){
	  t1 = *(rt[j].first);
	  t2 = *(rt[k].first);
	}else{
	  t1 = *(rt[k].first);
	  t2 = *(rt[j].first);
	}
	
	double deltaR3d = sqrt(pow(t1.outerPosition().x()-t2.innerPosition().x(),2) + pow(t1.outerPosition().y()-t2.innerPosition().y(),2) + pow(t1.outerPosition().z()-t2.innerPosition().z(),2));
	
	if(t1.outerPosition().Rho() > t2.innerPosition().Rho())deltaR3d *= -1.0;

	//TrackRef tr1 = t1;
	//TrackRef tr2 = t2;
	
	GlobalPoint avgPoint((t1.outerPosition().x()+t2.innerPosition().x())*0.5,(t1.outerPosition().y()+t2.innerPosition().y())*0.5,(t1.outerPosition().z()+t2.innerPosition().z())*0.5);
	
	matchedTracks.insert(pair<Track,Track>(t2,t1));
	matchedTracks.insert(pair<Track,Track>(t1,t2));

	
	if(deltaR3d < m_minDeltaR3d)continue;
	if(t1.trackerExpectedHitsOuter().numberOfLostHits() < m_minMissingOuterHitsFromInner)continue;
	if(sqrt(pow(0.5*(t1.outerPosition().x()+t2.innerPosition().x()),2) + pow(0.5*(t1.outerPosition().y()+t2.innerPosition().y()),2)) < m_minAvgRho) continue;

	FreeTrajectoryState fts1 = trajectoryStateTransform::initialFreeState(t1, &*m_magfield);
	FreeTrajectoryState fts2 = trajectoryStateTransform::initialFreeState(t2, &*m_magfield);
	TrajectoryStateClosestToPoint TSCP1 = tscpBuilder(fts1, avgPoint);
	TrajectoryStateClosestToPoint TSCP2 = tscpBuilder(fts2, avgPoint);
	
	if(!TSCP1.isValid())continue;
	if(!TSCP2.isValid())continue;

	double qoverp1 = TSCP1.theState().signedInverseMomentum();
	double phi1 = TSCP1.theState().momentum().phi();
	double lambda1 =  M_PI/2 - TSCP1.theState().momentum().theta();
	double dxy1 = (-TSCP1.theState().position().x() * TSCP1.theState().momentum().y() + TSCP1.theState().position().y() * TSCP1.theState().momentum().x())/TSCP1.pt();
	double dsz1 = TSCP1.theState().position().z() * TSCP1.pt() / TSCP1.momentum().mag() - (TSCP1.theState().position().x() * TSCP1.theState().momentum().y() + TSCP1.theState().position().y() * TSCP1.theState().momentum().x())/TSCP1.pt() * TSCP1.theState().momentum().z()/TSCP1.theState().momentum().mag();

	double qoverp2 = TSCP2.theState().signedInverseMomentum();
	double phi2 = TSCP2.theState().momentum().phi();
	double lambda2 =  M_PI/2 - TSCP2.theState().momentum().theta();
	double dxy2 = (-TSCP2.theState().position().x() * TSCP2.theState().momentum().y() + TSCP2.theState().position().y() * TSCP2.theState().momentum().x())/TSCP2.pt();
	double dsz2 = TSCP2.theState().position().z() * TSCP2.pt() / TSCP2.momentum().mag() - (TSCP2.theState().position().x() * TSCP2.theState().momentum().y() + TSCP2.theState().position().y() * TSCP2.theState().momentum().x())/TSCP2.pt() * TSCP2.theState().momentum().z()/TSCP2.theState().momentum().mag();
	
	m_tmva_ddsz = dsz1-dsz2;
	m_tmva_ddxy = dxy1-dxy2;
	m_tmva_dphi = phi1-phi2;
	m_tmva_dlambda = lambda1-lambda2;
	m_tmva_dqoverp = qoverp1-qoverp2;
	m_tmva_d3dr = avgPoint.perp();
	m_tmva_d3dz = avgPoint.z();
	m_tmva_outer_nMissingInner = t2.trackerExpectedHitsInner().numberOfLostHits();
	m_tmva_inner_nMissingOuter = t1.trackerExpectedHitsOuter().numberOfLostHits();

	double mvaBDTG = m_tmvaReader->EvaluateMVA("BDTG");
	//cout<<mvaBDTG<<endl;
	if(mvaBDTG < m_minBDTG)continue;


	//if(t1.trackerExpectedHitsOuter().numberOfLostHits() + t2.trackerExpectedHitsInner().numberOfLostHits() < 3)continue;
	m_nDuplicatesGood++;
	
	TrackCandidate mergedTrack = merger_.merge(t1,t2);
	out_duplicateCandidates->push_back(mergedTrack);
	//DuplicateRecord duprec;
	pair<Track,Track> trackpair(t1,t2);
	//duprec.recoTracks = trackpair;
	//duprec.simulationTrack = tpr;
	//out_duplicateRecords->push_back(duprec);


	if(mergedTrack.recHits().second - mergedTrack.recHits().first > 0){
	  m_nDuplicatesMerged++;
	  //m_duplicatesMerged_eta->Fill(mergedTrack.seed()
	}
	/*
	  FreeTrajectoryState fts1 = trajectoryStateTransform::initialFreeState(t1, &*m_magfield);
	FreeTrajectoryState fts2 = trajectoryStateTransform::initialFreeState(t2, &*m_magfield);
	TrajectoryStateClosestToPoint TSCP1 = tscpBuilder(fts1, avgPoint);
	TrajectoryStateClosestToPoint TSCP2 = tscpBuilder(fts2, avgPoint);
	
	if(!TSCP1.isValid())continue;
	if(!TSCP2.isValid())continue;
	double e1_0 = TSCP1.theState().curvilinearError().matrix().At(0,0);
	double e1_1 = TSCP1.theState().curvilinearError().matrix().At(1,1);
	double e1_2 = TSCP1.theState().curvilinearError().matrix().At(2,2);
	double e1_3 = TSCP1.theState().curvilinearError().matrix().At(3,3);
	double e1_4 = TSCP1.theState().curvilinearError().matrix().At(4,4);
	double e2_0 = TSCP2.theState().curvilinearError().matrix().At(0,0);
	double e2_1 = TSCP2.theState().curvilinearError().matrix().At(1,1);
	double e2_2 = TSCP2.theState().curvilinearError().matrix().At(2,2);
	double e2_3 = TSCP2.theState().curvilinearError().matrix().At(3,3);
	double e2_4 = TSCP2.theState().curvilinearError().matrix().At(4,4);

	double qoverp1 = TSCP1.theState().signedInverseMomentum();
	double phi1 = TSCP1.theState().momentum().phi();
	double lambda1 =  M_PI/2 - TSCP1.theState().momentum().theta();
	double dxy1 = (-TSCP1.theState().position().x() * TSCP1.theState().momentum().y() + TSCP1.theState().position().y() * TSCP1.theState().momentum().x())/TSCP1.pt();
	double dsz1 = TSCP1.theState().position().z() * TSCP1.pt() / TSCP1.momentum().mag() - (TSCP1.theState().position().x() * TSCP1.theState().momentum().y() + TSCP1.theState().position().y() * TSCP1.theState().momentum().x())/TSCP1.pt() * TSCP1.theState().momentum().z()/TSCP1.theState().momentum().mag();

	double qoverp2 = TSCP2.theState().signedInverseMomentum();
	double phi2 = TSCP2.theState().momentum().phi();
	double lambda2 =  M_PI/2 - TSCP2.theState().momentum().theta();
	double dxy2 = (-TSCP2.theState().position().x() * TSCP2.theState().momentum().y() + TSCP2.theState().position().y() * TSCP2.theState().momentum().x())/TSCP2.pt();
	double dsz2 = TSCP2.theState().position().z() * TSCP2.pt() / TSCP2.momentum().mag() - (TSCP2.theState().position().x() * TSCP2.theState().momentum().y() + TSCP2.theState().position().y() * TSCP2.theState().momentum().x())/TSCP2.pt() * TSCP2.theState().momentum().z()/TSCP2.theState().momentum().mag();
	*/
      }
    }
  }


  for(int i = 0; i < (int)handle->size(); i++){
    Track rt1 = (handle->at(i));
    if(rt1.innerMomentum().Rho() < 1.0)continue;
    for(int j = i+1; j < (int)handle->size();j++){
      Track rt2 = (handle->at(j));
      if(rt2.innerMomentum().Rho() < 1.0)continue;
      if(rt1.charge() != rt2.charge())continue;
      if(matchedTracks.find(rt1) != matchedTracks.end() && compareTracks(matchedTracks[rt1],rt2))continue;
      m_nCombinatorics++;
	Track t1,t2;
	if(rt1.outerPosition().Rho() < rt2.outerPosition().Rho()){
	  t1 = rt1;
	  t2 = rt2;
	}else{
	  t1 = rt2;
	  t2 = rt1;
	}

	double deltaR3d = sqrt(pow(t1.outerPosition().x()-t2.innerPosition().x(),2) + pow(t1.outerPosition().y()-t2.innerPosition().y(),2) + pow(t1.outerPosition().z()-t2.innerPosition().z(),2));

	if(t1.outerPosition().Rho() > t2.innerPosition().Rho())deltaR3d *= -1.0;
	if(deltaR3d < m_minDeltaR3d)continue;
	if(t1.trackerExpectedHitsOuter().numberOfLostHits() + t2.trackerExpectedHitsInner().numberOfLostHits() < m_minMissingOuterHitsFromInner)continue;
	if(sqrt(pow(0.5*(t1.outerPosition().x()+t2.innerPosition().x()),2) + pow(0.5*(t1.outerPosition().y()+t2.innerPosition().y()),2)) < m_minAvgRho) continue;
	FreeTrajectoryState fts1 = trajectoryStateTransform::initialFreeState(t1, &*m_magfield);
	FreeTrajectoryState fts2 = trajectoryStateTransform::initialFreeState(t2, &*m_magfield);
	GlobalPoint avgPoint((t1.outerPosition().x()+t2.innerPosition().x())*0.5,(t1.outerPosition().y()+t2.innerPosition().y())*0.5,(t1.outerPosition().z()+t2.innerPosition().z())*0.5);
	TrajectoryStateClosestToPoint TSCP1 = tscpBuilder(fts1, avgPoint);
	TrajectoryStateClosestToPoint TSCP2 = tscpBuilder(fts2, avgPoint);
	if(!TSCP1.isValid())continue;
	if(!TSCP2.isValid())continue;
	      
	double qoverp1 = TSCP1.theState().signedInverseMomentum();
	double phi1 = TSCP1.theState().momentum().phi();
	double lambda1 =  M_PI/2 - TSCP1.theState().momentum().theta();
	double dxy1 = (-TSCP1.theState().position().x() * TSCP1.theState().momentum().y() + TSCP1.theState().position().y() * TSCP1.theState().momentum().x())/TSCP1.pt();
	double dsz1 = TSCP1.theState().position().z() * TSCP1.pt() / TSCP1.momentum().mag() - (TSCP1.theState().position().x() * TSCP1.theState().momentum().y() + TSCP1.theState().position().y() * TSCP1.theState().momentum().x())/TSCP1.pt() * TSCP1.theState().momentum().z()/TSCP1.theState().momentum().mag();
	
	double qoverp2 = TSCP2.theState().signedInverseMomentum();
	double phi2 = TSCP2.theState().momentum().phi();
	double lambda2 =  M_PI/2 - TSCP2.theState().momentum().theta();
	double dxy2 = (-TSCP2.theState().position().x() * TSCP2.theState().momentum().y() + TSCP2.theState().position().y() * TSCP2.theState().momentum().x())/TSCP2.pt();
	double dsz2 = TSCP2.theState().position().z() * TSCP2.pt() / TSCP2.momentum().mag() - (TSCP2.theState().position().x() * TSCP2.theState().momentum().y() + TSCP2.theState().position().y() * TSCP2.theState().momentum().x())/TSCP2.pt() * TSCP2.theState().momentum().z()/TSCP2.theState().momentum().mag();
	
	m_tmva_ddsz = dsz1-dsz2;
	m_tmva_ddxy = dxy1-dxy2;
	m_tmva_dphi = phi1-phi2;
	m_tmva_dlambda = lambda1-lambda2;
	m_tmva_dqoverp = qoverp1-qoverp2;
	m_tmva_d3dr = avgPoint.perp();
	m_tmva_d3dz = avgPoint.z();
	m_tmva_outer_nMissingInner = t2.trackerExpectedHitsInner().numberOfLostHits();
	m_tmva_inner_nMissingOuter = t1.trackerExpectedHitsOuter().numberOfLostHits();
	
	double mvaBDTG = m_tmvaReader->EvaluateMVA("BDTG");
	//cout<<mvaBDTG<<endl;
	if(mvaBDTG < m_minBDTG)continue;
	

	m_nCombinatoricsGood++;

	TrackCandidate mergedTrack = merger_.merge(t1,t2);
	out_combinatoricCandidates->push_back(mergedTrack);
	//DuplicateRecord duprec;
	pair<Track,Track> trackpair(t1,t2);
	//duprec.recoTracks = trackpair;
	//duprec.simulationTrack = tpr;
	//out_duplicateRecords->push_back(duprec);
	//if(!m_produceDuplicates)out->push_back(mergedTrack);
	if(mergedTrack.recHits().second - mergedTrack.recHits().first > 0){
	  m_nCombinatoricsMerged++;
	  //m_duplicatesMerged_eta->Fill(mergedTrack.seed()
	}
	/*
      FreeTrajectoryState fts1 = trajectoryStateTransform::initialFreeState(t1, &*m_magfield);
      FreeTrajectoryState fts2 = trajectoryStateTransform::initialFreeState(t2, &*m_magfield);
      GlobalPoint avgPoint((t1.outerPosition().x()+t2.innerPosition().x())*0.5,(t1.outerPosition().y()+t2.innerPosition().y())*0.5,(t1.outerPosition().z()+t2.innerPosition().z())*0.5);
      TrajectoryStateClosestToPoint TSCP1 = tscpBuilder(fts1, avgPoint);
      TrajectoryStateClosestToPoint TSCP2 = tscpBuilder(fts2, avgPoint);
      if(!TSCP1.isValid())continue;
      if(!TSCP2.isValid())continue;

      double e1_0 = TSCP1.theState().curvilinearError().matrix().At(0,0);
      double e1_1 = TSCP1.theState().curvilinearError().matrix().At(1,1);
      double e1_2 = TSCP1.theState().curvilinearError().matrix().At(2,2);
      double e1_3 = TSCP1.theState().curvilinearError().matrix().At(3,3);
      double e1_4 = TSCP1.theState().curvilinearError().matrix().At(4,4);
      double e2_0 = TSCP2.theState().curvilinearError().matrix().At(0,0);
      double e2_1 = TSCP2.theState().curvilinearError().matrix().At(1,1);
      double e2_2 = TSCP2.theState().curvilinearError().matrix().At(2,2);
      double e2_3 = TSCP2.theState().curvilinearError().matrix().At(3,3);
      double e2_4 = TSCP2.theState().curvilinearError().matrix().At(4,4);
      
      double qoverp1 = TSCP1.theState().signedInverseMomentum();
      double phi1 = TSCP1.theState().momentum().phi();
      double lambda1 =  M_PI/2 - TSCP1.theState().momentum().theta();
      double dxy1 = (-TSCP1.theState().position().x() * TSCP1.theState().momentum().y() + TSCP1.theState().position().y() * TSCP1.theState().momentum().x())/TSCP1.pt();
      double dsz1 = TSCP1.theState().position().z() * TSCP1.pt() / TSCP1.momentum().mag() - (TSCP1.theState().position().x() * TSCP1.theState().momentum().y() + TSCP1.theState().position().y() * TSCP1.theState().momentum().x())/TSCP1.pt() * TSCP1.theState().momentum().z()/TSCP1.theState().momentum().mag();
      
      double qoverp2 = TSCP2.theState().signedInverseMomentum();
      double phi2 = TSCP2.theState().momentum().phi();
      double lambda2 =  M_PI/2 - TSCP2.theState().momentum().theta();
      double dxy2 = (-TSCP2.theState().position().x() * TSCP2.theState().momentum().y() + TSCP2.theState().position().y() * TSCP2.theState().momentum().x())/TSCP2.pt();
      double dsz2 = TSCP2.theState().position().z() * TSCP2.pt() / TSCP2.momentum().mag() - (TSCP2.theState().position().x() * TSCP2.theState().momentum().y() + TSCP2.theState().position().y() * TSCP2.theState().momentum().x())/TSCP2.pt() * TSCP2.theState().momentum().z()/TSCP2.theState().momentum().mag();

      float deltaPhi = phi1-phi2;
      if(fabs(deltaPhi) > M_PI) deltaPhi = 2*M_PI-fabs(deltaPhi);
	*/
    }
  }
  iEvent.put(out_duplicateCandidates,"duplicateCandidates");
  iEvent.put(out_combinatoricCandidates,"combinatoricCandidates");
  //iEvent.put(out_duplicateRecords,"duplicateRecords");
  //iEvent.put(out_combinatoricRecords,"combinatoricRecords");
}
//------------------------------------------------------------
//------------------------------------------------------------
int MWFindAndMerge::numberOfSharedHits(Track t1,Track t2)
{
  trackingRecHit_iterator iter1;
  trackingRecHit_iterator iter2;
  int nshared = 0;
  vector<unsigned int> t1GoodHits;
  for(iter1 = t1.recHitsBegin(); iter1 != t1.recHitsEnd(); iter1++){
    if(!(*iter1)->isValid())continue;
    t1GoodHits.push_back((*iter1)->rawId());
  }
  for(iter2 = t2.recHitsBegin(); iter2 != t2.recHitsEnd(); iter2++){
    if(!(*iter2)->isValid())continue;
    if(find(t1GoodHits.begin(),t1GoodHits.end(),(*iter2)->rawId()) != t1GoodHits.end())nshared++;
  }
  return nshared;
}
//------------------------------------------------------------
//------------------------------------------------------------
float MWFindAndMerge::bestDeltaR(Track t1,Track t2)
{
  Point t1inner = t1.innerPosition();
  Point t1outer = t1.outerPosition();
  Point t2inner = t2.innerPosition();
  Point t2outer = t2.innerPosition();

  //m_duplicate_innerR->Fill(t1inner.Rho(),t2inner.Rho());

  Vector t1p,t2p;
  float d1 = sqrt(pow(t1inner.x()-t2outer.x(),2) + pow(t1inner.y() - t2outer.y(),2) + pow(t1inner.z() - t2outer.z(),2));
  float d2 = sqrt(pow(t2inner.x()-t1outer.x(),2) + pow(t2inner.y() - t1outer.y(),2) + pow(t2inner.z() - t1outer.z(),2));
  if(d1 < d2){
    t1p = t1.innerMomentum();
    t2p = t2.outerMomentum();
    //m_minDelta->Fill(d1);
    //m_duplicate_deltaR->Fill(t1inner.Rho() - t2outer.Rho());
  }else{
    t1p = t1.outerMomentum();
    t2p = t2.innerMomentum();
    //m_minDelta->Fill(d2);
    //m_duplicate_deltaR->Fill(t2inner.Rho() - t1outer.Rho());
  }
  return deltaR(t1p,t2p);

}
//------------------------------------------------------------
//------------------------------------------------------------
bool MWFindAndMerge::compareTracks(Track t1,Track t2)
{
  if(t1.innerPosition() != t2.innerPosition())return false;
  if(t1.outerPosition() != t2.outerPosition())return false;
  if(t1.innerMomentum() != t2.innerMomentum())return false;
  if(t1.outerMomentum() != t2.outerMomentum())return false;
  return true;

}
//------------------------------------------------------------
//------------------------------------------------------------

DEFINE_FWK_MODULE(MWFindAndMerge);
