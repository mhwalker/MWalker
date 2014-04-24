#include "MWalker/TrackAnalyzer/interface/CompareCandidateToTrack.h"

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

MWCompareCandidateToTrack::MWCompareCandidateToTrack(const edm::ParameterSet& iPara) 
{
  m_outFile = 0;
  m_trackSource = "generalTracks";
  //m_candidateSource = "duplicateCandidates";
  m_ofname = "cc2t.root";
  m_maxDeltaHits = 5;
  //m_simSource = "mergedtruth";
  if(iPara.exists("trackSource"))m_trackSource = iPara.getParameter<string>("trackSource");
  if(iPara.exists("candidateSource"))m_candidateSource = iPara.getParameter<InputTag>("candidateSource");
  if(iPara.exists("outfile"))m_ofname = iPara.getParameter<string>("outfile");
  if(iPara.exists("maxDeltaHits"))m_maxDeltaHits = iPara.getParameter<int>("maxDeltaHits");
  m_dHits = new TH1F("dHits","",41,-20.5,20.5);

  produces<std::vector<Track> >(); 

}
//------------------------------------------------------------
//------------------------------------------------------------
MWCompareCandidateToTrack::~MWCompareCandidateToTrack()
{
  /* no op */
}
//------------------------------------------------------------
//------------------------------------------------------------
void MWCompareCandidateToTrack::beginJob()
{
  m_outFile = new TFile(m_ofname.Data(),"RECREATE");
}
//------------------------------------------------------------
//------------------------------------------------------------
void MWCompareCandidateToTrack::endJob()
{
  m_outFile->cd();
  m_dHits->Write();
  m_outFile->Close();
}
//------------------------------------------------------------
//------------------------------------------------------------
void MWCompareCandidateToTrack::beginRun(const edm::Run& iRun, const edm::EventSetup& iSetup)
{

}
//------------------------------------------------------------
//------------------------------------------------------------
void MWCompareCandidateToTrack::endRun(const edm::Run& iRun, const edm::EventSetup& iSetup)
{
  /* no op */
}
//------------------------------------------------------------
//------------------------------------------------------------
void MWCompareCandidateToTrack::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  m_totalEvents++;


  auto_ptr<vector<Track> > out(new vector<Track>());
  edm::Handle<View<Track> >trackHandle;
  iEvent.getByLabel(m_trackSource,trackHandle);
  edm::Handle<TrackCandidateCollection >candidateHandle;
  iEvent.getByLabel(m_candidateSource,candidateHandle);


  for(int i = 0; i < (int)trackHandle->size(); i++){
    Track track = (trackHandle->at(i));
    for(int j = 0; j < (int)candidateHandle->size();j++){
      TrackCandidate candidate = (candidateHandle->at(j));
      if(track.seedRef() != candidate.seedRef())continue;
      int dHits = (candidate.recHits().second - candidate.recHits().first) - track.recHitsSize();
      m_dHits->Fill(dHits);
      if(dHits > m_maxDeltaHits)continue;
      out->push_back(track);
    }
  }
  iEvent.put(out);
}
//------------------------------------------------------------
//------------------------------------------------------------

DEFINE_FWK_MODULE(MWCompareCandidateToTrack);
