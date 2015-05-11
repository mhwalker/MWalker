#ifndef MWALKER_TRIGGERANALYZER_TRIGGERTH1F
#define MWALKER_TRIGGERANALYZER_TRIGGERTH1F

#include "TH1F.h"

class TriggerAnalyzer;

class TriggerTH1F : public TH1F {
 public:
  TriggerTH1F(const char* name, const char* title, int nbins, double xmin, double xmax);
  TriggerTH1F(TH1F h);
  TriggerTH1F():TH1F(){/* no-op */}
  virtual ~TriggerTH1F(){/* no-op */}
  virtual Int_t Fill(TriggerAnalyzer*) = 0;


};

inline TriggerTH1F::TriggerTH1F(const char* name, const char* title, int nbins, double xmin, double xmax) : TH1F(name,title,nbins,xmin,xmax){

}

inline TriggerTH1F::TriggerTH1F(TH1F h):TH1F(h){

}

#endif
