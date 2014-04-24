#ifndef MWALKER_TRIGGERFILTER_EVENTCUTN
#define MWALKER_TRIGGERFILTER_EVENTCUTN


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

class EventCutN : public EventCut {
 public:
  EventCutN(const edm::ParameterSet& iPara);
  ~EventCutN();
  virtual bool passCut(EventFilter* filter);

 private:
  std::vector<TString> m_products;
  int m_nlow;
  int m_nhigh;

};

#endif
