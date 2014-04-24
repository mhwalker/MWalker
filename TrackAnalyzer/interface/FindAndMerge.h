#ifndef MWALKER_TRACKANALYZER_FINDANDMERGE
#define MWALKER_TRACKANALYZER_FINDANDMERGE


#include "FWCore/Framework/interface/EDProducer.h"
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
#include "RecoTracker/TrackProducer/interface/TrackMerger.h"
#include "SimDataFormats/TrackingAnalysis/interface/TrackingParticle.h"
//#include "MWalker/Utilities/interface/DuplicateRecord.h"
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
#include "TMVA/Reader.h"
//#include "TClonesArray.h"

namespace edm{
  class Event;
  class EventSetup;
  class ParameterSet;
}

class MWFindAndMerge : public edm::EDProducer {
 public:
  explicit MWFindAndMerge(const edm::ParameterSet& iPara);
  ~MWFindAndMerge();

  virtual void produce(edm::Event&, const edm::EventSetup&);
 private:
  virtual void beginJob();
  void beginRun(const edm::Run&, const edm::EventSetup&);
  void endRun(  const edm::Run&, const edm::EventSetup&);
  virtual void endJob();

  int m_minMissingOuterHitsFromInner;
  double m_minDeltaR3d;
  double m_minAvgRho;
  double m_minBDTG;

  TMVA::Reader* m_tmvaReader;

  float m_tmva_ddsz;
  float m_tmva_ddxy;
  float m_tmva_dphi;
  float m_tmva_dlambda;
  float m_tmva_dqoverp;
  float m_tmva_d3dr;
  float m_tmva_d3dz;
  float m_tmva_outer_nMissingInner;
  float m_tmva_inner_nMissingOuter;

  int numberOfSharedHits(reco::Track t1, reco::Track t2);
  float bestDeltaR(reco::Track t1, reco::Track t2);
  bool compareTracks(reco::Track t1,reco::Track t2);

  bool m_produceDuplicates;

  TH1F* m_duplicatesMerged_eta;
  TH1F* m_combMerged_eta;

  int m_nDuplicates;
  int m_nDuplicatesGood;
  int m_nDuplicatesMerged;

  int m_nCombinatorics;
  int m_nCombinatoricsGood;
  int m_nCombinatoricsMerged;

  const TrackAssociatorBase* m_associator;
  TrackMerger merger_;

  unsigned int m_totalEvents;
  std::string m_associatorName;
  std::string m_source;
  //std::string m_weightsFile;
  edm::InputTag m_simSource;
  TFile* m_outFile;


  edm::ESHandle<MagneticField> m_magfield;
};
class trackCompare{
 public:
  bool operator()(const reco::Track t1, const reco::Track t2){return t1.innerMomentum().Rho() > t2.innerMomentum().Rho();}
};

#endif
