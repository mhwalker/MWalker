#include "MWalker/TrackAnalyzer/interface/PurityTreeMaker.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
//#include "FWCore/Framework/interface/eventSetupGetImplementation.h"
#include "FWCore/Framework/interface/TriggerNamesService.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "SimDataFormats/TrackingAnalysis/interface/TrackingParticle.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/Common/interface/AssociationMap.h"
#include "DataFormats/Common/interface/OneToOne.h"
#include "SimDataFormats/Track/interface/SimTrackContainer.h"
#include "SimDataFormats/Vertex/interface/SimVertexContainer.h"
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

MWPurityTreeMaker::MWPurityTreeMaker(const edm::ParameterSet& iPara)
{
  m_outFile = 0;
  m_source = "generalTracks";
  m_associatorName = "TrackAssociatorByHits";
  p_mvaValues_ = &mvaValues_;
  beamspot_ = iPara.getParameter<edm::InputTag>( "beamspot" );
  if(iPara.exists("outfile"))m_outFile = new TFile(iPara.getParameter<string>("outfile").c_str(),"RECREATE");
  if(iPara.exists("source"))m_source = iPara.getParameter<string>("source");
  if(iPara.exists("associator"))m_associatorName = iPara.getParameter<string>("associator");
  if(iPara.exists("simSource"))m_simSource = iPara.getParameter<InputTag>("simSource");
  if(iPara.exists("vertices"))m_vertices = consumes<reco::VertexCollection>(iPara.getParameter<edm::InputTag>("vertices"));
  m_beamspotToken = consumes<reco::BeamSpot>(beamspot_);
  m_assocToken = consumes<reco::TrackToTrackingParticleAssociator>(edm::InputTag(m_associatorName));
  m_trackToken = consumes<edm::View<Track> >(edm::InputTag(m_source));
  m_trackHighPurityToken = consumes<edm::View<Track > >(edm::InputTag("selectHighPurity"));
  m_simTPToken = consumes<TrackingParticleCollection>(m_simSource);

  doMVA_ = false;
  //tmvaReaders_  = NULL;
  //mvaType_ = "BDTG";
  vector<string> mvaFileNames;// = "weights.xml";

  if(iPara.exists("doMVA"))doMVA_ = iPara.getParameter<bool>("doMVA");
  if(iPara.exists("mvaType"))mvaTypes_  = iPara.getParameter<vector<string> >("mvaType");
  if(iPara.exists("mvaFileName"))mvaFileNames = iPara.getParameter<vector<string> >("mvaFileName");

  if(doMVA_){
    for(unsigned int i = 0; i < mvaTypes_.size(); i++){

      TMVA::Reader* tmvaReader_ = new TMVA::Reader("!Color:Silent");
      tmvaReader_->AddVariable("pt",&m_tvpt);
      tmvaReader_->AddVariable("lostmidfrac",&m_tvLostMidFrac);
      tmvaReader_->AddVariable("minlost",&m_tvMinLost);
      tmvaReader_->AddVariable("nhits",&m_tvNhits);
      tmvaReader_->AddVariable("relpterr",&m_tvRelPtErr);
      tmvaReader_->AddVariable("eta",&m_tvEta);
      tmvaReader_->AddVariable("chi2n_no1Dmod",&m_tvChi2n_no1Dmod);
      tmvaReader_->AddVariable("chi2n",&m_tvChi2n);
      tmvaReader_->AddVariable("nlayerslost",&m_tvNlayersLost);
      tmvaReader_->AddVariable("nlayers3D",&m_tvNlayers3D);
      tmvaReader_->AddVariable("nlayers",&m_tvNlayers);
      tmvaReader_->AddVariable("ndof",&m_tvNdof);
      if(mvaTypes_[i] == "Prompt"){
	tmvaReader_->AddVariable("absd0PV",&m_tvAbsD0PV);
	tmvaReader_->AddVariable("absdzPV",&m_tvAbsDzPV);
	tmvaReader_->AddVariable("absdz",&m_tvAbsDz);
	tmvaReader_->AddVariable("absd0",&m_tvAbsD0);
      }
      tmvaReader_->BookMVA("BDTG",mvaFileNames[i]);
      tmvaReaders_.push_back(tmvaReader_);
    }
  }

  m_outTree = new TTree("purityTree","",1);
  m_outTree->Branch("fake",&m_tvFake,"fake/F");
  m_outTree->Branch("iter",&m_tvIter,"iter/F");
  m_outTree->Branch("ndof",&m_tvNdof,"ndof/F");
  m_outTree->Branch("pt",&m_tvpt,"pt/F");
  m_outTree->Branch("nlayers",&m_tvNlayers,"nlayers/F");
  m_outTree->Branch("nlayers3D",&m_tvNlayers3D,"nlayers3D/F");
  m_outTree->Branch("nlayerslost",&m_tvNlayersLost,"nlayerslost/F");
  m_outTree->Branch("chi2n",&m_tvChi2n,"chi2n/F");
  m_outTree->Branch("chi2n_no1Dmod",&m_tvChi2n_no1Dmod,"chi2n_no1Dmod/F");
  m_outTree->Branch("eta",&m_tvEta,"eta/F");
  m_outTree->Branch("relpterr",&m_tvRelPtErr,"relpterr/F");
  m_outTree->Branch("nhits",&m_tvNhits,"nhits/F");
  m_outTree->Branch("lostin",&m_tvLostIn,"lostin/F");
  m_outTree->Branch("lostout",&m_tvLostOut,"lostout/F");
  m_outTree->Branch("minlost",&m_tvMinLost,"minlost/F");
  m_outTree->Branch("lostmidfrac",&m_tvLostMidFrac,"lostmidfrac/F");
  m_outTree->Branch("absdz",&m_tvAbsDz,"absdz/F");
  m_outTree->Branch("absd0",&m_tvAbsD0,"absd0/F");
  m_outTree->Branch("absdzPV",&m_tvAbsDzPV,"absdzPV/F");
  m_outTree->Branch("absd0PV",&m_tvAbsD0PV,"absd0PV/F");
  m_outTree->Branch("mvavals","std::vector<float>",&p_mvaValues_);
  //m_outTree->Branch("mvaval",&m_tvMvaVal,"mvaval/F");

  consumes<reco::TrackToTrackingParticleAssociator>(edm::InputTag(m_associatorName));
}
//------------------------------------------------------------
//------------------------------------------------------------
MWPurityTreeMaker::~MWPurityTreeMaker()
{
  /* no op */
}
//------------------------------------------------------------
//------------------------------------------------------------
void MWPurityTreeMaker::beginJob()
{
}

