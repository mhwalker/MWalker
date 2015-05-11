import FWCore.ParameterSet.Config as cms

simuProductZpt150 = cms.EDProducer("SimParticleFilter",
                                   sourceName = cms.InputTag("genParticles"),
                                   ptlow = cms.double(150),
                                   pdgIDs = cms.vdouble(23)
                                   )
simuProductMET130 = cms.EDProducer("SimMETFilter",
                                    sourceName = cms.InputTag("genMetTrue"),
                                    ptlow = cms.double(130)
                                    )
simuProductJet250 = cms.EDProducer("SimJetFilter",
                                   sourceName = cms.InputTag("ak5GenJets"),
                                   ptlow = cms.double(250)
                                   )
simuProductElectrons = cms.EDProducer("SimParticleFilter",
                                      sourceName = cms.InputTag("genParticles"),
                                      pdgIDs = cms.vdouble(-11,11),
                                      statuses = cms.vdouble(1)
                                      )
simuProductElectronsPt45 = cms.EDProducer("SimParticleFilter",
                                          sourceName = cms.InputTag("genParticles"),
                                          ptlow = cms.double(45),
                                          pdgIDs = cms.vdouble(-11,11),
                                          statuses = cms.vdouble(1)
                                          )

simuProductMuons = cms.EDProducer("SimParticleFilter",
                                  sourceName = cms.InputTag("genParticles"),
                                  pdgIDs = cms.vdouble(-13,13),
                                  statuses = cms.vdouble(1)
                                  )
simuProductMuonsPt45 = cms.EDProducer("SimParticleFilter",
                                      sourceName = cms.InputTag("genParticles"),
                                      ptlow = cms.double(45),
                                      pdgIDs = cms.vdouble(-13,13),
                                      statuses = cms.vdouble(1)
                                      )

simuProductPhotonsPt145 = cms.EDProducer("SimParticleFilter",
                                         sourceName = cms.InputTag("genParticles"),
                                         pdgIDs = cms.vdouble(22),
                                         statuses = cms.vdouble(1),
                                         ptlow = cms.double(145),
                                         etalow = cms.double(-1.5),
                                         etahigh = cms.double(1.5)
                                         )
simuProductDarkMatter = cms.EDProducer("SimParticleFilter",
                                       sourceName = cms.InputTag("genParticles"),
                                       #statuses = cms.vdouble(1),
                                       pdgIDs = cms.vdouble(39,-39,18,-18)
                                       )
simuProductAllFinal = cms.EDProducer("SimParticleFilter",
                                     sourceName = cms.InputTag("genParticles"),
                                     statuses = cms.vdouble(1)
                                     )

WqqllFilter = cms.EDFilter("EventFilter",
                           products = cms.VInputTag("simuProductZpt150","simuProductElectronsPt45","simuProductMuonsPt45","simuProductJet250","simuProductAllFinal"),
                           cuts = cms.VPSet(
    cms.PSet(cutType = cms.string("N"),
             nlow = cms.int32(1),
             products = cms.vstring("simuProductZpt150")
             ),
    cms.PSet(cutType = cms.string("Z"),
             zlow = cms.double(70),
             zhigh = cms.double(110),
             products = cms.vstring("simuProductElectronsPt45","simuProductMuonsPt45")
             ),
    cms.PSet(cutType = cms.string("N"),
             nlow = cms.int32(1),
             products = cms.vstring("simuProductJet250")
             )
    )
                           )

#WqqllFilter.addCut()
#WqqllFilter.addCut()

ADDmonoPhotonFilter = cms.EDFilter("EventFilter",
                                   products = cms.VInputTag("simuProductPhotonsPt145","simuProductDarkMatter","simuProductAllFinal","simuProductMET130"),
                                   cuts = cms.VPSet(cms.PSet(cutType = cms.string("N"),
                                    nlow = cms.int32(1),
                                    products = cms.vstring("simuProductPhotonsPt145")
                                    ),cms.PSet(cutType=cms.string("N"),
                                               nlow = cms.int32(1),
                                               products = cms.vstring("simuProductMET130")
                                               )
                                                    #,cms.PSet(cutType = cms.string("SUMPT"),
                                    #sumlow = cms.double(130),
                                    #usevector = cms.bool(True),
                                    #products = cms.vstring("simuProductDarkMatter")
                                    )#)
                                   )

#ADDmonoPhotonFilter.addCut()
#ADDmonoPhotonFilter.addCut()

multiLeptonFilter = cms.EDFilter("EventFilter",
                                 products = cms.VInputTag("simuProductElectrons","simuProductMuons","simuProductAllFinal"),
                                 cuts = cms.VPSet(cms.PSet(cutType = cms.string("N"),
                                  nlow = cms.int32(3),
                                  products = cms.vstring("simuProductElectrons","simuProductMuons")
                                  ),cms.PSet(cutType = cms.string("SUMPT"),
                                  sumlow = cms.double(600),
                                  products = cms.vstring("simuProductAllFinal")
                                  ))
                                 )
#multiLeptonFilter.addCut()
#multiLeptonFilter.addCut()
