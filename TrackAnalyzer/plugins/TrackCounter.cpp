#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include <iostream>
#include <cmath>
#include "FWCore/Framework/interface/MakerMacros.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"

class TrackCounter : public edm::EDAnalyzer {

 public:
  explicit TrackCounter( const edm::ParameterSet&);
  void endJob();

 private:
  virtual void analyze( const edm::Event&, const edm::EventSetup&);

  std::string src_;
  bool verbose_;

  unsigned long n_,nSum_,n2Sum_;

};


TrackCounter::TrackCounter( const edm::ParameterSet& iPara)
{
  src_ = iPara.getParameter<std::string>("src");
  verbose_ = iPara.getParameter<bool>("verbose");
  n_ = 0;
  nSum_ = 0;
  n2Sum_ = 0;
}

void TrackCounter::endJob ()
{

  double n = 0, n2 = 0, s;
  if(n_ != 0){
    n = double(nSum_)/n_;
    n2 = double(n2Sum_)/n_;
  }
  s = sqrt(n2 - n*n);
  if(verbose_){
    std::cout<< "TRACKCOUNTER -- collection "<<src_<<" contains ("<<n<< "+/-" << s << ") objects, total: "<<nSum_<<std::endl;
  }
}

void TrackCounter::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  edm::Handle<reco::TrackCollection> h;
  iEvent.getByLabel(src_,h);
  if(!h.isValid()){
    std::cerr<< "product "<<src_<<"not found"<<std::endl;
  }else{
    int n = h->size();
    nSum_ += n;
    n2Sum_ += (n*n);
  }
  ++n_;
}
 
DEFINE_FWK_MODULE( TrackCounter );
