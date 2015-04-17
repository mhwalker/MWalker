#ifndef MWALKER_DUPLICATEANALYZER_DUPLICATEANALYZER
#define MWALKER_DUPLICATEANALYZER_DUPLICATEANALYZER


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
#include "MagneticField/Engine/interface/MagneticField.h"
#include "DataFormats/TrackCandidate/interface/TrackCandidate.h"
#include "DataFormats/TrackingRecHit/interface/TrackingRecHit.h"
#include "SimDataFormats/Associations/interface/TrackToTrackingParticleAssociator.h"
#include "SimTracker/TrackAssociatorProducers/plugins/QuickTrackAssociatorByHitsImpl.h"
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

class MWDuplicateAnalyzer : public edm::EDAnalyzer {
 public:
  typedef std::vector<TrackCandidate> TrackCandidateCollection;
  typedef edm::OwnVector<TrackingRecHit> RecHitContainer;

  explicit MWDuplicateAnalyzer(const edm::ParameterSet& iPara);
  ~MWDuplicateAnalyzer();



 private:
  virtual void beginJob();
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  void beginRun(const edm::Run&, const edm::EventSetup&);
  void endRun(  const edm::Run&, const edm::EventSetup&);
  virtual void endJob();

  int m_minMissingOuterHitsFromInner;
  double m_minDeltaR3d;
  double m_minAvgRho;

  int matchCandidateToTrack(TrackCandidate,edm::Handle<edm::View<reco::Track> >);

  int numberOfSharedHits(reco::Track t1, reco::Track t2);
  bool compareTracks(reco::Track t1,reco::Track t2);
  bool trackInCollection(reco::Track t,edm::Handle<edm::View<reco::Track> > coll);
  const reco::TrackToTrackingParticleAssociator* m_associator;

  unsigned int m_totalEvents;
  unsigned int m_totalDuplicates;
  unsigned int m_realDuplicates;
  unsigned int m_realDuplicatesFit;
  unsigned int m_realDuplicatesFinal;
  unsigned int m_fakeDuplicates;
  unsigned int m_fakeDuplicatesFit;
  unsigned int m_fakeDuplicatesFinal;
  unsigned int m_matchedCandidates;
  std::string m_associatorName;
  std::string m_trackSource;
  edm::InputTag m_simSource;

  edm::InputTag m_duplicateCandidateSource;
  //std::string m_duplicateCandidateSource;

  edm::InputTag m_duplicateRecordSource;

  std::string m_duplicateFitSource;

  std::string m_duplicateFinalSource;

  TFile* m_outFile;

  edm::ESHandle<MagneticField> m_magfield;
};

#endif
