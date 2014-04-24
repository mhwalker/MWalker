#ifndef MWALKER_TRIGGERANALYZER_TRIGGERANALYZER
#define MWALKER_TRIGGERANALYZER_TRIGGERANALYZER


#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Provenance/interface/ParameterSetID.h"
#include "DataFormats/Candidate/interface/LeafCandidate.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "MWalker/TriggerAnalyzer/interface/TriggerTH1F.h"
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>
#include <map>

#include "TTree.h"
#include "TFile.h"
#include "TLorentzVector.h"
#include "TString.h"
//#include "TClonesArray.h"

namespace edm{
  class Event;
  class EventSetup;
  class ParameterSet;
}

class TriggerAnalyzer : public edm::EDAnalyzer {
 public:
  explicit TriggerAnalyzer(const edm::ParameterSet& iPara);
  ~TriggerAnalyzer();
  std::vector<reco::LeafCandidate> getProduct(TString);

 private:
  virtual void beginJob();
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  void beginRun(const edm::Run&, const edm::EventSetup&);
  void endRun(  const edm::Run&, const edm::EventSetup&);
  virtual void endJob();
  void printTable();

  void addHistogram(edm::ParameterSet& iPara);

  std::vector<std::string> m_triggers;
  std::map<std::string,int> m_trigger_pass;
  int m_totalEvents;
  int m_passEvents;
  int m_filterPassEvents;
  edm::InputTag m_triggerSource;
  HLTConfigProvider m_hltConfig;

  TFile* m_outFile;

  std::map<TString, std::vector<reco::LeafCandidate> > m_products;
  std::vector<edm::InputTag> m_product_names;
  std::map<std::string, std::vector<TriggerTH1F*> > m_histograms;
};

#endif
