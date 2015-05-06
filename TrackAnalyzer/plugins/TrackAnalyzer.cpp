#include "MWalker/TrackAnalyzer/interface/TrackAnalyzer.h"

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

#include <functional>
#include <sstream>
#include <iostream>
using namespace edm;
using namespace reco;

typedef math::XYZTLorentzVectorD LorentzVector;
typedef math::XYZVector Vector;
typedef math::XYZPoint Point;

using namespace std;

MWTrackAnalyzer::MWTrackAnalyzer(const edm::ParameterSet& iPara)
{
  m_totalEvents = 0;
  m_outFile = 0;
  m_nDuplicateInnerHighPurity = 0;
  m_nCombinatoricsInnerHighPurity = 0;
  m_source = "generalTracks";
  m_associatorName = "TrackAssociatorByHits";
  m_saveTrees = true;
  m_minMissingOuterHitsFromInner = 2;
  m_minDeltaR3d = -4.0;
  m_minAvgRho = 15.0;
  m_minPt = 0.2;
  m_minP = 0.4;
  //m_simSource = "mergedtruth";
  if(iPara.exists("minPt"))m_minPt = iPara.getParameter<double>("minPt");
  if(iPara.exists("minP"))m_minP = iPara.getParameter<double>("minP");
  if(iPara.exists("nMissingOuterFromInner")) m_minMissingOuterHitsFromInner = iPara.getParameter<int>("nMissingOuterFromInner");
  if(iPara.exists("minDeltaR3d"))m_minDeltaR3d = iPara.getParameter<double>("minDeltaR3d");
  if(iPara.exists("minAvgRho"))m_minAvgRho = iPara.getParameter<double>("minAvgRho");
  if(iPara.exists("outfile"))m_outFile = new TFile(iPara.getParameter<string>("outfile").c_str(),"RECREATE");
  if(iPara.exists("source"))m_source = iPara.getParameter<string>("source");
  if(iPara.exists("simSource"))m_simSource = iPara.getParameter<InputTag>("simSource");
  if(iPara.exists("associator"))m_associatorName = iPara.getParameter<string>("associator");
  if(iPara.exists("saveTrees"))m_saveTrees = iPara.getParameter<bool>("saveTrees");

  m_hnTracks = new TH1F("hnTracks","",1000,-0.5,999.5);
  m_duplicate_eta = new TH1F("duplicate_eta","",300,-3.0,3.0);
  m_hmatchedTracks = new TH1F("hmatchedTracks","",1000,-0.5,999.5);
  m_duplicate_pdR = new TH1F("duplicate_pdR","",500,-5.0,5.0);
  m_duplicate_bestdR = new TH1F("duplicate_bestdR","",500,-5.0,5.0);
  m_duplicate_deltapT = new TH1F("duplicate_deltapT","",500,-5.0,5.0);
  m_duplicate_diffpT = new TH1F("duplicate_diffpT","",200,-10,10);
  m_duplicate_vdR = new TH1F("duplicate_vdR","",500,-5.0,5.0);
  m_duplicate_nSharedHits = new TH1F("duplicate_nSharedHits","",30,-0.5,29.5);
  m_hmatchedPerTrack = new TH1F("duplicate_matchedPerTrack","",20,-0.5,19.5);
  m_minDelta = new TH1F("duplicate_minDelta","",500,0.0,100.0);
  m_duplicate_qoverp = new TH2F("duplicate_qoverp","",100,-1,1,100,-1,1);
  m_duplicate_phi = new TH2F("duplicate_phi","",100,-3.142,3.142,100,-3.142,3.142);
  m_duplicate_lambda = new TH2F("duplicate_lambda","",100,-2,2,100,-2,2);
  m_duplicate_dxy = new TH2F("duplicate_dxy","",100,-5,5,100,-5,5);
  m_duplicate_dsz = new TH2F("duplicate_dsz","",100,-25,25,100,-25,25);
  m_duplicate_innerR = new TH2F("duplicate_innerR","",80,0,80,80,0,80);
  m_duplicate_outerR = new TH2F("duplicate_outerR","",100,0,100,100,0,100);
  m_duplicate_nHits = new TH2F("duplicate_nHits","",30,-0.5,29.5,30,-0.5,29.5);
  m_duplicate_nMissingHits = new TH2F("duplicate_nMissingHits","",30,-0.5,29.5,30,-0.5,29.5);
  m_duplicate_pT = new TH2F("duplicate_pT","",80,0,80,80,0,80);
  m_duplicate_deltaR = new TH1F("duplicate_deltaR","",100,-50,50);

  m_duplicate_innerMatched = new TH1F("duplicate_innerMatched","",20,-0.5,19.5);
  m_duplicate_outerMatched = new TH1F("duplicate_outerMatched","",20,-0.5,19.5);
  m_duplicate_innerMatchedRealFake = new TH2F("duplicate_innerMatchedRealFake","",20,-0.5,19.5,20,-0.5,19.5);
  m_duplicate_outerMatchedRealFake = new TH2F("duplicate_outerMatchedRealFake","",20,-0.5,19.5,20,-0.5,19.5);
  m_comb_innerMatched = new TH1F("comb_innerMatched","",20,-0.5,19.5);
  m_comb_outerMatched = new TH1F("comb_outerMatched","",20,-0.5,19.5);


  m_comb_dqoverp = new TH1F("comb_dqoverp","",100,-20,20);
  m_comb_dlambda = new TH1F("comb_dlambda","",100,-20,20);
  m_comb_dphi = new TH1F("comb_dphi","",100,-20,20);
  m_comb_ddxy = new TH1F("comb_ddxy","",100,-20,20);
  m_comb_ddsz = new TH1F("comb_ddsz","",100,-20,20);
  m_comb_q_lambda = new TH2F("comb_q_lambda","",100,-20,20,100,-20,20);
  m_comb_bestdR = new TH1F("comb_bestdR","",500,-5.0,5.0);
  m_comb_chi2 = new TH1F("comb_chi2","",300,0.0,30.0);
  m_comb_pcaR = new TH1F("comb_pcaR","",500,0,100);
  m_comb_qoverp = new TH2F("comb_qoverp","",100,-1,1,100,-1,1);
  m_comb_phi = new TH2F("comb_phi","",100,-3.142,3.142,100,-3.142,3.142);
  m_comb_lambda = new TH2F("comb_lambda","",100,-2,2,100,-2,2);
  m_comb_dxy = new TH2F("comb_dxy","",100,-5,5,100,-5,5);
  m_comb_dsz = new TH2F("comb_dsz","",100,-25,25,100,-25,25);
  m_comb_nHits = new TH2F("comb_nHits","",30,-0.5,29.5,30,-0.5,29.5);
  m_comb_nMissingHits = new TH2F("comb_nMissingHits","",30,-0.5,29.5,30,-0.5,29.5);
  m_comb_pT = new TH2F("comb_pT","",80,0,80,80,0,80);
  m_comb_nFakes = new TH1F("comb_nFakes","",3,-0.5,2.5);
  m_comb_deltaV = new TH1F("comb_deltaV","",500,-50,50);
  m_comb_outerV = new TH2F("comb_outerV","",400,-200,200,200,0,100);
  m_comb_parentDaughter = new TH1F("comb_parentDaughter","",2,-0.5,1.5);

  m_comb_cut0_pcaR = new TH1F("comb_cut0_pcaR","",100,-20,20);
  m_comb_cut1_dphi = new TH1F("comb_cut1_dphi","",100,-20,20);
  m_comb_cut2_ddsz = new TH1F("comb_cut2_ddsz","",100,-20,20);
  m_comb_cut3_dlambda = new TH1F("comb_cut3_dlambda","",100,-20,20);
  m_comb_cut4_ddxy = new TH1F("comb_cut4_ddxy","",100,-20,20);
  m_comb_cut5_innerR = new TH1F("comb_cut5_innerR","",100,-20,20);

  m_duplicate_dqoverp = new TH1F("duplicate_dqoverp","",100,-20,20);
  m_duplicate_dlambda = new TH1F("duplicate_dlambda","",100,-20,20);
  m_duplicate_dphi = new TH1F("duplicate_dphi","",100,-20,20);
  m_duplicate_ddxy = new TH1F("duplicate_ddxy","",100,-20,20);
  m_duplicate_ddsz = new TH1F("duplicate_ddsz","",100,-20,20);
  m_duplicate_q_lambda = new TH2F("duplicate_q_lambda","",100,-20,20,100,-20,20);
  m_duplicate_chi2 = new TH1F("duplicate_chi2","",300,0,30.0);
  m_duplicate_pcaR = new TH1F("duplicate_pcaR","",500,0,100);

  m_duplicate_cut0_pcaR = new TH1F("duplicate_cut0_pcaR","",100,-20,20);
  m_duplicate_cut1_dphi = new TH1F("duplicate_cut1_dphi","",100,-20,20);
  m_duplicate_cut2_ddsz = new TH1F("duplicate_cut2_ddsz","",100,-20,20);
  m_duplicate_cut3_dlambda = new TH1F("duplicate_cut3_dlambda","",100,-20,20);
  m_duplicate_cut4_ddxy = new TH1F("duplicate_cut4_ddxy","",100,-20,20);
  m_duplicate_cut5_innerR = new TH1F("duplicate_cut5_innerR","",100,-20,20);

  m_duplicate_tree = new TTree("duplicate_tree","");
  m_duplicate_tree->Branch("inner_inner_x",&mt_inner_inner_x,"inner_inner_x/D");
  m_duplicate_tree->Branch("inner_inner_y",&mt_inner_inner_y,"inner_inner_y/D");
  m_duplicate_tree->Branch("inner_inner_z",&mt_inner_inner_z,"inner_inner_z/D");
  m_duplicate_tree->Branch("inner_outer_x",&mt_inner_outer_x,"inner_outer_x/D");
  m_duplicate_tree->Branch("inner_outer_y",&mt_inner_outer_y,"inner_outer_y/D");
  m_duplicate_tree->Branch("inner_outer_z",&mt_inner_outer_z,"inner_outer_z/D");
  m_duplicate_tree->Branch("outer_inner_x",&mt_outer_inner_x,"outer_inner_x/D");
  m_duplicate_tree->Branch("outer_inner_y",&mt_outer_inner_y,"outer_inner_y/D");
  m_duplicate_tree->Branch("outer_inner_z",&mt_outer_inner_z,"outer_inner_z/D");
  m_duplicate_tree->Branch("outer_outer_x",&mt_outer_outer_x,"outer_outer_x/D");
  m_duplicate_tree->Branch("outer_outer_y",&mt_outer_outer_y,"outer_outer_y/D");
  m_duplicate_tree->Branch("outer_outer_z",&mt_outer_outer_z,"outer_outer_z/D");
  m_duplicate_tree->Branch("pca_x",&mt_pca_x,"pca_x/D");
  m_duplicate_tree->Branch("pca_y",&mt_pca_y,"pca_y/D");
  m_duplicate_tree->Branch("pca_z",&mt_pca_z,"pca_z/D");
  m_duplicate_tree->Branch("delta3d_x",&mt_delta3d_x,"delta3d_x/D");
  m_duplicate_tree->Branch("delta3d_y",&mt_delta3d_y,"delta3d_y/D");
  m_duplicate_tree->Branch("delta3d_z",&mt_delta3d_z,"delta3d_z/D");
  m_duplicate_tree->Branch("delta3d_r",&mt_delta3d_r,"delta3d_r/D");
  m_duplicate_tree->Branch("inner_nMissingInner",&mt_inner_nMissingInner,"inner_nMissingInner/I");
  m_duplicate_tree->Branch("inner_nMissingOuter",&mt_inner_nMissingOuter,"inner_nMissingOuter/I");
  m_duplicate_tree->Branch("outer_nMissingInner",&mt_outer_nMissingInner,"outer_nMissingInner/I");
  m_duplicate_tree->Branch("outer_nMissingOuter",&mt_outer_nMissingOuter,"outer_nMissingOuter/I");
  m_duplicate_tree->Branch("inner_qoverp",&mt_inner_qoverp,"inner_qoverp/D");
  m_duplicate_tree->Branch("inner_qoverp_err",&mt_inner_qoverp_err,"inner_qoverp_err/D");
  m_duplicate_tree->Branch("inner_lambda",&mt_inner_lambda,"inner_lambda/D");
  m_duplicate_tree->Branch("inner_lambda_err",&mt_inner_lambda_err,"inner_lambda_err/D");
  m_duplicate_tree->Branch("inner_phi",&mt_inner_phi,"inner_phi/D");
  m_duplicate_tree->Branch("inner_phi_err",&mt_inner_phi_err,"inner_phi_err/D");
  m_duplicate_tree->Branch("inner_dxy",&mt_inner_dxy,"inner_dxy/D");
  m_duplicate_tree->Branch("inner_dxy_err",&mt_inner_dxy_err,"inner_dxy_err/D");
  m_duplicate_tree->Branch("inner_dsz",&mt_inner_dsz,"inner_dsz/D");
  m_duplicate_tree->Branch("inner_dsz_err",&mt_inner_dsz_err,"inner_dsz_err/D");
  m_duplicate_tree->Branch("outer_qoverp",&mt_outer_qoverp,"outer_qoverp/D");
  m_duplicate_tree->Branch("outer_qoverp_err",&mt_outer_qoverp_err,"outer_qoverp_err/D");
  m_duplicate_tree->Branch("outer_lambda",&mt_outer_lambda,"outer_lambda/D");
  m_duplicate_tree->Branch("outer_lambda_err",&mt_outer_lambda_err,"outer_lambda_err/D");
  m_duplicate_tree->Branch("outer_phi",&mt_outer_phi,"outer_phi/D");
  m_duplicate_tree->Branch("outer_phi_err",&mt_outer_phi_err,"outer_phi_err/D");
  m_duplicate_tree->Branch("outer_dxy",&mt_outer_dxy,"outer_dxy/D");
  m_duplicate_tree->Branch("outer_dxy_err",&mt_outer_dxy_err,"outer_dxy_err/D");
  m_duplicate_tree->Branch("outer_dsz",&mt_outer_dsz,"outer_dsz/D");
  m_duplicate_tree->Branch("outer_dsz_err",&mt_outer_dsz_err,"outer_dsz_err/D");
  m_duplicate_tree->Branch("dqoverp",&mt_dqoverp,"dqoverp/D");
  m_duplicate_tree->Branch("dlambda",&mt_dlambda,"dlambda/D");
  m_duplicate_tree->Branch("dphi",&mt_dphi,"dphi/D");
  m_duplicate_tree->Branch("ddxy",&mt_ddxy,"ddxy/D");
  m_duplicate_tree->Branch("ddsz",&mt_ddsz,"ddsz/D");
  m_duplicate_tree->Branch("inner_pdgid",&mt_inner_pdgid,"inner_pdgid/I");
  m_duplicate_tree->Branch("outer_pdgid",&mt_outer_pdgid,"outer_pdgid/I");
  m_duplicate_tree->Branch("dca", &mt_dca,"dca/D");


  m_comb_tree = new TTree("comb_tree","");
  m_comb_tree->Branch("inner_inner_x",&mt_inner_inner_x,"inner_inner_x/D");
  m_comb_tree->Branch("inner_inner_y",&mt_inner_inner_y,"inner_inner_y/D");
  m_comb_tree->Branch("inner_inner_z",&mt_inner_inner_z,"inner_inner_z/D");
  m_comb_tree->Branch("inner_outer_x",&mt_inner_outer_x,"inner_outer_x/D");
  m_comb_tree->Branch("inner_outer_y",&mt_inner_outer_y,"inner_outer_y/D");
  m_comb_tree->Branch("inner_outer_z",&mt_inner_outer_z,"inner_outer_z/D");
  m_comb_tree->Branch("outer_inner_x",&mt_outer_inner_x,"outer_inner_x/D");
  m_comb_tree->Branch("outer_inner_y",&mt_outer_inner_y,"outer_inner_y/D");
  m_comb_tree->Branch("outer_inner_z",&mt_outer_inner_z,"outer_inner_z/D");
  m_comb_tree->Branch("outer_outer_x",&mt_outer_outer_x,"outer_outer_x/D");
  m_comb_tree->Branch("outer_outer_y",&mt_outer_outer_y,"outer_outer_y/D");
  m_comb_tree->Branch("outer_outer_z",&mt_outer_outer_z,"outer_outer_z/D");
  m_comb_tree->Branch("pca_x",&mt_pca_x,"pca_x/D");
  m_comb_tree->Branch("pca_y",&mt_pca_y,"pca_y/D");
  m_comb_tree->Branch("pca_z",&mt_pca_z,"pca_z/D");
  m_comb_tree->Branch("delta3d_x",&mt_delta3d_x,"delta3d_x/D");
  m_comb_tree->Branch("delta3d_y",&mt_delta3d_y,"delta3d_y/D");
  m_comb_tree->Branch("delta3d_z",&mt_delta3d_z,"delta3d_z/D");
  m_comb_tree->Branch("delta3d_r",&mt_delta3d_r,"delta3d_r/D");
  m_comb_tree->Branch("inner_nMissingInner",&mt_inner_nMissingInner,"inner_nMissingInner/I");
  m_comb_tree->Branch("inner_nMissingOuter",&mt_inner_nMissingOuter,"inner_nMissingOuter/I");
  m_comb_tree->Branch("outer_nMissingInner",&mt_outer_nMissingInner,"outer_nMissingInner/I");
  m_comb_tree->Branch("outer_nMissingOuter",&mt_outer_nMissingOuter,"outer_nMissingOuter/I");
  m_comb_tree->Branch("inner_qoverp",&mt_inner_qoverp,"inner_qoverp/D");
  m_comb_tree->Branch("inner_qoverp_err",&mt_inner_qoverp_err,"inner_qoverp_err/D");
  m_comb_tree->Branch("inner_lambda",&mt_inner_lambda,"inner_lambda/D");
  m_comb_tree->Branch("inner_lambda_err",&mt_inner_lambda_err,"inner_lambda_err/D");
  m_comb_tree->Branch("inner_phi",&mt_inner_phi,"inner_phi/D");
  m_comb_tree->Branch("inner_phi_err",&mt_inner_phi_err,"inner_phi_err/D");
  m_comb_tree->Branch("inner_dxy",&mt_inner_dxy,"inner_dxy/D");
  m_comb_tree->Branch("inner_dxy_err",&mt_inner_dxy_err,"inner_dxy_err/D");
  m_comb_tree->Branch("inner_dsz",&mt_inner_dsz,"inner_dsz/D");
  m_comb_tree->Branch("inner_dsz_err",&mt_inner_dsz_err,"inner_dsz_err/D");
  m_comb_tree->Branch("outer_qoverp",&mt_outer_qoverp,"outer_qoverp/D");
  m_comb_tree->Branch("outer_qoverp_err",&mt_outer_qoverp_err,"outer_qoverp_err/D");
  m_comb_tree->Branch("outer_lambda",&mt_outer_lambda,"outer_lambda/D");
  m_comb_tree->Branch("outer_lambda_err",&mt_outer_lambda_err,"outer_lambda_err/D");
  m_comb_tree->Branch("outer_phi",&mt_outer_phi,"outer_phi/D");
  m_comb_tree->Branch("outer_phi_err",&mt_outer_phi_err,"outer_phi_err/D");
  m_comb_tree->Branch("outer_dxy",&mt_outer_dxy,"outer_dxy/D");
  m_comb_tree->Branch("outer_dxy_err",&mt_outer_dxy_err,"outer_dxy_err/D");
  m_comb_tree->Branch("outer_dsz",&mt_outer_dsz,"outer_dsz/D");
  m_comb_tree->Branch("outer_dsz_err",&mt_outer_dsz_err,"outer_dsz_err/D");
  m_comb_tree->Branch("dqoverp",&mt_dqoverp,"dqoverp/D");
  m_comb_tree->Branch("dlambda",&mt_dlambda,"dlambda/D");
  m_comb_tree->Branch("dphi",&mt_dphi,"dphi/D");
  m_comb_tree->Branch("ddxy",&mt_ddxy,"ddxy/D");
  m_comb_tree->Branch("ddsz",&mt_ddsz,"ddsz/D");
  m_comb_tree->Branch("inner_pdgid",&mt_inner_pdgid,"inner_pdgid/I");
  m_comb_tree->Branch("outer_pdgid",&mt_outer_pdgid,"outer_pdgid/I");
  m_comb_tree->Branch("dca", &mt_dca,"dca/D");

  consumes<reco::TrackToTrackingParticleAssociator>(edm::InputTag(m_associatorName));

}
//------------------------------------------------------------
//------------------------------------------------------------
MWTrackAnalyzer::~MWTrackAnalyzer()
{
  /* no op */
}
//------------------------------------------------------------
//------------------------------------------------------------
void MWTrackAnalyzer::beginJob()
{
  m_totalEvents = 0;
}

