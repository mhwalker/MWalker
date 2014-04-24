from ROOT import *

gROOT.SetStyle("Plain")
gStyle.SetPalette(1)
#gROOT.SetOptStat(0)

f = TFile("trackAnalyzerOut.root")
d_eta = f.Get("duplicate_eta")
d_pdR = f.Get("duplicate_pdR")
d_vdR = f.Get("duplicate_vdR")
d_bestdR = f.Get("duplicate_bestdR")
d_minDelta = f.Get("duplicate_minDelta")
d_mPT = f.Get("duplicate_matchedPerTrack")
d_dpT = f.Get("duplicate_deltapT")
d_nHits = f.Get("duplicate_nSharedHits")
d_innerR = f.Get("duplicate_innerR")
d_outerR = f.Get("duplicate_outerR")
d_nHits2 = f.Get("duplicate_nHits")
d_pT = f.Get("duplicate_pT")
d_R = f.Get("duplicate_deltaR")
d_nMissingHits = f.Get("duplicate_nMissingHits")

d2_q = f.Get("duplicate_qoverp")
d2_l = f.Get("duplicate_lambda")
d2_p = f.Get("duplicate_phi")
d2_x = f.Get("duplicate_dxy")
d2_z = f.Get("duplicate_dsz")
c2_q = f.Get("comb_qoverp")
c2_l = f.Get("comb_lambda")
c2_p = f.Get("comb_phi")
c2_x = f.Get("comb_dxy")
c2_z = f.Get("comb_dsz")


c = TCanvas("c","",800,600)
c.SetLogy()

d_eta.SetXTitle("#eta of sim tracks")
d_eta.Draw()
c.SaveAs("eta.eps")
c.Clear()

d_nHits.SetXTitle("number of shared hits")
d_nHits.Draw()
c.SaveAs("nSharedHits.eps")
c.Clear()

d_minDelta.GetXaxis().SetRangeUser(0,50)
d_minDelta.SetXTitle("#Delta x inner to outer")
d_minDelta.Draw()
c.SaveAs("minDelta.eps")
c.Clear()

d_dpT.SetXTitle("(p_{T1} - p_{T2})/p_{T1}")
d_dpT.Draw()
c.SaveAs("dpT.eps")
c.Clear()

d_mPT.SetXTitle("N matched reco tracks to a sim track")
d_mPT.Draw()
c.SaveAs("matchedTracks.eps")
c.Clear()

d_bestdR.SetXTitle("#Delta R inner to outer")
d_bestdR.Draw()
c.SaveAs("bestdR.eps")
c.Clear()
c.SetLogy(0)

d_innerR.SetXTitle("innerPosition Radius")
d_innerR.SetYTitle("innerPosition Radius")
d_innerR.Draw("colz")
c.SaveAs("innerR.eps")
c.Clear()

d_outerR.SetXTitle("outerPosition Radius")
d_outerR.SetYTitle("outerPosition Radius")
d_outerR.Draw("colz")
c.SaveAs("outerR.eps")
c.Clear()

d_nHits2.SetXTitle("nHits")
d_nHits2.SetYTitle("nHits")
d_nHits2.Draw("colz")
c.SaveAs("nHits.eps")
c.Clear()

d_nMissingHits.SetXTitle("nMissingHits")
d_nMissingHits.SetYTitle("nMissingHits")
d_nMissingHits.Draw("colz")
c.SaveAs("nMissingHits.eps")
c.Clear()

d_pT.SetXTitle("innerMomentum pT")
d_pT.SetYTitle("innerMomentum pT")
d_pT.Draw("colz")
c.SaveAs("pT2d.eps")
c.Clear()

d_R.SetXTitle("deltaR inner to outer")
d_R.Draw()
c.SaveAs("deltaR.eps")
c.Clear()

d2_q.SetXTitle("q over p")
d2_q.SetYTitle("q over p")
d2_q.Draw("colz")
c.SaveAs("duplicate_qoverp2d.eps")
c.Clear()

d2_l.SetXTitle("lambda")
d2_l.SetYTitle("lambda")
d2_l.Draw("colz")
c.SaveAs("duplicate_lambda2d.eps")
c.Clear()

d2_p.SetXTitle("phi")
d2_p.SetYTitle("phi")
d2_p.Draw("colz")
c.SaveAs("duplicate_phi2d.eps")
c.Clear()

d2_x.SetXTitle("dxy")
d2_x.SetYTitle("dxy")
d2_x.Draw("colz")
c.SaveAs("duplicate_dxy2d.eps")
c.Clear()

d2_z.SetXTitle("dsz")
d2_z.SetYTitle("dsz")
d2_z.Draw("colz")
c.SaveAs("duplicate_dsz2d.eps")
c.Clear()


