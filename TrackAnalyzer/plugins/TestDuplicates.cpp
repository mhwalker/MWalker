#include "MWalker/TrackAnalyzer/interface/TrackAnalyzer.h"
#include "MWalker/TrackAnalyzer/interface/TestDuplicates.h"

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
#include "DataFormats/TrajectorySeed/interface/TrajectorySeed.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"
#include <functional>
#include <sstream>
#include <iostream>

#include "TMath.h"

using namespace edm;
using namespace reco;

typedef math::XYZTLorentzVectorD LorentzVector;
typedef math::XYZVector Vector;
typedef math::XYZPoint Point;

using namespace std;

MWTestDuplicates::MWTestDuplicates(const edm::ParameterSet& iPara)
{
  originalTrackSource_ = edm::InputTag("generalTracks");
  mergedTrackSource_ = edm::InputTag("mergedDuplicateTracks");
  if(iPara.exists("mergedSource"))mergedTrackSource_ = iPara.getParameter<edm::InputTag>("mergedSource");
  if(iPara.exists("originalSource"))originalTrackSource_ = iPara.getParameter<edm::InputTag>("originalSource");
  ofname_ = "testDuplicates.root";
  if(iPara.exists("outputName"))ofname_ = iPara.getParameter<string>("outputName");

  outfile_ = new TFile(TString(ofname_),"RECREATE");
  h_prob_ = new TH1F("hProb","",100,0,1);
}
//------------------------------------------------------------
//------------------------------------------------------------
MWTestDuplicates::~MWTestDuplicates()
{
  /* no op */
  outfile_->cd();
  h_prob_->Write();
  outfile_->Close();
}
//------------------------------------------------------------
//------------------------------------------------------------
void MWTestDuplicates::beginJob()
{
}

//------------------------------------------------------------
//------------------------------------------------------------
void MWTestDuplicates::endJob()
{

}
//------------------------------------------------------------
//------------------------------------------------------------
void MWTestDuplicates::beginRun(const edm::Run& iRun, const edm::EventSetup& iSetup)
{
}
//------------------------------------------------------------
//------------------------------------------------------------
void MWTestDuplicates::endRun(const edm::Run& iRun, const edm::EventSetup& iSetup)
{
  /* no op */
}
//------------------------------------------------------------
//------------------------------------------------------------
void MWTestDuplicates::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{


  edm::Handle<edm::View<reco::Track> > originalHandle;
  iEvent.getByLabel(originalTrackSource_,originalHandle);
  edm::Handle< std::vector<Trajectory> >  originalTrajHandle;
  iEvent.getByLabel(originalTrackSource_,originalTrajHandle);
  edm::Handle< TrajTrackAssociationCollection >  originalTrajTrackHandle;
  iEvent.getByLabel(originalTrackSource_,originalTrajTrackHandle);

  edm::Handle<edm::View<reco::Track> > mergedHandle;
  iEvent.getByLabel(mergedTrackSource_,mergedHandle);
  edm::Handle< std::vector<Trajectory> >  mergedTrajHandle;
  iEvent.getByLabel(mergedTrackSource_,mergedTrajHandle);
  edm::Handle< TrajTrackAssociationCollection >  mergedTrajTrackHandle;
  iEvent.getByLabel(mergedTrackSource_,mergedTrajTrackHandle);

  
  /*
  std::cout<<"test duplicates: "<<originalTrajHandle->size()<<" "<<originalTrajTrackHandle->size()<<std::endl;
  TrajTrackAssociationCollection::const_iterator iTer1;
  for(iTer1 = originalTrajTrackHandle->begin(); iTer1 != originalTrajTrackHandle->end(); iTer1++){
    std::cout<<"test duplicates iter: "<<(iTer1->key).isNonnull()<<" "<<(iTer1->val).isNonnull()<<" "<<(iTer1->key)->foundHits()<<std::endl;
  }
  */
  for(int i = 0; i < (int)mergedHandle->size(); i++){
    //std::cout<<"merged track normalized chi2: "<<(mergedHandle->at(i)).normalizedChi2()<<" "<<(mergedHandle->at(i)).chi2()<<" "<<(mergedHandle->at(i)).ndof()<<" "<<(mergedHandle->at(i)).algoName()<<" "<<TMath::Prob((mergedHandle->at(i)).chi2(),(mergedHandle->at(i)).ndof())<<std::endl;
    h_prob_->Fill(TMath::Prob((mergedHandle->at(i)).chi2(),(mergedHandle->at(i)).ndof()));
  }

}
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------

DEFINE_FWK_MODULE(MWTestDuplicates);
