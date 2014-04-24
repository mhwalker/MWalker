#ifndef MWALKER_TRACKANALYZER_TRACKANALYZER
#define MWALKER_TRACKANALYZER_TRACKANALYZER


#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Provenance/interface/ParameterSetID.h"
#include "DataFormats/Candidate/interface/LeafCandidate.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackExtra.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "TrackingTools/PatternTools/interface/Trajectory.h"
#include "TrackingTools/PatternTools/interface/TrajTrackAssociation.h"
#include "DataFormats/TrackerRecHit2D/interface/SiStripRecHit1D.h"
#include "CommonTools/Utils/interface/StringCutObjectSelector.h"
#include "SimTracker/TrackAssociation/interface/TrackAssociatorByChi2.h"
#include "SimTracker/TrackAssociation/interface/TrackAssociatorBase.h"
#include "MagneticField/Engine/interface/MagneticField.h"
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>
#include <map>

#include "TTree.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TFile.h"
#include "TLorentzVector.h"
#include "TString.h"
//#include "TClonesArray.h"

namespace edm{
  class Event;
  class EventSetup;
  class ParameterSet;
}

class MWTrackAnalyzer : public edm::EDAnalyzer {
 public:
  explicit MWTrackAnalyzer(const edm::ParameterSet& iPara);
  ~MWTrackAnalyzer();

 private:
  virtual void beginJob();
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  void beginRun(const edm::Run&, const edm::EventSetup&);
  void endRun(  const edm::Run&, const edm::EventSetup&);
  virtual void endJob();

  int m_minMissingOuterHitsFromInner;
  double m_minDeltaR3d;
  double m_minAvgRho;
  double m_minPt;
  double m_minP;

  int m_nDuplicateInnerHighPurity;
  int m_nCombinatoricsInnerHighPurity;

  int numberOfSharedHits(reco::Track t1, reco::Track t2);
  float bestDeltaR(reco::Track t1, reco::Track t2);
  bool compareTracks(reco::Track t1,reco::Track t2);
  bool trackInCollection(reco::Track t,edm::Handle<edm::View<reco::Track> > coll);

  const TrackAssociatorBase* m_associator;
  TH1F* m_hnTracks;
  TH1F* m_hmatchedTracks;
  TH1F* m_duplicate_eta;
  TH1F* m_duplicate_pdR;
  TH1F* m_duplicate_bestdR;
  TH1F* m_duplicate_deltapT;
  TH1F* m_duplicate_diffpT;
  TH1F* m_duplicate_vdR;
  TH1F* m_duplicate_nSharedHits;
  TH1F* m_hmatchedPerTrack;
  TH1F* m_minDelta;
  TH2F* m_duplicate_qoverp;
  TH2F* m_duplicate_phi;
  TH2F* m_duplicate_lambda;
  TH2F* m_duplicate_dxy;
  TH2F* m_duplicate_dsz;
  TH2F* m_duplicate_innerR;
  TH2F* m_duplicate_nHits;
  TH2F* m_duplicate_nMissingHits;
  TH2F* m_duplicate_pT;
  TH2F* m_duplicate_outerR;
  TH1F* m_duplicate_deltaR;
  TH1F* m_duplicate_innerMatched;
  TH1F* m_duplicate_outerMatched;
  TH2F* m_duplicate_innerMatchedRealFake;
  TH2F* m_duplicate_outerMatchedRealFake;

  TH1F* m_comb_dqoverp;
  TH1F* m_comb_dlambda;
  TH1F* m_comb_dphi;
  TH1F* m_comb_ddxy;
  TH1F* m_comb_ddsz;
  TH2F* m_comb_q_lambda;
  TH1F* m_comb_bestdR;
  TH1F* m_comb_chi2;
  TH1F* m_comb_pcaR;
  TH2F* m_comb_qoverp;
  TH2F* m_comb_phi;
  TH2F* m_comb_lambda;
  TH2F* m_comb_dxy;
  TH2F* m_comb_dsz;
  TH2F* m_comb_nHits;
  TH2F* m_comb_nMissingHits;
  TH2F* m_comb_pT;
  TH1F* m_comb_nFakes;
  TH1F* m_comb_deltaV;
  TH1F* m_comb_parentDaughter;
  TH2F* m_comb_outerV;
  TH1F* m_comb_innerMatched;
  TH1F* m_comb_outerMatched;

  TH1F* m_comb_cut0_pcaR;//0
  TH1F* m_comb_cut1_dphi;//5
  TH1F* m_comb_cut2_ddsz;//5
  TH1F* m_comb_cut3_dlambda;//5
  TH1F* m_comb_cut4_ddxy;//20
  TH1F* m_comb_cut5_innerR;//20

  TH1F* m_duplicate_dqoverp;
  TH1F* m_duplicate_dlambda;
  TH1F* m_duplicate_dphi;
  TH1F* m_duplicate_ddxy;
  TH1F* m_duplicate_ddsz;
  TH2F* m_duplicate_q_lambda;
  TH1F* m_duplicate_chi2;
  TH1F* m_duplicate_pcaR;

  TH1F* m_duplicate_cut0_pcaR;//0
  TH1F* m_duplicate_cut1_dphi;//5
  TH1F* m_duplicate_cut2_ddsz;//5
  TH1F* m_duplicate_cut3_dlambda;//5
  TH1F* m_duplicate_cut4_ddxy;//20
  TH1F* m_duplicate_cut5_innerR;//20

  unsigned int m_totalEvents;
  std::string m_associatorName;
  std::string m_source;
  edm::InputTag m_simSource;
  TFile* m_outFile;

  TTree* m_duplicate_tree;
  TTree* m_comb_tree;
  double mt_inner_inner_x;
  double mt_inner_inner_y;
  double mt_inner_inner_z;
  double mt_inner_outer_x;
  double mt_inner_outer_y;
  double mt_inner_outer_z;
  double mt_outer_inner_x;
  double mt_outer_inner_y;
  double mt_outer_inner_z;
  double mt_outer_outer_x;
  double mt_outer_outer_y;
  double mt_outer_outer_z;
  double mt_pca_x;
  double mt_pca_y;
  double mt_pca_z;
  double mt_delta3d_x;
  double mt_delta3d_y;
  double mt_delta3d_z;
  double mt_delta3d_r;
  int mt_inner_nMissingInner;
  int mt_inner_nMissingOuter;
  int mt_outer_nMissingInner;
  int mt_outer_nMissingOuter;
  double mt_inner_qoverp;
  double mt_inner_qoverp_err;
  double mt_inner_lambda;
  double mt_inner_lambda_err;
  double mt_inner_phi;
  double mt_inner_phi_err;
  double mt_inner_dxy;
  double mt_inner_dxy_err;
  double mt_inner_dsz;
  double mt_inner_dsz_err;
  double mt_outer_qoverp;
  double mt_outer_qoverp_err;
  double mt_outer_lambda;
  double mt_outer_lambda_err;
  double mt_outer_phi;
  double mt_outer_phi_err;
  double mt_outer_dxy;
  double mt_outer_dxy_err;
  double mt_outer_dsz;
  double mt_outer_dsz_err;
  double mt_dqoverp;
  double mt_dlambda;
  double mt_dphi;
  double mt_ddxy;
  double mt_ddsz;
  double mt_dca;

  int mt_inner_pdgid;
  int mt_outer_pdgid;

  bool m_saveTrees;

  edm::ESHandle<MagneticField> m_magfield;
};
class trackCompare{
 public:
  bool operator()(const reco::Track t1, const reco::Track t2){return t1.innerMomentum().Rho() > t2.innerMomentum().Rho();}
};

#endif
