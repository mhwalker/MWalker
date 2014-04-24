#include "MWalker/TriggerFilter/interface/EventCutN.h"
#include "MWalker/TriggerFilter/interface/EventFilter.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

using namespace std;

EventCutN::EventCutN(const edm::ParameterSet& iPara):EventCut(iPara){
  m_nlow = -1;
  m_nhigh = 9999999;

  if(iPara.exists("nlow")) m_nlow = iPara.getParameter<int>("nlow");
  if(iPara.exists("nhigh")) m_nhigh = iPara.getParameter<int>("nhigh");
  if(iPara.exists("products")){
    vector<string> products = iPara.getParameter<vector<string> >("products");
    for(int i = 0; i < (int)products.size(); i++){
      m_products.push_back(TString(products[i]));
    }
  }

}

EventCutN::~EventCutN()
{
  /* no op */
}

bool EventCutN::passCut(EventFilter* filter)
{
  int ntot = 0;
  for(int i = 0; i < (int)m_products.size(); i++){
    vector<reco::LeafCandidate> product = filter->getProduct(m_products[i]);
    ntot += (int)product.size();
  }
  if(ntot < m_nlow)return false;
  if(ntot > m_nhigh) return false;
  return true;
}
