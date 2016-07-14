# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --customise SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2017 --conditions auto:phase1_2017_design -s RAW2DIGI,L1Reco,RECO --datatier GEN-SIM-RECO -n 10 --geometry Extended2017 --eventcontent FEVTDEBUGHLT --no_exec --filein file:step2.root --fileout file:step3.root
import FWCore.ParameterSet.Config as cms
import sys

process = cms.Process('RECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2017Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(sys.argv[2]),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True),
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition
process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('outputRECO1/output_'+sys.argv[3]+'.root'),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)


usePhase1 = True


process.load("CondCore.DBCommon.CondDBCommon_cfi")
# input database (in this case local sqlite file)
process.CondDBCommon.connect = 'sqlite_file:GBRWrapper_13TeV_800pre5_phase1.db'

process.PoolDBESSource = cms.ESSource("PoolDBESSource",
    process.CondDBCommon,
    DumpStat=cms.untracked.bool(True),
    toGet = cms.VPSet(
      cms.PSet(
        record = cms.string('GBRWrapperRcd'),
        label = cms.untracked.string('MVASelectorIter0_13TeV_v1'),
        tag = cms.string('MVASelectorIter0_13TeV_v1')
      ),
      cms.PSet(
        record = cms.string('GBRWrapperRcd'),
        label = cms.untracked.string('MVASelectorIter1_13TeV_v1'),
        tag = cms.string('MVASelectorIter1_13TeV_v1')
      ),
      cms.PSet(
        record = cms.string('GBRWrapperRcd'),
        label = cms.untracked.string('MVASelectorIter2_13TeV_v1'),
        tag = cms.string('MVASelectorIter2_13TeV_v1')
      ),
      cms.PSet(
        record = cms.string('GBRWrapperRcd'),
        label = cms.untracked.string('MVASelectorIter3_13TeV_v1'),
        tag = cms.string('MVASelectorIter3_13TeV_v1')
      ),
      cms.PSet(
        record = cms.string('GBRWrapperRcd'),
        label = cms.untracked.string('MVASelectorIter4_13TeV_v1'),
        tag = cms.string('MVASelectorIter4_13TeV_v1')
      ),
      cms.PSet(
        record = cms.string('GBRWrapperRcd'),
        label = cms.untracked.string('MVASelectorIter5_13TeV_v1'),
        tag = cms.string('MVASelectorIter5_13TeV_v1')
      ),
      cms.PSet(
        record = cms.string('GBRWrapperRcd'),
        label = cms.untracked.string('MVASelectorIter6_13TeV_v1'),
        tag = cms.string('MVASelectorIter6_13TeV_v1')
      ),
      cms.PSet(
        record = cms.string('GBRWrapperRcd'),
        label = cms.untracked.string('MVASelectorIter7_13TeV_v1'),
        tag = cms.string('MVASelectorIter7_13TeV_v1')
      ),
    )
)


# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2017_design', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.endjob_step,process.RECOSIMoutput_step)

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.combinedCustoms
from SLHCUpgradeSimulations.Configuration.combinedCustoms import cust_2017 

#call to customisation function cust_2017 imported from SLHCUpgradeSimulations.Configuration.combinedCustoms
process = cust_2017(process)

#print sys.argv

if usePhase1:
    from RecoTracker.FinalTrackSelectors.TrackMVAClassifierPrompt_cfi import *
#process.initialStepClassifier1.qualityCuts = [-100,-100,-100]
    process.initialStepClassifier1.GBRForestLabel = "MVASelectorIter0_13TeV_v1"
    process.initialStepClassifier2.GBRForestLabel = "MVASelectorIter2_13TeV_v1"#DetachedQuad
    process.initialStepClassifier3.GBRForestLabel = "MVASelectorIter4_13TeV_v1"#lowpt triplet
    process.highPtTripletStep = TrackMVAClassifierPrompt.clone()
    process.highPtTripletStep.src = 'highPtTripletStepTracks'
    process.highPtTripletStep.GBRForestLabel = "MVASelectorIter1_13TeV_v1"
    process.highPtTripletStep.qualityCuts = [-0.9,-0.8,-0.7]
    process.detachedQuadStepClassifier1.GBRForestLabel = "MVASelectorIter2_13TeV_v1"
    process.detachedQuadStepClassifier2.GBRForestLabel = "MVASelectorIter0_13TeV_v1"
    process.lowPtQuadStep.GBRForestLabel = "MVASelectorIter3_13TeV_v1"
