#include "MWalker/TriggerAnalyzer/interface/TriggerAnalyzer.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/TriggerNamesService.h"
#include "MWalker/TriggerAnalyzer/interface/TriggerTH1F_PT.h"
#include <functional>
#include <sstream>
#include <iostream>

using namespace std;

TriggerAnalyzer::TriggerAnalyzer(const edm::ParameterSet& iPara)
{
  m_totalEvents = 0;
  m_passEvents = 0;
  m_filterPassEvents = 0;
  m_outFile = 0;
  if(iPara.exists("outfile"))m_outFile = new TFile(iPara.getParameter<string>("outfile").c_str(),"RECREATE");

  gDirectory->cd();
  m_triggerSource = iPara.getParameter<edm::InputTag>("triggerSource");
  vector<string> triggers = iPara.getParameter<vector<string> >("triggers");
  for(int i = 0; i < (int)triggers.size(); i++){
    m_triggers.push_back(triggers[i]);
    m_trigger_pass[triggers[i]] = 0;
    vector<TriggerTH1F*> histos;
    m_histograms[triggers[i]] = histos;
  }

  m_product_names = iPara.getParameter<vector<edm::InputTag> >("products");

  if(iPara.exists("histograms")){
    vector<edm::ParameterSet> histos = iPara.getParameter<vector<edm::ParameterSet> >("histograms");
    for(int i = 0; i < (int)histos.size(); i++){
      addHistogram(histos[i]);
    }
  }

}
//------------------------------------------------------------
//------------------------------------------------------------
TriggerAnalyzer::~TriggerAnalyzer()
{
  /* no op */
}
//------------------------------------------------------------
//------------------------------------------------------------
void TriggerAnalyzer::beginJob()
{
  m_totalEvents = 0;
  m_passEvents = 0;
  m_filterPassEvents = 0;
}

//------------------------------------------------------------
//------------------------------------------------------------
void TriggerAnalyzer::endJob()
{
  printTable();

  m_outFile->cd();
  map<string, vector<TriggerTH1F*> >::const_iterator iter;
  for(iter = m_histograms.begin(); iter != m_histograms.end(); iter++){
    vector<TriggerTH1F*> vec = (*iter).second;
    for(int j = 0; j < (int) vec.size(); j++){
      TH1F h = *(dynamic_cast<TH1F *>(vec[j]));
      h.Write();
    }
  }
  m_outFile->Close();
  //cout<<"Of "<<m_totalEvents<<" events "<<m_passEvents<<" passed at least one trigger and "<<m_filterPassEvents<<" passed the filter"<<endl;
}
//------------------------------------------------------------
//------------------------------------------------------------
void TriggerAnalyzer::beginRun(const edm::Run& iRun, const edm::EventSetup& iSetup)
{
  //string process = "HLT3";
  //bool changed = true;
  //bool good = m_hltConfig.init(iRun,iSetup,process,changed);
}
//------------------------------------------------------------
//------------------------------------------------------------
void TriggerAnalyzer::endRun(const edm::Run& iRun, const edm::EventSetup& iSetup)
{
  /* no op */
}

