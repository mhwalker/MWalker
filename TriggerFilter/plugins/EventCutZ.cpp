#include "MWalker/TriggerFilter/interface/EventCutZ.h"
#include "MWalker/TriggerFilter/interface/EventFilter.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Candidate/interface/LeafCandidate.h"
#include "DataFormats/Math/interface/LorentzVector.h"

using namespace std;

EventCutZ::EventCutZ(const edm::ParameterSet& iPara):EventCut(iPara){
  m_zlow = 75;
  m_zhigh = 105;
  m_hasZ = true;

  if(iPara.exists("zlow")) m_zlow = iPara.getParameter<double>("zlow");
  if(iPara.exists("zhigh")) m_zhigh = iPara.getParameter<double>("zhigh");
  if(iPara.exists("hasZ")) m_hasZ = iPara.getParameter<bool>("hasZ");
  if(iPara.exists("products")){
    vector<string> products = iPara.getParameter<vector<string> >("products");
    for(int i = 0; i < (int)products.size(); i++){
      m_products.push_back(TString(products[i]));
    }
  }

}

EventCutZ::~EventCutZ()
{
  /* no op */
}

bool EventCutZ::passCut(EventFilter* filter)
{
  bool eventHasZ = false;
  for(int i = 0; i < (int)m_products.size(); i++){
    vector<reco::LeafCandidate> product = filter->getProduct(m_products[i]);
    for(int j = 0; j < (int)product.size() && !eventHasZ; j++){
      int pdgIDj = product[j].pdgId();
      const math::XYZTLorentzVector vectorj = product[j].p4();
      for(int k = j + 1; k < (int)product.size() && !eventHasZ; k++){
	if(pdgIDj + product[k].pdgId() != 0)continue;
	const math::XYZTLorentzVector vectork = product[k].p4();
	double m = (vectorj + vectork).M();
	if(m < m_zlow)continue;
	if(m > m_zhigh)continue;
	eventHasZ = true;
      }
    }
  }
  if(m_hasZ)return eventHasZ;
  if(!m_hasZ)return !eventHasZ;
  return true;
}
