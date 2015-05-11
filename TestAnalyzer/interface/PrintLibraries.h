#ifndef MWALKER_TESTANALYZER_PRINTLIBRARIES
#define MWALKER_TESTANALYZER_PRINTLIBRARIES


#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

namespace edm{
  class Event;
  class EventSetup;
  class ParameterSet;
}

class MWPrintLibraries : public edm::EDProducer {
 public:
  explicit MWPrintLibraries(const edm::ParameterSet& iPara);
  ~MWPrintLibraries();

  virtual void produce(edm::Event&, const edm::EventSetup&);
 private:
  virtual void beginJob();
  void beginRun(const edm::Run&, const edm::EventSetup&);
  void endRun(  const edm::Run&, const edm::EventSetup&);
  virtual void endJob();

};

#endif
