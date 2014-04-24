#include "MWalker/TriggerFilter/interface/SimMETFilter.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/FileInPath.h"

#include "DataFormats/Common/interface/Association.h"
#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/HepMCCandidate/interface/GenParticleFwd.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include "DataFormats/ParticleFlowCandidate/interface/PFCandidateFwd.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"

#include "PhysicsTools/PatUtils/interface/TrackerIsolationPt.h"
#include "PhysicsTools/PatUtils/interface/CaloIsolationEnergy.h"

#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ConfigurationDescriptions.h"
#include "FWCore/ParameterSet/interface/ParameterSetDescription.h"

#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"
#include "TrackingTools/TransientTrack/interface/TransientTrack.h"
#include "TrackingTools/IPTools/interface/IPTools.h"

#include "DataFormats/GsfTrackReco/interface/GsfTrackFwd.h"
#include "DataFormats/GsfTrackReco/interface/GsfTrack.h"

#include <vector>
#include <memory>


using namespace pat;
using namespace std;

SimMETFilter::SimMETFilter(const edm::ParameterSet &iConfig)
{
  m_ptlow = -1;
  m_pthigh = 9999999;
  m_etalow = -2.5;
  m_etahigh = 2.5;
  if(iConfig.exists("sourceName"))m_sourceName = iConfig.getParameter<edm::InputTag>("sourceName");
  //m_prodcutName = iConfig.getParameter<edm::InputTag>("productName");
  if(iConfig.exists("ptlow"))m_ptlow = iConfig.getParameter<double>("ptlow");
  if(iConfig.exists("pthigh"))m_pthigh = iConfig.getParameter<double>("pthigh");
  if(iConfig.exists("etalow"))m_etalow = iConfig.getParameter<double>("etalow");
  if(iConfig.exists("etahigh"))m_etahigh = iConfig.getParameter<double>("etahigh");

  vector<double> pdgList;
  vector<double> statusList;
  if(iConfig.exists("pdgIDs")) pdgList = iConfig.getParameter<vector<double> >("pdgIDs");
  if(iConfig.exists("statuses")) statusList = iConfig.getParameter<vector<double> >("statuses");

  for(int i = 0; i < (int)pdgList.size(); i++){
    m_pdgID.push_back(pdgList[i]);
  }

  for(int i = 0; i < (int)statusList.size(); i++){
    m_status.push_back(statusList[i]);
  }

  produces<vector<reco::LeafCandidate> >();
}
//-------------------------
//-------------------------
SimMETFilter::~SimMETFilter()
{
  /* no op */
}
//-------------------------
//-------------------------
void SimMETFilter::produce(edm::Event & iEvent, const edm::EventSetup & iSetup)
{
  edm::Handle<vector<reco::GenMET> > genParticles;
  iEvent.getByLabel(m_sourceName,genParticles);

  vector<reco::LeafCandidate>* outGenParticles = new vector<reco::LeafCandidate>();

  for(size_t i = 0; i < genParticles->size(); i++){
    const reco::GenParticle& iter = (*genParticles)[i];
    if(iter.pt() < m_ptlow)continue;
    if(iter.pt() > m_pthigh)continue;
    if(iter.eta() < m_etalow)continue;
    if(iter.eta() > m_etahigh)continue;
    int status = iter.status();
    int pdgID = iter.pdgId();
    if(m_pdgID.size() > 0 && find(m_pdgID.begin(),m_pdgID.end(),pdgID) == m_pdgID.end())continue;
    if(m_status.size() > 0 && find(m_status.begin(),m_status.end(),status) == m_status.end())continue;
    outGenParticles->push_back(reco::LeafCandidate(iter));
  }

  sort(outGenParticles->begin(),outGenParticles->end(),pTComparator_);
  auto_ptr<vector<reco::LeafCandidate> > ptr(outGenParticles);
  iEvent.put(ptr);
}

DEFINE_FWK_MODULE(SimMETFilter);
