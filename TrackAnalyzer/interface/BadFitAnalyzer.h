#ifndef MWALKER_TRACKANALYZER_BADFITANALYZER
#define MWALKER_TRACKANALYZER_BADFITANALYZER


#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/ESHandle.h"
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
#include "SimDataFormats/Associations/interface/TrackToTrackingParticleAssociator.h"
#include "SimTracker/TrackAssociatorProducers/plugins/QuickTrackAssociatorByHitsImpl.h"
#include "CommonTools/Utils/interface/StringCutObjectSelector.h"
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

class MWBadFitAnalyzer : public edm::EDAnalyzer {
 public:
  explicit MWBadFitAnalyzer(const edm::ParameterSet& iPara);
  ~MWBadFitAnalyzer();

 private:
  virtual void beginJob();
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  void beginRun(const edm::Run&, const edm::EventSetup&);
  void endRun(  const edm::Run&, const edm::EventSetup&);
  virtual void endJob();

  int fixPdgId(int);

  bool compareTracks(reco::Track t1,reco::Track t2);
  bool trackInCollection(reco::Track t,edm::Handle<edm::View<reco::Track> > coll);

  const reco::TrackToTrackingParticleAssociator* m_associator;
  std::string m_source;
  std::string m_associatorName;
  TFile* m_outFile;
  double m_probCut;
  edm::InputTag m_simSource;

  TH1F* m_nSimAssoc;
  TH1F* m_pT;
  TH2F* m_etaPhi;
  TH2F* m_pTinnerOuter;
  TH2F* m_nMissing;
  TH1F* m_sumResiduals;
  TH1F* m_sumResidualsBad;
  TH1F* m_numberHits;
  TH1F* m_numberHitsBad;
  TH1F* m_residualLocus;
  TH1F* m_residualLocusBad;
  TH1F* m_maxResidual;
  TH1F* m_maxResidualBad;
  TH1F* m_qoverp;
  TH1F* m_lambda;
  TH1F* m_phi;
  TH1F* m_dxy;
  TH1F* m_dsz;
  TH1F* m_qoverpBad;
  TH1F* m_lambdaBad;
  TH1F* m_phiBad;
  TH1F* m_dxyBad;
  TH1F* m_dszBad;
  TH1F* m_associatedFraction;
  TH1F* m_associatedFractionBad;
  TH1F* m_pdgid;
  TH1F* m_pdgidBad;
  edm::ESHandle<MagneticField> m_magfield;
};
class trackCompare{
 public:
  bool operator()(const reco::Track t1, const reco::Track t2){return t1.innerMomentum().Rho() > t2.innerMomentum().Rho();}
};

#endif
