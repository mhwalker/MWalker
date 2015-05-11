import FWCore.ParameterSet.Config as cms
import sys

isData=False
outputRAW=False
maxNrEvents=-1
outputSummary=True
newL1Menu=False
hltProcName="HLT3"

if isData:
    from elePaths import *
else:
    from hlt_exononres_mc import *
#process.hltL1sMu16Eta2p1.L1SeedsLogicalExpression = cms.string("L1_SingleMu16er")
#process.hltL1sL1SingleEG22Temp.L1SeedsLogicalExpression = cms.string("L1_SingleEG20")
process.load("setup_cff")
process.load("MWalker.TriggerFilter.simFilterSetup_cfi")
eventFilter = process.multiLeptonFilter
ofname = sys.argv[len(sys.argv)-1]
if "hrpv" in ofname or "lambda" in ofname or "coNLSP" in ofname:
    eventFilter = process.multiLeptonFilter
elif "addmonophoton" in ofname or "AxialvectorUNI" in ofname or "VectorUNI" in ofname:
    eventFilter = process.ADDmonoPhotonFilter
elif "WprimeToWZTo2Q2L" in ofname:
    eventFilter = process.WqqllFilter

process.HLTBeginSequence.replace(process.hltTriggerType,process.simuProductZpt150+process.simuProductElectrons+process.simuProductMuons+process.simuProductPhotonsPt145+process.simuProductAllFinal+process.simuProductMET130+process.simuProductDarkMatter+process.simuProductElectronsPt45+process.simuProductMuonsPt45+eventFilter+process.hltTriggerType)

process.FILTERonly = cms.Path(process.HLTBeginSequence)

#process.HLTriggerFinalPath = cms.Path( process.hltGtDigis + process.hltScalersRawToDigi + process.hltFEDSelector + process.hltTriggerSummaryAOD + process.hltTriggerSummaryRAW )


# limit the number of events to be processed
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(maxNrEvents)
)
#MAXEVENTSOVERRIDE

# enable the TrigReport and TimeReport
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool( outputSummary )
)


filePrefex="file:"
if(sys.argv[2].find("/pnfs/")==0):
    filePrefex="dcap://heplnx209.pp.rl.ac.uk:22125"

if(sys.argv[2].find("/store/")==0):
    filePrefex=""

if(sys.argv[2].find("/castor/")==0):
    filePrefex="rfio:"
process.source = cms.Source("PoolSource",
                     #     fileNames = cms.untracked.vstring(filePrefex+sys.argv[2]),
                       #     inputCommands = cms.untracked.vstring("drop *","keep *_source_*_*"),
                            fileNames = cms.untracked.vstring(),
                           eventsToProcess =cms.untracked.VEventRange()
)
#process.source.eventsToProcess.extend( [ 
#"180250:893618311-180250:893618311",])

for i in range(2,len(sys.argv)-1):
    print filePrefex+sys.argv[i]
    process.source.fileNames.extend([filePrefex+sys.argv[i],])




process.load('Configuration/EventContent/EventContent_cff')
process.output = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
 #  outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
#outputCommands = process.RECOEventContent.outputCommands,
   
                                  outputCommands =cms.untracked.vstring("drop *",
                                                                        "keep *_TriggerResults_*_*",
                                                                        "keep *_hltTriggerSummaryAOD_*_*"),
                                  
  fileName = cms.untracked.string(sys.argv[len(sys.argv)-1]),
#  SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('skimP')),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('HLTDEBUG'),
  #      filterName = cms.untracked.string('JETMETFilter'),
        
                                     
    )
)
if outputRAW:
    process.output.outputCommands=cms.untracked.vstring("drop *","keep *_rawDataCollector_*_*","keep *_addPileupInfo_*_*","keep *_TriggerResults_*_*","keep *_hltTriggerSummaryAOD_*_*")
                                                                
process.HLTOutput_sam = cms.EndPath(process.output)

#process.output.outputCommands=cms.untracked.vstring("keep *")
isCrabJob=False

#if 1, its a crab job...
if isCrabJob:
    print "using crab specified filename"
    process.output.fileName= "OUTPUTFILE"
    
  
else:
    print "using user specified filename"
    process.output.fileName= sys.argv[len(sys.argv)-1]
    
    
##import PhysicsTools.PythonAnalysis.LumiList as LumiList
##import FWCore.ParameterSet.Types as CfgTypes
##myLumis = LumiList.LumiList(filename = 'goodList.json').getCMSSWString().split(',')
##process.source.lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())
##process.source.lumisToProcess.extend(myLumis)

#hlt stuff
process.MessageLogger.cerr.FwkReport = cms.untracked.PSet(
    reportEvery = cms.untracked.int32(500),
    limit = cms.untracked.int32(10000000)
)

