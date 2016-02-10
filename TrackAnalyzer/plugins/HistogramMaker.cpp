#include "MWalker/TrackAnalyzer/interface/HistogramMaker.h"

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

MWHistogramMaker::MWHistogramMaker(const edm::ParameterSet& iPara)
{
  m_outFile = 0;
  m_source = "generalTracks";
  //m_simSource = "mergedtruth";
  if(iPara.exists("outfile"))m_outFile = new TFile(iPara.getParameter<string>("outfile").c_str(),"RECREATE");
  if(iPara.exists("source"))m_source = iPara.getParameter<string>("source");

  m_hpt = new TH1F("pt","",300,0,300);
  m_hetaphi = new TH2F("etaphi","",300,-3.0,3.0,300,-3.142,3.142);


}
//------------------------------------------------------------
//------------------------------------------------------------
MWHistogramMaker::~MWHistogramMaker()
{
  /* no op */
}
//------------------------------------------------------------
//------------------------------------------------------------
void MWHistogramMaker::beginJob()
{

}

//------------------------------------------------------------
//------------------------------------------------------------
void MWHistogramMaker::endJob()
{
  m_outFile->cd();
  m_hpt->Write();
  m_hetaphi->Write();

  m_outFile->Close();
}
//------------------------------------------------------------
//------------------------------------------------------------
void MWHistogramMaker::beginRun(const edm::Run& iRun, const edm::EventSetup& iSetup)
{
}
//------------------------------------------------------------
//------------------------------------------------------------
void MWHistogramMaker::endRun(const edm::Run& iRun, const edm::EventSetup& iSetup)
{
  /* no op */
}
//------------------------------------------------------------
//------------------------------------------------------------
void MWHistogramMaker::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  edm::Handle<View<Track> >handle;
  iEvent.getByLabel(m_source,handle);

  for(int i = 0; i < (int)handle->size(); i++){
    Track rt1 = (handle->at(i));
    m_hpt->Fill(rt1.innerMomentum().Rho());
    m_hetaphi->Fill(rt1.innerMomentum().Eta(),rt1.innerMomentum().Phi());
  }
}
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------

DEFINE_FWK_MODULE(MWHistogramMaker);
