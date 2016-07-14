import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

#process.source = cms.Source("PoolSource",
    ## replace 'myfile.root' with the source file you want to use
    #fileNames = cms.untracked.vstring(
        #'file:myfile.root'
    #)
#)

process.source = cms.Source("EmptySource",
)
        

process.gbrwrappermaker = cms.EDAnalyzer('MVADBWriter',
                                         #files=cms.vstring("SelectorWeightBDTGIter0.root","SelectorWeightBDTGIter1.root","SelectorWeightBDTGIter3.root"),
                                         files=cms.vstring("SelectorWeightBDTGIter0.root","SelectorWeightBDTGIter1.root","SelectorWeightBDTGIter2.root","SelectorWeightBDTGIter3.root","SelectorWeightBDTGIter4.root","SelectorWeightBDTGIter5.root","SelectorWeightBDTGIter6.root","SelectorWeightBDTGIter7.root"),
                                         #labels=cms.vstring("PromptTrackSelector","LowPtPromptTrackSelector","DetachedTrackSelector"),
                                         #labels=cms.vstring("MVASelectorIter0v4","MVASelectorIter1v4","MVASelectorIter2v4","MVASelectorIter3v4","MVASelectorIter4v4","MVASelectorIter5v4","MVASelectorIter6v4"),
                                         labels=cms.vstring("MVASelectorIter0_13TeV_v1","MVASelectorIter1_13TeV_v1","MVASelectorIter2_13TeV_v1","MVASelectorIter3_13TeV_v1","MVASelectorIter4_13TeV_v1","MVASelectorIter5_13TeV_v1","MVASelectorIter6_13TeV_v1","MVASelectorIter7_13TeV_v1"),
)

process.load("CondCore.DBCommon.CondDBCommon_cfi")
# output database (in this case local sqlite file)
#process.CondDBCommon.connect = 'sqlite_file:GBRWrapper_13TeV_newScheme_750pre3_v1.db'
process.CondDBCommon.connect = 'sqlite_file:GBRWrapper_13TeV_800pre5_phase1.db'

process.PoolDBOutputService = cms.Service("PoolDBOutputService",
    process.CondDBCommon,
    timetype = cms.untracked.string('runnumber'),
    toPut = cms.VPSet(
      cms.PSet(
        record = cms.string('MVASelectorIter0_13TeV_v1'),
        tag = cms.string('MVASelectorIter0_13TeV_v1')
      ),
      cms.PSet(
        record = cms.string('MVASelectorIter1_13TeV_v1'),
        tag = cms.string('MVASelectorIter1_13TeV_v1')
      ),
      cms.PSet(
        record = cms.string('MVASelectorIter2_13TeV_v1'),
        tag = cms.string('MVASelectorIter2_13TeV_v1')
      ),
      cms.PSet(
        record = cms.string('MVASelectorIter3_13TeV_v1'),
        tag = cms.string('MVASelectorIter3_13TeV_v1')
      ),
      cms.PSet(
        record = cms.string('MVASelectorIter4_13TeV_v1'),
        tag = cms.string('MVASelectorIter4_13TeV_v1')
      ),
      cms.PSet(
        record = cms.string('MVASelectorIter5_13TeV_v1'),
        tag = cms.string('MVASelectorIter5_13TeV_v1')
      ),
      cms.PSet(
        record = cms.string('MVASelectorIter6_13TeV_v1'),
        tag = cms.string('MVASelectorIter6_13TeV_v1')
      ),
      cms.PSet(
        record = cms.string('MVASelectorIter7_13TeV_v1'),
        tag = cms.string('MVASelectorIter7_13TeV_v1')
      ),
      
  )
)

process.upload = cms.Path(process.gbrwrappermaker)