# override the process name
process.setName_(hltProcName)



# En-able HF Noise filters in GRun menu
if 'hltHfreco' in process.__dict__:
    process.hltHfreco.setNoiseFlags = cms.bool( True )

# override the L1 menu from an Xml file
if newL1Menu:
    process.l1GtTriggerMenuXml = cms.ESProducer("L1GtTriggerMenuXmlProducer",
                                                TriggerMenuLuminosity = cms.string('startup'),
                                                DefXmlFile = cms.string('L1Menu_Collisions2012_v0_L1T_Scales_20101224_Imp0_0x1027.xml'),
                                                VmeXmlFile = cms.string('')
                                                )
    
    process.L1GtTriggerMenuRcdSource = cms.ESSource("EmptyESSource",
                                                    recordName = cms.string('L1GtTriggerMenuRcd'),
                                                    iovIsRunNotTime = cms.bool(True),
                                                    firstValid = cms.vuint32(1)
                                                    )
    
    process.es_prefer_l1GtParameters = cms.ESPrefer('L1GtTriggerMenuXmlProducer','l1GtTriggerMenuXml') 


# adapt HLT modules to the correct process name
if 'hltTrigReport' in process.__dict__:
    process.hltTrigReport.HLTriggerResults                    = cms.InputTag( 'TriggerResults', '', hltProcName )

if 'hltPreExpressCosmicsOutputSmart' in process.__dict__:
    process.hltPreExpressCosmicsOutputSmart.TriggerResultsTag = cms.InputTag( 'TriggerResults', '', hltProcName )

if 'hltPreExpressOutputSmart' in process.__dict__:
    process.hltPreExpressOutputSmart.TriggerResultsTag        = cms.InputTag( 'TriggerResults', '', hltProcName )

if 'hltPreDQMForHIOutputSmart' in process.__dict__:
    process.hltPreDQMForHIOutputSmart.TriggerResultsTag       = cms.InputTag( 'TriggerResults', '', hltProcName )

if 'hltPreDQMForPPOutputSmart' in process.__dict__:
    process.hltPreDQMForPPOutputSmart.TriggerResultsTag       = cms.InputTag( 'TriggerResults', '', hltProcName )

if 'hltPreHLTDQMResultsOutputSmart' in process.__dict__:
    process.hltPreHLTDQMResultsOutputSmart.TriggerResultsTag  = cms.InputTag( 'TriggerResults', '', hltProcName )

if 'hltPreHLTDQMOutputSmart' in process.__dict__:
    process.hltPreHLTDQMOutputSmart.TriggerResultsTag         = cms.InputTag( 'TriggerResults', '', hltProcName )

if 'hltPreHLTMONOutputSmart' in process.__dict__:
    process.hltPreHLTMONOutputSmart.TriggerResultsTag         = cms.InputTag( 'TriggerResults', '', hltProcName )

if 'hltDQMHLTScalers' in process.__dict__:
    process.hltDQMHLTScalers.triggerResults                   = cms.InputTag( 'TriggerResults', '', hltProcName )
    process.hltDQMHLTScalers.processname                      = hltProcName

if 'hltDQML1SeedLogicScalers' in process.__dict__:
    process.hltDQML1SeedLogicScalers.processname              = hltProcName

# remove the HLT prescales
if 'PrescaleService' in process.__dict__:
    process.PrescaleService.lvl1DefaultLabel = cms.string( '0' )
    process.PrescaleService.lvl1Labels       = cms.vstring( '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' )
    process.PrescaleService.prescaleTable    = cms.VPSet( )


# override the GlobalTag, connection string and pfnPrefix
if 'GlobalTag' in process.__dict__:
    process.GlobalTag.connect   = 'frontier://FrontierProd/CMS_COND_31X_GLOBALTAG'
    process.GlobalTag.pfnPrefix = cms.untracked.string('frontier://FrontierProd/')
    from Configuration.AlCa.autoCond import autoCond
    if isData:
        process.GlobalTag.globaltag = autoCond['hltonline']
    else:
        process.GlobalTag.globaltag = autoCond['startup']


if 'MessageLogger' in process.__dict__:
    process.MessageLogger.categories.append('TriggerSummaryProducerAOD')
    process.MessageLogger.categories.append('L1GtTrigReport')
    process.MessageLogger.categories.append('HLTrigReport')
    process.MessageLogger.suppressInfo = cms.untracked.vstring('ElectronSeedProducer',"hltL1NonIsoStartUpElectronPixelSeeds","hltL1IsoStartUpElectronPixelSeeds","BasicTrajectoryState")

# version specific customizations
import os
cmsswVersion = os.environ['CMSSW_VERSION']


