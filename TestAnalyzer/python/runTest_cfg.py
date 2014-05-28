import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process("RutgersAOD")
options = VarParsing.VarParsing ('analysis')

#set default arguments
options.inputFiles= 'file:/cms/se/phedex/store/mc/Spring14dr/GJet_Pt-15to3000_Tune4C_13TeV_pythia8/AODSIM/PU20bx25_POSTLS170_V5-v1/010007/FEEC76AE-5BD1-E311-8A53-00266CF9BED8.root'
#options.inputFiles= 'file:/cms/thomassen/2012/Signal/StopRPV/store/aodsim/LLE122/StopRPV_8TeV_chunk3_stop950_bino800_LLE122_aodsim.root'
#options.maxEvents = 100 # -1 means all events
#options.maxEvents = 100

# get and parse the command line arguments
options.parseArguments()

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(options.inputFiles),
)

## Geometry and Detector Conditions (needed for a few patTuple production steps)
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:startup')
process.load("Configuration.StandardSequences.MagneticField_cff")

process.printLibraries = cms.EDProducer("MWPrintLibraries",
                                        )

process.load('PhysicsTools.PatAlgos.patSequences_cff')

process.load("MWalker.TestAnalyzer.testAOD_cfi")
#process.options.allowUnscheduled = cms.untracked.bool( True )

process.load("PhysicsTools.PatAlgos.producersLayer1.electronProducer_cff")

process.p = cms.Path(
#    process.printLibraries*
    process.particleFlowPtrs *
    process.pfParticleSelectionForIsoSequence *
    process.pfElectronIsolationSequence *
    process.electronMatch *
    process.patElectrons *
#    process.patCandidates *
#    process.selectedPatCandidates *
    process.baseAOD)
