#ifndef TestAODReader_H
#define TestAODReader_H

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/EgammaCandidates/interface/Photon.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include <TTree.h>
#include <TFile.h>

class TClonesArray;
class SignatureObject; 
class TestAODReader : public edm::EDAnalyzer {
public:
    TestAODReader (const edm::ParameterSet&);
    virtual ~TestAODReader();


protected:
    virtual void beginJob() ;
    virtual void beginRun(edm::Run const &, edm::EventSetup const&);
    virtual void analyze(const edm::Event&, const edm::EventSetup&);
    virtual void endJob() ;
    virtual void makeProducts(const edm::Event&, const edm::EventSetup&);
    virtual void finish();
    virtual void fillTree();
    virtual void initTree();

    virtual void makeJets();
    virtual void makeElectrons();
    virtual void makePhotons();
    virtual void makeTaus();
    virtual void makeMuons();
    virtual void makeTracks();
    virtual void makeVertices();
    virtual void makeBeamSpot();
    virtual void makeTriggers(const edm::Event&, const edm::EventSetup&);
    virtual void makeGenParticles();
    virtual void makeMET();

    long event_;
    int run_;
    int lumi_;

    TClonesArray* m_clonesarray;

    edm::Handle<edm::View<pat::Jet> > jetHandle_;
    edm::Handle<edm::View<pat::Electron> > electronHandle_;
    edm::Handle<edm::View<pat::Muon> > muonHandle_;
    edm::Handle<edm::View<reco::Photon> > photonHandle_;
    edm::Handle<edm::View<pat::Tau> > tauHandle_;
    edm::Handle<edm::View<reco::PFMET> > metHandle_;
    edm::Handle<edm::View<reco::Track> > trackHandle_;
    edm::Handle<edm::View<reco::Vertex> > vertexHandle_;
    edm::Handle<reco::BeamSpot> beamspotHandle_;
    edm::Handle<edm::TriggerResults> triggerHandle_;
    edm::Handle<reco::GenParticleCollection> genParticleHandle_;
    edm::Handle<trigger::TriggerEvent> triggerEventHandle_;

    edm::EDGetTokenT<edm::View<pat::Jet> > jetToken_;
    edm::EDGetTokenT<edm::View<pat::Electron> > electronToken_;
    edm::EDGetTokenT<edm::View<pat::Muon> > muonToken_;
    edm::EDGetTokenT<edm::View<reco::Photon> > photonToken_;
    edm::EDGetTokenT<edm::View<pat::Tau> > tauToken_;
    edm::EDGetTokenT<edm::View<reco::PFMET> > metToken_;
    edm::EDGetTokenT<edm::View<reco::Track> > trackToken_;
    edm::EDGetTokenT<edm::View<reco::Vertex> > vertexToken_;
    edm::EDGetTokenT<reco::BeamSpot> beamspotToken_;
    edm::EDGetTokenT<edm::TriggerResults> triggerToken_;
    edm::EDGetTokenT<reco::GenParticleCollection> genParticleToken_;
    edm::EDGetTokenT<trigger::TriggerEvent> triggerEventToken_;

    edm::InputTag jetLabel_;
    edm::InputTag electronLabel_;
    edm::InputTag muonLabel_;
    edm::InputTag tauLabel_;
    edm::InputTag photonLabel_;
    edm::InputTag metLabel_;
    edm::InputTag trackLabel_;
    edm::InputTag vertexLabel_;
    edm::InputTag triggerLabel_;
    edm::InputTag beamspotLabel_;
    edm::InputTag genParticleLabel_;
    edm::InputTag triggerEventLabel_;

    HLTConfigProvider hltConfig_;
    bool writeAllEvents_;
    std::string processName_;

    TTree* m_tree;
    TFile* m_outFile;

    std::map<TString,std::vector<SignatureObject*> > m_productmap;
};

#endif
