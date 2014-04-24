#include "MWalker/TriggerAnalyzer/interface/TriggerTH1F_PT.h"
#include "MWalker/TriggerAnalyzer/interface/TriggerAnalyzer.h"
#include "DataFormats/Candidate/interface/LeafCandidate.h"

using namespace std;

TriggerTH1F_PT::TriggerTH1F_PT(const char* name, const char* productname, int whichone, const char* title, int nbins, double xmin, double xmax):TriggerTH1F(name,title,nbins,xmin,xmax),m_productname(productname),m_whichone(whichone)
{
  /* no op */
}
//--------------------------------------------------------------
//--------------------------------------------------------------
Int_t TriggerTH1F_PT::Fill(TriggerAnalyzer* handler)
{
  vector<reco::LeafCandidate> product = handler->getProduct(m_productname);
  if(m_whichone > 0 && m_whichone > (int)product.size())return -1;
  int start = m_whichone -1;
  int length = m_whichone;
  if(m_whichone < 0){
    start = 0;
    length = (int)product.size();
  }

  int dummy = -1;

  for(int i = start; i < length; i++){
    dummy = TH1F::Fill(product[i].pt());
  }

  return dummy;

}
