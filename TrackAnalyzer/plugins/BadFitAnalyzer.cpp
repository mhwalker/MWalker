#include "MWalker/TrackAnalyzer/interface/BadFitAnalyzer.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/eventSetupGetImplementation.h"
#include "FWCore/Framework/interface/TriggerNamesService.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "SimDataFormats/TrackingAnalysis/interface/TrackingParticle.h"
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
#include "DataFormats/TrackReco/interface/TrackResiduals.h"
#include "TMath.h"

#include <functional>
#include <sstream>
#include <iostream>
using namespace edm;
using namespace reco;

typedef math::XYZTLorentzVectorD LorentzVector;
typedef math::XYZVector Vector;
typedef math::XYZPoint Point;

using namespace std;

MWBadFitAnalyzer::MWBadFitAnalyzer(const edm::ParameterSet& iPara)
{
  m_outFile = 0;
  m_source = "generalTracks";
  m_associatorName = "TrackAssociatorByHits";
  m_probCut = 1e-5;

  if(iPara.exists("outfile"))m_outFile = new TFile(iPara.getParameter<string>("outfile").c_str(),"RECREATE");
  if(iPara.exists("source"))m_source = iPara.getParameter<string>("source");
  if(iPara.exists("associator"))m_associatorName = iPara.getParameter<string>("associator");
  if(iPara.exists("simSource"))m_simSource = iPara.getParameter<InputTag>("simSource");
  if(iPara.exists("probCut"))m_probCut = iPara.getParameter<double>("probCut");

  m_nSimAssoc = new TH1F("nSimAssoc","",10,-0.5,9.5);
  m_pT = new TH1F("pT","",100,0,20);
  m_etaPhi = new TH2F("etaPhi","",200,-2.5,2.5,200,-3.142,3.142);
  m_pTinnerOuter = new TH2F("pTinnerOuter","",100,0,20,100,0,20);
  m_nMissing = new TH2F("nMissing","",20,-0.5,19.5,20,-0.5,19.5);
  m_sumResiduals = new TH1F("sumResiduals","",100,0,2);
  m_sumResidualsBad = new TH1F("sumResidualsBad","",100,0,2);
  m_numberHits = new TH1F("numberHits","",100,-0.5,99.5);
  m_numberHitsBad = new TH1F("numberHitsBad","",100,-0.5,99.5);
  m_residualLocus = new TH1F("residualLocus","",200,-2.0,2.0);
  m_residualLocusBad = new TH1F("residualLocusBad","",200,-2.0,2.0);
  m_maxResidual = new TH1F("maxResidual","",100,0,2);
  m_maxResidualBad = new TH1F("maxResidualBad","",100,0,2);

  m_qoverp = new TH1F("qoverp","",100,-10,10);
  m_phi = new TH1F("phi","",100,-3.142,3.142);
  m_lambda = new TH1F("lambda","",100,-3.142/2.,3.142/2.);
  m_dxy = new TH1F("dxy","",100,-10,10);
  m_dsz = new TH1F("dsz","",100,-10,10);
  m_qoverpBad = new TH1F("qoverpBad","",100,-10,10);
  m_phiBad = new TH1F("phiBad","",100,-3.142,3.142);
  m_lambdaBad = new TH1F("lambdaBad","",100,-3.142/2.,3.142/2.);
  m_dxyBad = new TH1F("dxyBad","",100,-10,10);
  m_dszBad = new TH1F("dszBad","",100,-10,10);

  m_associatedFraction = new TH1F("associatedFraction","",100,0,1);
  m_associatedFractionBad = new TH1F("associatedFractionBad","",100,0,1);

  m_pdgid = new TH1F("pdgid","",11,-5.5,5.5);
  m_pdgidBad = new TH1F("pdgidBad","",11,-5.5,5.5);

}
//------------------------------------------------------------
//------------------------------------------------------------
MWBadFitAnalyzer::~MWBadFitAnalyzer()
{
  /* no op */
}
//------------------------------------------------------------
//------------------------------------------------------------
void MWBadFitAnalyzer::beginJob()
{
}

