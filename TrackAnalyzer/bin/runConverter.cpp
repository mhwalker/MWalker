#include "MWalker/TrackAnalyzer/interface/BDTConverter.h"
#include <TString.h>
int main(int argc, char** argv)
{
  std::cout<<argc<<std::endl;
  if(argc == 1){
    for(int i = 0; i < 3; i++){
      TString wfname = TString::Format("./SelectorWeightBDTGIter%i.xml",i);
      TString rfname = TString::Format("./SelectorWeightBDTGIter%i.root",i);
      BDTConverter* converter = new BDTConverter(wfname,rfname);   
      
      converter->addVariable("pt");
      converter->addVariable("lostmidfrac");
      converter->addVariable("minlost");
      converter->addVariable("nhits");
      converter->addVariable("relpterr");
      converter->addVariable("eta");
      converter->addVariable("chi2n_no1Dmod");
      converter->addVariable("chi2n");
      converter->addVariable("nlayerslost");
      converter->addVariable("nlayers3D");
      converter->addVariable("nlayers");
      converter->addVariable("ndof");
      converter->addVariable("absd0PV");
      converter->addVariable("absdzPV");
      converter->addVariable("absdz");
      converter->addVariable("absd0");
      
      converter->convert();
    }
    for(int i = 3; i < 7; i++){
      TString wfname = TString::Format("./SelectorWeightBDTGIter%i.xml",i);
      TString rfname = TString::Format("./SelectorWeightBDTGIter%i.root",i);
      BDTConverter* converter = new BDTConverter(wfname,rfname);   
      
      converter->addVariable("pt");
      converter->addVariable("lostmidfrac");
      converter->addVariable("minlost");
      converter->addVariable("nhits");
      converter->addVariable("relpterr");
      converter->addVariable("eta");
      converter->addVariable("chi2n_no1Dmod");
      converter->addVariable("chi2n");
      converter->addVariable("nlayerslost");
      converter->addVariable("nlayers3D");
      converter->addVariable("nlayers");
      converter->addVariable("ndof");
      
      converter->convert();
    }
  }else if(argc == 3){
    TString wfname = TString::Format("%s",argv[1]);
    TString rfname = wfname;
    rfname.ReplaceAll(".xml",".root");
    BDTConverter* converter = new BDTConverter(wfname,rfname);

    converter->addVariable("pt");
    converter->addVariable("lostmidfrac");
    converter->addVariable("minlost");
    converter->addVariable("nhits");
    converter->addVariable("relpterr");
    converter->addVariable("eta");
    converter->addVariable("chi2n_no1Dmod");
    converter->addVariable("chi2n");
    converter->addVariable("nlayerslost");
    converter->addVariable("nlayers3D");
    converter->addVariable("nlayers");
    converter->addVariable("ndof");
    TString mvatype = TString::Format("%s",argv[2]);
    if(mvatype == "Prompt"){
      converter->addVariable("absd0PV");
      converter->addVariable("absdzPV");
      converter->addVariable("absdz");
      converter->addVariable("absd0");
    }
    converter->convert();
  }
}
