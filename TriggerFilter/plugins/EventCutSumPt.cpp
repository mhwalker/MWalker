#include "MWalker/TriggerFilter/interface/EventCutSumPt.h"
#include "MWalker/TriggerFilter/interface/EventFilter.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Candidate/interface/LeafCandidate.h"
#include "DataFormats/Math/interface/LorentzVector.h"

using namespace std;

EventCutSumPt::EventCutSumPt(const edm::ParameterSet& iPara):EventCut(iPara){
  m_sumlow = -1;
  m_sumhigh = 999999;
  m_useVector = false;
  m_includeLow = -1;
  m_includeHigh = 999999;

  if(iPara.exists("sumlow")) m_sumlow = iPara.getParameter<double>("sumlow");
  if(iPara.exists("sumhigh")) m_sumhigh = iPara.getParameter<double>("sumhigh");
  if(iPara.exists("usevector")) m_useVector = iPara.getParameter<bool>("usevector");
  if(iPara.exists("includelow"))m_includeLow = iPara.getParameter<double>("includelow");
  if(iPara.exists("includehigh"))m_includeHigh = iPara.getParameter<double>("includeHigh");
  if(iPara.exists("products")){
    vector<string> products = iPara.getParameter<vector<string> >("products");
    for(int i = 0; i < (int)products.size(); i++){
      m_products.push_back(TString(products[i]));
    }
  }

}

EventCutSumPt::~EventCutSumPt()
{
  /* no op */
}

bool EventCutSumPt::passCut(EventFilter* filter)
{
  double sumpT = 0;
  math::XYZTLorentzVector sumvec(0,0,0,0);
  for(int i = 0; i < (int)m_products.size(); i++){
    vector<reco::LeafCandidate> product = filter->getProduct(m_products[i]);
    //cout<<m_products[i]<<" "<<product.size()<<endl;
    for(int j = 0; j < (int)product.size(); j++){
      if(product[j].pt() < m_includeLow)continue;
      if(product[j].pt() > m_includeHigh)continue;
      sumpT += product[j].pt();
      if(m_useVector) sumvec += product[j].p4();
    }
  }
  //cout<<sumpT<<" "<<sumvec.Pt()<<endl;
  if(m_useVector && sumvec.Pt() < m_sumlow)return false;
  if(m_useVector && sumvec.Pt() > m_sumhigh)return false;
  if(!m_useVector && sumpT < m_sumlow) return false;
  if(!m_useVector && sumpT > m_sumhigh) return false;
  return true;
}