c2_q.SetXTitle("q over p")
c2_q.SetYTitle("q over p")
c2_q.Draw("colz")
c.SaveAs("comb_qoverp2d.eps")
c.Clear()

c2_l.SetXTitle("lambda")
c2_l.SetYTitle("lambda")
c2_l.Draw("colz")
c.SaveAs("comb_lambda2d.eps")
c.Clear()

c2_p.SetXTitle("phi")
c2_p.SetYTitle("phi")
c2_p.Draw("colz")
c.SaveAs("comb_phi2d.eps")
c.Clear()

c2_x.SetXTitle("dxy")
c2_x.SetYTitle("dxy")
c2_x.Draw("colz")
c.SaveAs("comb_dxy2d.eps")
c.Clear()

c2_z.SetXTitle("dsz")
c2_z.SetYTitle("dsz")
c2_z.Draw("colz")
c.SaveAs("comb_dsz2d.eps")
c.Clear()

comparisons = ['dqoverp','dlambda','dphi','ddxy','ddsz','bestdR','chi2','pcaR']
for co in comparisons:
    m = f.Get("duplicate_"+co)
    u = f.Get("comb_"+co)
    u.SetXTitle(co)
    u.GetYaxis().SetRangeUser(0,u.GetMaximum()*1.1)
    u.SetLineColor(kBlack)
    m.Scale(40)
    m.SetLineColor(kRed)
    c.SetLogy(0)
    if co == 'bestdR' or co == 'chi2' or co == 'pcaR':
        u.GetYaxis().SetRangeUser(0.1,u.GetMaximum()*5)
        c.SetLogy()
    u.Draw()
    m.Draw("same")
    leg = TLegend(0.6,0.5,0.85,0.85)
    leg.AddEntry(u,"combinatorics","l")
    leg.AddEntry(m,"duplicates  X40","l")
    leg.SetFillColor(kWhite)
    leg.Draw()
    c.SaveAs(co+".eps")
    c.Clear()

cuthistos = ['cut0_pcaR','cut1_dphi','cut2_ddsz','cut3_dlambda','cut4_ddxy','cut5_innerR']
dupcut = []
comcut = []
ratios = []
dupcut.append(f.Get("duplicate_dqoverp"))
comcut.append(f.Get("comb_dqoverp"))
for ch in cuthistos:
    dd = f.Get("duplicate_"+ch)
    cc = f.Get("comb_"+ch)
    dd.SetDirectory(0)
    dupcut.append(dd)
    comcut.append(cc)


c.Clear()
c.SetLogy()
comcut[0].SetLineColor(kRed)
dupcut[0].SetLineColor(kRed)
comcut[0].GetYaxis().SetRangeUser(0.1,5*comcut[0].GetMaximum())
dupcut[0].GetYaxis().SetRangeUser(0.1,5*dupcut[0].GetMaximum())
comcut[0].SetXTitle("q / p")
dupcut[0].SetXTitle("q / p")
dupcut[0].Scale(1./40.)
print dupcut[0].GetEntries(),dupcut[1].GetEntries()
leg1 = TLegend(0.6,0.5,0.88,0.85)
leg1.SetFillColor(kWhite)
leg1.AddEntry(comcut[0],"no cuts","l")
comcut[0].Draw()
ct = comcut[0].GetEntries()
for k,v in enumerate(comcut):
    print v.GetEntries()/ct
    if k != 0:
        v.SetLineColor(kBlue+k-3)
        leg1.AddEntry(v,cuthistos[k-1],"l")
    v.Draw("same")
leg1.Draw()
c.SaveAs("comb_cutFlow.eps")

c.Clear()
dupcut[0].Draw()
dt = dupcut[0].GetEntries()
for k,v in enumerate(dupcut):
    print v.GetEntries()/dt
    if k == 0:
        v.Draw()
    if k != 0:
        v.SetLineColor(kBlue+k-3)
    v.Draw("same")
leg1.Draw()
c.SaveAs("dup_cutFlow.eps")

for k,v in enumerate(dupcut):
    r = v.Clone("r"+str(k))
    print k,v.GetName(),r.GetName(),v.GetEntries(),r.GetEntries()
    r.SetDirectory(0)
    r.Divide(comcut[k])
    r.SetLineWidth(2)
    #if k == 0: r.Draw()
    ratios.append(r)
ratios[0].SetLineColor(kRed)
ratios[0].Draw()
ratios[0].GetYaxis().SetRangeUser(1e-5,10.0)
for k,r in enumerate(ratios):
    r.Draw("same")
    
leg1.Draw()
c.SaveAs("cutFlow.eps")
c.Clear()

c5 = TCanvas("c5","",1000,600)
c5.Divide(3,2)
