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

process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(1048576),
    fileName = cms.untracked.string('file:step3.root'),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

process.load("SimGeneral.TrackingAnalysis.trackingParticles_cfi")
#process.load("DQMServices.Components.EDMtoMEConverter_cff")

usePhase1 = True



process.load("SimTracker.TrackAssociatorProducers.quickTrackAssociatorByHits_cfi")

# Additional output definition
process.myAnalyzer = cms.EDAnalyzer("MWPurityTreeMaker",
				    isPhase1 = cms.bool(usePhase1),
                                    source=cms.string("generalTracks"),
                                    simSource=cms.InputTag("mix","MergedTrackTruth"),
                                    beamspot = cms.InputTag("offlineBeamSpot"),
                                    vertices = cms.InputTag("firstStepPrimaryVertices"),
                                    outfile=cms.string('outputTuple/output_'+sys.argv[3]+"_"+sys.argv[4]+'.root'),
                                    associator=cms.string("quickTrackAssociatorByHits"),
                                    )

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2017_design', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction*process.quickTrackAssociatorByHits*process.myAnalyzer)
process.endjob_step = cms.EndPath(process.endOfProcess)
#process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.endjob_step)

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.combinedCustoms
from SLHCUpgradeSimulations.Configuration.combinedCustoms import cust_2017 

#call to customisation function cust_2017 imported from SLHCUpgradeSimulations.Configuration.combinedCustoms
process = cust_2017(process)

print sys.argv

if usePhase1:
    if sys.argv[4] == 'iter0':
        process.initialStepClassifier1.qualityCuts = [-100,-100,-100]
    elif sys.argv[4] == 'iter1':
        process.highPtTripletStep.qualityCuts = [-100,-100,-100]
        process.highPtTripletStep.mva.minPixelHits = [0,0,0]
        process.highPtTripletStep.mva.maxChi2n = [9999.,9999.,9999.]
        process.highPtTripletStep.mva.minLayers = [0,0,0]
        process.highPtTripletStep.mva.min3DLayers = [0,0,0]
        process.highPtTripletStep.mva.maxLostLayers = [9999,9999,9999]
        process.highPtTripletStep.mva.dr_par.dr_par1 = [9999.,9999.,9999.]
        process.highPtTripletStep.mva.dz_par.dz_par1 = [9999.,9999.,9999.]
        process.highPtTripletStep.mva.dr_par.dr_par2 = [9999.,9999.,9999.]
        process.highPtTripletStep.mva.dz_par.dz_par2 = [9999.,9999.,9999.]
        process.highPtTripletStep.mva.dr_par.d0err_par = [0.001,0.001,0.001]
    elif sys.argv[4] == 'iter2':
        process.detachedQuadStepClassifier1.qualityCuts = [-100,-100,-100]
    elif sys.argv[4] == 'iter3':
        process.lowPtQuadStep.qualityCuts = [-100,-100,-100]
    elif sys.argv[4] == 'iter4':
        process.lowPtTripletStep.qualityCuts = [-100,-100,-100]
        process.lowPtTripletStep.mva.minPixelHits = [0,0,0]
        process.lowPtTripletStep.mva.maxChi2n = [9999.,9999.,9999.]
        process.lowPtTripletStep.mva.minLayers = [0,0,0]
        process.lowPtTripletStep.mva.min3DLayers = [0,0,0]
        process.lowPtTripletStep.mva.maxLostLayers = [9999,9999,9999]
        process.lowPtTripletStep.mva.dr_par.dr_par1 = [9999.,9999.,9999.]
        process.lowPtTripletStep.mva.dz_par.dz_par1 = [9999.,9999.,9999.]
        process.lowPtTripletStep.mva.dr_par.dr_par2 = [9999.,9999.,9999.]
        process.lowPtTripletStep.mva.dz_par.dz_par2 = [9999.,9999.,9999.]
        process.lowPtTripletStep.mva.dr_par.d0err_par = [0.001,0.001,0.001]
    elif sys.argv[4] == 'iter5':
        process.mixedTripletStepClassifier1.qualityCuts = [-100,-100,-100]
    elif sys.argv[4] == 'iter6':
        process.pixelLessStepClassifier1.qualityCuts = [-100,-100,-100]
    elif sys.argv[4] == 'iter7':
        process.tobTecStepClassifier1.qualityCuts = [-100,-100,-100]
else:
    if sys.argv[4] == 'iter0':
        process.initialStepClassifier1.qualityCuts = [-100,-100,-100]
    #process.initialStepSelector.trackSelectors[0].minHitsToBypassChecks = 0
    #process.pixelPairStepSelector.trackSelectors[0].minHitsToBypassChecks = 0
    elif sys.argv[4] == 'iter1':
        process.lowPtTripletStep.qualityCuts = [-100,-100,-100]
    #process.lowPtTripletStepSelector.trackSelectors[0].minHitsToBypassChecks = 0
    elif sys.argv[4] == 'iter2':
        process.pixelPairStep.qualityCuts = [-100,-100,-100]
    #process.pixelPairStepSelector.trackSelectors[0].minHitsToBypassChecks = 0
    elif sys.argv[4] == 'iter3':
        process.detachedTripletStepClassifier1.qualityCuts = [-100,-100,-100]
    #process.detachedTripletStepSelector.trackSelectors[0].minHitsToBypassChecks = 0
    #process.mixedTripletStepSelector.trackSelectors[0].minHitsToBypassChecks = 0
    #process.pixelLessStepSelector.trackSelectors[0].minHitsToBypassChecks = 0
    #process.tobTecStepSelector.trackSelectors[0].minHitsToBypassChecks = 0
    elif sys.argv[4] == 'iter4':
        process.mixedTripletStepClassifier1.qualityCuts = [-100,-100,-100]
    #process.mixedTripletStepSelector.trackSelectors[0].minHitsToBypassChecks = 0
    elif sys.argv[4] == 'iter5':
        process.pixelLessStepClassifier1.qualityCuts = [-100,-100,-100]
    #process.pixelLessStepSelector.trackSelectors[0].minHitsToBypassChecks = 0
    #a = True
    elif sys.argv[4] == 'iter6':
        process.tobTecStepClassifier1.qualityCuts = [-100,-100,-100]
    #process.tobTecStepSelector.trackSelectors[0].minHitsToBypassChecks = 0


# End of customisation functions

