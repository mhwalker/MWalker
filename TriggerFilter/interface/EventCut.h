#ifndef MWALKER_TRIGGERFILTER_EVENTCUT
#define MWALKER_TRIGGERFILTER_EVENTCUT


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

class EventFilter;

class EventCut {
 public:
  EventCut(const edm::ParameterSet& iPara);
  ~EventCut();
  virtual bool passCut(EventFilter* filter) = 0;

 private:

};

#endif