#process.lowPtTripletStep.qualityCuts = [-100,-100,-100]
    process.lowPtTripletStep =  TrackMVAClassifierPrompt.clone()
    process.lowPtTripletStep.GBRForestLabel = "MVASelectorIter4_13TeV_v1"
    process.lowPtTripletStep.src = 'lowPtTripletStepTracks'
    process.lowPtTripletStep.qualityCuts = [-0.6,-0.3,-0.1]
#process.mixedTripletStepClassifier1.qualityCuts = [-100,-100,-100]
    process.mixedTripletStepClassifier1.GBRForestLabel = "MVASelectorIter5_13TeV_v1"
    process.mixedTripletStepClassifier2.GBRForestLabel = "MVASelectorIter0_13TeV_v1"
#process.pixelLessStepClassifier1.qualityCuts = [-100,-100,-100]
    process.pixelLessStepClassifier1.GBRForestLabel = "MVASelectorIter6_13TeV_v1"
    process.pixelLessStepClassifier2.GBRForestLabel = "MVASelectorIter0_13TeV_v1"
#process.tobTecStepClassifier1.qualityCuts = [-100,-100,-100]
    process.tobTecStepClassifier1.GBRForestLabel = "MVASelectorIter7_13TeV_v1"
    process.tobTecStepClassifier2.GBRForestLabel = "MVASelectorIter0_13TeV_v1"
else:
#process.initialStepClassifier1.qualityCuts = [-100,-100,-100]
    process.initialStepClassifier1.GBRForestLabel = "MVASelectorIter0_13TeV_v1"
    process.initialStepClassifier2.GBRForestLabel = "MVASelectorIter3_13TeV_v1"
    process.initialStepClassifier3.GBRForestLabel = "MVASelectorIter1_13TeV_v1"
#process.lowPtTripletStep.qualityCuts = [-100,-100,-100]
    process.lowPtTripletStep.GBRForestLabel = "MVASelectorIter1_13TeV_v1"
#process.pixelPairStep.qualityCuts = [-100,-100,-100]
    process.pixelPairStep.GBRForestLabel = "MVASelectorIter2_13TeV_v1"
#process.detachedTripletStepClassifier1.qualityCuts = [-100,-100,-100]
    process.detachedTripletStepClassifier1.GBRForestLabel = "MVASelectorIter3_13TeV_v1"
    process.detachedTripletStepClassifier2.GBRForestLabel = "MVASelectorIter0_13TeV_v1"
#process.mixedTripletStepClassifier1.qualityCuts = [-100,-100,-100]
    process.mixedTripletStepClassifier1.GBRForestLabel = "MVASelectorIter4_13TeV_v1"
    process.mixedTripletStepClassifier2.GBRForestLabel = "MVASelectorIter0_13TeV_v1"
#process.pixelLessStepClassifier1.qualityCuts = [-100,-100,-100]
    process.pixelLessStepClassifier1.GBRForestLabel = "MVASelectorIter5_13TeV_v1"
    process.pixelLessStepClassifier2.GBRForestLabel = "MVASelectorIter0_13TeV_v1"
#process.tobTecStepClassifier1.qualityCuts = [-100,-100,-100]
    process.tobTecStepClassifier1.GBRForestLabel = "MVASelectorIter7_13TeV_v1"
    process.tobTecStepClassifier2.GBRForestLabel = "MVASelectorIter0_13TeV_v1"


# End of customisation functions