//------------------------------------------------------------
//------------------------------------------------------------
void MWPurityTreeMaker::endJob()
{
  m_outFile->cd();

  m_outTree->Write();


  m_outFile->Close();



}
//------------------------------------------------------------
//------------------------------------------------------------
void MWPurityTreeMaker::beginRun(const edm::Run& iRun, const edm::EventSetup& iSetup)
{

}
//------------------------------------------------------------
//------------------------------------------------------------
void MWPurityTreeMaker::endRun(const edm::Run& iRun, const edm::EventSetup& iSetup)
{
  /* no op */
}
//------------------------------------------------------------
//------------------------------------------------------------
void MWPurityTreeMaker::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  edm::Handle<reco::BeamSpot> hBsp;
  iEvent.getByToken(m_beamspotToken, hBsp);
  reco::BeamSpot vertexBeamSpot;
  vertexBeamSpot = *hBsp;

  edm::Handle<reco::TrackToTrackingParticleAssociator> assocHandle;
  iEvent.getByToken(m_assocToken,assocHandle);
  m_associator = assocHandle.product();

  iSetup.get<IdealMagneticFieldRecord>().get(m_magfield);

  edm::Handle<reco::VertexCollection> hVtx;
  iEvent.getByToken(m_vertices, hVtx);

  VertexCollection::const_iterator vtxIter = hVtx->begin();

  edm::Handle<View<Track> >handle;
  iEvent.getByToken(m_trackToken,handle);
  edm::Handle<View<Track> >handleHighPurity;
  iEvent.getByToken(m_trackHighPurityToken,handleHighPurity);
  edm::Handle<TrackingParticleCollection>  simTPhandle;
  iEvent.getByToken(m_simTPToken,simTPhandle);
  const TrackingParticleCollection simTracks = *(simTPhandle.product());

  reco::RecoToSimCollection recSimColl;
  reco::SimToRecoCollection simRecColl;

  recSimColl = m_associator->associateRecoToSim(handle,simTPhandle);
  simRecColl = m_associator->associateSimToReco(handle,simTPhandle);

  for(int i = 0; i < (int)handle->size(); i++){
    p_mvaValues_->clear();
    p_mvaValues_->reserve(mvaTypes_.size());
    Track tk = (handle->at(i));
    m_tvFake = 1;
    m_tvNdof = tk.ndof();
    m_tvNlayers = tk.hitPattern().trackerLayersWithMeasurement();
    m_tvNlayers3D = tk.hitPattern().pixelLayersWithMeasurement() + tk.hitPattern().numberOfValidStripLayersWithMonoAndStereo();
    m_tvNlayersLost = tk.hitPattern().trackerLayersWithoutMeasurement(HitPattern::TRACK_HITS);

    float chi2n =  tk.normalizedChi2();
    float chi2n_no1Dmod = chi2n;

    int count1dhits = 0;
    for (trackingRecHit_iterator ith = tk.recHitsBegin(), edh = tk.recHitsEnd(); ith != edh; ++ith) {
      const TrackingRecHit * hit = (*ith);
      if (hit->isValid()) {
	if (typeid(*hit) == typeid(SiStripRecHit1D)) ++count1dhits;
      }
    }
    if (count1dhits > 0) {
      float chi2 = tk.chi2();
      float ndof = tk.ndof();
      chi2n = (chi2+count1dhits)/float(ndof+count1dhits);
    }
    m_tvChi2n = chi2n;
    m_tvChi2n_no1Dmod = chi2n_no1Dmod;
    m_tvEta = tk.eta();
    m_tvpt = tk.pt();
    m_tvRelPtErr = float(tk.ptError())/std::max(float(tk.pt()),0.000001f);
    m_tvNhits = tk.numberOfValidHits();
    m_tvLostIn = tk.hitPattern().numberOfLostTrackerHits(reco::HitPattern::MISSING_INNER_HITS);
    m_tvLostOut = tk.hitPattern().numberOfLostTrackerHits(reco::HitPattern::MISSING_OUTER_HITS);
    m_tvMinLost = std::min(m_tvLostIn,m_tvLostOut);
    m_tvLostMidFrac = float(tk.numberOfLostHits()) / float(tk.numberOfValidHits() + tk.numberOfLostHits());

    RefToBase<Track> trackRef1(handle,i);

    m_tvAbsDz = fabs(tk.dz( vertexBeamSpot.position()));
    m_tvAbsD0 = fabs(tk.dxy( vertexBeamSpot.position()));

    Point bestVertex = getBestVertex(trackRef1,*(hVtx.product()));
    m_tvAbsDzPV = fabs(tk.dz(bestVertex));
    m_tvAbsD0PV = fabs(tk.dxy(bestVertex));

    TString algoName(tk.algoName());
    if (algoName == "initialStep"){
      m_tvIter = 0;
    }else if(algoName == "lowPtTripletStep"){
      m_tvIter = 1;
    }else if(algoName == "pixelPairStep"){
      m_tvIter = 2;
    }else if(algoName == "detachedTripletStep"){
      m_tvIter = 3;
    }else if(algoName == "mixedTripletStep"){
      m_tvIter = 4;
    }else if(algoName == "pixelLessStep"){
      m_tvIter = 5;
    }else if(algoName == "tobTecStep"){
      m_tvIter = 6;
    }else{
      m_tvIter = 9;
    }


    vector<pair<TrackingParticleRef, double> > tp1;
    if(recSimColl.find(trackRef1) != recSimColl.end())tp1 = recSimColl[trackRef1];
    if(tp1.size() > 0){
      m_tvFake = 0;
    }

    m_tvMvaVal = -99999;
    if(doMVA_){
      // m_tvMvaVal = tmvaReader_->EvaluateMVA(mvaType_);
      for(unsigned int i = 0; i < tmvaReaders_.size();i++){
	p_mvaValues_->push_back(tmvaReaders_[i]->EvaluateMVA("BDTG"));
      }
    }

    m_outTree->Fill();
  }


}
//------------------------------------------------------------
//------------------------------------------------------------
Point MWPurityTreeMaker::getBestVertex(TrackBaseRef track,VertexCollection vertices){
  Point p(0,0,-99999);
  Point p_dz(0,0,-99999);
  float bestWeight = 0;
  float dzmin = 10000;
  bool weightMatch = false;
  for(auto const & vertex : vertices){
    float w = vertex.trackWeight(track);
    Point v_pos = vertex.position();
    if(w > bestWeight){
      p = v_pos;
      bestWeight = w;
      weightMatch = true;
    }
    float dz = fabs(track.get()->dz(v_pos));
    if(dz < dzmin){
      p_dz = v_pos;
      dzmin = dz;
    }
  }
  if(weightMatch)return p;
  else return p_dz;
}

//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------

DEFINE_FWK_MODULE(MWPurityTreeMaker);
