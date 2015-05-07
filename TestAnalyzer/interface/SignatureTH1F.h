#ifndef SignatureTH1F_h
#define SignatureTH1F_h
#include <TH1F.h>
#include <TObject.h>
#include "MWalker/TestAnalyzer/interface/SignatureObject.h"

class SignatureTH1F : public TH1F  {
 public:
  SignatureTH1F(const char* name, const char* title, int nbins, double xmin, double xmax);
  SignatureTH1F(TH1F h);
  SignatureTH1F():TH1F(){/*no-op*/}
  virtual ~SignatureTH1F(){/* no-op*/}
  using TH1F::Fill;
  virtual Int_t Fill(SignatureObject*) = 0;
  virtual void Copy(TObject&) const = 0;

 protected:

  ClassDef(SignatureTH1F,1);

};

inline SignatureTH1F::SignatureTH1F(const char* name, const char* title, int nbins, double xmin, double xmax):TH1F(name,title,nbins,xmin,xmax){
}


inline SignatureTH1F::SignatureTH1F(TH1F v):TH1F(v){
}
#endif
