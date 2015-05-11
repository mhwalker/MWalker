#ifndef MWALKER_TRIGGERFILTER_EVENTFILTER
#define MWALKER_TRIGGERFILTER_EVENTFILTER


#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Provenance/interface/ParameterSetID.h"
#include "DataFormats/Candidate/interface/LeafCandidate.h"
#include <vector>
#include <string>
#include <iostream>
#include <map>

#include "TTree.h"
#include "TFile.h"
#include "TLorentzVector.h"
#include "TString.h"
//#include "TClonesArray.h"

class EventCut;

namespace edm{
  class Event;
  class EventSetup;
  class ParameterSet;
}

class EventFilter : public edm::EDFilter {
 public:
  explicit EventFilter(const edm::ParameterSet& iPara);
  ~EventFilter();
  virtual bool filter(edm::Event& iEvent,const edm::EventSetup& iSetup);
  virtual void endJob();
  virtual void addCut(edm::ParameterSet& iPara);
  std::vector<reco::LeafCandidate> getProduct(TString);

 private:
  std::vector<edm::InputTag> m_product_names;
  std::vector<EventCut*> m_cuts;
  std::map<TString, std::vector<reco::LeafCandidate> > m_products;
};

#endif
