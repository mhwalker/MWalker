#include "FWCore/Framework/interface/EventSetup.h"
#include "MWalker/TestAnalyzer/interface/TestAODReader.h"
#include <TClonesArray.h>
#include <TTree.h>
#include <TFile.h>
#include "MWalker/TestAnalyzer/interface/SignatureObject.h"
#include <TSystem.h>
#include <TLine.h>
#include <TClonesArray.h>

using namespace std;
using namespace edm;

TestAODReader::TestAODReader(const ParameterSet& pset) 
{
  TClass* cl = TClass::GetClass("SignatureObject");
  cout<<"1 inheritance: "<<cl->GetName()<<" "<<cl->InheritsFrom(TObject::Class())<<" "<<cl->GetCheckSum()<<" "<<cl->GetNmethods()<<" "<<TString(cl->GetSharedLibs())<<endl;

  const char* allLibs = gSystem->GetLibraries();
  cout<<"Print TestAODReader constructor: "<<allLibs<<endl;


  if(pset.exists("writeAllEvents"))writeAllEvents_ = pset.getParameter<bool>("writeAllEvents");

  jetLabel_ = pset.getParameter<InputTag>("patJetsInputTag");
  jetToken_ = consumes<edm::View<pat::Jet> >(jetLabel_);

  electronLabel_ = pset.getParameter<InputTag>("patElectronsInputTag");
  electronToken_ = consumes<edm::View<pat::Electron> >(electronLabel_);

  muonLabel_ = pset.getParameter<InputTag>("patMuonsInputTag");
  muonToken_ = consumes<edm::View<pat::Muon> >(muonLabel_);

  tauLabel_ = pset.getParameter<InputTag>("patTausInputTag");
  tauToken_ = consumes<edm::View<pat::Tau> >(tauLabel_);

  photonLabel_ = pset.getParameter<InputTag>("patPhotonsInputTag");
  photonToken_ = consumes<edm::View<reco::Photon> >(photonLabel_);

  metLabel_ = pset.getParameter<InputTag>("patMETInputTag");
  metToken_ = consumes<edm::View<reco::PFMET> >(metLabel_);

  trackLabel_ = pset.getParameter<InputTag>("trackInputTag");
  trackToken_ = consumes<edm::View<reco::Track> >(trackLabel_);

  vertexLabel_ = pset.getParameter<InputTag>("vtxInputTag");
  vertexToken_ = consumes<edm::View<reco::Vertex> >(vertexLabel_);

  beamspotLabel_ = pset.getParameter<InputTag>("beamSpotInputTag");
  beamspotToken_ = consumes<reco::BeamSpot>(beamspotLabel_);

  triggerLabel_ = pset.getParameter<InputTag>("triggerInputTag");
  triggerToken_ = consumes<edm::TriggerResults>(triggerLabel_);

  genParticleLabel_ = pset.getParameter<InputTag>("genParticleInputTag");
  genParticleToken_ = consumes<reco::GenParticleCollection>(genParticleLabel_);

  triggerEventLabel_ = pset.getParameter<InputTag>("triggerEventInputTag");
  triggerEventToken_ = consumes<trigger::TriggerEvent>(triggerEventLabel_);

  processName_ = pset.getParameter<std::string>("processName");

  m_outFile = new TFile("testout.root","RECREATE");

  initTree();
}

TestAODReader::~TestAODReader()
{

  delete m_clonesarray;

}

void TestAODReader::beginJob()
{

}

void TestAODReader::endJob()
{
  m_outFile->Close();
}

void TestAODReader::beginRun(edm::Run const& run, edm::EventSetup const& eventsetup)
{
  bool changed(true);
  if(hltConfig_.init(run,eventsetup,processName_,changed)){
    /*
    hltConfig_.dump("ProcessName");
    hltConfig_.dump("GlobalTag");
    hltConfig_.dump("TableName");
    hltConfig_.dump("Streams");
    hltConfig_.dump("Datasets");
    hltConfig_.dump("PrescaleTable");
    hltConfig_.dump("ProcessPSet");
    */
  }
}