//------------------------------------------------------------
//------------------------------------------------------------
void MWTrackAnalyzer::endJob()
{
  m_outFile->cd();
  m_hnTracks->Write();
  m_hmatchedTracks->Write();
  m_duplicate_eta->Write();
  m_duplicate_pdR->Write();
  m_duplicate_deltapT->Write();
  m_duplicate_diffpT->Write();
  m_duplicate_vdR->Write();
  m_duplicate_bestdR->Write();
  m_duplicate_nSharedHits->Write();
  m_hmatchedPerTrack->Write();
  m_minDelta->Write();
  m_duplicate_qoverp->Write();
  m_duplicate_phi->Write();
  m_duplicate_lambda->Write();
  m_duplicate_dxy->Write();
  m_duplicate_dsz->Write();
  m_duplicate_innerR->Write();
  m_duplicate_outerR->Write();
  m_duplicate_nHits->Write();
  m_duplicate_nMissingHits->Write();
  m_duplicate_pT->Write();
  m_duplicate_deltaR->Write();

  m_duplicate_innerMatched->Write();
  m_duplicate_outerMatched->Write();
  m_duplicate_innerMatchedRealFake->Write();
  m_duplicate_outerMatchedRealFake->Write();
  m_comb_innerMatched->Write();
  m_comb_outerMatched->Write();

  m_comb_dqoverp->Write();
  m_comb_dlambda->Write();
  m_comb_dphi->Write();
  m_comb_ddxy->Write();
  m_comb_ddsz->Write();
  m_comb_q_lambda->Write();
  m_comb_bestdR->Write();
  m_comb_chi2->Write();
  m_comb_pcaR->Write();
  m_comb_qoverp->Write();
  m_comb_phi->Write();
  m_comb_lambda->Write();
  m_comb_dxy->Write();
  m_comb_dsz->Write();
  m_comb_nHits->Write();
  m_comb_nMissingHits->Write();
  m_comb_pT->Write();
  m_comb_nFakes->Write();
  m_comb_deltaV->Write();
  m_comb_outerV->Write();
  m_comb_parentDaughter->Write();

  m_duplicate_dqoverp->Write();
  m_duplicate_dlambda->Write();
  m_duplicate_dphi->Write();
  m_duplicate_ddxy->Write();
  m_duplicate_ddsz->Write();
  m_duplicate_q_lambda->Write();
  m_duplicate_chi2->Write();
  m_duplicate_pcaR->Write();

  m_comb_cut0_pcaR->Write();
  m_comb_cut1_dphi->Write();
  m_comb_cut2_ddsz->Write();
  m_comb_cut3_dlambda->Write();
  m_comb_cut4_ddxy->Write();
  m_comb_cut5_innerR->Write();

  m_duplicate_cut0_pcaR->Write();
  m_duplicate_cut1_dphi->Write();
  m_duplicate_cut2_ddsz->Write();
  m_duplicate_cut3_dlambda->Write();
  m_duplicate_cut4_ddxy->Write();
  m_duplicate_cut5_innerR->Write();

  if(m_saveTrees){
    m_duplicate_tree->Write();
    m_comb_tree->Write();
  }

  m_outFile->Close();

  cout<<"nDuplicatesInnerHighPurity: "<<m_nDuplicateInnerHighPurity<<endl;
  cout<<"nCombinatoricsInnerHighPurity: "<<m_nCombinatoricsInnerHighPurity<<endl;


}
//------------------------------------------------------------
//------------------------------------------------------------
void MWTrackAnalyzer::beginRun(const edm::Run& iRun, const edm::EventSetup& iSetup)
{

}
//------------------------------------------------------------
//------------------------------------------------------------
void MWTrackAnalyzer::endRun(const edm::Run& iRun, const edm::EventSetup& iSetup)
{
  /* no op */
}
//------------------------------------------------------------
//------------------------------------------------------------
void MWTrackAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  double minPt = m_minPt;
  double minP = m_minP;

  m_totalEvents++;
  iSetup.get<IdealMagneticFieldRecord>().get(m_magfield);

  edm::Handle<View<Track> >handle;
  iEvent.getByLabel(m_source,handle);
  edm::Handle<View<Track> >handleHighPurity;
  iEvent.getByLabel("selectHighPurity",handleHighPurity);
  m_hnTracks->Fill(handle->size());
  edm::Handle<TrackingParticleCollection>  simTPhandle;
  iEvent.getByLabel(m_simSource,simTPhandle);
  const TrackingParticleCollection simTracks = *(simTPhandle.product());

  edm::Handle<reco::TrackToTrackingParticleAssociator> assocHandle;
  iEvent.getByLabel(m_associatorName,assocHandle);
  m_associator = assocHandle.product();


  reco::RecoToSimCollection recSimColl;
  reco::SimToRecoCollection simRecColl;

  recSimColl = m_associator->associateRecoToSim(handle,simTPhandle);
  simRecColl = m_associator->associateSimToReco(handle,simTPhandle);

  TwoTrackMinimumDistance ttmd;
  TSCPBuilderNoMaterial tscpBuilder;
  //TrajectoryStateTransform transformer;
  //AssociationMap<OneToOne<vector<Track>,vector<Track> > > matchedTracks;
  map<Track,Track,trackCompare> matchedTracks;
  map<Track,vector<Track>,trackCompare> innerMatchedTracks;
  map<Track,vector<Track>,trackCompare> outerMatchedTracks;
  map<Track,vector<Track>,trackCompare> duplicateInnerMatched;
  map<Track,vector<Track>,trackCompare> duplicateOuterMatched;

  vector<Track> duplicateInner;
  vector<Track> duplicateOuter;
  for(int i = 0; i < (int)simTracks.size(); i++){
    TrackingParticleRef tpr(simTPhandle, i);
    TrackingParticle* tp=const_cast<TrackingParticle*>(tpr.get());
    if(simRecColl.find(tpr) == simRecColl.end())continue;
    vector<pair<RefToBase<Track>, double> > rt = (std::vector<std::pair<RefToBase<Track>, double> >) simRecColl[tpr];
    if(rt.size() == 0)continue;
    if(tp->p4().Rho() < minPt)continue;
    if(tp->p4().R() < minP)continue;
    int nGoodPt = 0;
    for(int j = 0; j < (int)rt.size(); j++){
      if((rt[j].first)->innerMomentum().Rho() > minPt && (rt[j].first)->innerMomentum().R() > minP)nGoodPt++;
    }
    m_hmatchedPerTrack->Fill(nGoodPt);
    if(nGoodPt < 2)continue;
    m_duplicate_eta->Fill(tp->p4().Eta());
    for(int j = 0; j < (int)rt.size(); j++){
      if((rt[j].first)->innerMomentum().Rho() < minPt)continue;
      if((rt[j].first)->innerMomentum().Rho() < minP)continue;
      for(int k = j+1; k < (int)rt.size(); k++){
	if((rt[k].first)->innerMomentum().Rho() < minPt)continue;
	if((rt[k].first)->innerMomentum().Rho() < minP)continue;
	int nshared = numberOfSharedHits(*(rt[j].first),*(rt[k].first));
	m_duplicate_nSharedHits->Fill(nshared);
	float bestdeltaR = bestDeltaR(*(rt[j].first),*(rt[k].first));
	bestdeltaR += 0.0;
	Track t1,t2;
	if((rt[j].first)->outerPosition().Rho() < (rt[k].first)->outerPosition().Rho()){
	  t1 = *(rt[j].first);
	  t2 = *(rt[k].first);
	}else{
	  t1 = *(rt[k].first);
	  t2 = *(rt[j].first);
	}

	//TrackRef tr1 = t1;
	//TrackRef tr2 = t2;
	FreeTrajectoryState fts1 = trajectoryStateTransform::initialFreeState(t1, &*m_magfield);
	FreeTrajectoryState fts2 = trajectoryStateTransform::initialFreeState(t2, &*m_magfield);
	if(!ttmd.calculate(fts1,fts2)){cerr<<"ttmd failed"<<endl;continue;}

	GlobalPoint avgPoint((t1.outerPosition().x()+t2.innerPosition().x())*0.5,(t1.outerPosition().y()+t2.innerPosition().y())*0.5,(t1.outerPosition().z()+t2.innerPosition().z())*0.5);
	//TrajectoryStateClosestToPoint TSCP1 = tscpBuilder(fts1, ttmd.crossingPoint());
	//TrajectoryStateClosestToPoint TSCP2 = tscpBuilder(fts2, ttmd.crossingPoint());
	TrajectoryStateClosestToPoint TSCP1 = tscpBuilder(fts1, avgPoint);
	TrajectoryStateClosestToPoint TSCP2 = tscpBuilder(fts2, avgPoint);
	if(!TSCP1.isValid())continue;
	if(!TSCP2.isValid())continue;
	matchedTracks.insert(pair<Track,Track>(t2,t1));
	matchedTracks.insert(pair<Track,Track>(t1,t2));
	//matchedTracks[t1] = t2;
	//matchedTracks[t2] = t1;

	const FreeTrajectoryState ftsn1 = TSCP1.theState();
	const FreeTrajectoryState ftsn2 = TSCP2.theState();
 
	mt_dca =  (ftsn2.position()-ftsn1.position()).mag();
	if(trackInCollection(t1,handleHighPurity))m_nDuplicateInnerHighPurity++;

	Point t1inner = t1.innerPosition();
	Point t2inner = t2.innerPosition();
	m_duplicate_bestdR->Fill(ttmd.distance());
	m_duplicate_pcaR->Fill(ttmd.crossingPoint().perp());
	m_duplicate_innerR->Fill(t1inner.Rho(),t2inner.Rho());
	m_duplicate_outerR->Fill(t1.outerPosition().Rho(),t2.outerPosition().Rho());
	m_duplicate_pdR->Fill(deltaR(t1,t2));
	m_duplicate_deltapT->Fill((TSCP1.pt() - TSCP2.pt())/TSCP1.pt());
	m_duplicate_diffpT->Fill(TSCP1.pt()-TSCP2.pt());

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



	///////////////////////
	//Fill tree variables//
	///////////////////////
	mt_inner_inner_x = t1.innerPosition().x();
	mt_inner_inner_y = t1.innerPosition().y();
	mt_inner_inner_z = t1.innerPosition().z();
	mt_inner_outer_x = t1.outerPosition().x();
	mt_inner_outer_y = t1.outerPosition().y();
	mt_inner_outer_z = t1.outerPosition().z();
	mt_outer_inner_x = t2.innerPosition().x();
	mt_outer_inner_y = t2.innerPosition().y();
	mt_outer_inner_z = t2.innerPosition().z();
	mt_outer_outer_x = t2.outerPosition().x();
	mt_outer_outer_y = t2.outerPosition().y();
	mt_outer_outer_z = t2.outerPosition().z();
	mt_pca_x = ttmd.crossingPoint().x();
	mt_pca_y = ttmd.crossingPoint().y();
	mt_pca_z = ttmd.crossingPoint().z();
	mt_delta3d_x = (mt_inner_outer_x + mt_outer_inner_x)/2.;
	mt_delta3d_y = (mt_inner_outer_y + mt_outer_inner_y)/2.;
	mt_delta3d_z = (mt_inner_outer_z + mt_outer_inner_z)/2.;
	mt_delta3d_r = sqrt(pow(mt_delta3d_x,2)+pow(mt_delta3d_y,2));
	//cout<<mt_delta3d_x<<" "<<avgPoint.x()<<" "<<mt_delta3d_y<<" "<<avgPoint.y()<<" "<<mt_delta3d_z<<" "<<avgPoint.z()<<endl;
	mt_inner_nMissingInner = t1.hitPattern().numberOfLostTrackerHits(reco::HitPattern::MISSING_INNER_HITS);
	mt_inner_nMissingOuter = t1.hitPattern().numberOfLostTrackerHits(reco::HitPattern::MISSING_OUTER_HITS);
	mt_outer_nMissingInner = t2.hitPattern().numberOfLostTrackerHits(reco::HitPattern::MISSING_INNER_HITS);
	mt_outer_nMissingOuter = t2.hitPattern().numberOfLostTrackerHits(reco::HitPattern::MISSING_OUTER_HITS);
	mt_inner_qoverp = qoverp1;
	mt_inner_qoverp_err = e1_0;
	mt_inner_lambda = lambda1;
	mt_inner_lambda_err = e1_1;
	mt_inner_phi = phi1;
	mt_inner_phi_err = e1_2;
	mt_inner_dxy = dxy1;
	mt_inner_dxy_err = e1_3;
	mt_inner_dsz = dsz1;
	mt_inner_dsz_err = e1_4;
	mt_outer_qoverp = qoverp2;
	mt_outer_qoverp_err = e2_0;
	mt_outer_lambda = lambda2;
	mt_outer_lambda_err = e2_1;
	mt_outer_phi = phi2;
	mt_outer_phi_err = e2_2;
	mt_outer_dxy = dxy2;
	mt_outer_dxy_err = e2_3;
	mt_outer_dsz = dsz2;
	mt_outer_dsz_err = e2_4;
	mt_dqoverp = qoverp1 - qoverp2;
	mt_dlambda = lambda1 - lambda2;
	mt_dphi = deltaPhi;
	mt_ddxy = dxy1-dxy2;
	mt_ddsz = dsz1-dsz2;

	mt_inner_pdgid = 123456;
	mt_outer_pdgid = 123456;


	double delta3dr = sqrt(pow(mt_inner_outer_x - mt_outer_inner_x,2) + pow(mt_inner_outer_y - mt_outer_inner_y,2) + pow(mt_inner_outer_z - mt_outer_inner_z,2));

	if((pow(mt_inner_outer_x,2)+pow(mt_inner_outer_y,2)) > (pow(mt_outer_inner_x,2)+pow(mt_outer_inner_y,2)))delta3dr *= -1.0;
	/////////////
	//Fill tree//
	/////////////
	if(m_saveTrees)m_duplicate_tree->Fill();

	if(delta3dr < m_minDeltaR3d)continue;
	//if(mt_outer_nMissingInner + mt_inner_nMissingOuter < 3)continue;
	if(mt_inner_nMissingOuter < m_minMissingOuterHitsFromInner)continue;
	if(sqrt(pow(0.5*(t1.outerPosition().x()+t2.innerPosition().x()),2) + pow(0.5*(t1.outerPosition().y()+t2.innerPosition().y()),2)) < m_minAvgRho) continue;


	duplicateInner.push_back(t1);
	duplicateOuter.push_back(t2);
	m_duplicate_qoverp->Fill(qoverp1,qoverp2);
	m_duplicate_lambda->Fill(lambda1,lambda2);
	m_duplicate_phi->Fill(phi1,phi2);
	m_duplicate_dxy->Fill(dxy1,dxy2);
	m_duplicate_dsz->Fill(dsz1,dsz2);
	m_duplicate_pT->Fill(TSCP1.pt(),TSCP2.pt());
	m_duplicate_nHits->Fill(t1.numberOfValidHits(),t2.numberOfValidHits());
	m_duplicate_nMissingHits->Fill(max(t1.hitPattern().numberOfLostTrackerHits(reco::HitPattern::MISSING_INNER_HITS),t1.hitPattern().numberOfLostTrackerHits(reco::HitPattern::MISSING_OUTER_HITS)),max(t2.hitPattern().numberOfLostTrackerHits(reco::HitPattern::MISSING_INNER_HITS),t2.hitPattern().numberOfLostTrackerHits(reco::HitPattern::MISSING_OUTER_HITS)));
	m_duplicate_dqoverp->Fill((qoverp1-qoverp2)/sqrt(e1_0 + e2_0));
	m_duplicate_dlambda->Fill((lambda1-lambda2)/sqrt(e1_1 + e2_1));
	m_duplicate_dphi->Fill(deltaPhi/sqrt(e1_2 + e2_2));
	m_duplicate_ddxy->Fill((dxy1-dxy2)/sqrt(e1_3 + e2_3));
	m_duplicate_ddsz->Fill((dsz1-dsz2)/sqrt(e1_4 + e2_4));
	m_duplicate_q_lambda->Fill((qoverp1-qoverp2)/sqrt(e1_0 + e2_0),(lambda1-lambda2)/sqrt(e1_1 + e2_1));
	m_duplicate_chi2->Fill((qoverp1-qoverp2)/sqrt(e1_0 + e2_0) + (lambda1-lambda2)/sqrt(e1_1 + e2_1) + (phi1-phi2)/sqrt(e1_2 + e2_2) + (dxy1-dxy2)/sqrt(e1_3 + e2_3) + (dsz1-dsz2)/sqrt(e1_4 + e2_4));


	/*	
	if(ttmd.crossingPoint().perp() < 1.0)continue;
	m_duplicate_cut0_pcaR->Fill((qoverp1-qoverp2)/sqrt(e1_0 + e2_0));
	if(fabs(deltaPhi/sqrt(e1_2 + e2_2)) > 5.0)continue;
	m_duplicate_cut1_dphi->Fill((qoverp1-qoverp2)/sqrt(e1_0 + e2_0));
	if(fabs((dsz1-dsz2)/sqrt(e1_4 + e2_4)) > 5.0)continue;
	m_duplicate_cut2_ddsz->Fill((qoverp1-qoverp2)/sqrt(e1_0 + e2_0));
	if(fabs((lambda1-lambda2)/sqrt(e1_1 + e2_1)) > 5.0)continue;
	m_duplicate_cut3_dlambda->Fill((qoverp1-qoverp2)/sqrt(e1_0 + e2_0));
	if(fabs((dxy1-dxy2)/sqrt(e1_3 + e2_3)) > 20.0)continue;
	m_duplicate_cut4_ddxy->Fill((qoverp1-qoverp2)/sqrt(e1_0 + e2_0));
	if(min(t1.numberOfValidHits(),t2.numberOfValidHits()) > 20)continue;
	m_duplicate_cut5_innerR->Fill((qoverp1-qoverp2)/sqrt(e1_0 + e2_0));
	*/
      }
    }
  }


  //    TrackingParticleRef tpr(simTPhandle, i);
  //TrackingParticle* tp=const_cast<TrackingParticle*>(tpr.get());
  //if(simRecColl.find(tpr) == simRecColl.end())continue;
  //vector<pair<RefToBase<Track>, double> > rt = (std::vector<std::pair<RefToBase<Track>, double> >) simRecColl[tpr];
  //if(rt.size() == 0)continue;
  for(int i = 0; i < (int)handle->size(); i++){
    Track rt1 = (handle->at(i));
    if(rt1.innerMomentum().Rho() < minPt)continue;
    if(rt1.innerMomentum().Rho() < minP)continue;
    for(int j = i+1; j < (int)handle->size();j++){
      Track rt2 = (handle->at(j));
      if(rt2.innerMomentum().Rho() < minPt)continue;
      if(rt2.innerMomentum().Rho() < minP)continue;
      if(rt1.charge() != rt2.charge())continue;
      if(matchedTracks.find(rt1) != matchedTracks.end() && compareTracks(matchedTracks[rt1],rt2))continue;
      Track t1,t2;
      if(rt1.outerPosition().Rho() < rt2.outerPosition().Rho()){
	t1 = rt1;
	t2 = rt2;
      }else{
	t1 = rt2;
	t2 = rt1;
      }
      
      FreeTrajectoryState fts1 = trajectoryStateTransform::initialFreeState(t1, &*m_magfield);
      FreeTrajectoryState fts2 = trajectoryStateTransform::initialFreeState(t2, &*m_magfield);
      if(!ttmd.calculate(fts1,fts2)){cerr<<"ttmd failed"<<endl;continue;}
      GlobalPoint avgPoint((t1.outerPosition().x()+t2.innerPosition().x())*0.5,(t1.outerPosition().y()+t2.innerPosition().y())*0.5,(t1.outerPosition().z()+t2.innerPosition().z())*0.5);
      //TrajectoryStateClosestToPoint TSCP1 = tscpBuilder(fts1, ttmd.crossingPoint());
      //TrajectoryStateClosestToPoint TSCP2 = tscpBuilder(fts2, ttmd.crossingPoint());
      TrajectoryStateClosestToPoint TSCP1 = tscpBuilder(fts1, avgPoint);
      TrajectoryStateClosestToPoint TSCP2 = tscpBuilder(fts2, avgPoint);
      if(!TSCP1.isValid())continue;
      if(!TSCP2.isValid())continue;
      const FreeTrajectoryState ftsn1 = TSCP1.theState();
      const FreeTrajectoryState ftsn2 = TSCP2.theState();
 
      mt_dca =  (ftsn2.position()-ftsn1.position()).mag();
	

      m_comb_pcaR->Fill(ttmd.crossingPoint().perp());
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

      m_comb_dqoverp->Fill((qoverp1-qoverp2)/sqrt(e1_0 + e2_0));
      m_comb_dlambda->Fill((lambda1-lambda2)/sqrt(e1_1 + e2_1));
      m_comb_dphi->Fill(deltaPhi/sqrt(e1_2 + e2_2));
      m_comb_ddxy->Fill((dxy1-dxy2)/sqrt(e1_3 + e2_3));
      m_comb_ddsz->Fill((dsz1-dsz2)/sqrt(e1_4 + e2_4));
      m_comb_q_lambda->Fill((qoverp1-qoverp2)/sqrt(e1_0 + e2_0),(lambda1-lambda2)/sqrt(e1_1 + e2_1));      
      m_comb_bestdR->Fill(ttmd.distance());
      m_comb_chi2->Fill((qoverp1-qoverp2)/sqrt(e1_0 + e2_0) + (lambda1-lambda2)/sqrt(e1_1 + e2_1) + (phi1-phi2)/sqrt(e1_2 + e2_2) + (dxy1-dxy2)/sqrt(e1_3 + e2_3) + (dsz1-dsz2)/sqrt(e1_4 + e2_4));


	///////////////////////
	//Fill tree variables//
	///////////////////////
	mt_inner_inner_x = t1.innerPosition().x();
	mt_inner_inner_y = t1.innerPosition().y();
	mt_inner_inner_z = t1.innerPosition().z();
	mt_inner_outer_x = t1.outerPosition().x();
	mt_inner_outer_y = t1.outerPosition().y();
	mt_inner_outer_z = t1.outerPosition().z();
	mt_outer_inner_x = t2.innerPosition().x();
	mt_outer_inner_y = t2.innerPosition().y();
	mt_outer_inner_z = t2.innerPosition().z();
	mt_outer_outer_x = t2.outerPosition().x();
	mt_outer_outer_y = t2.outerPosition().y();
	mt_outer_outer_z = t2.outerPosition().z();
	mt_pca_x = ttmd.crossingPoint().x();
	mt_pca_y = ttmd.crossingPoint().y();
	mt_pca_z = ttmd.crossingPoint().z();
	mt_delta3d_x = (mt_inner_outer_x + mt_outer_inner_x)/2.;
	mt_delta3d_y = (mt_inner_outer_y + mt_outer_inner_y)/2.;
	mt_delta3d_z = (mt_inner_outer_z + mt_outer_inner_z)/2.;
	mt_delta3d_r = sqrt(pow(mt_delta3d_x,2) + pow(mt_delta3d_y,2));
	mt_inner_nMissingInner = t1.hitPattern().numberOfLostTrackerHits(reco::HitPattern::MISSING_INNER_HITS);
	mt_inner_nMissingOuter = t1.hitPattern().numberOfLostTrackerHits(reco::HitPattern::MISSING_OUTER_HITS);
	mt_outer_nMissingInner = t2.hitPattern().numberOfLostTrackerHits(reco::HitPattern::MISSING_INNER_HITS);
	mt_outer_nMissingOuter = t2.hitPattern().numberOfLostTrackerHits(reco::HitPattern::MISSING_OUTER_HITS);
	mt_inner_qoverp = qoverp1;
	mt_inner_qoverp_err = e1_0;
	mt_inner_lambda = lambda1;
	mt_inner_lambda_err = e1_1;
	mt_inner_phi = phi1;
	mt_inner_phi_err = e1_2;
	mt_inner_dxy = dxy1;
	mt_inner_dxy_err = e1_3;
	mt_inner_dsz = dsz1;
	mt_inner_dsz_err = e1_4;
	mt_outer_qoverp = qoverp2;
	mt_outer_qoverp_err = e2_0;
	mt_outer_lambda = lambda2;
	mt_outer_lambda_err = e2_1;
	mt_outer_phi = phi2;
	mt_outer_phi_err = e2_2;
	mt_outer_dxy = dxy2;
	mt_outer_dxy_err = e2_3;
	mt_outer_dsz = dsz2;
	mt_outer_dsz_err = e2_4;
	mt_dqoverp = qoverp1 - qoverp2;
	mt_dlambda = lambda1 - lambda2;
	mt_dphi = deltaPhi;
	mt_ddxy = dxy1-dxy2;
	mt_ddsz = dsz1-dsz2;
	mt_inner_pdgid = 123456;
	mt_outer_pdgid = 123456;

	double delta3dr = sqrt(pow(mt_inner_outer_x - mt_outer_inner_x,2) + pow(mt_inner_outer_y - mt_outer_inner_y,2) + pow(mt_inner_outer_z - mt_outer_inner_z,2));

	if((pow(mt_inner_outer_x,2)+pow(mt_inner_outer_y,2)) > (pow(mt_outer_inner_x,2)+pow(mt_outer_inner_y,2)))delta3dr *= -1.0;


	/////////////
	//Fill tree//
	/////////////

	/*
	if(delta3dr < -4.0)continue;
	//if(mt_outer_nMissingInner + mt_inner_nMissingOuter < 3)continue;
	if(mt_inner_nMissingOuter < 2)continue;
	if(sqrt(pow(0.5*(t1.outerPosition().x()+t2.innerPosition().x()),2) + pow(0.5*(t1.outerPosition().y()+t2.innerPosition().y()),2)) < 15) continue;
	*/
	if(delta3dr > m_minDeltaR3d && mt_inner_nMissingOuter > (m_minMissingOuterHitsFromInner-1) && sqrt(pow(0.5*(t1.outerPosition().x()+t2.innerPosition().x()),2) + pow(0.5*(t1.outerPosition().y()+t2.innerPosition().y()),2)) > m_minAvgRho){

	  if(innerMatchedTracks.find(t1) != innerMatchedTracks.end()){
	    innerMatchedTracks[t1].push_back(t2);
	  }else{
	    vector<Track> imt;
	    imt.push_back(t2);
	    innerMatchedTracks[t1] = imt;
	  }
	  if(outerMatchedTracks.find(t2) != outerMatchedTracks.end()){
	    outerMatchedTracks[t2].push_back(t1);
	  }else{
	    vector<Track> omt;
	    omt.push_back(t1);
	    outerMatchedTracks[t2] = omt;
	  }

	  m_comb_qoverp->Fill(qoverp1,qoverp2);
	  m_comb_lambda->Fill(lambda1,lambda2);
	  m_comb_phi->Fill(phi1,phi2);
	  m_comb_dxy->Fill(dxy1,dxy2);
	  m_comb_dsz->Fill(dsz1,dsz2);
	  m_comb_pT->Fill(TSCP1.pt(),TSCP2.pt());
	  m_comb_nHits->Fill(t1.numberOfValidHits(),t2.numberOfValidHits());
	  m_comb_nMissingHits->Fill(max(t1.hitPattern().numberOfLostTrackerHits(reco::HitPattern::MISSING_INNER_HITS),t1.hitPattern().numberOfLostTrackerHits(reco::HitPattern::MISSING_OUTER_HITS)),max(t2.hitPattern().numberOfLostTrackerHits(reco::HitPattern::MISSING_INNER_HITS),t2.hitPattern().numberOfLostTrackerHits(reco::HitPattern::MISSING_OUTER_HITS)));
	  m_comb_dqoverp->Fill((qoverp1-qoverp2)/sqrt(e1_0 + e2_0));
	  m_comb_dlambda->Fill((lambda1-lambda2)/sqrt(e1_1 + e2_1));
	  m_comb_dphi->Fill(deltaPhi/sqrt(e1_2 + e2_2));
	  m_comb_ddxy->Fill((dxy1-dxy2)/sqrt(e1_3 + e2_3));
	  m_comb_ddsz->Fill((dsz1-dsz2)/sqrt(e1_4 + e2_4));
	  m_comb_q_lambda->Fill((qoverp1-qoverp2)/sqrt(e1_0 + e2_0),(lambda1-lambda2)/sqrt(e1_1 + e2_1));      
	  m_comb_bestdR->Fill(ttmd.distance());
	  m_comb_chi2->Fill((qoverp1-qoverp2)/sqrt(e1_0 + e2_0) + (lambda1-lambda2)/sqrt(e1_1 + e2_1) + (phi1-phi2)/sqrt(e1_2 + e2_2) + (dxy1-dxy2)/sqrt(e1_3 + e2_3) + (dsz1-dsz2)/sqrt(e1_4 + e2_4));
	  
	  RefToBase<Track> trackRef1(handle,i);
	  RefToBase<Track> trackRef2(handle,j);
	  vector<pair<TrackingParticleRef, double> > tp1;
	  vector<pair<TrackingParticleRef, double> > tp2;
	  TrackingParticleRef tpr1;
	  TrackingParticleRef tpr2;
	  //TrackingParticle* tp=const_cast<TrackingParticle*>(tpr.get());
	  int nFake = 0;
	  
	  if(recSimColl.find(trackRef1) != recSimColl.end())tp1 = recSimColl[trackRef1];
	  if(recSimColl.find(trackRef2) != recSimColl.end())tp2 = recSimColl[trackRef2];
	  if(tp1.size() > 0)tpr1 = tp1[0].first;
	  else nFake++;
	  if(tp2.size() > 0)tpr2 = tp2[0].first;
	  else nFake++;
	  
	  m_comb_nFakes->Fill(nFake);
	  if(nFake == 0){
	    TrackingParticle* tp1=const_cast<TrackingParticle*>(tpr1.get());
	    TrackingParticle* tp2=const_cast<TrackingParticle*>(tpr2.get());
	    TrackingVertexRef vr2 = tp2->parentVertex();
	    TrackingVertex* tv2 = const_cast<TrackingVertex*>(vr2.get());
	    TrackingParticleRefVector tprv2= tv2->sourceTracks();
	    int parentDaughter = 0;
	    mt_inner_pdgid = tp1->pdgId();
	    mt_outer_pdgid = tp2->pdgId();
	    for(int lll = 0; lll < (int)tprv2.size(); lll++){
	      if(tprv2[lll] == tpr1){
		parentDaughter = 1;
		m_comb_outerV->Fill(tp2->vz(),tp2->vertex().Rho());
		double dv = sqrt(pow(tp2->vertex().x() - tv2->position().x(),2) + pow(tp2->vertex().y() - tv2->position().y(),2) + pow(tp2->vertex().z() - tv2->position().z(),2));
		if(tp2->vertex().Rho() < tv2->position().Rho()) dv *= -1;
		m_comb_deltaV->Fill(dv);
		
	      }
	    }
	    m_comb_parentDaughter->Fill(parentDaughter);
	    //TrackingVertexRefVector vr1 = tp1->decayVertices();
	    //float bestDr = 9999.0;
	    //float bestSign = 0.0;
	    
	    
	  }
	}
	if(m_saveTrees)m_comb_tree->Fill();
	if(trackInCollection(t1,handleHighPurity))m_nCombinatoricsInnerHighPurity++;

	/*
      if(ttmd.crossingPoint().perp() < 1.0)continue;
      m_comb_cut0_pcaR->Fill((qoverp1-qoverp2)/sqrt(e1_0 + e2_0));
      if(fabs(deltaPhi/sqrt(e1_2 + e2_2)) > 5.0)continue;
      m_comb_cut1_dphi->Fill((qoverp1-qoverp2)/sqrt(e1_0 + e2_0));
      if(fabs((dsz1-dsz2)/sqrt(e1_4 + e2_4)) > 5.0)continue;
      m_comb_cut2_ddsz->Fill((qoverp1-qoverp2)/sqrt(e1_0 + e2_0));
      if(fabs((lambda1-lambda2)/sqrt(e1_1 + e2_1)) > 5.0)continue;
      m_comb_cut3_dlambda->Fill((qoverp1-qoverp2)/sqrt(e1_0 + e2_0));
      if(fabs((dxy1-dxy2)/sqrt(e1_3 + e2_3)) > 20.0)continue;
      m_comb_cut4_ddxy->Fill((qoverp1-qoverp2)/sqrt(e1_0 + e2_0));
      if(min(rt1.numberOfValidHits(),rt2.numberOfValidHits()) > 20)continue;
      m_comb_cut5_innerR->Fill((qoverp1-qoverp2)/sqrt(e1_0 + e2_0));
	*/
    }
  }

  map<Track,vector<Track>,trackCompare>::const_iterator omt_iter;
  for(omt_iter = innerMatchedTracks.begin(); omt_iter != innerMatchedTracks.end(); omt_iter++){
    m_comb_innerMatched->Fill((*omt_iter).second.size());
  }
  for(omt_iter = outerMatchedTracks.begin(); omt_iter != outerMatchedTracks.end(); omt_iter++){
    m_comb_outerMatched->Fill((*omt_iter).second.size());
  }

  for(int i = 0; i < (int)duplicateInner.size(); i++){
    Track rt1 = duplicateInner[i];
    int nMatches = 0;
    int nFake = 0;
    int nReal = 0;
    for(int j = 0; j < (int)handle->size(); j++){
      Track rt2 = (handle->at(j));
      if(rt1.charge() != rt2.charge())continue;
      if(compareTracks(rt1,rt2))continue;
      bool isMatch = compareTracks(rt2,duplicateOuter[i]);

      Track t1,t2;
      if(rt1.outerPosition().Rho() < rt2.outerPosition().Rho()){
	t1 = rt1;
	t2 = rt2;
      }else{
	t1 = rt2;
	t2 = rt1;
      }
      mt_inner_inner_x = t1.innerPosition().x();
      mt_inner_inner_y = t1.innerPosition().y();
      mt_inner_inner_z = t1.innerPosition().z();
      mt_inner_outer_x = t1.outerPosition().x();
      mt_inner_outer_y = t1.outerPosition().y();
      mt_inner_outer_z = t1.outerPosition().z();
      mt_outer_inner_x = t2.innerPosition().x();
      mt_outer_inner_y = t2.innerPosition().y();
      mt_outer_inner_z = t2.innerPosition().z();
      mt_outer_outer_x = t2.outerPosition().x();
      mt_outer_outer_y = t2.outerPosition().y();
      mt_outer_outer_z = t2.outerPosition().z();
      mt_inner_nMissingInner = t1.hitPattern().numberOfLostTrackerHits(reco::HitPattern::MISSING_INNER_HITS);
      mt_inner_nMissingOuter = t1.hitPattern().numberOfLostTrackerHits(reco::HitPattern::MISSING_OUTER_HITS);
      mt_outer_nMissingInner = t2.hitPattern().numberOfLostTrackerHits(reco::HitPattern::MISSING_INNER_HITS);
      mt_outer_nMissingOuter = t2.hitPattern().numberOfLostTrackerHits(reco::HitPattern::MISSING_OUTER_HITS);
      double delta3dr = sqrt(pow(mt_inner_outer_x - mt_outer_inner_x,2) + pow(mt_inner_outer_y - mt_outer_inner_y,2) + pow(mt_inner_outer_z - mt_outer_inner_z,2));
      if((pow(mt_inner_outer_x,2)+pow(mt_inner_outer_y,2)) > (pow(mt_outer_inner_x,2)+pow(mt_outer_inner_y,2)))delta3dr *= -1.0;

      if(delta3dr < m_minDeltaR3d)continue;
      //if(mt_outer_nMissingInner + mt_inner_nMissingOuter < 3)continue;
      if(mt_inner_nMissingOuter < m_minMissingOuterHitsFromInner)continue;
      if(sqrt(pow(0.5*(t1.outerPosition().x()+t2.innerPosition().x()),2) + pow(0.5*(t1.outerPosition().y()+t2.innerPosition().y()),2)) < m_minAvgRho) continue;
      RefToBase<Track> trackRef2(handle,j);
      vector<pair<TrackingParticleRef, double> > tp2;
      TrackingParticleRef tpr2;
      if(recSimColl.find(trackRef2) != recSimColl.end())tp2 = recSimColl[trackRef2];
      if(tp2.size() > 0){
	tpr2 = tp2[0].first;
	//int outerpdg = tpr2->pdgId();
	if(!isMatch)nReal++;
      }else{
	nFake++;
      }

      nMatches++;
    }
    m_duplicate_innerMatched->Fill(nMatches);
    m_duplicate_innerMatchedRealFake->Fill(nFake,nReal);
  }

  for(int i = 0; i < (int)duplicateOuter.size(); i++){
    Track rt1 = duplicateOuter[i];
    int nMatches = 0;
    int nFake = 0;
    int nReal = 0;
    for(int j = 0; j < (int)handle->size(); j++){
      Track rt2 = (handle->at(j));
      if(rt1.charge() != rt2.charge())continue;
      if(compareTracks(rt1,rt2))continue;
      bool isMatch = compareTracks(rt2,duplicateInner[i]);
      Track t1,t2;
      if(rt1.outerPosition().Rho() < rt2.outerPosition().Rho()){
	t1 = rt1;
	t2 = rt2;
      }else{
	t1 = rt2;
	t2 = rt1;
      }
      mt_inner_inner_x = t1.innerPosition().x();
      mt_inner_inner_y = t1.innerPosition().y();
      mt_inner_inner_z = t1.innerPosition().z();
      mt_inner_outer_x = t1.outerPosition().x();
      mt_inner_outer_y = t1.outerPosition().y();
      mt_inner_outer_z = t1.outerPosition().z();
      mt_outer_inner_x = t2.innerPosition().x();
      mt_outer_inner_y = t2.innerPosition().y();
      mt_outer_inner_z = t2.innerPosition().z();
      mt_outer_outer_x = t2.outerPosition().x();
      mt_outer_outer_y = t2.outerPosition().y();
      mt_outer_outer_z = t2.outerPosition().z();
      mt_inner_nMissingInner = t1.hitPattern().numberOfLostTrackerHits(reco::HitPattern::MISSING_INNER_HITS);
      mt_inner_nMissingOuter = t1.hitPattern().numberOfLostTrackerHits(reco::HitPattern::MISSING_OUTER_HITS);
      mt_outer_nMissingInner = t2.hitPattern().numberOfLostTrackerHits(reco::HitPattern::MISSING_INNER_HITS);
      mt_outer_nMissingOuter = t2.hitPattern().numberOfLostTrackerHits(reco::HitPattern::MISSING_OUTER_HITS);
      double delta3dr = sqrt(pow(mt_inner_outer_x - mt_outer_inner_x,2) + pow(mt_inner_outer_y - mt_outer_inner_y,2) + pow(mt_inner_outer_z - mt_outer_inner_z,2));
      if((pow(mt_inner_outer_x,2)+pow(mt_inner_outer_y,2)) > (pow(mt_outer_inner_x,2)+pow(mt_outer_inner_y,2)))delta3dr *= -1.0;
      if(delta3dr < m_minDeltaR3d)continue;
      //if(mt_outer_nMissingInner + mt_inner_nMissingOuter < 3)continue;
      if(mt_inner_nMissingOuter < m_minMissingOuterHitsFromInner)continue;
      if(sqrt(pow(0.5*(t1.outerPosition().x()+t2.innerPosition().x()),2) + pow(0.5*(t1.outerPosition().y()+t2.innerPosition().y()),2)) < m_minAvgRho) continue;

      RefToBase<Track> trackRef2(handle,j);
      vector<pair<TrackingParticleRef, double> > tp2;
      TrackingParticleRef tpr2;
      if(recSimColl.find(trackRef2) != recSimColl.end())tp2 = recSimColl[trackRef2];
      if(tp2.size() > 0){
	tpr2 = tp2[0].first;
	//int innerpdg = tpr2->pdgId();
	if(!isMatch)nReal++;
      }else{
	nFake++;
      }


      nMatches++;
    }
    m_duplicate_outerMatched->Fill(nMatches);
    m_duplicate_outerMatchedRealFake->Fill(nFake,nReal);
  }

}
//------------------------------------------------------------
//------------------------------------------------------------
int MWTrackAnalyzer::numberOfSharedHits(Track t1,Track t2)
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
float MWTrackAnalyzer::bestDeltaR(Track t1,Track t2)
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
    m_minDelta->Fill(d1);
    m_duplicate_deltaR->Fill(t1inner.Rho() - t2outer.Rho());
  }else{
    t1p = t1.outerMomentum();
    t2p = t2.innerMomentum();
    m_minDelta->Fill(d2);
    m_duplicate_deltaR->Fill(t2inner.Rho() - t1outer.Rho());
  }
  return deltaR(t1p,t2p);

}
//------------------------------------------------------------
//------------------------------------------------------------
bool MWTrackAnalyzer::compareTracks(Track t1,Track t2)
{
  if(t1.innerPosition() != t2.innerPosition())return false;
  if(t1.outerPosition() != t2.outerPosition())return false;
  if(t1.innerMomentum() != t2.innerMomentum())return false;
  if(t1.outerMomentum() != t2.outerMomentum())return false;
  return true;

}
//------------------------------------------------------------
//------------------------------------------------------------
bool MWTrackAnalyzer::trackInCollection(Track t,Handle<View<Track> > coll)
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
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------

DEFINE_FWK_MODULE(MWTrackAnalyzer);
