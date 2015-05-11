#include "MWalker/TriggerFilter/interface/EventFilter.h"
#include "MWalker/TriggerFilter/interface/EventCut.h"
#include "MWalker/TriggerFilter/interface/EventCutN.h"
#include "MWalker/TriggerFilter/interface/EventCutZ.h"
#include "MWalker/TriggerFilter/interface/EventCutSumPt.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/MuonReco/interface/MuonFwd.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include <functional>
#include <sstream>
#include <iostream>

using namespace std;

EventFilter::EventFilter(const edm::ParameterSet& iPara)
{
  m_product_names = iPara.getParameter<vector<edm::InputTag> >("products");
  if(iPara.exists("cuts")){
    vector<edm::ParameterSet> cuts = iPara.getParameter<vector<edm::ParameterSet> >("cuts");
    for(int i = 0; i < (int)cuts.size(); i++){
      addCut(cuts[i]);
    }
  }
}
//--------------------------------------------------------
//--------------------------------------------------------
EventFilter::~EventFilter()
{
  /* no op */
}
//--------------------------------------------------------
//--------------------------------------------------------
bool EventFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  for(int i = 0; i < (int)m_product_names.size(); i++){
    edm::Handle<vector<reco::LeafCandidate> > handle;
    iEvent.getByLabel(m_product_names[i],handle);
    const vector<reco::LeafCandidate> candVec = *handle;
    m_products[TString(m_product_names[i].label())] = candVec;
  }

  for(int i = 0; i < (int) m_cuts.size(); i++){
    if(!m_cuts[i]->passCut(this))return false;
  }

  return true;

}
//--------------------------------------------------------
//--------------------------------------------------------
void EventFilter::endJob()
{
  /* no op */
}
//--------------------------------------------------------
//--------------------------------------------------------
void EventFilter::addCut(edm::ParameterSet& iPara)
{
  TString cutType = (TString)iPara.getParameter<string>("cutType");
  if(cutType == "N"){
    EventCutN* cut = new EventCutN(iPara);
    m_cuts.push_back(cut);
  }else if(cutType == "Z"){
    EventCutZ* cut = new EventCutZ(iPara);
    m_cuts.push_back(cut);
  }else if(cutType == "SUMPT"){
    EventCutSumPt* cut = new EventCutSumPt(iPara);
    m_cuts.push_back(cut);
  }
}
//--------------------------------------------------------
//--------------------------------------------------------
vector<reco::LeafCandidate> EventFilter::getProduct(TString productName)
{
  vector<reco::LeafCandidate> retVec;
  if(m_products.find(productName) != m_products.end())retVec = m_products[productName];

  return retVec;

}

DEFINE_FWK_MODULE(EventFilter);
