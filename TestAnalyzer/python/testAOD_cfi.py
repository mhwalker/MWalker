import FWCore.ParameterSet.Config as cms

baseAOD = cms.EDAnalyzer(
  "TestAODReader",
  patMuonsInputTag = cms.InputTag("selectedPatMuons"),
  patElectronsInputTag = cms.InputTag("selectedPatElectrons"),
  patTausInputTag = cms.InputTag("selectedPatTaus"),
  patPhotonsInputTag = cms.InputTag("selectedPatPhotons"),
  patJetsInputTag = cms.InputTag('selectedPatJets'),
  patMETInputTag = cms.InputTag('patMETs'),
  trackInputTag = cms.InputTag('generalTracks'),
  vtxInputTag = cms.InputTag("offlinePrimaryVertices"),
  beamSpotInputTag = cms.InputTag('offlineBeamSpot'),
  triggerInputTag = cms.InputTag("TriggerResults","","HLT"),
  triggerEventInputTag = cms.InputTag("hltTriggerSummaryAOD","","HLT"),
  genParticleInputTag = cms.InputTag('genParticles'),
  processName = cms.string('HLT'),
  outFilename=cms.untracked.string("output.root"),
  treeName=cms.untracked.string("tree"),
  writeAllEvents=cms.bool(True),
  cutList=cms.VPSet(),
)
