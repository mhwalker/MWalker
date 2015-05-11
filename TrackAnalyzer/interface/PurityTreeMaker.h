#ifndef MWALKER_TRACKANALYZER_PURITYTREEKMAKER
#define MWALKER_TRACKANALYZER_PURITYTREEMAKER


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
#include "CommonTools/Utils/interface/StringCutObjectSelector.h"
#include "MagneticField/Engine/interface/MagneticField.h"
#include "SimDataFormats/Associations/interface/TrackToTrackingParticleAssociator.h"
#include "DataFormats/Math/interface/Point3D.h"
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

#include "TMVA/Reader.h"

namespace edm{
  class Event;
  class EventSetup;
  class ParameterSet;
}

class MWPurityTreeMaker : public edm::EDAnalyzer {
 public:
  explicit MWPurityTreeMaker(const edm::ParameterSet& iPara);
  ~MWPurityTreeMaker();

  typedef math::XYZPoint Point;

 private:
  virtual void beginJob();
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  void beginRun(const edm::Run&, const edm::EventSetup&);
  void endRun(  const edm::Run&, const edm::EventSetup&);
  virtual void endJob();

  Point getBestVertex(reco::TrackBaseRef,reco::VertexCollection);

  const reco::TrackToTrackingParticleAssociator* m_associator;
  std::string m_source;
  std::string m_associatorName;
  TFile* m_outFile;
  edm::InputTag m_simSource;
  edm::InputTag beamspot_;
  edm::EDGetTokenT<reco::VertexCollection> m_vertices;

  float m_tvFake;
  float m_tvIter;
  float m_tvNdof;
  float m_tvpt;
  float m_tvNlayers;
  float m_tvNlayers3D;
  float m_tvNlayersLost;
  float m_tvChi2n;
  float m_tvChi2n_no1Dmod;
  float m_tvEta;
  float m_tvRelPtErr;
  float m_tvNhits;
  float m_tvLostIn;
  float m_tvLostOut;
  float m_tvMinLost;
  float m_tvLostMidFrac;
  float m_tvAbsDz;
  float m_tvAbsD0;
  float m_tvAbsDzPV;
  float m_tvAbsD0PV;
  float m_tvMvaVal;

  bool doMVA_;
  TMVA::Reader* tmvaReader_;
  std::string mvaType_;

  TTree* m_outTree;

  edm::ESHandle<MagneticField> m_magfield;
};
class trackCompare{
 public:
  bool operator()(const reco::Track t1, const reco::Track t2){return t1.innerMomentum().Rho() > t2.innerMomentum().Rho();}
};

#endif
