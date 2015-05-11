#ifndef MWALKER_TRIGGERANALYZER_TRIGGERTH1F_PT
#define MWALKER_TRIGGERANALYZER_TRIGGERTH1F_PT

#include "TH1F.h"
#include "MWalker/TriggerAnalyzer/interface/TriggerTH1F.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include <vector>
#include "TString.h"

class TriggerAnalyzer;

class TriggerTH1F_PT : public TriggerTH1F {
 public:
  TriggerTH1F_PT(const char* name, const char* productname, int whichone = -1, const char* title = "p_{T} distribution ; p_{T} GeV; ", int nbins=50, double xmin=0, double xmax=250);
  TriggerTH1F_PT(TH1F h):TriggerTH1F(h){/* no-op*/ }
  TriggerTH1F_PT():TriggerTH1F(){/* no-op */}
  virtual ~TriggerTH1F_PT(){/* no-op */}
  Int_t Fill(TriggerAnalyzer*);

 protected:
  TString m_productname;
  int m_whichone;
};


#endif