void TestAODReader::analyze(const Event& event, const EventSetup& eventsetup)
{


  event_ = (long)event.id().event();
  run_ = (int)event.id().run();
  lumi_ = (int)event.luminosityBlock();

  makeProducts(event,eventsetup);

}

void TestAODReader::finish()
{

}

void TestAODReader::makeProducts(const Event& event, const EventSetup& eventsetup)
{
  event.getByToken(jetToken_,jetHandle_);
  makeJets();

  event.getByToken(electronToken_,electronHandle_);
  makeElectrons();

  event.getByToken(muonToken_,muonHandle_);
  makeMuons();

  event.getByToken(photonToken_,photonHandle_);
  makePhotons();

  event.getByToken(tauToken_,tauHandle_);
  makeTaus();

  event.getByToken(metToken_,metHandle_);
  makeMET();

  event.getByToken(trackToken_,trackHandle_);
  makeTracks();

  event.getByToken(vertexToken_,vertexHandle_);
  makeVertices();

  event.getByToken(triggerToken_, triggerHandle_);
  event.getByToken(triggerEventToken_, triggerEventHandle_);
  makeTriggers(event,eventsetup);

  event.getByToken(beamspotToken_, beamspotHandle_);
  makeBeamSpot();

  event.getByToken(genParticleToken_, genParticleHandle_);
  makeGenParticles();
}


void TestAODReader::fillTree()
{


}

void TestAODReader::initTree()
{

  TClass* cl = TClass::GetClass("SignatureObject");
  cout<<"inheritance: "<<cl->InheritsFrom(TObject::Class())<<endl;

  m_tree = new TTree("outtree","");

  //m_clonesarray = new TClonesArray("TLine");
  m_clonesarray = new TClonesArray("SignatureObject");
  
  m_tree->Branch("event", &event_,"event/L");
  m_tree->Branch("run", &run_, "run/I");
  m_tree->Branch("lumi", &lumi_, "lumi/I");
  
  m_tree->Branch("objects",&m_clonesarray,64000,0);

}

void TestAODReader::makeJets()
{

  vector<SignatureObject*> jets;
  for(int i = 0; i < (int)jetHandle_->size(); i++){
    const pat::Jet& pat_jet = jetHandle_->at(i);
    SignatureObject* jet = new SignatureObject(pat_jet.px(),pat_jet.py(),pat_jet.pz(),pat_jet.energy());
    jets.push_back(jet);
  }

  sort(jets.begin(),jets.end(),SignatureObjectComparison);
  reverse(jets.begin(),jets.end());

  m_productmap["ALLJETS"] = jets;


}

void TestAODReader::makeElectrons()
{

  vector<SignatureObject*> electrons;
  for(int i = 0; i < (int)electronHandle_->size(); i++){
    const pat::Electron& pat_electron = electronHandle_->at(i);
    SignatureObject* electron = new SignatureObject(pat_electron.px(),pat_electron.py(),pat_electron.pz(),pat_electron.energy());
    electrons.push_back(electron);
  }

  sort(electrons.begin(),electrons.end(),SignatureObjectComparison);
  reverse(electrons.begin(),electrons.end());

  m_productmap["ALLELECTRONS"] = electrons;

}

void TestAODReader::makeMuons()
{
  vector<SignatureObject*> muons;
  for(int i = 0; i < (int)muonHandle_->size(); i++){
    const pat::Muon& pat_muon = muonHandle_->at(i);
    SignatureObject* muon = new SignatureObject(pat_muon.px(),pat_muon.py(),pat_muon.pz(),pat_muon.energy());
    muons.push_back(muon);
  }

  sort(muons.begin(),muons.end(),SignatureObjectComparison);
  reverse(muons.begin(),muons.end());

  m_productmap["ALLMUONS"] = muons;

}

void TestAODReader::makePhotons()
{
  vector<SignatureObject*> photons;
  for(int i = 0; i < (int)photonHandle_->size(); i++){
    const reco::Photon& pat_photon = photonHandle_->at(i);
    SignatureObject* photon = new SignatureObject(pat_photon.px(),pat_photon.py(),pat_photon.pz(),pat_photon.energy());
    photons.push_back(photon);
  }

  sort(photons.begin(),photons.end(),SignatureObjectComparison);
  reverse(photons.begin(),photons.end());

  m_productmap["ALLPHOTONS"] = photons;

}

