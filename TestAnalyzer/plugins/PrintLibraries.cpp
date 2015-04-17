#include "MWalker/TestAnalyzer/interface/PrintLibraries.h"
#include <TSystem.h>
#include <iostream>
using namespace edm;


using namespace std;

MWPrintLibraries::MWPrintLibraries(const edm::ParameterSet& iPara) 
{
  const char* allLibs = gSystem->GetLibraries();
  cout<<"Print libraries constructor: "<<allLibs<<endl;
}
//------------------------------------------------------------
//------------------------------------------------------------
MWPrintLibraries::~MWPrintLibraries()
{
  /* no op */
}
//------------------------------------------------------------
//------------------------------------------------------------
void MWPrintLibraries::beginJob()
{
  const char* allLibs = gSystem->GetLibraries();
  cout<<"Print libraries beginJob: "<<allLibs<<endl;

}

//------------------------------------------------------------
//------------------------------------------------------------
void MWPrintLibraries::endJob()
{

}
//------------------------------------------------------------
//------------------------------------------------------------
void MWPrintLibraries::beginRun(const edm::Run& iRun, const edm::EventSetup& iSetup)
{
  const char* allLibs = gSystem->GetLibraries();
  cout<<"Print libraries beginRun: "<<allLibs<<endl;

}
//------------------------------------------------------------
//------------------------------------------------------------
void MWPrintLibraries::endRun(const edm::Run& iRun, const edm::EventSetup& iSetup)
{
  /* no op */
}
//------------------------------------------------------------
//------------------------------------------------------------
void MWPrintLibraries::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

}
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------
//------------------------------------------------------------

DEFINE_FWK_MODULE(MWPrintLibraries);
