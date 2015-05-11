#ifndef SignatureObject_h
#define SignatureObject_h
#include <TLorentzVector.h>
#include <TROOT.h>
#include <TString.h>
#include <map>
#include <iostream>

class SignatureObject : public TLorentzVector {
 public:
  SignatureObject(double x=0,double y=0, double z=0, double t=0);
  SignatureObject(TLorentzVector v);
  SignatureObject(SignatureObject&);
  virtual ~SignatureObject();
  bool operator>(SignatureObject &s);
  bool operator<(SignatureObject &s);

  friend std::ostream& operator<<(std::ostream& os, const SignatureObject& so);

  bool getVariable(TString,int&);
  void setVariable(TString,int);
  bool getVariable(TString,bool&);
  void setVariable(TString,bool);
  bool getVariable(TString,double&);
  void setVariable(TString,double);
  bool getVariable(TString,TString&);
  void setVariable(TString,TString);

  SignatureObject* getAssociate(TString);
  void setAssociate(TString,SignatureObject*);
  std::map<TString,SignatureObject*> getAssociates(){return m_association_map;}
  void setAssociates(std::map<TString,SignatureObject*> c){m_association_map = c;}

  double Eta() const;

 protected:
  std::map<TString,double> m_variableMapDouble;
  std::map<TString,int> m_variableMapInt;
  std::map<TString,TString> m_variableMapTString;
  std::map<TString,bool> m_variableMapBool;
  std::map<TString,SignatureObject*> m_association_map;

  ClassDef(SignatureObject,1);

};

inline SignatureObject::SignatureObject(double x,double y, double z, double t):TLorentzVector(x,y,z,t){
}
inline SignatureObject::SignatureObject(TLorentzVector v):TLorentzVector(v){
}
inline bool SignatureObject::operator>(SignatureObject &s)
{
  return Pt() > s.Pt();
}
inline bool SignatureObject::operator<(SignatureObject &s)
{
  return Pt() < s.Pt();
}

inline SignatureObject* SignatureObject::getAssociate(TString name)
{
  std::map<TString,SignatureObject*>::const_iterator iter=m_association_map.find(name);
  if(iter != m_association_map.end())return (*iter).second;

  return 0;
}
inline void SignatureObject::setAssociate(TString name, SignatureObject* associate)
{
  std::map<TString,SignatureObject*>::const_iterator iter=m_association_map.find(name);
  if(iter != m_association_map.end() && (*iter).second != associate){
    std::cerr<<"Warning changing associate"<<std::endl;
  }
  m_association_map[name] = associate;
}

// This override is to prevent a warning if pT is zero (which is the case for incoming particles in simulation)
inline double SignatureObject::Eta() const {
  return -log(tan(Vect().Theta()/2));
}

inline void SignatureObject::setVariable(TString name, int val)
{
  m_variableMapInt[name] = val;
}

inline bool SignatureObject::getVariable(TString name, int &val)
{
  std::map<TString,int>::const_iterator iter = m_variableMapInt.find(name);
  if(iter != m_variableMapInt.end()){
    val = (*iter).second;
    return true;
  }
  return false;
}
inline void SignatureObject::setVariable(TString name, TString val)
{
  m_variableMapTString[name] = val;
}

inline bool SignatureObject::getVariable(TString name, TString &val)
{
  std::map<TString,TString>::const_iterator iter = m_variableMapTString.find(name);
  if(iter != m_variableMapTString.end()){
    val = (*iter).second;
    return true;
  }
  return false;
}
inline void SignatureObject::setVariable(TString name, bool val)
{
  m_variableMapBool[name] = val;
}

inline bool SignatureObject::getVariable(TString name, bool &val)
{
  std::map<TString,bool>::const_iterator iter = m_variableMapBool.find(name);
  if(iter != m_variableMapBool.end()){
    val = (*iter).second;
    return true;
  }
  return false;
}
inline void SignatureObject::setVariable(TString name, double val)
{
  m_variableMapDouble[name] = val;
}

inline bool SignatureObject::getVariable(TString name, double &val)
{
  std::map<TString,double>::const_iterator iter = m_variableMapDouble.find(name);
  if(iter != m_variableMapDouble.end()){
    val = (*iter).second;
    return true;
  }
  return false;
}

bool SignatureObjectComparison(SignatureObject*,SignatureObject*);

#endif
