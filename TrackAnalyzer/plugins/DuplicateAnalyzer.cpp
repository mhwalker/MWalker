#include "MWalker/TrackAnalyzer/interface/TrackAnalyzer.h"
#include "MWalker/TrackAnalyzer/interface/DuplicateAnalyzer.h"

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
#include "DataFormats/TrajectorySeed/interface/TrajectorySeed.h"
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

MWDuplicateAnalyzer::MWDuplicateAnalyzer(const edm::ParameterSet& iPara)
{
  m_trackSource = "generalTracks";
  m_associatorName = "TrackAssociatorByHits";
  if(iPara.exists("simSource"))m_simSource = iPara.getParameter<InputTag>("simSource");
  if(iPara.exists("source"))m_trackSource = iPara.getParameter<string>("source");
  if(iPara.exists("associator"))m_associatorName = iPara.getParameter<string>("associator");
  if(iPara.exists("duplicateCandidateSource"))m_duplicateCandidateSource = iPara.getParameter<InputTag>("duplicateCandidateSource");
  //if(iPara.exists("duplicateCandidateSource"))m_duplicateCandidateSource = iPara.getParameter<string>("duplicateCandidateSource");
  if(iPara.exists("duplicateFitSource"))m_duplicateFitSource = iPara.getParameter<string>("duplicateFitSource");
  if(iPara.exists("duplicateFinalSource"))m_duplicateFinalSource = iPara.getParameter<string>("duplicateFinalSource");
}
//------------------------------------------------------------
//------------------------------------------------------------
MWDuplicateAnalyzer::~MWDuplicateAnalyzer()
{
  /* no op */
}
//------------------------------------------------------------
//------------------------------------------------------------
void MWDuplicateAnalyzer::beginJob()
{
  m_totalEvents = 0;
  m_totalDuplicates = 0;
  m_realDuplicates = 0;
  m_realDuplicatesFit = 0;
  m_realDuplicatesFinal = 0;
  m_fakeDuplicates = 0;
  m_fakeDuplicatesFit = 0;
  m_fakeDuplicatesFinal = 0;
  m_matchedCandidates = 0;
}

