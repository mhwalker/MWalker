#ifndef MWALKER_TRIGGERFILTER_SIMMETFILTER
#define MWALKER_TRIGGERFILTER_SIMMETFILTER


#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "CommonTools/Utils/interface/StringObjectFunction.h"
#include "CommonTools/Utils/interface/StringCutObjectSelector.h"

#include "TString.h"

#include "CommonTools/Utils/interface/PtComparator.h"

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/PatCandidates/interface/Photon.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/GenericParticle.h"
#include "DataFormats/METReco/interface/MET.h"
#include "DataFormats/METReco/interface/METFwd.h"
#include "DataFormats/Candidate/interface/LeafCandidate.h"

class SimMETFilter : public edm::EDProducer{
 public:
  explicit SimMETFilter(const edm::ParameterSet &iConfig);
  virtual ~SimMETFilter();

  virtual void produce(edm::Event& iEvent, const edm::EventSetup& iSetup);

 private:
  edm::InputTag m_sourceName;
  TString m_productName;
  double m_ptlow,m_pthigh;
  double m_etalow,m_etahigh;
  std::vector<double> m_pdgID;
  std::vector<double> m_status;

  GreaterByPt<reco::LeafCandidate>       pTComparator_;
};




#endif