//------------------------------------------------------------
//------------------------------------------------------------
void TriggerAnalyzer::addHistogram(edm::ParameterSet& iPara){
  TString histoType = (TString)iPara.getParameter<string>("type");
  map<string, vector<TriggerTH1F*> >::const_iterator iter;
  if(histoType == "PT"){
    if(iPara.exists("product")){
      TString productname = iPara.getParameter<string>("product");
      int whichone = -1;
      if(iPara.exists("whichone"))whichone = iPara.getParameter<int>("whichone");
      TriggerTH1F_PT* hall = new TriggerTH1F_PT(TString("ALL_"+iPara.getParameter<string>("name")).Data(),productname.Data(),whichone);
      hall->SetDirectory(0);
      m_histograms["ALL"].push_back(hall);
      TriggerTH1F_PT* hfilt = new TriggerTH1F_PT(TString("FILT_"+iPara.getParameter<string>("name")).Data(),productname.Data(),whichone);
      hfilt->SetDirectory(0);
      m_histograms["FILT"].push_back(hfilt);
      for(iter = m_histograms.begin(); iter != m_histograms.end(); iter++){
	TString name = (*iter).first;
	name += "_";
	name += iPara.getParameter<string>("name");
	TriggerTH1F_PT* h = new TriggerTH1F_PT(name.Data(),productname.Data(),whichone);
	h->SetDirectory(0);
	m_histograms[(*iter).first].push_back(h);
      }
    }
  }
}
//------------------------------------------------------------
//------------------------------------------------------------
void TriggerAnalyzer::printTable()
{
  cout<<"\\begin{table}"<<endl;
  cout<<"\\scriptsize"<<endl;
  cout<<"\\begin{center}"<<endl;
  cout<<"\\caption{Trigger Acceptance, "<<m_filterPassEvents<<" Selected Events}"<<endl;
  cout<<"\\begin{tabular}{|c|c|}"<<endl;
  cout<<"\\hline"<<endl;
  cout<<"Trigger Name & Acceptance \\\\"<<endl;
  cout<<"\\hline"<<endl;
  map<string,int>::const_iterator iter;
  for(iter = m_trigger_pass.begin(); iter!= m_trigger_pass.end(); iter++){
    cout<<(*iter).first<<" & "<<(float)(*iter).second/m_filterPassEvents<<" \\\\"<<endl;
  }
  cout<<"\\hline"<<endl;
  cout<<"OR of all triggers & "<<(float)m_passEvents/m_filterPassEvents<<" \\\\"<<endl;
  cout<<"\\hline"<<endl;
  cout<<"\\end{tabular}"<<endl;
  cout<<"\\end{center}"<<endl;
  cout<<"\\end{table}"<<endl;
}
//------------------------------------------------------------
//------------------------------------------------------------
vector<reco::LeafCandidate> TriggerAnalyzer::getProduct(TString name)
{
  vector<reco::LeafCandidate> retVec;
  if(m_products.find(name) != m_products.end())retVec = m_products[name];
  return retVec;
}
//------------------------------------------------------------
//------------------------------------------------------------
void TriggerAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  m_totalEvents++;

  for(int i = 0; i < (int)m_product_names.size(); i++){
    edm::Handle<vector<reco::LeafCandidate> > handle;
    iEvent.getByLabel(m_product_names[i],handle);
    const vector<reco::LeafCandidate> candVec = *handle;
    m_products[TString(m_product_names[i].label())] = candVec;
  }

  for(int i = 0; i < (int)m_histograms["ALL"].size();i++){
    m_histograms["ALL"][i]->Fill(this);
  }

  bool passOne = false;
  edm::Handle<edm::TriggerResults>handle;
  iEvent.getByLabel(m_triggerSource,handle);
  edm::Service<edm::service::TriggerNamesService> service;
  vector<string> triggerNames;
  service->getTrigPaths(*handle,triggerNames);
  for(int i = 0; i < (int)triggerNames.size(); i++){
    bool passThis = (*handle).accept(i);
    //bool passThis = (*handle).accept(m_hltConfig.triggerIndex(triggerNames[i]));
    if(passThis && find(m_triggers.begin(),m_triggers.end(),triggerNames[i]) != m_triggers.end()){
      passOne = true;
      m_trigger_pass[triggerNames[i]]++;
      for(int j = 0; j < (int)m_histograms[triggerNames[i]].size(); j++){
	m_histograms[triggerNames[i]][j]->Fill(this);
      }
    }
    if(passThis && triggerNames[i] == "FILTERonly"){
      m_filterPassEvents++;
      for(int j = 0; j < (int)m_histograms["FILT"].size(); j++){
	m_histograms["FILT"][j]->Fill(this);
      }

    }
  }


  if(passOne)m_passEvents++;
}
//------------------------------------------------------------
//------------------------------------------------------------

DEFINE_FWK_MODULE(TriggerAnalyzer);