//------------------------------------------------------------
//------------------------------------------------------------
void MWDuplicateAnalyzer::endJob()
{
  cout<<"total Events: "<<m_totalEvents<<endl;
  cout<<"total Duplicates: "<<m_totalDuplicates<<endl;
  cout<<"matched Candidate to Track: "<<m_matchedCandidates<<endl;
  cout<<"real Duplicates: "<<m_realDuplicatesFit<<endl;
  cout<<"fake Duplicates: "<<m_fakeDuplicatesFit<<endl;
  cout<<"real Duplicates Final: "<<m_realDuplicatesFinal<<endl;
  cout<<"fake Duplicates Final: "<<m_fakeDuplicatesFinal<<endl;

}
//------------------------------------------------------------
//------------------------------------------------------------
void MWDuplicateAnalyzer::beginRun(const edm::Run& iRun, const edm::EventSetup& iSetup)
{
  edm::ESHandle<TrackAssociatorBase> theAssociator;
  iSetup.get<TrackAssociatorRecord>().get(m_associatorName,theAssociator);
  m_associator = theAssociator.product();
}
//------------------------------------------------------------
//------------------------------------------------------------
void MWDuplicateAnalyzer::endRun(const edm::Run& iRun, const edm::EventSetup& iSetup)
{
  /* no op */
}
//------------------------------------------------------------
//------------------------------------------------------------
void MWDuplicateAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  m_totalEvents++;
  iSetup.get<IdealMagneticFieldRecord>().get(m_magfield);

  edm::Handle<View<Track> >handle;
  iEvent.getByLabel(m_trackSource,handle);

  edm::Handle<View<Track> >handleHighPurity;
  iEvent.getByLabel("selectHighPurity",handleHighPurity);

  edm::Handle<TrackCandidateCollection> handleDuplicateCandidate;
  iEvent.getByLabel(m_duplicateCandidateSource,handleDuplicateCandidate);

  TrackCandidateCollection duplicateCandidates = *(handleDuplicateCandidate.product());

  edm::Handle<View<Track> > handleDuplicateFit;
  iEvent.getByLabel(m_duplicateFitSource,handleDuplicateFit);

  edm::Handle<View<Track> > handleDuplicateFinal;
  iEvent.getByLabel(m_duplicateFinalSource,handleDuplicateFinal);

  edm::Handle<TrackingParticleCollection>  simTPhandle;
  iEvent.getByLabel(m_simSource,simTPhandle);
  const TrackingParticleCollection simTracks = *(simTPhandle.product());

  reco::RecoToSimCollection recSimColl,recSimCollDuplicates;
  reco::SimToRecoCollection simRecColl,simRecCollDuplicates;

  recSimColl = m_associator->associateRecoToSim(handle,simTPhandle,&iEvent,&iSetup);
  simRecColl = m_associator->associateSimToReco(handle,simTPhandle,&iEvent,&iSetup);
  recSimCollDuplicates = m_associator->associateRecoToSim(handleDuplicateFit,simTPhandle,&iEvent,&iSetup);
  simRecCollDuplicates = m_associator->associateSimToReco(handleDuplicateFit,simTPhandle,&iEvent,&iSetup);


  TwoTrackMinimumDistance ttmd;
  TSCPBuilderNoMaterial tscpBuilder;
  map<Track,Track,trackCompare> matchedTracks;
  map<Track,vector<Track>,trackCompare> innerMatchedTracks;
  map<Track,vector<Track>,trackCompare> outerMatchedTracks;
  map<Track,vector<Track>,trackCompare> duplicateInnerMatched;
  map<Track,vector<Track>,trackCompare> duplicateOuterMatched;

  for(int i = 0; i < (int)handleDuplicateCandidate->size(); i++){
    m_totalDuplicates++;
    TrackCandidate candidate =  handleDuplicateCandidate->at(i);

    int fitTrack = matchCandidateToTrack(candidate,handleDuplicateFit);
    if(fitTrack < 0)continue;
   
    m_matchedCandidates++;
    bool isReal = false;

    edm::RefToBase<reco::Track> trackRef(handleDuplicateFit,fitTrack);
    TrackingParticleRef tpr;

    std::vector<std::pair<TrackingParticleRef, double> > tpv;

    if(recSimCollDuplicates.find(trackRef) != recSimCollDuplicates.end())tpv=recSimCollDuplicates[trackRef];
    if(tpv.size() > 0){
      tpr = tpv[0].first;
      if(simRecColl.find(tpr) != simRecColl.end()){
	std::vector<std::pair<RefToBase<reco::Track>, double> > rt = (std::vector<std::pair<RefToBase<reco::Track>, double> >) simRecColl[tpr];
	int nGood = 0;
	for(int j = 0; j < (int)rt.size(); j++){
	  if((rt[j].first)->innerMomentum().Rho() < 1.0)continue;
	  nGood++;
	}
	if(nGood > 1){
	  isReal = true;
	}
      }
    }

    if(isReal)m_realDuplicatesFit++;
    else m_fakeDuplicatesFit++;



    bool isFinal = trackInCollection(*(trackRef.get()),handleDuplicateFinal);
    if(!isFinal)continue;

    if(isReal)m_realDuplicatesFinal++;
    else m_fakeDuplicatesFinal++;
  }
  


}
//------------------------------------------------------------
//------------------------------------------------------------
int MWDuplicateAnalyzer::numberOfSharedHits(Track t1,Track t2)
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
bool MWDuplicateAnalyzer::compareTracks(Track t1,Track t2)
{
  if(t1.innerPosition() != t2.innerPosition())return false;
  if(t1.outerPosition() != t2.outerPosition())return false;
  if(t1.innerMomentum() != t2.innerMomentum())return false;
  if(t1.outerMomentum() != t2.outerMomentum())return false;
  return true;

}
//------------------------------------------------------------
//------------------------------------------------------------
bool MWDuplicateAnalyzer::trackInCollection(Track t,Handle<View<Track> > coll)
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
int MWDuplicateAnalyzer::matchCandidateToTrack(TrackCandidate candidate, edm::Handle<edm::View<reco::Track> > tracks){
  int track = -1;
  vector<int> rawIds;
  RecHitContainer::const_iterator candBegin = candidate.recHits().first;
  RecHitContainer::const_iterator candEnd = candidate.recHits().second;
  for(; candBegin != candEnd; candBegin++){
    rawIds.push_back((*(candBegin)).rawId());
  }
 

  for(int i = 0; i < (int)tracks->size() && track < 0;i++){
    if((tracks->at(i)).seedRef() != candidate.seedRef())continue;
    int match = 0;
    trackingRecHit_iterator trackRecBegin = tracks->at(i).recHitsBegin();
    trackingRecHit_iterator trackRecEnd = tracks->at(i).recHitsEnd();
    for(;trackRecBegin != trackRecEnd; trackRecBegin++){
      if(find(rawIds.begin(),rawIds.end(),(*(trackRecBegin))->rawId()) != rawIds.end())match++;
    }
    if(match != (int)tracks->at(i).recHitsSize())continue;
    track = i;
  }

  return track;
}
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------

DEFINE_FWK_MODULE(MWDuplicateAnalyzer);