//------------------------------------------------------------
//------------------------------------------------------------
void MWBadFitAnalyzer::endJob()
{
  m_outFile->cd();

  m_nSimAssoc->Write();
  m_pT->Write();
  m_etaPhi->Write();
  m_pTinnerOuter->Write();
  m_nMissing->Write();
  m_sumResiduals->Write();
  m_sumResidualsBad->Write();
  m_numberHits->Write();
  m_numberHitsBad->Write();
  m_residualLocus->Write();
  m_residualLocusBad->Write();
  m_maxResidual->Write();
  m_maxResidualBad->Write();
  m_qoverp->Write();
  m_lambda->Write();
  m_phi->Write();
  m_dxy->Write();
  m_dsz->Write();
  m_qoverpBad->Write();
  m_lambdaBad->Write();
  m_phiBad->Write();
  m_dxyBad->Write();
  m_dszBad->Write();
  m_associatedFraction->Write();
  m_associatedFractionBad->Write();
  m_pdgid->Write();
  m_pdgidBad->Write();



  m_outFile->Close();



}
//------------------------------------------------------------
//------------------------------------------------------------
void MWBadFitAnalyzer::beginRun(const edm::Run& iRun, const edm::EventSetup& iSetup)
{
  edm::ESHandle<TrackAssociatorBase> theAssociator;
  iSetup.get<TrackAssociatorRecord>().get(m_associatorName,theAssociator);
  m_associator = theAssociator.product();
}
//------------------------------------------------------------
//------------------------------------------------------------
void MWBadFitAnalyzer::endRun(const edm::Run& iRun, const edm::EventSetup& iSetup)
{
  /* no op */
}
//------------------------------------------------------------
//------------------------------------------------------------
void MWBadFitAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  iSetup.get<IdealMagneticFieldRecord>().get(m_magfield);

  edm::Handle<View<Track> >handle;
  iEvent.getByLabel(m_source,handle);
  edm::Handle<View<Track> >handleHighPurity;
  iEvent.getByLabel("selectHighPurity",handleHighPurity);
  edm::Handle<TrackingParticleCollection>  simTPhandle;
  iEvent.getByLabel(m_simSource,simTPhandle);
  const TrackingParticleCollection simTracks = *(simTPhandle.product());

  reco::RecoToSimCollection recSimColl;
  reco::SimToRecoCollection simRecColl;

  recSimColl = m_associator->associateRecoToSim(handle,simTPhandle,&iEvent,&iSetup);
  simRecColl = m_associator->associateSimToReco(handle,simTPhandle,&iEvent,&iSetup);


  for(int i = 0; i < (int)handle->size(); i++){
    Track rt1 = (handle->at(i));
    HitPattern p = rt1.hitPattern();
    TrackResiduals r = rt1.residuals();
    int numHits = p.numberOfHits();        
      /*
      p.numberOfLostHits() +         
      p.numberOfValidMuonHits() +    
      p.numberOfLostMuonHits() +     
      p.numberOfValidTrackerHits() + 
      p.numberOfLostTrackerHits() +  
      p.numberOfValidPixelHits() +   
      p.numberOfLostPixelHits();
      */
    double residualSum = 0;
    double locus = 0;
    double maxResidual = 0;
    m_numberHits->Fill(numHits);
    for(int h = 0; h < numHits; h++){
      double xx = (double)h/(double)numHits - 0.5;
      double residual = r.residualX(h,p) + r.residualY(h,p);
      residualSum += residual;
      locus += xx*residual;
      if(residual > maxResidual) maxResidual = residual;
    }
    m_sumResiduals->Fill(residualSum/numHits);
    m_residualLocus->Fill(locus);
    m_maxResidual->Fill(maxResidual);

    double qoverp = rt1.qoverp();
    double lambda = rt1.lambda();
    double phi = rt1.phi();
    double dxy = rt1.dxy();
    double dsz = rt1.dsz();
    /*
    double qoverp = rt1.qoverpError()/rt1.qoverp();
    double lambda = rt1.lambdaError()/rt1.lambda();
    double phi = rt1.phiError()/rt1.phi();
    double dxy = rt1.dxyError()/rt1.dxy();
    double dsz = rt1.dszError()/rt1.dsz();
    */
    m_qoverp->Fill(qoverp);
    m_lambda->Fill(lambda);
    m_phi->Fill(phi);
    m_dxy->Fill(dxy);
    m_dsz->Fill(dsz);

    int pdgid = 0;
    double assocFrac = 0;

    RefToBase<Track> trackRef1(handle,i);
    vector<pair<TrackingParticleRef, double> > tp1;
    TrackingParticleRef tpr1;
    if(recSimColl.find(trackRef1) != recSimColl.end())tp1 = recSimColl[trackRef1];
    m_nSimAssoc->Fill(tp1.size());
    if(tp1.size() > 0){
      tpr1 = tp1[0].first;
      assocFrac = tp1[0].second;
      TrackingParticle* trkpart1=const_cast<TrackingParticle*>(tpr1.get());
      pdgid = trkpart1->pdgId();
    }
    m_pdgid->Fill(fixPdgId(pdgid));
    m_associatedFraction->Fill(assocFrac);
    if(TMath::Prob(rt1.chi2(),rt1.ndof()) > m_probCut)continue;
    //cout<<rt1.momentum().Rho()<<" "<<rt1.chi2()<<" "<<rt1.ndof()<<endl;
    cout<<assocFrac<<endl;
    m_sumResidualsBad->Fill(residualSum/numHits);
    m_numberHitsBad->Fill(numHits);
    m_maxResidualBad->Fill(maxResidual);
    m_residualLocusBad->Fill(locus);
    m_qoverpBad->Fill(qoverp);
    m_lambdaBad->Fill(lambda);
    m_phiBad->Fill(phi);
    m_dxyBad->Fill(dxy);
    m_dszBad->Fill(dsz);
    m_pdgidBad->Fill(fixPdgId(pdgid));
    m_associatedFractionBad->Fill(assocFrac);

    m_pT->Fill(rt1.momentum().Rho());
    m_pTinnerOuter->Fill(rt1.innerMomentum().Rho(),rt1.outerMomentum().Rho());
    m_etaPhi->Fill(rt1.momentum().Eta(),rt1.momentum().Phi());      
    m_nMissing->Fill(rt1.trackerExpectedHitsInner().numberOfLostHits(),rt1.trackerExpectedHitsOuter().numberOfLostHits());
  }


}
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------
bool MWBadFitAnalyzer::compareTracks(Track t1,Track t2)
{
  if(t1.innerPosition() != t2.innerPosition())return false;
  if(t1.outerPosition() != t2.outerPosition())return false;
  if(t1.innerMomentum() != t2.innerMomentum())return false;
  if(t1.outerMomentum() != t2.outerMomentum())return false;
  return true;

}
//------------------------------------------------------------
//------------------------------------------------------------
bool MWBadFitAnalyzer::trackInCollection(Track t,Handle<View<Track> > coll)
{
  bool present=false;

  for(int i = 0; i < (int)coll->size() && !present; i++){
    Track rt2 = (coll->at(i));
    if(!compareTracks(t,rt2))continue;
    if(t.seedRef() != rt2.seedRef())continue;
    present = true;
  }
  return present;
}
//------------------------------------------------------------
//------------------------------------------------------------
int MWBadFitAnalyzer::fixPdgId(int inputPdgId)
{
  int retval = 0;
  switch(inputPdgId){
  case 211:
    retval = 1;
    break;
  case -211:
    retval = -1;
    break;
  case 321:
    retval = 2;
    break;
  case -321:
    retval = -2;
    break;
  case 2212:
    retval = 3;
    break;
  case -2212:
    retval = -3;
    break;
  case 11:
    retval = 4;
    break;
  case -11:
    retval = -4;
    break;
  case 13: 
    retval = 5;
    break;
  case -13:
    retval = -5;
    break;
  default:
    break;

  }
  return retval;
}
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------

DEFINE_FWK_MODULE(MWBadFitAnalyzer);
