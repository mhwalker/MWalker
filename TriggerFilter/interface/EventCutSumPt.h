#ifndef MWALKER_TRIGGERFILTER_EVENTCUTSUMPT
#define MWALKER_TRIGGERFILTER_EVENTCUTSUMPT


#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Provenance/interface/ParameterSetID.h"
#include <vector>
#include <string>
#include <iostream>
#include <map>

#include "TTree.h"
#include "TFile.h"
#include "TLorentzVector.h"
#include "TString.h"
//#include "TClonesArray.h"
#include "MWalker/TriggerFilter/interface/EventCut.h"

class EventFilter;

class EventCutSumPt : public EventCut {
 public:
  EventCutSumPt(const edm::ParameterSet& iPara);
  ~EventCutSumPt();
  virtual bool passCut(EventFilter* filter);

 private:
  std::vector<TString> m_products;
  double m_sumlow;
  double m_sumhigh;
  double m_includeLow;
  double m_includeHigh;
  bool m_useVector;

};

#endif
