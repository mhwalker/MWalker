void histoTest()
{
  gSystem->Load("libMWalkerTestAnalyzer.so");
  SignatureTH1F_ObjectVariable<double>* hd0 = new SignatureTH1F_ObjectVariable<double>("hd0","PT","goodJets","PT",100,0,100);
  hd0->addProduct("goodElectrons");

  SignatureTH1F_ObjectVariable<double>* hd1 = hd0->Clone("hd1");

  cout<<hd0->GetName()<<" "<<hd0->m_varname<<" "<<hd0->m_productnames.size()<<endl;
  cout<<hd1->GetName()<<" "<<hd1->m_varname<<" "<<hd1->m_productnames.size()<<endl;
}
