#ifndef MWALKER_TRIGGERFILTER_EVENTCUTZ
#define MWALKER_TRIGGERFILTER_EVENTCUTZ


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

class EventCutZ : public EventCut {
 public:
  EventCutZ(const edm::ParameterSet& iPara);
  ~EventCutZ();
  virtual bool passCut(EventFilter* filter);

 private:
  std::vector<TString> m_products;
  double m_zlow;
  double m_zhigh;
  bool m_hasZ;

};

#endif