void TestAODReader::makeTaus()
{
  vector<SignatureObject*> taus;
  for(int i = 0; i < (int)tauHandle_->size(); i++){
    const pat::Tau& pat_tau = tauHandle_->at(i);
    SignatureObject* tau = new SignatureObject(pat_tau.px(),pat_tau.py(),pat_tau.pz(),pat_tau.energy());
    taus.push_back(tau);
  }

  sort(taus.begin(),taus.end(),SignatureObjectComparison);
  reverse(taus.begin(),taus.end());

  m_productmap["ALLTAUS"] = taus;

}

void TestAODReader::makeTracks()
{
  vector<SignatureObject*> tracks;
  for(int i = 0; i < (int)trackHandle_->size(); i++){
    const reco::Track& pat_track = trackHandle_->at(i);
    SignatureObject* track = new SignatureObject(pat_track.px(),pat_track.py(),pat_track.pz(),pat_track.p());
    tracks.push_back(track);
  }

  sort(tracks.begin(),tracks.end(),SignatureObjectComparison);
  reverse(tracks.begin(),tracks.end());

  m_productmap["ALLTRACKS"] = tracks;

}

void TestAODReader::makeVertices()
{
  vector<SignatureObject*> vertices;
  for(int i = 0; i < (int)vertexHandle_->size(); i++){
    const reco::Vertex& pat_vertex = vertexHandle_->at(i);
    SignatureObject* vertex = new SignatureObject(0,0,0,0);
    vertex->setVariable("VX",pat_vertex.x());
    vertex->setVariable("VY",pat_vertex.y());
    vertex->setVariable("VZ",pat_vertex.z());
    vertices.push_back(vertex);
  }

  m_productmap["ALLVERTICES"] = vertices;
}

void TestAODReader::makeBeamSpot()
{
  vector<SignatureObject*> beamspots;
  const reco::BeamSpot& pat_beamspot = (*beamspotHandle_);
  SignatureObject* beamspot = new SignatureObject(0,0,0,0);
  beamspot->setVariable("X0",pat_beamspot.x0());
  beamspot->setVariable("Y0",pat_beamspot.y0());
  beamspot->setVariable("Z0",pat_beamspot.z0());
  beamspots.push_back(beamspot);

  m_productmap["ALLBEAMSPOTS"] = beamspots;

}

void TestAODReader::makeTriggers(const edm::Event& event, const edm::EventSetup& eventsetup)
{
  vector<SignatureObject*> triggers;
  for(int i = 0; i < (int)hltConfig_.size(); i++){
    string trigName = hltConfig_.triggerName(i);
    const pair<int,int> prescales = hltConfig_.prescaleValues(event,eventsetup,trigName);
    const unsigned int triggerIndex = hltConfig_.triggerIndex(trigName);
    SignatureObject* trigger = new SignatureObject(0,0,0,0);
    trigger->setVariable("TRIGGERNAME",TString(trigName));
    trigger->setVariable("L1PRESCALE",prescales.first);
    trigger->setVariable("HLTPRESCALE",prescales.second);
    trigger->setVariable("PRESCALE",prescales.first*prescales.second);
    trigger->setVariable("WASRUN",triggerHandle_->wasrun(triggerIndex));
    trigger->setVariable("ACCEPT",triggerHandle_->accept(triggerIndex));
    trigger->setVariable("ERROR",triggerHandle_->accept(triggerIndex));
    triggers.push_back(trigger);
  }

  m_productmap["ALLTRIGGERS"] = triggers;
}

void TestAODReader::makeGenParticles()
{

}

void TestAODReader::makeMET()
{
  vector<SignatureObject*> mets;
  for(int i = 0; i < (int)metHandle_->size(); i++){
    const reco::PFMET& pat_met = metHandle_->at(i);
    SignatureObject* met = new SignatureObject(pat_met.px(),pat_met.py(),0,pat_met.pt());
    mets.push_back(met);
  }
  m_productmap["ALLMET"] = mets;
}



DEFINE_FWK_MODULE(TestAODReader);
