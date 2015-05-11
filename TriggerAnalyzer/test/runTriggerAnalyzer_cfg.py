import sys
import FWCore.ParameterSet.Config as cms
process = cms.Process("TriggerAnalysis")

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkSummary = cms.untracked.PSet(
    reportEvery = cms.untracked.int32(500),
    limit = cms.untracked.int32(10000000)
)
process.MessageLogger.cerr.FwkReport = cms.untracked.PSet(
    reportEvery = cms.untracked.int32(500),
    limit = cms.untracked.int32(10000000)
)

filePrefex="file:"
if(sys.argv[2].find("/pnfs/")==0):
    filePrefex="dcap://heplnx209.pp.rl.ac.uk:22125"

if(sys.argv[2].find("/store/")==0):
    filePrefex=""

if(sys.argv[2].find("/castor/")==0):
    filePrefex="rfio:"

process.source = cms.Source("PoolSource",
                 #         fileNames = cms.untracked.vstring(filePrefex+sys.argv[2]),
                       #     inputCommands = cms.untracked.vstring("drop *","keep *_source_*_*"),
                            fileNames = cms.untracked.vstring(),
)

fname=""
triggerList = cms.vstring()
histogramList = cms.VPSet()
for i in range(2,len(sys.argv)):
    print filePrefex+sys.argv[i]
    fname = sys.argv[i]
    process.source.fileNames.extend([filePrefex+sys.argv[i],])

ofName = cms.string(fname.replace("TRIGFILES","HISTFILES"))

if "hrpv" in fname or "lambda" in fname or "coNLSP" in fname:
    triggerList = cms.vstring("HLT_Ele65_CaloIdVT_TrkIdT_v8","HLT_Ele80_CaloIdVT_TrkIdT_v5","HLT_Ele100_CaloIdVT_TrkIdT_v5","HLT_DoubleEle33_CaloIdL_v9","HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v1","HLT_DoubleEle33_CaloIdT_v5","HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v12","HLT_Mu17_TkMu8_v7","HLT_Mu22_TkMu8_v2","HLT_Mu22_TkMu22_v2","HLT_Mu30_Ele30_CaloIdL_v2","HLT_Mu40_eta2p1_v8","HLT_IsoMu24_eta2p1_v10","HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v2","HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v2")
    histogramList = cms.VPSet(
    cms.PSet(type=cms.string("PT"),product=cms.string("electrons"),whichone=cms.int32(1),name=cms.string("leadingElectron_pT")),
    cms.PSet(type=cms.string("PT"),product=cms.string("electrons"),whichone=cms.int32(2),name=cms.string("subleadingElectron_pT")),
    cms.PSet(type=cms.string("PT"),product=cms.string("muons"),whichone=cms.int32(1),name=cms.string("leadingMuon_pT")),
    cms.PSet(type=cms.string("PT"),product=cms.string("muons"),whichone=cms.int32(2),name=cms.string("subleadingMuon_pT"))
    )    
elif "addmonophoton" in fname or "AxialvectorUNI" in fname or "VectorUNI" in fname:
    triggerList = cms.vstring("HLT_Photon135_v4","HLT_Photon150_v1","HLT_Photon160_v1","HLT_Photon250_NoHE_v1","HLT_Photon300_NoHE_v1")
elif "WprimeToWZTo2Q2L" in fname:
    triggerList = cms.vstring("HLT_DoubleEle33_CaloIdL_v9","HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v1","HLT_DoubleEle33_CaloIdT_v5","HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v12","HLT_Mu17_TkMu8_v7","HLT_Mu22_TkMu8_v2","HLT_Mu22_TkMu22_v2")
    histogramList = cms.VPSet(
    cms.PSet(type=cms.string("PT"),product=cms.string("electrons"),whichone=cms.int32(1),name=cms.string("leadingElectron_pT")),
    cms.PSet(type=cms.string("PT"),product=cms.string("electrons"),whichone=cms.int32(2),name=cms.string("subleadingElectron_pT")),
    cms.PSet(type=cms.string("PT"),product=cms.string("muons"),whichone=cms.int32(1),name=cms.string("leadingMuon_pT")),
    cms.PSet(type=cms.string("PT"),product=cms.string("muons"),whichone=cms.int32(2),name=cms.string("subleadingMuon_pT"))
    )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.electrons = cms.EDProducer("SimParticleFilter",
                                   sourceName = cms.InputTag("genParticles"),
                                   statuses = cms.vdouble(1),
                                   pdgIDs = cms.vdouble(-11,11)
                                   )

process.muons = cms.EDProducer("SimParticleFilter",
                               sourceName = cms.InputTag("genParticles"),
                               statuses = cms.vdouble(1),
                               pdgIDs = cms.vdouble(-13,13)
                               )

process.met = cms.EDProducer("SimMETFilter",
                             sourceName = cms.InputTag("genMetTrue")
                             )

process.photons = cms.EDProducer("SimParticleFilter",
                                 sourceName = cms.InputTag("genParticles"),
                                 status = cms.vdouble(1),
                                 pdgIDs = cms.vdouble(22)
                                 )

process.jets = cms.EDProducer("SimJetFilter",
                              sourceName = cms.InputTag("ak5GenJets")
                              )

process.triggerAnalyzer = cms.EDAnalyzer("TriggerAnalyzer",
                                         triggerSource = cms.InputTag("TriggerResults"),
                                         triggers = triggerList,
                                         products = cms.VInputTag("electrons","muons","met","jets","photons"),
                                         histograms = histogramList,
                                         outfile = ofName
                                         )

process.analyzerSequence = cms.Sequence(process.electrons+process.muons+process.met+process.photons+process.jets+process.triggerAnalyzer)

#process.p = cms.Path(process.triggerAnalyzer)

process.p = cms.Path(process.analyzerSequence)
