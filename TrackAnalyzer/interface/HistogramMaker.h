#ifndef MWALKER_TRACKANALYZER_HISTOGRAMMAKER
#define MWALKER_TRACKANALYZER_HISTOGRAMMAKER


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

class MWHistogramMaker : public edm::EDAnalyzer {
 public:
  explicit MWHistogramMaker(const edm::ParameterSet& iPara);
  ~MWHistogramMaker();

 private:
  virtual void beginJob();
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  void beginRun(const edm::Run&, const edm::EventSetup&);
  void endRun(  const edm::Run&, const edm::EventSetup&);
  virtual void endJob();

  TFile* m_outFile;
  std::string m_source;

  TH1F* m_hpt;
  TH2F* m_hetaphi;

};

#endif
