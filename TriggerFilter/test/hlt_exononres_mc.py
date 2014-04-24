# /users/sharper/2012/exo/EXORNRTrigs5E33/V3 (CMSSW_5_2_1_HLT2)

import FWCore.ParameterSet.Config as cms

process = cms.Process( "HLT" )

process.HLTConfigVersion = cms.PSet(
  tableName = cms.string('/users/sharper/2012/exo/EXORNRTrigs5E33/V3')
)

process.hltTriggerType = cms.EDFilter( "HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32( 1 )
)
process.hltGtDigis = cms.EDProducer( "L1GlobalTriggerRawToDigi",
    DaqGtFedId = cms.untracked.int32( 813 ),
    DaqGtInputTag = cms.InputTag( "rawDataCollector" ),
    UnpackBxInEvent = cms.int32( 5 ),
    ActiveBoardsMask = cms.uint32( 0xffff )
)
process.hltGctDigis = cms.EDProducer( "GctRawToDigi",
    unpackSharedRegions = cms.bool( False ),
    numberOfGctSamplesToUnpack = cms.uint32( 1 ),
    verbose = cms.untracked.bool( False ),
    numberOfRctSamplesToUnpack = cms.uint32( 1 ),
    inputLabel = cms.InputTag( "rawDataCollector" ),
    unpackerVersion = cms.uint32( 0 ),
    gctFedId = cms.untracked.int32( 745 ),
    hltMode = cms.bool( True )
)
process.hltL1GtObjectMap = cms.EDProducer( "L1GlobalTrigger",
    TechnicalTriggersUnprescaled = cms.bool( True ),
    ProduceL1GtObjectMapRecord = cms.bool( True ),
    AlgorithmTriggersUnmasked = cms.bool( False ),
    EmulateBxInEvent = cms.int32( 1 ),
    AlgorithmTriggersUnprescaled = cms.bool( True ),
    ProduceL1GtDaqRecord = cms.bool( False ),
    ReadTechnicalTriggerRecords = cms.bool( True ),
    RecordLength = cms.vint32( 3, 0 ),
    TechnicalTriggersUnmasked = cms.bool( False ),
    ProduceL1GtEvmRecord = cms.bool( False ),
    GmtInputTag = cms.InputTag( "hltGtDigis" ),
    TechnicalTriggersVetoUnmasked = cms.bool( True ),
    AlternativeNrBxBoardEvm = cms.uint32( 0 ),
    TechnicalTriggersInputTags = cms.VInputTag( 'simBscDigis' ),
    CastorInputTag = cms.InputTag( "castorL1Digis" ),
    GctInputTag = cms.InputTag( "hltGctDigis" ),
    AlternativeNrBxBoardDaq = cms.uint32( 0 ),
    WritePsbL1GtDaqRecord = cms.bool( False ),
    BstLengthBytes = cms.int32( -1 )
)
process.hltL1extraParticles = cms.EDProducer( "L1ExtraParticlesProd",
    tauJetSource = cms.InputTag( 'hltGctDigis','tauJets' ),
    etHadSource = cms.InputTag( "hltGctDigis" ),
    etTotalSource = cms.InputTag( "hltGctDigis" ),
    centralBxOnly = cms.bool( True ),
    centralJetSource = cms.InputTag( 'hltGctDigis','cenJets' ),
    etMissSource = cms.InputTag( "hltGctDigis" ),
    hfRingEtSumsSource = cms.InputTag( "hltGctDigis" ),
    produceMuonParticles = cms.bool( True ),
    forwardJetSource = cms.InputTag( 'hltGctDigis','forJets' ),
    ignoreHtMiss = cms.bool( False ),
    htMissSource = cms.InputTag( "hltGctDigis" ),
    produceCaloParticles = cms.bool( True ),
    muonSource = cms.InputTag( "hltGtDigis" ),
    isolatedEmSource = cms.InputTag( 'hltGctDigis','isoEm' ),
    nonIsolatedEmSource = cms.InputTag( 'hltGctDigis','nonIsoEm' ),
    hfRingBitCountsSource = cms.InputTag( "hltGctDigis" )
)
process.hltScalersRawToDigi = cms.EDProducer( "ScalersRawToDigi",
    scalersInputTag = cms.InputTag( "rawDataCollector" )
)
process.hltOnlineBeamSpot = cms.EDProducer( "BeamSpotOnlineProducer",
    maxZ = cms.double( 40.0 ),
    src = cms.InputTag( "hltScalersRawToDigi" ),
    gtEvmLabel = cms.InputTag( "" ),
    changeToCMSCoordinates = cms.bool( False ),
    setSigmaZ = cms.double( 0.0 ),
    maxRadius = cms.double( 2.0 )
)
process.hltOfflineBeamSpot = cms.EDProducer( "BeamSpotProducer" )
process.hltL1sL1SingleEG30 = cms.EDFilter( "HLTLevel1GTSeed",
    saveTags = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG30" ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreDoublePhoton70 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltESRawToRecHitFacility = cms.EDProducer( "EcalRawToRecHitFacility",
    sourceTag = cms.InputTag( "rawDataCollector" ),
    workerName = cms.string( "hltESPESUnpackerWorker" )
)
process.hltEcalRawToRecHitFacility = cms.EDProducer( "EcalRawToRecHitFacility",
    sourceTag = cms.InputTag( "rawDataCollector" ),
    workerName = cms.string( "" )
)
process.hltEcalRegionalEgammaFEDs = cms.EDProducer( "EcalRawToRecHitRoI",
    JetJobPSet = cms.VPSet( 
    ),
    sourceTag_es = cms.InputTag( "hltESRawToRecHitFacility" ),
    doES = cms.bool( True ),
    type = cms.string( "egamma" ),
    sourceTag = cms.InputTag( "hltEcalRawToRecHitFacility" ),
    EmJobPSet = cms.VPSet( 
      cms.PSet(  regionEtaMargin = cms.double( 0.25 ),
        regionPhiMargin = cms.double( 0.4 ),
        Ptmin = cms.double( 5.0 ),
        Source = cms.InputTag( 'hltL1extraParticles','Isolated' )
      ),
      cms.PSet(  regionEtaMargin = cms.double( 0.25 ),
        regionPhiMargin = cms.double( 0.4 ),
        Ptmin = cms.double( 5.0 ),
        Source = cms.InputTag( 'hltL1extraParticles','NonIsolated' )
      )
    ),
    CandJobPSet = cms.VPSet( 
    ),
    MuonJobPSet = cms.PSet(  ),
    esInstance = cms.untracked.string( "es" ),
    MuJobPSet = cms.PSet(  )
)
process.hltEcalRegionalEgammaRecHit = cms.EDProducer( "EcalRawToRecHitProducer",
    splitOutput = cms.bool( True ),
    rechitCollection = cms.string( "NotNeededsplitOutputTrue" ),
    EErechitCollection = cms.string( "EcalRecHitsEE" ),
    EBrechitCollection = cms.string( "EcalRecHitsEB" ),
    sourceTag = cms.InputTag( "hltEcalRegionalEgammaFEDs" ),
    lazyGetterTag = cms.InputTag( "hltEcalRawToRecHitFacility" )
)
process.hltESRegionalEgammaRecHit = cms.EDProducer( "EcalRawToRecHitProducer",
    splitOutput = cms.bool( False ),
    rechitCollection = cms.string( "EcalRecHitsES" ),
    EErechitCollection = cms.string( "" ),
    EBrechitCollection = cms.string( "" ),
    sourceTag = cms.InputTag( 'hltEcalRegionalEgammaFEDs','es' ),
    lazyGetterTag = cms.InputTag( "hltESRawToRecHitFacility" )
)
process.hltHybridSuperClustersL1Seeded = cms.EDProducer( "EgammaHLTHybridClusterProducer",
    xi = cms.double( 0.0 ),
    regionEtaMargin = cms.double( 0.14 ),
    regionPhiMargin = cms.double( 0.4 ),
    severityRecHitThreshold = cms.double( 4.0 ),
    RecHitFlagToBeExcluded = cms.vstring(  ),
    ecalhitcollection = cms.string( "EcalRecHitsEB" ),
    eThreshA = cms.double( 0.0030 ),
    basicclusterCollection = cms.string( "" ),
    eThreshB = cms.double( 0.1 ),
    dynamicPhiRoad = cms.bool( False ),
    RecHitSeverityToBeExcluded = cms.vstring( 'kWeird' ),
    l1UpperThr = cms.double( 999.0 ),
    excludeFlagged = cms.bool( True ),
    posCalcParameters = cms.PSet( 
      T0_barl = cms.double( 7.4 ),
      LogWeighted = cms.bool( True ),
      T0_endc = cms.double( 3.1 ),
      T0_endcPresh = cms.double( 1.2 ),
      W0 = cms.double( 4.2 ),
      X0 = cms.double( 0.89 )
    ),
    l1LowerThr = cms.double( 5.0 ),
    doIsolated = cms.bool( True ),
    eseed = cms.double( 0.35 ),
    ethresh = cms.double( 0.1 ),
    ewing = cms.double( 0.0 ),
    useEtForXi = cms.bool( True ),
    step = cms.int32( 17 ),
    debugLevel = cms.string( "INFO" ),
    dynamicEThresh = cms.bool( False ),
    l1TagIsolated = cms.InputTag( 'hltL1extraParticles','Isolated' ),
    superclusterCollection = cms.string( "" ),
    HybridBarrelSeedThr = cms.double( 1.5 ),
    l1TagNonIsolated = cms.InputTag( 'hltL1extraParticles','NonIsolated' ),
    l1LowerThrIgnoreIsolation = cms.double( 0.0 ),
    ecalhitproducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" )
)
process.hltCorrectedHybridSuperClustersL1Seeded = cms.EDProducer( "EgammaSCCorrectionMaker",
    corectedSuperClusterCollection = cms.string( "" ),
    sigmaElectronicNoise = cms.double( 0.03 ),
    superClusterAlgo = cms.string( "Hybrid" ),
    etThresh = cms.double( 1.0 ),
    rawSuperClusterProducer = cms.InputTag( "hltHybridSuperClustersL1Seeded" ),
    applyEnergyCorrection = cms.bool( True ),
    isl_fCorrPset = cms.PSet(  ),
    VerbosityLevel = cms.string( "ERROR" ),
    recHitProducer = cms.InputTag( 'hltEcalRegionalEgammaRecHit','EcalRecHitsEB' ),
    fix_fCorrPset = cms.PSet(  ),
    modeEE = cms.int32( 0 ),
    modeEB = cms.int32( 0 ),
    dyn_fCorrPset = cms.PSet(  ),
    energyCorrectorName = cms.string( "EcalClusterEnergyCorrectionObjectSpecific" ),
    applyCrackCorrection = cms.bool( False ),
    hyb_fCorrPset = cms.PSet( 
      brLinearLowThr = cms.double( 1.1 ),
      fBremVec = cms.vdouble( -0.05208, 0.1331, 0.9196, -5.735E-4, 1.343 ),
      brLinearHighThr = cms.double( 8.0 ),
      fEtEtaVec = cms.vdouble( 1.0012, -0.5714, 0.0, 0.0, 0.0, 0.5549, 12.74, 1.0448, 0.0, 0.0, 0.0, 0.0, 8.0, 1.023, -0.00181, 0.0, 0.0 )
    )
)
process.hltMulti5x5BasicClustersL1Seeded = cms.EDProducer( "EgammaHLTMulti5x5ClusterProducer",
    l1LowerThr = cms.double( 5.0 ),
    Multi5x5BarrelSeedThr = cms.double( 0.5 ),
    Multi5x5EndcapSeedThr = cms.double( 0.18 ),
    endcapHitCollection = cms.string( "EcalRecHitsEE" ),
    barrelClusterCollection = cms.string( "notused" ),
    doEndcaps = cms.bool( True ),
    regionEtaMargin = cms.double( 0.3 ),
    regionPhiMargin = cms.double( 0.4 ),
    RecHitFlagToBeExcluded = cms.vstring(  ),
    l1TagNonIsolated = cms.InputTag( 'hltL1extraParticles','NonIsolated' ),
    endcapHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" ),
    posCalcParameters = cms.PSet( 
      T0_barl = cms.double( 7.4 ),
      LogWeighted = cms.bool( True ),
      T0_endc = cms.double( 3.1 ),
      T0_endcPresh = cms.double( 1.2 ),
      W0 = cms.double( 4.2 ),
      X0 = cms.double( 0.89 )
    ),
    VerbosityLevel = cms.string( "ERROR" ),
    doIsolated = cms.bool( True ),
    barrelHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" ),
    l1LowerThrIgnoreIsolation = cms.double( 0.0 ),
    l1TagIsolated = cms.InputTag( 'hltL1extraParticles','Isolated' ),
    barrelHitCollection = cms.string( "EcalRecHitsEB" ),
    doBarrel = cms.bool( False ),
    endcapClusterCollection = cms.string( "multi5x5EndcapBasicClusters" ),
    l1UpperThr = cms.double( 999.0 )
)
process.hltMulti5x5SuperClustersL1Seeded = cms.EDProducer( "Multi5x5SuperClusterProducer",
    barrelSuperclusterCollection = cms.string( "multi5x5BarrelSuperClusters" ),
    endcapEtaSearchRoad = cms.double( 0.14 ),
    barrelClusterCollection = cms.string( "multi5x5BarrelBasicClusters" ),
    dynamicPhiRoad = cms.bool( False ),
    endcapClusterProducer = cms.string( "hltMulti5x5BasicClustersL1Seeded" ),
    barrelPhiSearchRoad = cms.double( 0.8 ),
    endcapPhiSearchRoad = cms.double( 0.6 ),
    barrelClusterProducer = cms.string( "notused" ),
    seedTransverseEnergyThreshold = cms.double( 1.0 ),
    endcapSuperclusterCollection = cms.string( "multi5x5EndcapSuperClusters" ),
    barrelEtaSearchRoad = cms.double( 0.06 ),
    bremRecoveryPset = cms.PSet( 
      barrel = cms.PSet(  ),
      endcap = cms.PSet( 
        a = cms.double( 47.85 ),
        c = cms.double( 0.1201 ),
        b = cms.double( 108.8 )
      ),
      doEndcaps = cms.bool( True ),
      doBarrel = cms.bool( False )
    ),
    doEndcaps = cms.bool( True ),
    endcapClusterCollection = cms.string( "multi5x5EndcapBasicClusters" ),
    doBarrel = cms.bool( False )
)
process.hltMulti5x5EndcapSuperClustersWithPreshowerL1Seeded = cms.EDProducer( "PreshowerClusterProducer",
    assocSClusterCollection = cms.string( "" ),
    preshStripEnergyCut = cms.double( 0.0 ),
    preshClusterCollectionY = cms.string( "preshowerYClusters" ),
    preshClusterCollectionX = cms.string( "preshowerXClusters" ),
    etThresh = cms.double( 5.0 ),
    preshRecHitProducer = cms.InputTag( 'hltESRegionalEgammaRecHit','EcalRecHitsES' ),
    endcapSClusterProducer = cms.InputTag( 'hltMulti5x5SuperClustersL1Seeded','multi5x5EndcapSuperClusters' ),
    preshNclust = cms.int32( 4 ),
    preshClusterEnergyCut = cms.double( 0.0 ),
    preshSeededNstrip = cms.int32( 15 )
)
process.hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Seeded = cms.EDProducer( "EgammaSCCorrectionMaker",
    corectedSuperClusterCollection = cms.string( "" ),
    sigmaElectronicNoise = cms.double( 0.15 ),
    superClusterAlgo = cms.string( "Multi5x5" ),
    etThresh = cms.double( 1.0 ),
    rawSuperClusterProducer = cms.InputTag( "hltMulti5x5EndcapSuperClustersWithPreshowerL1Seeded" ),
    applyEnergyCorrection = cms.bool( True ),
    isl_fCorrPset = cms.PSet(  ),
    VerbosityLevel = cms.string( "ERROR" ),
    recHitProducer = cms.InputTag( 'hltEcalRegionalEgammaRecHit','EcalRecHitsEE' ),
    fix_fCorrPset = cms.PSet( 
      brLinearLowThr = cms.double( 0.6 ),
      fBremVec = cms.vdouble( -0.04163, 0.08552, 0.95048, -0.002308, 1.077 ),
      brLinearHighThr = cms.double( 6.0 ),
      fEtEtaVec = cms.vdouble( 0.9746, -6.512, 0.0, 0.0, 0.02771, 4.983, 0.0, 0.0, -0.007288, -0.9446, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0 )
    ),
    modeEE = cms.int32( 0 ),
    modeEB = cms.int32( 0 ),
    dyn_fCorrPset = cms.PSet(  ),
    energyCorrectorName = cms.string( "EcalClusterEnergyCorrectionObjectSpecific" ),
    applyCrackCorrection = cms.bool( False ),
    hyb_fCorrPset = cms.PSet(  )
)
process.hltL1SeededRecoEcalCandidate = cms.EDProducer( "EgammaHLTRecoEcalCandidateProducers",
    scIslandEndcapProducer = cms.InputTag( "hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Seeded" ),
    scHybridBarrelProducer = cms.InputTag( "hltCorrectedHybridSuperClustersL1Seeded" ),
    recoEcalCandidateCollection = cms.string( "" )
)
process.hltEGRegionalL1SingleEG30 = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    saveTags = cms.bool( False ),
    endcap_end = cms.double( 2.65 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    barrel_end = cms.double( 1.4791 ),
    l1IsolatedTag = cms.InputTag( 'hltL1extraParticles','Isolated' ),
    candIsolatedTag = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    region_phi_size = cms.double( 1.044 ),
    region_eta_size = cms.double( 0.522 ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG30" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    candNonIsolatedTag = cms.InputTag( "" ),
    l1NonIsolatedTag = cms.InputTag( 'hltL1extraParticles','NonIsolated' )
)
process.hltEG70EtFilterL1EG30 = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( False ),
    L1NonIsoCand = cms.InputTag( "" ),
    relaxed = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    inputTag = cms.InputTag( "hltEGRegionalL1SingleEG30" ),
    etcutEB = cms.double( 70.0 ),
    ncandcut = cms.int32( 1 ),
    etcutEE = cms.double( 70.0 )
)
process.hltHcalDigis = cms.EDProducer( "HcalRawToDigi",
    UnpackZDC = cms.untracked.bool( True ),
    FilterDataQuality = cms.bool( True ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    ComplainEmptyData = cms.untracked.bool( False ),
    UnpackCalib = cms.untracked.bool( True ),
    UnpackTTP = cms.untracked.bool( False ),
    lastSample = cms.int32( 9 ),
    firstSample = cms.int32( 0 )
)
process.hltHbhereco = cms.EDProducer( "HcalHitReconstructor",
    digiTimeFromDB = cms.bool( True ),
    S9S1stat = cms.PSet(  ),
    saturationParameters = cms.PSet(  maxADCvalue = cms.int32( 127 ) ),
    tsFromDB = cms.bool( True ),
    samplesToAdd = cms.int32( 4 ),
    correctionPhaseNS = cms.double( 13.0 ),
    HFInWindowStat = cms.PSet(  ),
    digiLabel = cms.InputTag( "hltHcalDigis" ),
    setHSCPFlags = cms.bool( False ),
    firstAuxTS = cms.int32( 4 ),
    setSaturationFlags = cms.bool( False ),
    hfTimingTrustParameters = cms.PSet(  ),
    PETstat = cms.PSet(  ),
    digistat = cms.PSet(  ),
    useLeakCorrection = cms.bool( False ),
    setTimingTrustFlags = cms.bool( False ),
    S8S1stat = cms.PSet(  ),
    correctForPhaseContainment = cms.bool( True ),
    correctForTimeslew = cms.bool( True ),
    setNoiseFlags = cms.bool( False ),
    correctTiming = cms.bool( False ),
    setPulseShapeFlags = cms.bool( False ),
    Subdetector = cms.string( "HBHE" ),
    dropZSmarkedPassed = cms.bool( True ),
    recoParamsFromDB = cms.bool( True ),
    firstSample = cms.int32( 4 ),
    setTimingShapedCutsFlags = cms.bool( False ),
    timingshapedcutsParameters = cms.PSet( 
      ignorelowest = cms.bool( True ),
      win_offset = cms.double( 0.0 ),
      ignorehighest = cms.bool( False ),
      win_gain = cms.double( 1.0 ),
      tfilterEnvelope = cms.vdouble( 4.0, 12.04, 13.0, 10.56, 23.5, 8.82, 37.0, 7.38, 56.0, 6.3, 81.0, 5.64, 114.5, 5.44, 175.5, 5.38, 350.5, 5.14 )
    ),
    pulseShapeParameters = cms.PSet(  ),
    flagParameters = cms.PSet( 
      nominalPedestal = cms.double( 3.0 ),
      hitMultiplicityThreshold = cms.int32( 17 ),
      hitEnergyMinimum = cms.double( 1.0 ),
      pulseShapeParameterSets = cms.VPSet( 
        cms.PSet(  pulseShapeParameters = cms.vdouble( 0.0, 100.0, -50.0, 0.0, -15.0, 0.15 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( 100.0, 2000.0, -50.0, 0.0, -5.0, 0.05 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( 2000.0, 1000000.0, -50.0, 0.0, 95.0, 0.0 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( -1000000.0, 1000000.0, 45.0, 0.1, 1000000.0, 0.0 )        )
      )
    ),
    hscpParameters = cms.PSet( 
      slopeMax = cms.double( -0.6 ),
      r1Max = cms.double( 1.0 ),
      r1Min = cms.double( 0.15 ),
      TimingEnergyThreshold = cms.double( 30.0 ),
      slopeMin = cms.double( -1.5 ),
      outerMin = cms.double( 0.0 ),
      outerMax = cms.double( 0.1 ),
      fracLeaderMin = cms.double( 0.4 ),
      r2Min = cms.double( 0.1 ),
      r2Max = cms.double( 0.5 ),
      fracLeaderMax = cms.double( 0.7 )
    )
)
process.hltHfreco = cms.EDProducer( "HcalHitReconstructor",
    digiTimeFromDB = cms.bool( True ),
    S9S1stat = cms.PSet( 
      longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      shortEnergyParams = cms.vdouble( 35.1773, 35.37, 35.7933, 36.4472, 37.3317, 38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 47.4813, 49.98, 52.7093 ),
      flagsToSkip = cms.int32( 24 ),
      shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      short_optimumSlope = cms.vdouble( -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296, 0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 0.135313, 0.136289, 0.0589927 ),
      longEnergyParams = cms.vdouble( 43.5, 45.7, 48.32, 51.36, 54.82, 58.7, 63.0, 67.72, 72.86, 78.42, 84.4, 90.8, 97.62 ),
      long_optimumSlope = cms.vdouble( -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296, 0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 0.135313, 0.136289, 0.0589927 ),
      isS8S1 = cms.bool( False ),
      HcalAcceptSeverityLevel = cms.int32( 9 )
    ),
    saturationParameters = cms.PSet(  maxADCvalue = cms.int32( 127 ) ),
    tsFromDB = cms.bool( True ),
    samplesToAdd = cms.int32( 2 ),
    correctionPhaseNS = cms.double( 13.0 ),
    HFInWindowStat = cms.PSet( 
      hflongEthresh = cms.double( 40.0 ),
      hflongMinWindowTime = cms.vdouble( -10.0 ),
      hfshortEthresh = cms.double( 40.0 ),
      hflongMaxWindowTime = cms.vdouble( 10.0 ),
      hfshortMaxWindowTime = cms.vdouble( 10.0 ),
      hfshortMinWindowTime = cms.vdouble( -12.0 )
    ),
    digiLabel = cms.InputTag( "hltHcalDigis" ),
    setHSCPFlags = cms.bool( False ),
    firstAuxTS = cms.int32( 1 ),
    setSaturationFlags = cms.bool( False ),
    hfTimingTrustParameters = cms.PSet( 
      hfTimingTrustLevel2 = cms.int32( 4 ),
      hfTimingTrustLevel1 = cms.int32( 1 )
    ),
    PETstat = cms.PSet( 
      longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      short_R_29 = cms.vdouble( 0.8 ),
      shortEnergyParams = cms.vdouble( 35.1773, 35.37, 35.7933, 36.4472, 37.3317, 38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 47.4813, 49.98, 52.7093 ),
      flagsToSkip = cms.int32( 0 ),
      short_R = cms.vdouble( 0.8 ),
      shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      long_R_29 = cms.vdouble( 0.8 ),
      longEnergyParams = cms.vdouble( 43.5, 45.7, 48.32, 51.36, 54.82, 58.7, 63.0, 67.72, 72.86, 78.42, 84.4, 90.8, 97.62 ),
      long_R = cms.vdouble( 0.98 ),
      HcalAcceptSeverityLevel = cms.int32( 9 )
    ),
    digistat = cms.PSet( 
      HFdigiflagFirstSample = cms.int32( 1 ),
      HFdigiflagMinEthreshold = cms.double( 40.0 ),
      HFdigiflagSamplesToAdd = cms.int32( 3 ),
      HFdigiflagExpectedPeak = cms.int32( 2 ),
      HFdigiflagCoef = cms.vdouble( 0.93, -0.012667, -0.38275 )
    ),
    useLeakCorrection = cms.bool( False ),
    setTimingTrustFlags = cms.bool( False ),
    S8S1stat = cms.PSet( 
      longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      shortEnergyParams = cms.vdouble( 40.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0 ),
      flagsToSkip = cms.int32( 16 ),
      shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      short_optimumSlope = cms.vdouble( 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 ),
      longEnergyParams = cms.vdouble( 40.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0 ),
      long_optimumSlope = cms.vdouble( 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 ),
      isS8S1 = cms.bool( True ),
      HcalAcceptSeverityLevel = cms.int32( 9 )
    ),
    correctForPhaseContainment = cms.bool( False ),
    correctForTimeslew = cms.bool( False ),
    setNoiseFlags = cms.bool( True ),
    correctTiming = cms.bool( False ),
    setPulseShapeFlags = cms.bool( False ),
    Subdetector = cms.string( "HF" ),
    dropZSmarkedPassed = cms.bool( True ),
    recoParamsFromDB = cms.bool( True ),
    firstSample = cms.int32( 2 ),
    setTimingShapedCutsFlags = cms.bool( False ),
    timingshapedcutsParameters = cms.PSet(  ),
    pulseShapeParameters = cms.PSet(  ),
    flagParameters = cms.PSet(  ),
    hscpParameters = cms.PSet(  )
)
process.hltL1SeededPhotonHcalForHE = cms.EDProducer( "EgammaHLTHcalIsolationProducersRegional",
    eMinHE = cms.double( 0.8 ),
    hbheRecHitProducer = cms.InputTag( "hltHbhereco" ),
    effectiveAreaBarrel = cms.double( 0.105 ),
    outerCone = cms.double( 0.14 ),
    eMinHB = cms.double( 0.7 ),
    innerCone = cms.double( 0.0 ),
    etMinHE = cms.double( -1.0 ),
    etMinHB = cms.double( -1.0 ),
    rhoProducer = cms.InputTag( 'hltKT6CaloJets','rho' ),
    depth = cms.int32( -1 ),
    doRhoCorrection = cms.bool( False ),
    effectiveAreaEndcap = cms.double( 0.17 ),
    recoEcalCandidateProducer = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    rhoMax = cms.double( 9.9999999E7 ),
    rhoScale = cms.double( 1.0 ),
    doEtSum = cms.bool( False )
)
process.hltEG70HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.1 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( 0.15 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededPhotonHcalForHE" ),
    candTag = cms.InputTag( "hltEG70EtFilterL1EG30" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltEcalRegionalRestFEDs = cms.EDProducer( "EcalRawToRecHitRoI",
    JetJobPSet = cms.VPSet( 
    ),
    sourceTag_es = cms.InputTag( "NotNeededoESfalse" ),
    doES = cms.bool( False ),
    type = cms.string( "all" ),
    sourceTag = cms.InputTag( "hltEcalRawToRecHitFacility" ),
    EmJobPSet = cms.VPSet( 
    ),
    CandJobPSet = cms.VPSet( 
    ),
    MuonJobPSet = cms.PSet(  ),
    esInstance = cms.untracked.string( "es" ),
    MuJobPSet = cms.PSet(  )
)
process.hltEcalRegionalESRestFEDs = cms.EDProducer( "EcalRawToRecHitRoI",
    JetJobPSet = cms.VPSet( 
    ),
    sourceTag_es = cms.InputTag( "hltESRawToRecHitFacility" ),
    doES = cms.bool( True ),
    type = cms.string( "all" ),
    sourceTag = cms.InputTag( "hltEcalRawToRecHitFacility" ),
    EmJobPSet = cms.VPSet( 
    ),
    CandJobPSet = cms.VPSet( 
    ),
    MuonJobPSet = cms.PSet(  ),
    esInstance = cms.untracked.string( "es" ),
    MuJobPSet = cms.PSet(  )
)
process.hltEcalRecHitAll = cms.EDProducer( "EcalRawToRecHitProducer",
    splitOutput = cms.bool( True ),
    rechitCollection = cms.string( "NotNeededsplitOutputTrue" ),
    EErechitCollection = cms.string( "EcalRecHitsEE" ),
    EBrechitCollection = cms.string( "EcalRecHitsEB" ),
    sourceTag = cms.InputTag( "hltEcalRegionalRestFEDs" ),
    lazyGetterTag = cms.InputTag( "hltEcalRawToRecHitFacility" )
)
process.hltESRecHitAll = cms.EDProducer( "EcalRawToRecHitProducer",
    splitOutput = cms.bool( False ),
    rechitCollection = cms.string( "EcalRecHitsES" ),
    EErechitCollection = cms.string( "" ),
    EBrechitCollection = cms.string( "" ),
    sourceTag = cms.InputTag( 'hltEcalRegionalESRestFEDs','es' ),
    lazyGetterTag = cms.InputTag( "hltESRawToRecHitFacility" )
)
process.hltHybridSuperClustersActivity = cms.EDProducer( "HybridClusterProducer",
    eThreshA = cms.double( 0.0030 ),
    basicclusterCollection = cms.string( "hybridBarrelBasicClusters" ),
    clustershapecollection = cms.string( "" ),
    ethresh = cms.double( 0.1 ),
    ewing = cms.double( 0.0 ),
    RecHitSeverityToBeExcluded = cms.vstring( 'kWeird' ),
    posCalcParameters = cms.PSet( 
      T0_barl = cms.double( 7.4 ),
      LogWeighted = cms.bool( True ),
      T0_endc = cms.double( 3.1 ),
      T0_endcPresh = cms.double( 1.2 ),
      W0 = cms.double( 4.2 ),
      X0 = cms.double( 0.89 )
    ),
    HybridBarrelSeedThr = cms.double( 1.0 ),
    dynamicPhiRoad = cms.bool( False ),
    shapeAssociation = cms.string( "hybridShapeAssoc" ),
    RecHitFlagToBeExcluded = cms.vstring(  ),
    useEtForXi = cms.bool( True ),
    step = cms.int32( 17 ),
    eThreshB = cms.double( 0.1 ),
    xi = cms.double( 0.0 ),
    eseed = cms.double( 0.35 ),
    ecalhitproducer = cms.string( "hltEcalRecHitAll" ),
    dynamicEThresh = cms.bool( False ),
    ecalhitcollection = cms.string( "EcalRecHitsEB" ),
    excludeFlagged = cms.bool( True ),
    superclusterCollection = cms.string( "" )
)
process.hltCorrectedHybridSuperClustersActivity = cms.EDProducer( "EgammaSCCorrectionMaker",
    corectedSuperClusterCollection = cms.string( "" ),
    sigmaElectronicNoise = cms.double( 0.15 ),
    superClusterAlgo = cms.string( "Hybrid" ),
    etThresh = cms.double( 5.0 ),
    rawSuperClusterProducer = cms.InputTag( "hltHybridSuperClustersActivity" ),
    applyEnergyCorrection = cms.bool( True ),
    isl_fCorrPset = cms.PSet(  ),
    VerbosityLevel = cms.string( "ERROR" ),
    recHitProducer = cms.InputTag( 'hltEcalRecHitAll','EcalRecHitsEB' ),
    fix_fCorrPset = cms.PSet(  ),
    modeEE = cms.int32( 0 ),
    modeEB = cms.int32( 0 ),
    dyn_fCorrPset = cms.PSet(  ),
    energyCorrectorName = cms.string( "EcalClusterEnergyCorrectionObjectSpecific" ),
    applyCrackCorrection = cms.bool( False ),
    hyb_fCorrPset = cms.PSet( 
      brLinearLowThr = cms.double( 1.1 ),
      fEtEtaVec = cms.vdouble( 0.0, 1.00121, -0.63672, 0.0, 0.0, 0.0, 0.5655, 6.457, 0.5081, 8.0, 1.023, -0.00181 ),
      brLinearHighThr = cms.double( 8.0 ),
      fBremVec = cms.vdouble( -0.04382, 0.1169, 0.9267, -9.413E-4, 1.419 )
    )
)
process.hltMulti5x5BasicClustersActivity = cms.EDProducer( "Multi5x5ClusterProducer",
    endcapHitCollection = cms.string( "EcalRecHitsEE" ),
    barrelClusterCollection = cms.string( "multi5x5BarrelBasicClusters" ),
    IslandEndcapSeedThr = cms.double( 0.18 ),
    doEndcap = cms.bool( True ),
    posCalcParameters = cms.PSet( 
      T0_barl = cms.double( 7.4 ),
      LogWeighted = cms.bool( True ),
      T0_endc = cms.double( 3.1 ),
      T0_endcPresh = cms.double( 1.2 ),
      W0 = cms.double( 4.2 ),
      X0 = cms.double( 0.89 )
    ),
    barrelShapeAssociation = cms.string( "multi5x5BarrelShapeAssoc" ),
    endcapShapeAssociation = cms.string( "multi5x5EndcapShapeAssoc" ),
    endcapHitProducer = cms.string( "hltEcalRecHitAll" ),
    clustershapecollectionEB = cms.string( "multi5x5BarrelShape" ),
    IslandBarrelSeedThr = cms.double( 0.5 ),
    barrelHitProducer = cms.string( "hltEcalRecHitAll" ),
    RecHitFlagToBeExcluded = cms.vstring(  ),
    barrelHitCollection = cms.string( "EcalRecHitsEB" ),
    clustershapecollectionEE = cms.string( "multi5x5EndcapShape" ),
    endcapClusterCollection = cms.string( "multi5x5EndcapBasicClusters" ),
    doBarrel = cms.bool( False )
)
process.hltMulti5x5SuperClustersActivity = cms.EDProducer( "Multi5x5SuperClusterProducer",
    barrelSuperclusterCollection = cms.string( "multi5x5BarrelSuperClusters" ),
    endcapEtaSearchRoad = cms.double( 0.14 ),
    barrelClusterCollection = cms.string( "multi5x5BarrelBasicClusters" ),
    dynamicPhiRoad = cms.bool( False ),
    endcapClusterProducer = cms.string( "hltMulti5x5BasicClustersActivity" ),
    barrelPhiSearchRoad = cms.double( 0.8 ),
    endcapPhiSearchRoad = cms.double( 0.6 ),
    barrelClusterProducer = cms.string( "hltMulti5x5BasicClustersActivity" ),
    seedTransverseEnergyThreshold = cms.double( 1.0 ),
    endcapSuperclusterCollection = cms.string( "multi5x5EndcapSuperClusters" ),
    barrelEtaSearchRoad = cms.double( 0.06 ),
    bremRecoveryPset = cms.PSet( 
      barrel = cms.PSet( 
        cryVec = cms.vint32( 16, 13, 11, 10, 9, 8, 7, 6, 5, 4, 3 ),
        cryMin = cms.int32( 2 ),
        etVec = cms.vdouble( 5.0, 10.0, 15.0, 20.0, 30.0, 40.0, 45.0, 55.0, 135.0, 195.0, 225.0 )
      ),
      endcap = cms.PSet( 
        a = cms.double( 47.85 ),
        c = cms.double( 0.1201 ),
        b = cms.double( 108.8 )
      )
    ),
    doEndcaps = cms.bool( True ),
    endcapClusterCollection = cms.string( "multi5x5EndcapBasicClusters" ),
    doBarrel = cms.bool( False )
)
process.hltMulti5x5SuperClustersWithPreshowerActivity = cms.EDProducer( "PreshowerClusterProducer",
    assocSClusterCollection = cms.string( "" ),
    preshStripEnergyCut = cms.double( 0.0 ),
    preshClusterCollectionY = cms.string( "preshowerYClusters" ),
    preshClusterCollectionX = cms.string( "preshowerXClusters" ),
    etThresh = cms.double( 0.0 ),
    preshRecHitProducer = cms.InputTag( 'hltESRecHitAll','EcalRecHitsES' ),
    endcapSClusterProducer = cms.InputTag( 'hltMulti5x5SuperClustersActivity','multi5x5EndcapSuperClusters' ),
    preshNclust = cms.int32( 4 ),
    preshClusterEnergyCut = cms.double( 0.0 ),
    preshSeededNstrip = cms.int32( 15 )
)
process.hltCorrectedMulti5x5SuperClustersWithPreshowerActivity = cms.EDProducer( "EgammaSCCorrectionMaker",
    corectedSuperClusterCollection = cms.string( "" ),
    sigmaElectronicNoise = cms.double( 0.15 ),
    superClusterAlgo = cms.string( "Multi5x5" ),
    etThresh = cms.double( 5.0 ),
    rawSuperClusterProducer = cms.InputTag( "hltMulti5x5SuperClustersWithPreshowerActivity" ),
    applyEnergyCorrection = cms.bool( True ),
    isl_fCorrPset = cms.PSet(  ),
    VerbosityLevel = cms.string( "ERROR" ),
    recHitProducer = cms.InputTag( 'hltEcalRecHitAll','EcalRecHitsEE' ),
    fix_fCorrPset = cms.PSet( 
      brLinearLowThr = cms.double( 0.9 ),
      fEtEtaVec = cms.vdouble( 1.0, -0.4386, -32.38, 0.6372, 15.67, -0.0928, -2.462, 1.138, 20.93 ),
      brLinearHighThr = cms.double( 6.0 ),
      fBremVec = cms.vdouble( -0.05228, 0.08738, 0.9508, 0.002677, 1.221 )
    ),
    modeEE = cms.int32( 0 ),
    modeEB = cms.int32( 0 ),
    dyn_fCorrPset = cms.PSet(  ),
    energyCorrectorName = cms.string( "EcalClusterEnergyCorrectionObjectSpecific" ),
    applyCrackCorrection = cms.bool( False ),
    hyb_fCorrPset = cms.PSet(  )
)
process.hltRecoEcalSuperClusterActivityCandidate = cms.EDProducer( "EgammaHLTRecoEcalCandidateProducers",
    scIslandEndcapProducer = cms.InputTag( "hltCorrectedMulti5x5SuperClustersWithPreshowerActivity" ),
    scHybridBarrelProducer = cms.InputTag( "hltCorrectedHybridSuperClustersActivity" ),
    recoEcalCandidateCollection = cms.string( "" )
)
process.hltEcalActivitySuperClusterWrapper = cms.EDFilter( "HLTEgammaTriggerFilterObjectWrapper",
    saveTags = cms.bool( False ),
    doIsolated = cms.bool( True ),
    candIsolatedTag = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    candNonIsolatedTag = cms.InputTag( "" )
)
process.hltDoubleEG70EtDoubleFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( False ),
    L1NonIsoCand = cms.InputTag( "" ),
    relaxed = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    inputTag = cms.InputTag( "hltEcalActivitySuperClusterWrapper" ),
    etcutEB = cms.double( 70.0 ),
    ncandcut = cms.int32( 2 ),
    etcutEE = cms.double( 70.0 )
)
process.hltActivityPhotonHcalForHE = cms.EDProducer( "EgammaHLTHcalIsolationProducersRegional",
    eMinHE = cms.double( 0.8 ),
    hbheRecHitProducer = cms.InputTag( "hltHbhereco" ),
    effectiveAreaBarrel = cms.double( 0.105 ),
    outerCone = cms.double( 0.14 ),
    eMinHB = cms.double( 0.7 ),
    innerCone = cms.double( 0.0 ),
    etMinHE = cms.double( -1.0 ),
    etMinHB = cms.double( -1.0 ),
    rhoProducer = cms.InputTag( 'hltKT6CaloJets','rho' ),
    depth = cms.int32( -1 ),
    doRhoCorrection = cms.bool( False ),
    effectiveAreaEndcap = cms.double( 0.17 ),
    recoEcalCandidateProducer = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    rhoMax = cms.double( 9.9999999E7 ),
    rhoScale = cms.double( 1.0 ),
    doEtSum = cms.bool( False )
)
process.hltDoubleEG70HEDoubleFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.1 ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    thrOverEEB = cms.double( 0.15 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( "hltActivityPhotonHcalForHE" ),
    candTag = cms.InputTag( "hltDoubleEG70EtDoubleFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltBoolEnd = cms.EDFilter( "HLTBool",
    result = cms.bool( True )
)
process.hltPreDoublePhoton80 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltEG80EtFilterL1EG30 = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( False ),
    L1NonIsoCand = cms.InputTag( "" ),
    relaxed = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    inputTag = cms.InputTag( "hltEGRegionalL1SingleEG30" ),
    etcutEB = cms.double( 80.0 ),
    ncandcut = cms.int32( 1 ),
    etcutEE = cms.double( 80.0 )
)
process.hltEG80HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.1 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( 0.15 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededPhotonHcalForHE" ),
    candTag = cms.InputTag( "hltEG80EtFilterL1EG30" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltDoubleIsoEG80EtFilterUnseededTight = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( False ),
    L1NonIsoCand = cms.InputTag( "" ),
    relaxed = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    inputTag = cms.InputTag( "hltEcalActivitySuperClusterWrapper" ),
    etcutEB = cms.double( 80.0 ),
    ncandcut = cms.int32( 2 ),
    etcutEE = cms.double( 80.0 )
)
process.hltDoublePhoton80EgammaLHEDoubleFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.1 ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    thrOverEEB = cms.double( 0.15 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( "hltActivityPhotonHcalForHE" ),
    candTag = cms.InputTag( "hltDoubleIsoEG80EtFilterUnseededTight" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltPrePhoton135 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltEG135EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( False ),
    L1NonIsoCand = cms.InputTag( "" ),
    relaxed = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    inputTag = cms.InputTag( "hltEGRegionalL1SingleEG30" ),
    etcutEB = cms.double( 135.0 ),
    ncandcut = cms.int32( 1 ),
    etcutEE = cms.double( 135.0 )
)
process.hltPhoton135HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.1 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( 0.15 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededPhotonHcalForHE" ),
    candTag = cms.InputTag( "hltEG135EtFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltPrePhoton150 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltEG150EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( False ),
    L1NonIsoCand = cms.InputTag( "" ),
    relaxed = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    inputTag = cms.InputTag( "hltEGRegionalL1SingleEG30" ),
    etcutEB = cms.double( 150.0 ),
    ncandcut = cms.int32( 1 ),
    etcutEE = cms.double( 150.0 )
)
process.hltPhoton150HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.1 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( 0.15 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededPhotonHcalForHE" ),
    candTag = cms.InputTag( "hltEG150EtFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltPrePhoton160 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltEG160EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( False ),
    L1NonIsoCand = cms.InputTag( "" ),
    relaxed = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    inputTag = cms.InputTag( "hltEGRegionalL1SingleEG30" ),
    etcutEB = cms.double( 160.0 ),
    ncandcut = cms.int32( 1 ),
    etcutEE = cms.double( 160.0 )
)
process.hltPhoton160HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.1 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( 0.15 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededPhotonHcalForHE" ),
    candTag = cms.InputTag( "hltEG160EtFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltPrePhoton250NoHE = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltEG300EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    L1NonIsoCand = cms.InputTag( "" ),
    relaxed = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    inputTag = cms.InputTag( "hltEGRegionalL1SingleEG30" ),
    etcutEB = cms.double( 250.0 ),
    ncandcut = cms.int32( 1 ),
    etcutEE = cms.double( 250.0 )
)
process.hltPrePhoton300NoHE = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sL1SingleEG20 = cms.EDFilter( "HLTLevel1GTSeed",
    saveTags = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG20" ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreEle65CaloIdVTTrkIdT = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltEGRegionalL1SingleEG20 = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    saveTags = cms.bool( False ),
    endcap_end = cms.double( 2.65 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    barrel_end = cms.double( 1.4791 ),
    l1IsolatedTag = cms.InputTag( 'hltL1extraParticles','Isolated' ),
    candIsolatedTag = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    region_phi_size = cms.double( 1.044 ),
    region_eta_size = cms.double( 0.522 ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG20" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    candNonIsolatedTag = cms.InputTag( "" ),
    l1NonIsolatedTag = cms.InputTag( 'hltL1extraParticles','NonIsolated' )
)
process.hltEG65EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( False ),
    L1NonIsoCand = cms.InputTag( "" ),
    relaxed = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    inputTag = cms.InputTag( "hltEGRegionalL1SingleEG20" ),
    etcutEB = cms.double( 65.0 ),
    ncandcut = cms.int32( 1 ),
    etcutEE = cms.double( 65.0 )
)
process.hltL1SeededHLTClusterShape = cms.EDProducer( "EgammaHLTClusterShapeProducer",
    recoEcalCandidateProducer = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    ecalRechitEB = cms.InputTag( 'hltEcalRegionalEgammaRecHit','EcalRecHitsEB' ),
    ecalRechitEE = cms.InputTag( 'hltEcalRegionalEgammaRecHit','EcalRecHitsEE' ),
    isIeta = cms.bool( True )
)
process.hltEG65CaloIdTClusterShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 0.031 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 0.011 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededHLTClusterShape" ),
    candTag = cms.InputTag( "hltEG65EtFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltEG65CaloIdVTHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.05 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( 0.05 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededPhotonHcalForHE" ),
    candTag = cms.InputTag( "hltEG65CaloIdTClusterShapeFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltSiPixelDigis = cms.EDProducer( "SiPixelRawToDigi",
    UseQualityInfo = cms.bool( False ),
    CheckPixelOrder = cms.bool( False ),
    IncludeErrors = cms.bool( False ),
    UseCablingTree = cms.untracked.bool( True ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    ErrorList = cms.vint32(  ),
    Regions = cms.PSet(  ),
    Timing = cms.untracked.bool( False ),
    UserErrorList = cms.vint32(  )
)
process.hltSiPixelClusters = cms.EDProducer( "SiPixelClusterProducer",
    src = cms.InputTag( "hltSiPixelDigis" ),
    ChannelThreshold = cms.int32( 1000 ),
    maxNumberOfClusters = cms.int32( 20000 ),
    VCaltoElectronGain = cms.int32( 65 ),
    MissCalibrate = cms.untracked.bool( True ),
    SplitClusters = cms.bool( False ),
    VCaltoElectronOffset = cms.int32( -414 ),
    payloadType = cms.string( "HLT" ),
    SeedThreshold = cms.int32( 1000 ),
    ClusterThreshold = cms.double( 4000.0 )
)
process.hltSiPixelRecHits = cms.EDProducer( "SiPixelRecHitConverter",
    VerboseLevel = cms.untracked.int32( 0 ),
    src = cms.InputTag( "hltSiPixelClusters" ),
    CPE = cms.string( "hltESPPixelCPEGeneric" )
)
process.hltSiStripExcludedFEDListProducer = cms.EDProducer( "SiStripExcludedFEDListProducer",
    ProductLabel = cms.InputTag( "rawDataCollector" )
)
process.hltSiStripRawToClustersFacility = cms.EDProducer( "SiStripRawToClusters",
    ProductLabel = cms.InputTag( "rawDataCollector" ),
    Algorithms = cms.PSet( 
      SiStripFedZeroSuppressionMode = cms.uint32( 4 ),
      CommonModeNoiseSubtractionMode = cms.string( "Median" ),
      PedestalSubtractionFedMode = cms.bool( True ),
      TruncateInSuppressor = cms.bool( True ),
      doAPVRestore = cms.bool( False ),
      useCMMeanMap = cms.bool( False )
    ),
    Clusterizer = cms.PSet( 
      ChannelThreshold = cms.double( 2.0 ),
      MaxSequentialBad = cms.uint32( 1 ),
      MaxSequentialHoles = cms.uint32( 0 ),
      Algorithm = cms.string( "ThreeThresholdAlgorithm" ),
      MaxAdjacentBad = cms.uint32( 0 ),
      QualityLabel = cms.string( "" ),
      SeedThreshold = cms.double( 3.0 ),
      ClusterThreshold = cms.double( 5.0 ),
      setDetId = cms.bool( True ),
      RemoveApvShots = cms.bool( True )
    )
)
process.hltSiStripClusters = cms.EDProducer( "MeasurementTrackerSiStripRefGetterProducer",
    InputModuleLabel = cms.InputTag( "hltSiStripRawToClustersFacility" ),
    measurementTrackerName = cms.string( "hltESPMeasurementTracker" )
)
process.hltL1SeededStartUpElectronPixelSeeds = cms.EDProducer( "ElectronSeedProducer",
    endcapSuperClusters = cms.InputTag( "hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Seeded" ),
    SeedConfiguration = cms.PSet( 
      searchInTIDTEC = cms.bool( True ),
      HighPtThreshold = cms.double( 35.0 ),
      r2MinF = cms.double( -0.15 ),
      OrderedHitsFactoryPSet = cms.PSet( 
        maxElement = cms.uint32( 0 ),
        ComponentName = cms.string( "StandardHitPairGenerator" ),
        SeedingLayers = cms.string( "hltESPMixedLayerPairs" ),
        useOnDemandTracker = cms.untracked.int32( 0 )
      ),
      DeltaPhi1Low = cms.double( 0.23 ),
      DeltaPhi1High = cms.double( 0.08 ),
      ePhiMin1 = cms.double( -0.08 ),
      PhiMin2 = cms.double( -0.0040 ),
      LowPtThreshold = cms.double( 3.0 ),
      RegionPSet = cms.PSet( 
        deltaPhiRegion = cms.double( 0.4 ),
        originHalfLength = cms.double( 15.0 ),
        useZInVertex = cms.bool( True ),
        deltaEtaRegion = cms.double( 0.1 ),
        ptMin = cms.double( 1.5 ),
        originRadius = cms.double( 0.2 ),
        VertexProducer = cms.InputTag( "dummyVertices" )
      ),
      maxHOverE = cms.double( 999999.0 ),
      dynamicPhiRoad = cms.bool( False ),
      ePhiMax1 = cms.double( 0.04 ),
      DeltaPhi2 = cms.double( 0.0040 ),
      measurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
      SizeWindowENeg = cms.double( 0.675 ),
      nSigmasDeltaZ1 = cms.double( 5.0 ),
      rMaxI = cms.double( 0.2 ),
      PhiMax2 = cms.double( 0.0040 ),
      preFilteredSeeds = cms.bool( True ),
      r2MaxF = cms.double( 0.15 ),
      pPhiMin1 = cms.double( -0.04 ),
      initialSeeds = cms.InputTag( "noSeedsHere" ),
      pPhiMax1 = cms.double( 0.08 ),
      hbheModule = cms.string( "hbhereco" ),
      SCEtCut = cms.double( 3.0 ),
      z2MaxB = cms.double( 0.09 ),
      fromTrackerSeeds = cms.bool( True ),
      hcalRecHits = cms.InputTag( "hltHbhereco" ),
      z2MinB = cms.double( -0.09 ),
      hbheInstance = cms.string( "" ),
      rMinI = cms.double( -0.2 ),
      hOverEConeSize = cms.double( 0.0 ),
      hOverEHBMinE = cms.double( 999999.0 ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      applyHOverECut = cms.bool( False ),
      hOverEHFMinE = cms.double( 999999.0 )
    ),
    barrelSuperClusters = cms.InputTag( "hltCorrectedHybridSuperClustersL1Seeded" )
)
process.hltEle65CaloIdVTPixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    saveTags = cms.bool( False ),
    doIsolated = cms.bool( True ),
    L1NonIsoCand = cms.InputTag( "" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "" ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    candTag = cms.InputTag( "hltEG65CaloIdVTHEFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltL1SeededStartUpElectronPixelSeeds" )
)
process.hltCkfL1SeededTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltL1SeededStartUpElectronPixelSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "hltESPCkfTrajectoryBuilder" )
)
process.hltCtfL1SeededWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltCkfL1SeededTrackCandidates" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    Propagator = cms.string( "PropagatorWithMaterial" )
)
process.hltPixelMatchElectronsL1Seeded = cms.EDProducer( "EgammaHLTPixelMatchElectronProducers",
    BSProducer = cms.InputTag( "hltOnlineBeamSpot" ),
    UseGsfTracks = cms.bool( False ),
    TrackProducer = cms.InputTag( "hltCtfL1SeededWithMaterialTracks" ),
    GsfTrackProducer = cms.InputTag( "" )
)
process.hltEle65CaloIdVTOneOEMinusOneOPFilter = cms.EDFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    saveTags = cms.bool( False ),
    doIsolated = cms.bool( True ),
    electronNonIsolatedProducer = cms.InputTag( "" ),
    barrelcut = cms.double( 999.9 ),
    electronIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1Seeded" ),
    ncandcut = cms.int32( 1 ),
    candTag = cms.InputTag( "hltEle65CaloIdVTPixelMatchFilter" ),
    endcapcut = cms.double( 999.9 )
)
process.hltElectronL1SeededDetaDphi = cms.EDProducer( "EgammaHLTElectronDetaDphiProducer",
    variablesAtVtx = cms.bool( False ),
    useSCRefs = cms.bool( False ),
    BSProducer = cms.InputTag( "hltOnlineBeamSpot" ),
    electronProducer = cms.InputTag( "hltPixelMatchElectronsL1Seeded" ),
    recoEcalCandidateProducer = cms.InputTag( "" ),
    useTrackProjectionToEcal = cms.bool( False )
)
process.hltEle65CaloIdVTTrkIdTDetaFilter = cms.EDFilter( "HLTElectronGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    thrTimesPtEB = cms.double( -1.0 ),
    saveTags = cms.bool( False ),
    thrRegularEE = cms.double( 0.0080 ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Seeded" ),
    thrRegularEB = cms.double( 0.0080 ),
    lessThan = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( 'hltElectronL1SeededDetaDphi','Deta' ),
    candTag = cms.InputTag( "hltEle65CaloIdVTOneOEMinusOneOPFilter" ),
    thrTimesPtEE = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrOverPtEB = cms.double( -1.0 )
)
process.hltEle65CaloIdVTTrkIdTDphiFilter = cms.EDFilter( "HLTElectronGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    thrTimesPtEB = cms.double( -1.0 ),
    saveTags = cms.bool( True ),
    thrRegularEE = cms.double( 0.05 ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Seeded" ),
    thrRegularEB = cms.double( 0.07 ),
    lessThan = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( 'hltElectronL1SeededDetaDphi','Dphi' ),
    candTag = cms.InputTag( "hltEle65CaloIdVTTrkIdTDetaFilter" ),
    thrTimesPtEE = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrOverPtEB = cms.double( -1.0 )
)
process.hltPreEle80CaloIdVTTrkIdT = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltEG80EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( False ),
    L1NonIsoCand = cms.InputTag( "" ),
    relaxed = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    inputTag = cms.InputTag( "hltEGRegionalL1SingleEG20" ),
    etcutEB = cms.double( 80.0 ),
    ncandcut = cms.int32( 1 ),
    etcutEE = cms.double( 80.0 )
)
process.hltEG80CaloIdTClusterShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 0.031 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 0.011 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededHLTClusterShape" ),
    candTag = cms.InputTag( "hltEG80EtFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltEG80CaloIdVTHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.05 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( 0.05 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededPhotonHcalForHE" ),
    candTag = cms.InputTag( "hltEG80CaloIdTClusterShapeFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltEle80CaloIdVTPixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    saveTags = cms.bool( False ),
    doIsolated = cms.bool( True ),
    L1NonIsoCand = cms.InputTag( "" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "" ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    candTag = cms.InputTag( "hltEG80CaloIdVTHEFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltL1SeededStartUpElectronPixelSeeds" )
)
process.hltEle80CaloIdVTOneOEMinusOneOPFilter = cms.EDFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    saveTags = cms.bool( False ),
    doIsolated = cms.bool( True ),
    electronNonIsolatedProducer = cms.InputTag( "" ),
    barrelcut = cms.double( 999.9 ),
    electronIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1Seeded" ),
    ncandcut = cms.int32( 1 ),
    candTag = cms.InputTag( "hltEle80CaloIdVTPixelMatchFilter" ),
    endcapcut = cms.double( 999.9 )
)
process.hltEle80CaloIdVTTrkIdTDetaFilter = cms.EDFilter( "HLTElectronGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    thrTimesPtEB = cms.double( -1.0 ),
    saveTags = cms.bool( False ),
    thrRegularEE = cms.double( 0.0080 ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Seeded" ),
    thrRegularEB = cms.double( 0.0080 ),
    lessThan = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( 'hltElectronL1SeededDetaDphi','Deta' ),
    candTag = cms.InputTag( "hltEle80CaloIdVTOneOEMinusOneOPFilter" ),
    thrTimesPtEE = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrOverPtEB = cms.double( -1.0 )
)
process.hltEle80CaloIdVTTrkIdTDphiFilter = cms.EDFilter( "HLTElectronGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    thrTimesPtEB = cms.double( -1.0 ),
    saveTags = cms.bool( True ),
    thrRegularEE = cms.double( 0.05 ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Seeded" ),
    thrRegularEB = cms.double( 0.07 ),
    lessThan = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( 'hltElectronL1SeededDetaDphi','Dphi' ),
    candTag = cms.InputTag( "hltEle80CaloIdVTTrkIdTDetaFilter" ),
    thrTimesPtEE = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrOverPtEB = cms.double( -1.0 )
)
process.hltPreEle100CaloIdVTTrkIdT = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltEG100EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( False ),
    L1NonIsoCand = cms.InputTag( "" ),
    relaxed = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    inputTag = cms.InputTag( "hltEGRegionalL1SingleEG20" ),
    etcutEB = cms.double( 100.0 ),
    ncandcut = cms.int32( 1 ),
    etcutEE = cms.double( 100.0 )
)
process.hltEG100CaloIdTClusterShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 0.031 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 0.011 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededHLTClusterShape" ),
    candTag = cms.InputTag( "hltEG100EtFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltEG100CaloIdVTHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.05 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( 0.05 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededPhotonHcalForHE" ),
    candTag = cms.InputTag( "hltEG100CaloIdTClusterShapeFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltEle100CaloIdVTPixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    saveTags = cms.bool( False ),
    doIsolated = cms.bool( True ),
    L1NonIsoCand = cms.InputTag( "" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "" ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    candTag = cms.InputTag( "hltEG100CaloIdVTHEFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltL1SeededStartUpElectronPixelSeeds" )
)
process.hltEle100CaloIdVTOneOEMinusOneOPFilter = cms.EDFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    saveTags = cms.bool( False ),
    doIsolated = cms.bool( True ),
    electronNonIsolatedProducer = cms.InputTag( "" ),
    barrelcut = cms.double( 999.9 ),
    electronIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1Seeded" ),
    ncandcut = cms.int32( 1 ),
    candTag = cms.InputTag( "hltEle100CaloIdVTPixelMatchFilter" ),
    endcapcut = cms.double( 999.9 )
)
process.hltEle100CaloIdVTTrkIdTDetaFilter = cms.EDFilter( "HLTElectronGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    thrTimesPtEB = cms.double( -1.0 ),
    saveTags = cms.bool( False ),
    thrRegularEE = cms.double( 0.0080 ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Seeded" ),
    thrRegularEB = cms.double( 0.0080 ),
    lessThan = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( 'hltElectronL1SeededDetaDphi','Deta' ),
    candTag = cms.InputTag( "hltEle100CaloIdVTOneOEMinusOneOPFilter" ),
    thrTimesPtEE = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrOverPtEB = cms.double( -1.0 )
)
process.hltEle100CaloIdVTTrkIdTDphiFilter = cms.EDFilter( "HLTElectronGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    thrTimesPtEB = cms.double( -1.0 ),
    saveTags = cms.bool( True ),
    thrRegularEE = cms.double( 0.05 ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Seeded" ),
    thrRegularEB = cms.double( 0.07 ),
    lessThan = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( 'hltElectronL1SeededDetaDphi','Dphi' ),
    candTag = cms.InputTag( "hltEle100CaloIdVTTrkIdTDetaFilter" ),
    thrTimesPtEE = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrOverPtEB = cms.double( -1.0 )
)
process.hltL1sL1SingleEG22 = cms.EDFilter( "HLTLevel1GTSeed",
    saveTags = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG22" ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreDoubleEle33CaloIdL = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltEGRegionalL1SingleEG22 = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    saveTags = cms.bool( False ),
    endcap_end = cms.double( 2.65 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    barrel_end = cms.double( 1.4791 ),
    l1IsolatedTag = cms.InputTag( 'hltL1extraParticles','Isolated' ),
    candIsolatedTag = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    region_phi_size = cms.double( 1.044 ),
    region_eta_size = cms.double( 0.522 ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG22" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    candNonIsolatedTag = cms.InputTag( "" ),
    l1NonIsolatedTag = cms.InputTag( 'hltL1extraParticles','NonIsolated' )
)
process.hltEG33EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( False ),
    L1NonIsoCand = cms.InputTag( "" ),
    relaxed = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    inputTag = cms.InputTag( "hltEGRegionalL1SingleEG22" ),
    etcutEB = cms.double( 33.0 ),
    ncandcut = cms.int32( 1 ),
    etcutEE = cms.double( 33.0 )
)
process.hltEG33HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.1 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( 0.15 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededPhotonHcalForHE" ),
    candTag = cms.InputTag( "hltEG33EtFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltEG33CaloIdLClusterShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 0.035 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 0.014 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededHLTClusterShape" ),
    candTag = cms.InputTag( "hltEG33HEFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltEle33CaloIdLPixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    saveTags = cms.bool( True ),
    doIsolated = cms.bool( True ),
    L1NonIsoCand = cms.InputTag( "" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "" ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    candTag = cms.InputTag( "hltEG33CaloIdLClusterShapeFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltL1SeededStartUpElectronPixelSeeds" )
)
process.hltDoubleEG33EtDoubleFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( False ),
    L1NonIsoCand = cms.InputTag( "" ),
    relaxed = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    inputTag = cms.InputTag( "hltEcalActivitySuperClusterWrapper" ),
    etcutEB = cms.double( 33.0 ),
    ncandcut = cms.int32( 2 ),
    etcutEE = cms.double( 33.0 )
)
process.hltDoubleEG33HEDoubleFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.1 ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    thrOverEEB = cms.double( 0.15 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( "hltActivityPhotonHcalForHE" ),
    candTag = cms.InputTag( "hltDoubleEG33EtDoubleFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltActivityPhotonClusterShape = cms.EDProducer( "EgammaHLTClusterShapeProducer",
    recoEcalCandidateProducer = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    ecalRechitEB = cms.InputTag( 'hltEcalRecHitAll','EcalRecHitsEB' ),
    ecalRechitEE = cms.InputTag( 'hltEcalRecHitAll','EcalRecHitsEE' ),
    isIeta = cms.bool( True )
)
process.hltDoubleEG33CaloIdLClusterShapeDoubleFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 0.035 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 0.014 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( "hltActivityPhotonClusterShape" ),
    candTag = cms.InputTag( "hltDoubleEG33HEDoubleFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltActivityStartUpElectronPixelSeeds = cms.EDProducer( "ElectronSeedProducer",
    endcapSuperClusters = cms.InputTag( "hltCorrectedMulti5x5SuperClustersWithPreshowerActivity" ),
    SeedConfiguration = cms.PSet( 
      searchInTIDTEC = cms.bool( True ),
      HighPtThreshold = cms.double( 35.0 ),
      r2MinF = cms.double( -0.15 ),
      OrderedHitsFactoryPSet = cms.PSet( 
        maxElement = cms.uint32( 0 ),
        ComponentName = cms.string( "StandardHitPairGenerator" ),
        SeedingLayers = cms.string( "hltESPMixedLayerPairs" ),
        useOnDemandTracker = cms.untracked.int32( 0 )
      ),
      DeltaPhi1Low = cms.double( 0.23 ),
      DeltaPhi1High = cms.double( 0.08 ),
      ePhiMin1 = cms.double( -0.08 ),
      PhiMin2 = cms.double( -0.0040 ),
      LowPtThreshold = cms.double( 3.0 ),
      RegionPSet = cms.PSet( 
        deltaPhiRegion = cms.double( 0.4 ),
        originHalfLength = cms.double( 15.0 ),
        useZInVertex = cms.bool( True ),
        deltaEtaRegion = cms.double( 0.1 ),
        ptMin = cms.double( 1.5 ),
        originRadius = cms.double( 0.2 ),
        VertexProducer = cms.InputTag( "dummyVertices" )
      ),
      maxHOverE = cms.double( 999999.0 ),
      dynamicPhiRoad = cms.bool( False ),
      ePhiMax1 = cms.double( 0.04 ),
      DeltaPhi2 = cms.double( 0.0040 ),
      measurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
      SizeWindowENeg = cms.double( 0.675 ),
      nSigmasDeltaZ1 = cms.double( 5.0 ),
      rMaxI = cms.double( 0.2 ),
      rMinI = cms.double( -0.2 ),
      preFilteredSeeds = cms.bool( True ),
      r2MaxF = cms.double( 0.15 ),
      pPhiMin1 = cms.double( -0.04 ),
      initialSeeds = cms.InputTag( "noSeedsHere" ),
      pPhiMax1 = cms.double( 0.08 ),
      hbheModule = cms.string( "hbhereco" ),
      SCEtCut = cms.double( 3.0 ),
      z2MaxB = cms.double( 0.09 ),
      fromTrackerSeeds = cms.bool( True ),
      hcalRecHits = cms.InputTag( "hltHbhereco" ),
      z2MinB = cms.double( -0.09 ),
      hbheInstance = cms.string( "" ),
      PhiMax2 = cms.double( 0.0040 ),
      hOverEConeSize = cms.double( 0.0 ),
      hOverEHBMinE = cms.double( 999999.0 ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      applyHOverECut = cms.bool( False ),
      hOverEHFMinE = cms.double( 999999.0 )
    ),
    barrelSuperClusters = cms.InputTag( "hltCorrectedHybridSuperClustersActivity" )
)
process.hltDiEle33CaloIdLPixelMatchDoubleFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    saveTags = cms.bool( True ),
    doIsolated = cms.bool( True ),
    L1NonIsoCand = cms.InputTag( "" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "" ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 2 ),
    candTag = cms.InputTag( "hltDoubleEG33CaloIdLClusterShapeDoubleFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltActivityStartUpElectronPixelSeeds" )
)
process.hltPreDoubleEle33CaloIdLGsfTrkIdVL = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltActivityCkfTrackCandidatesForGSF = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltActivityStartUpElectronPixelSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 1000000 ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "hltESPTrajectoryBuilderForElectrons" )
)
process.hltActivityElectronGsfTracks = cms.EDProducer( "GsfTrackProducer",
    src = cms.InputTag( "hltActivityCkfTrackCandidatesForGSF" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    producer = cms.string( "" ),
    Fitter = cms.string( "hltESPGsfElectronFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "hltESPMeasurementTracker" ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "gsf" ),
    Propagator = cms.string( "hltESPFwdElectronPropagator" )
)
process.hltActivityGsfElectrons = cms.EDProducer( "EgammaHLTPixelMatchElectronProducers",
    BSProducer = cms.InputTag( "hltOnlineBeamSpot" ),
    UseGsfTracks = cms.bool( True ),
    TrackProducer = cms.InputTag( "" ),
    GsfTrackProducer = cms.InputTag( "hltActivityElectronGsfTracks" )
)
process.hltActivityGsfTrackVars = cms.EDProducer( "EgammaHLTGsfTrackVarProducer",
    recoEcalCandidateProducer = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    beamSpotProducer = cms.InputTag( "hltOnlineBeamSpot" ),
    upperTrackNrToRemoveCut = cms.int32( 9999 ),
    lowerTrackNrToRemoveCut = cms.int32( -1 ),
    inputCollection = cms.InputTag( "hltActivityElectronGsfTracks" )
)
process.hltDiEle33CaloIdLGsfTrkIdVLDEtaDoubleFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 0.02 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 0.02 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( 'hltActivityGsfTrackVars','Deta' ),
    candTag = cms.InputTag( "hltDiEle33CaloIdLPixelMatchDoubleFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltDiEle33CaloIdLGsfTrkIdVLDPhiDoubleFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 0.15 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 0.15 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( 'hltActivityGsfTrackVars','Dphi' ),
    candTag = cms.InputTag( "hltDiEle33CaloIdLGsfTrkIdVLDEtaDoubleFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltPreDoubleEle33CaloIdT = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltEG33CaloIdTHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.075 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( 0.1 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededPhotonHcalForHE" ),
    candTag = cms.InputTag( "hltEG33EtFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltEG33CaloIdTClusterShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 0.031 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 0.011 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededHLTClusterShape" ),
    candTag = cms.InputTag( "hltEG33CaloIdTHEFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltEle33CaloIdTPixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    saveTags = cms.bool( True ),
    doIsolated = cms.bool( True ),
    L1NonIsoCand = cms.InputTag( "" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "" ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    candTag = cms.InputTag( "hltEG33CaloIdTClusterShapeFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltL1SeededStartUpElectronPixelSeeds" )
)
process.hltDoubleEG33CaloIdTHEDoubleFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.075 ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    thrOverEEB = cms.double( 0.1 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( "hltActivityPhotonHcalForHE" ),
    candTag = cms.InputTag( "hltDoubleEG33EtDoubleFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltDoubleEG33CaloIdTClusterShapeDoubleFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 0.031 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 0.011 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( "hltActivityPhotonClusterShape" ),
    candTag = cms.InputTag( "hltDoubleEG33CaloIdTHEDoubleFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltDiEle33CaloIdTPixelMatchDoubleFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    saveTags = cms.bool( True ),
    doIsolated = cms.bool( True ),
    L1NonIsoCand = cms.InputTag( "" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "" ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 2 ),
    candTag = cms.InputTag( "hltDoubleEG33CaloIdTClusterShapeDoubleFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltActivityStartUpElectronPixelSeeds" )
)
process.hltL1sL1DoubleEG137 = cms.EDFilter( "HLTLevel1GTSeed",
    saveTags = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_DoubleEG_13_7" ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreEle17CaloIdTCaloIsoVLTrkIdVLTrkIsoVLEle8CaloIdTCaloIsoVLTrkIdVLTrkIsoVL = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltEGRegionalL1DoubleEG137 = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    saveTags = cms.bool( False ),
    endcap_end = cms.double( 2.65 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    barrel_end = cms.double( 1.4791 ),
    l1IsolatedTag = cms.InputTag( 'hltL1extraParticles','Isolated' ),
    candIsolatedTag = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    region_phi_size = cms.double( 1.044 ),
    region_eta_size = cms.double( 0.522 ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1DoubleEG137" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    candNonIsolatedTag = cms.InputTag( "" ),
    l1NonIsolatedTag = cms.InputTag( 'hltL1extraParticles','NonIsolated' )
)
process.hltEG17EtFilterDoubleEG137 = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( False ),
    L1NonIsoCand = cms.InputTag( "" ),
    relaxed = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    inputTag = cms.InputTag( "hltEGRegionalL1DoubleEG137" ),
    etcutEB = cms.double( 17.0 ),
    ncandcut = cms.int32( 1 ),
    etcutEE = cms.double( 17.0 )
)
process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoClusterShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 0.031 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 0.011 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededHLTClusterShape" ),
    candTag = cms.InputTag( "hltEG17EtFilterDoubleEG137" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltL1SeededPhotonEcalIsol = cms.EDProducer( "EgammaHLTEcalRecIsolationProducer",
    etMinEndcap = cms.double( 0.11 ),
    tryBoth = cms.bool( True ),
    ecalBarrelRecHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useNumCrystals = cms.bool( True ),
    etMinBarrel = cms.double( -9999.0 ),
    doRhoCorrection = cms.bool( False ),
    eMinEndcap = cms.double( -9999.0 ),
    intRadiusEndcap = cms.double( 3.0 ),
    jurassicWidth = cms.double( 3.0 ),
    useIsolEt = cms.bool( True ),
    ecalBarrelRecHitCollection = cms.InputTag( "EcalRecHitsEB" ),
    recoEcalCandidateProducer = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    eMinBarrel = cms.double( 0.095 ),
    effectiveAreaEndcap = cms.double( 0.046 ),
    ecalEndcapRecHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" ),
    extRadius = cms.double( 0.3 ),
    intRadiusBarrel = cms.double( 3.0 ),
    subtract = cms.bool( False ),
    rhoScale = cms.double( 1.0 ),
    effectiveAreaBarrel = cms.double( 0.101 ),
    ecalEndcapRecHitCollection = cms.InputTag( "EcalRecHitsEE" ),
    rhoProducer = cms.InputTag( 'hltKT6CaloJets','rho' )
)
process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoEcalIsoFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.2 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( 0.2 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededPhotonEcalIsol" ),
    candTag = cms.InputTag( "hltEle17TightIdLooseIsoEle8TightIdLooseIsoClusterShapeFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.1 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( 0.15 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededPhotonHcalForHE" ),
    candTag = cms.InputTag( "hltEle17TightIdLooseIsoEle8TightIdLooseIsoEcalIsoFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltL1SeededPhotonHcalIsol = cms.EDProducer( "EgammaHLTHcalIsolationProducersRegional",
    eMinHE = cms.double( 0.8 ),
    hbheRecHitProducer = cms.InputTag( "hltHbhereco" ),
    effectiveAreaBarrel = cms.double( 0.105 ),
    outerCone = cms.double( 0.29 ),
    eMinHB = cms.double( 0.7 ),
    innerCone = cms.double( 0.16 ),
    etMinHE = cms.double( -1.0 ),
    etMinHB = cms.double( -1.0 ),
    rhoProducer = cms.InputTag( 'hltKT6CaloJets','rho' ),
    depth = cms.int32( -1 ),
    doRhoCorrection = cms.bool( False ),
    effectiveAreaEndcap = cms.double( 0.17 ),
    recoEcalCandidateProducer = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    rhoMax = cms.double( 9.9999999E7 ),
    rhoScale = cms.double( 1.0 ),
    doEtSum = cms.bool( True )
)
process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoHcalIsoFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.2 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( 0.2 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededPhotonHcalIsol" ),
    candTag = cms.InputTag( "hltEle17TightIdLooseIsoEle8TightIdLooseIsoHEFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoPixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    saveTags = cms.bool( False ),
    doIsolated = cms.bool( True ),
    L1NonIsoCand = cms.InputTag( "" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "" ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    candTag = cms.InputTag( "hltEle17TightIdLooseIsoEle8TightIdLooseIsoHcalIsoFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltL1SeededStartUpElectronPixelSeeds" )
)
process.hltCkf3HitL1SeededTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltL1SeededStartUpElectronPixelSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "hltESPCkf3HitTrajectoryBuilder" )
)
process.hltCtf3HitL1SeededWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltCkf3HitL1SeededTrackCandidates" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    Propagator = cms.string( "PropagatorWithMaterial" )
)
process.hltPixelMatch3HitElectronsL1Seeded = cms.EDProducer( "EgammaHLTPixelMatchElectronProducers",
    BSProducer = cms.InputTag( "hltOnlineBeamSpot" ),
    UseGsfTracks = cms.bool( False ),
    TrackProducer = cms.InputTag( "hltCtf3HitL1SeededWithMaterialTracks" ),
    GsfTrackProducer = cms.InputTag( "" )
)
process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoOneOEMinusOneOPFilter = cms.EDFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    saveTags = cms.bool( False ),
    doIsolated = cms.bool( True ),
    electronNonIsolatedProducer = cms.InputTag( "" ),
    barrelcut = cms.double( 999.9 ),
    electronIsolatedProducer = cms.InputTag( "hltPixelMatch3HitElectronsL1Seeded" ),
    ncandcut = cms.int32( 1 ),
    candTag = cms.InputTag( "hltEle17TightIdLooseIsoEle8TightIdLooseIsoPixelMatchFilter" ),
    endcapcut = cms.double( 999.9 )
)
process.hlt3HitElectronL1SeededDetaDphi = cms.EDProducer( "EgammaHLTElectronDetaDphiProducer",
    variablesAtVtx = cms.bool( True ),
    useSCRefs = cms.bool( False ),
    BSProducer = cms.InputTag( "hltOnlineBeamSpot" ),
    electronProducer = cms.InputTag( "hltPixelMatch3HitElectronsL1Seeded" ),
    recoEcalCandidateProducer = cms.InputTag( "" ),
    useTrackProjectionToEcal = cms.bool( False )
)
process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoDetaFilter = cms.EDFilter( "HLTElectronGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    thrTimesPtEB = cms.double( -1.0 ),
    saveTags = cms.bool( False ),
    thrRegularEE = cms.double( 0.01 ),
    L1IsoCand = cms.InputTag( "hltPixelMatch3HitElectronsL1Seeded" ),
    thrRegularEB = cms.double( 0.01 ),
    lessThan = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( 'hlt3HitElectronL1SeededDetaDphi','Deta' ),
    candTag = cms.InputTag( "hltEle17TightIdLooseIsoEle8TightIdLooseIsoOneOEMinusOneOPFilter" ),
    thrTimesPtEE = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrOverPtEB = cms.double( -1.0 )
)
process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoDphiFilter = cms.EDFilter( "HLTElectronGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    thrTimesPtEB = cms.double( -1.0 ),
    saveTags = cms.bool( False ),
    thrRegularEE = cms.double( 0.1 ),
    L1IsoCand = cms.InputTag( "hltPixelMatch3HitElectronsL1Seeded" ),
    thrRegularEB = cms.double( 0.15 ),
    lessThan = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( 'hlt3HitElectronL1SeededDetaDphi','Dphi' ),
    candTag = cms.InputTag( "hltEle17TightIdLooseIsoEle8TightIdLooseIsoDetaFilter" ),
    thrTimesPtEE = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrOverPtEB = cms.double( -1.0 )
)
process.hltL1SeededEgammaRegionalPixelSeedGenerator = cms.EDProducer( "EgammaHLTRegionalPixelSeedGeneratorProducers",
    deltaPhiRegion = cms.double( 0.3 ),
    vertexZ = cms.double( 0.0 ),
    originHalfLength = cms.double( 15.0 ),
    BSProducer = cms.InputTag( "hltOnlineBeamSpot" ),
    UseZInVertex = cms.bool( False ),
    OrderedHitsFactoryPSet = cms.PSet( 
      maxElement = cms.uint32( 0 ),
      ComponentName = cms.string( "StandardHitPairGenerator" ),
      SeedingLayers = cms.string( "hltESPPixelLayerPairs" )
    ),
    deltaEtaRegion = cms.double( 0.3 ),
    ptMin = cms.double( 1.5 ),
    TTRHBuilder = cms.string( "WithTrackAngle" ),
    candTag = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    candTagEle = cms.InputTag( "pixelMatchElectrons" ),
    originRadius = cms.double( 0.02 )
)
process.hltL1SeededEgammaRegionalCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltL1SeededEgammaRegionalPixelSeedGenerator" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "hltESPCkfTrajectoryBuilder" )
)
process.hltL1SeededEgammaRegionalCTFFinalFitWithMaterial = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltL1SeededEgammaRegionalCkfTrackCandidates" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    alias = cms.untracked.string( "hltEgammaRegionalCTFFinalFitWithMaterial" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    Propagator = cms.string( "PropagatorWithMaterial" )
)
process.hltL1Seeded3HitElectronTrackIsol = cms.EDProducer( "EgammaHLTElectronTrackIsolationProducers",
    egTrkIsoStripEndcap = cms.double( 0.03 ),
    electronProducer = cms.InputTag( "hltPixelMatch3HitElectronsL1Seeded" ),
    egTrkIsoZSpan = cms.double( 0.15 ),
    useGsfTrack = cms.bool( False ),
    useSCRefs = cms.bool( False ),
    egTrkIsoConeSize = cms.double( 0.3 ),
    trackProducer = cms.InputTag( "hltL1SeededEgammaRegionalCTFFinalFitWithMaterial" ),
    egTrkIsoStripBarrel = cms.double( 0.03 ),
    egTrkIsoVetoConeSizeBarrel = cms.double( 0.03 ),
    egTrkIsoVetoConeSize = cms.double( 0.03 ),
    egTrkIsoRSpan = cms.double( 999999.0 ),
    egTrkIsoVetoConeSizeEndcap = cms.double( 0.03 ),
    recoEcalCandidateProducer = cms.InputTag( "" ),
    beamSpotProducer = cms.InputTag( "hltOnlineBeamSpot" ),
    egTrkIsoPtMin = cms.double( 1.0 ),
    egCheckForOtherEleInCone = cms.untracked.bool( False )
)
process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoTrackIsolFilter = cms.EDFilter( "HLTElectronGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    thrTimesPtEB = cms.double( -1.0 ),
    saveTags = cms.bool( True ),
    thrRegularEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltPixelMatch3HitElectronsL1Seeded" ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1Seeded3HitElectronTrackIsol" ),
    candTag = cms.InputTag( "hltEle17TightIdLooseIsoEle8TightIdLooseIsoOneOEMinusOneOPFilter" ),
    thrTimesPtEE = cms.double( -1.0 ),
    thrOverPtEE = cms.double( 0.2 ),
    thrOverPtEB = cms.double( 0.2 )
)
process.hltDoubleEG8EtFilterUnseeded = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( False ),
    L1NonIsoCand = cms.InputTag( "" ),
    relaxed = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    inputTag = cms.InputTag( "hltEcalActivitySuperClusterWrapper" ),
    etcutEB = cms.double( 8.0 ),
    ncandcut = cms.int32( 2 ),
    etcutEE = cms.double( 8.0 )
)
process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoClusterShapeDoubleFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 0.031 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 0.011 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( "hltActivityPhotonClusterShape" ),
    candTag = cms.InputTag( "hltDoubleEG8EtFilterUnseeded" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltActivityPhotonEcalIsol = cms.EDProducer( "EgammaHLTEcalRecIsolationProducer",
    etMinEndcap = cms.double( 0.11 ),
    tryBoth = cms.bool( True ),
    ecalBarrelRecHitProducer = cms.InputTag( "hltEcalRecHitAll" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useNumCrystals = cms.bool( True ),
    etMinBarrel = cms.double( -9999.0 ),
    doRhoCorrection = cms.bool( False ),
    eMinEndcap = cms.double( -9999.0 ),
    intRadiusEndcap = cms.double( 3.0 ),
    jurassicWidth = cms.double( 3.0 ),
    useIsolEt = cms.bool( True ),
    ecalBarrelRecHitCollection = cms.InputTag( "EcalRecHitsEB" ),
    recoEcalCandidateProducer = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    eMinBarrel = cms.double( 0.095 ),
    effectiveAreaEndcap = cms.double( 0.046 ),
    ecalEndcapRecHitProducer = cms.InputTag( "hltEcalRecHitAll" ),
    extRadius = cms.double( 0.3 ),
    intRadiusBarrel = cms.double( 3.0 ),
    subtract = cms.bool( False ),
    rhoScale = cms.double( 1.0 ),
    effectiveAreaBarrel = cms.double( 0.101 ),
    ecalEndcapRecHitCollection = cms.InputTag( "EcalRecHitsEE" ),
    rhoProducer = cms.InputTag( 'hltKT6CaloJets','rho' )
)
process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoEcalIsolDoubleFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.2 ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    thrOverEEB = cms.double( 0.2 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( "hltActivityPhotonEcalIsol" ),
    candTag = cms.InputTag( "hltEle17TightIdLooseIsoEle8TightIdLooseIsoClusterShapeDoubleFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoHEDoubleFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.1 ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    thrOverEEB = cms.double( 0.15 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( "hltActivityPhotonHcalForHE" ),
    candTag = cms.InputTag( "hltEle17TightIdLooseIsoEle8TightIdLooseIsoEcalIsolDoubleFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltActivityPhotonHcalIsol = cms.EDProducer( "EgammaHLTHcalIsolationProducersRegional",
    eMinHE = cms.double( 0.8 ),
    hbheRecHitProducer = cms.InputTag( "hltHbhereco" ),
    effectiveAreaBarrel = cms.double( 0.105 ),
    outerCone = cms.double( 0.29 ),
    eMinHB = cms.double( 0.7 ),
    innerCone = cms.double( 0.16 ),
    etMinHE = cms.double( -1.0 ),
    etMinHB = cms.double( -1.0 ),
    rhoProducer = cms.InputTag( 'hltKT6CaloJets','rho' ),
    depth = cms.int32( -1 ),
    doRhoCorrection = cms.bool( False ),
    effectiveAreaEndcap = cms.double( 0.17 ),
    recoEcalCandidateProducer = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    rhoMax = cms.double( 9.9999999E7 ),
    rhoScale = cms.double( 1.0 ),
    doEtSum = cms.bool( True )
)
process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoHcalIsolDoubleFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.2 ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    thrOverEEB = cms.double( 0.2 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( "hltActivityPhotonHcalIsol" ),
    candTag = cms.InputTag( "hltEle17TightIdLooseIsoEle8TightIdLooseIsoHEDoubleFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoPixelMatchDoubleFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    saveTags = cms.bool( False ),
    doIsolated = cms.bool( True ),
    L1NonIsoCand = cms.InputTag( "" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "" ),
    L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 2 ),
    candTag = cms.InputTag( "hltEle17TightIdLooseIsoEle8TightIdLooseIsoHcalIsolDoubleFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltActivityStartUpElectronPixelSeeds" )
)
process.hltCkf3HitActivityTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltActivityStartUpElectronPixelSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "hltESPCkf3HitTrajectoryBuilder" )
)
process.hltCtf3HitActivityWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltCkf3HitActivityTrackCandidates" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    Propagator = cms.string( "PropagatorWithMaterial" )
)
process.hltPixelMatch3HitElectronsActivity = cms.EDProducer( "EgammaHLTPixelMatchElectronProducers",
    BSProducer = cms.InputTag( "hltOnlineBeamSpot" ),
    UseGsfTracks = cms.bool( False ),
    TrackProducer = cms.InputTag( "hltCtf3HitActivityWithMaterialTracks" ),
    GsfTrackProducer = cms.InputTag( "" )
)
process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoOneOEMinusOneOPDoubleFilter = cms.EDFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    saveTags = cms.bool( False ),
    doIsolated = cms.bool( True ),
    electronNonIsolatedProducer = cms.InputTag( "" ),
    barrelcut = cms.double( 999.9 ),
    electronIsolatedProducer = cms.InputTag( "hltPixelMatch3HitElectronsActivity" ),
    ncandcut = cms.int32( 2 ),
    candTag = cms.InputTag( "hltEle17TightIdLooseIsoEle8TightIdLooseIsoPixelMatchDoubleFilter" ),
    endcapcut = cms.double( 999.9 )
)
process.hlt3HitElectronActivityDetaDphi = cms.EDProducer( "EgammaHLTElectronDetaDphiProducer",
    variablesAtVtx = cms.bool( True ),
    useSCRefs = cms.bool( False ),
    BSProducer = cms.InputTag( "hltOnlineBeamSpot" ),
    electronProducer = cms.InputTag( "hltPixelMatch3HitElectronsActivity" ),
    recoEcalCandidateProducer = cms.InputTag( "" ),
    useTrackProjectionToEcal = cms.bool( False )
)
process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoDetaDoubleFilter = cms.EDFilter( "HLTElectronGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    thrTimesPtEB = cms.double( -1.0 ),
    saveTags = cms.bool( False ),
    thrRegularEE = cms.double( 0.01 ),
    L1IsoCand = cms.InputTag( "hltPixelMatch3HitElectronsActivity" ),
    thrRegularEB = cms.double( 0.01 ),
    lessThan = cms.bool( True ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( 'hlt3HitElectronActivityDetaDphi','Deta' ),
    candTag = cms.InputTag( "hltEle17TightIdLooseIsoEle8TightIdLooseIsoOneOEMinusOneOPDoubleFilter" ),
    thrTimesPtEE = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrOverPtEB = cms.double( -1.0 )
)
process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoDphiDoubleFilter = cms.EDFilter( "HLTElectronGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    thrTimesPtEB = cms.double( -1.0 ),
    saveTags = cms.bool( False ),
    thrRegularEE = cms.double( 0.1 ),
    L1IsoCand = cms.InputTag( "hltPixelMatch3HitElectronsActivity" ),
    thrRegularEB = cms.double( 0.15 ),
    lessThan = cms.bool( True ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( 'hlt3HitElectronActivityDetaDphi','Dphi' ),
    candTag = cms.InputTag( "hltEle17TightIdLooseIsoEle8TightIdLooseIsoDetaDoubleFilter" ),
    thrTimesPtEE = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrOverPtEB = cms.double( -1.0 )
)
process.hltEcalActivityEgammaRegionalPixelSeedGenerator = cms.EDProducer( "EgammaHLTRegionalPixelSeedGeneratorProducers",
    deltaPhiRegion = cms.double( 0.3 ),
    vertexZ = cms.double( 0.0 ),
    originHalfLength = cms.double( 15.0 ),
    BSProducer = cms.InputTag( "hltOnlineBeamSpot" ),
    UseZInVertex = cms.bool( False ),
    OrderedHitsFactoryPSet = cms.PSet( 
      maxElement = cms.uint32( 0 ),
      ComponentName = cms.string( "StandardHitPairGenerator" ),
      SeedingLayers = cms.string( "hltESPPixelLayerPairs" )
    ),
    deltaEtaRegion = cms.double( 0.3 ),
    ptMin = cms.double( 1.5 ),
    TTRHBuilder = cms.string( "WithTrackAngle" ),
    candTag = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
    candTagEle = cms.InputTag( "pixelMatchElectrons" ),
    originRadius = cms.double( 0.02 )
)
process.hltEcalActivityEgammaRegionalCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltEcalActivityEgammaRegionalPixelSeedGenerator" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "hltESPCkfTrajectoryBuilder" )
)
process.hltEcalActivityEgammaRegionalCTFFinalFitWithMaterial = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltEcalActivityEgammaRegionalCkfTrackCandidates" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    alias = cms.untracked.string( "hltEcalActivityEgammaRegionalCTFFinalFitWithMaterial" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    Propagator = cms.string( "PropagatorWithMaterial" )
)
process.hlt3HitElectronActivityTrackIsol = cms.EDProducer( "EgammaHLTElectronTrackIsolationProducers",
    egTrkIsoStripEndcap = cms.double( 0.03 ),
    electronProducer = cms.InputTag( "hltPixelMatch3HitElectronsActivity" ),
    egTrkIsoZSpan = cms.double( 0.15 ),
    useGsfTrack = cms.bool( False ),
    useSCRefs = cms.bool( False ),
    egTrkIsoConeSize = cms.double( 0.3 ),
    trackProducer = cms.InputTag( "hltEcalActivityEgammaRegionalCTFFinalFitWithMaterial" ),
    egTrkIsoStripBarrel = cms.double( 0.03 ),
    egTrkIsoVetoConeSizeBarrel = cms.double( 0.03 ),
    egTrkIsoVetoConeSize = cms.double( 0.03 ),
    egTrkIsoRSpan = cms.double( 999999.0 ),
    egTrkIsoVetoConeSizeEndcap = cms.double( 0.03 ),
    recoEcalCandidateProducer = cms.InputTag( "" ),
    beamSpotProducer = cms.InputTag( "hltOnlineBeamSpot" ),
    egTrkIsoPtMin = cms.double( 1.0 ),
    egCheckForOtherEleInCone = cms.untracked.bool( False )
)
process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoTrackIsolDoubleFilter = cms.EDFilter( "HLTElectronGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    thrTimesPtEB = cms.double( -1.0 ),
    saveTags = cms.bool( True ),
    thrRegularEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltPixelMatch3HitElectronsActivity" ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( "hlt3HitElectronActivityTrackIsol" ),
    candTag = cms.InputTag( "hltEle17TightIdLooseIsoEle8TightIdLooseIsoOneOEMinusOneOPDoubleFilter" ),
    thrTimesPtEE = cms.double( -1.0 ),
    thrOverPtEE = cms.double( 0.2 ),
    thrOverPtEB = cms.double( 0.2 )
)
process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoTrackIsolDZ = cms.EDFilter( "HLT2ElectronElectronDZ",
    saveTags = cms.bool( True ),
    originTag1 = cms.InputTag( "hltOriginal1" ),
    originTag2 = cms.InputTag( "hltOriginal2" ),
    MinN = cms.int32( 1 ),
    triggerType1 = cms.int32( 82 ),
    triggerType2 = cms.int32( 82 ),
    MinDR = cms.double( -1.0 ),
    MaxDZ = cms.double( 0.2 ),
    inputTag1 = cms.InputTag( "hltEle17TightIdLooseIsoEle8TightIdLooseIsoTrackIsolDoubleFilter" ),
    inputTag2 = cms.InputTag( "hltEle17TightIdLooseIsoEle8TightIdLooseIsoTrackIsolDoubleFilter" )
)
process.hltL1sL1Mu3p5EG12 = cms.EDFilter( "HLTLevel1GTSeed",
    saveTags = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_Mu3p5_EG12" ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreMu22Photon22CaloIdL = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltL1Mu3p5EG12L1Filtered3p5 = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1Mu3p5EG12" ),
    MinPt = cms.double( 3.5 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltMuonDTDigis = cms.EDProducer( "DTUnpackingModule",
    useStandardFEDid = cms.bool( True ),
    inputLabel = cms.InputTag( "rawDataCollector" ),
    dataType = cms.string( "DDU" ),
    fedbyType = cms.bool( False ),
    readOutParameters = cms.PSet( 
      debug = cms.untracked.bool( False ),
      rosParameters = cms.PSet( 
        writeSC = cms.untracked.bool( True ),
        readingDDU = cms.untracked.bool( True ),
        performDataIntegrityMonitor = cms.untracked.bool( False ),
        readDDUIDfromDDU = cms.untracked.bool( True ),
        debug = cms.untracked.bool( False ),
        localDAQ = cms.untracked.bool( False )
      ),
      localDAQ = cms.untracked.bool( False ),
      performDataIntegrityMonitor = cms.untracked.bool( False )
    ),
    dqmOnly = cms.bool( False )
)
process.hltDt1DRecHits = cms.EDProducer( "DTRecHitProducer",
    debug = cms.untracked.bool( False ),
    recAlgoConfig = cms.PSet( 
      tTrigMode = cms.string( "DTTTrigSyncFromDB" ),
      minTime = cms.double( -3.0 ),
      stepTwoFromDigi = cms.bool( False ),
      doVdriftCorr = cms.bool( False ),
      debug = cms.untracked.bool( False ),
      maxTime = cms.double( 420.0 ),
      tTrigModeConfig = cms.PSet( 
        vPropWire = cms.double( 24.4 ),
        doTOFCorrection = cms.bool( True ),
        tofCorrType = cms.int32( 0 ),
        wirePropCorrType = cms.int32( 0 ),
        tTrigLabel = cms.string( "" ),
        doWirePropCorrection = cms.bool( True ),
        doT0Correction = cms.bool( True ),
        debug = cms.untracked.bool( False )
      )
    ),
    dtDigiLabel = cms.InputTag( "hltMuonDTDigis" ),
    recAlgo = cms.string( "DTLinearDriftFromDBAlgo" )
)
process.hltDt4DSegments = cms.EDProducer( "DTRecSegment4DProducer",
    debug = cms.untracked.bool( False ),
    Reco4DAlgoName = cms.string( "DTCombinatorialPatternReco4D" ),
    recHits2DLabel = cms.InputTag( "dt2DSegments" ),
    recHits1DLabel = cms.InputTag( "hltDt1DRecHits" ),
    Reco4DAlgoConfig = cms.PSet( 
      segmCleanerMode = cms.int32( 2 ),
      Reco2DAlgoName = cms.string( "DTCombinatorialPatternReco" ),
      recAlgoConfig = cms.PSet( 
        tTrigMode = cms.string( "DTTTrigSyncFromDB" ),
        minTime = cms.double( -3.0 ),
        stepTwoFromDigi = cms.bool( False ),
        doVdriftCorr = cms.bool( False ),
        debug = cms.untracked.bool( False ),
        maxTime = cms.double( 420.0 ),
        tTrigModeConfig = cms.PSet( 
          vPropWire = cms.double( 24.4 ),
          doTOFCorrection = cms.bool( True ),
          tofCorrType = cms.int32( 0 ),
          wirePropCorrType = cms.int32( 0 ),
          tTrigLabel = cms.string( "" ),
          doWirePropCorrection = cms.bool( True ),
          doT0Correction = cms.bool( True ),
          debug = cms.untracked.bool( False )
        )
      ),
      nSharedHitsMax = cms.int32( 2 ),
      hit_afterT0_resolution = cms.double( 0.03 ),
      Reco2DAlgoConfig = cms.PSet( 
        segmCleanerMode = cms.int32( 2 ),
        recAlgoConfig = cms.PSet( 
          tTrigMode = cms.string( "DTTTrigSyncFromDB" ),
          minTime = cms.double( -3.0 ),
          stepTwoFromDigi = cms.bool( False ),
          doVdriftCorr = cms.bool( False ),
          debug = cms.untracked.bool( False ),
          maxTime = cms.double( 420.0 ),
          tTrigModeConfig = cms.PSet( 
            vPropWire = cms.double( 24.4 ),
            doTOFCorrection = cms.bool( True ),
            tofCorrType = cms.int32( 0 ),
            wirePropCorrType = cms.int32( 0 ),
            tTrigLabel = cms.string( "" ),
            doWirePropCorrection = cms.bool( True ),
            doT0Correction = cms.bool( True ),
            debug = cms.untracked.bool( False )
          )
        ),
        nSharedHitsMax = cms.int32( 2 ),
        AlphaMaxPhi = cms.double( 1.0 ),
        hit_afterT0_resolution = cms.double( 0.03 ),
        MaxAllowedHits = cms.uint32( 50 ),
        performT0_vdriftSegCorrection = cms.bool( False ),
        AlphaMaxTheta = cms.double( 0.9 ),
        debug = cms.untracked.bool( False ),
        recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
        nUnSharedHitsMin = cms.int32( 2 ),
        performT0SegCorrection = cms.bool( False ),
        perform_delta_rejecting = cms.bool( False )
      ),
      performT0_vdriftSegCorrection = cms.bool( False ),
      debug = cms.untracked.bool( False ),
      recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
      nUnSharedHitsMin = cms.int32( 2 ),
      AllDTRecHits = cms.bool( True ),
      performT0SegCorrection = cms.bool( False ),
      perform_delta_rejecting = cms.bool( False )
    )
)
process.hltMuonCSCDigis = cms.EDProducer( "CSCDCCUnpacker",
    PrintEventNumber = cms.untracked.bool( False ),
    UseSelectiveUnpacking = cms.bool( True ),
    UseExaminer = cms.bool( True ),
    ErrorMask = cms.uint32( 0x0 ),
    InputObjects = cms.InputTag( "rawDataCollector" ),
    UseFormatStatus = cms.bool( True ),
    ExaminerMask = cms.uint32( 0x1febf3f6 ),
    UnpackStatusDigis = cms.bool( False ),
    VisualFEDInspect = cms.untracked.bool( False ),
    FormatedEventDump = cms.untracked.bool( False ),
    Debug = cms.untracked.bool( False ),
    VisualFEDShort = cms.untracked.bool( False )
)
process.hltCsc2DRecHits = cms.EDProducer( "CSCRecHitDProducer",
    XTasymmetry_ME1b = cms.double( 0.0 ),
    XTasymmetry_ME1a = cms.double( 0.0 ),
    ConstSyst_ME1a = cms.double( 0.022 ),
    ConstSyst_ME1b = cms.double( 0.0070 ),
    XTasymmetry_ME41 = cms.double( 0.0 ),
    CSCStripxtalksOffset = cms.double( 0.03 ),
    CSCUseCalibrations = cms.bool( True ),
    CSCUseTimingCorrections = cms.bool( True ),
    CSCNoOfTimeBinsForDynamicPedestal = cms.int32( 2 ),
    XTasymmetry_ME22 = cms.double( 0.0 ),
    UseFivePoleFit = cms.bool( True ),
    XTasymmetry_ME21 = cms.double( 0.0 ),
    ConstSyst_ME21 = cms.double( 0.0 ),
    CSCDebug = cms.untracked.bool( False ),
    ConstSyst_ME22 = cms.double( 0.0 ),
    CSCUseGasGainCorrections = cms.bool( False ),
    XTasymmetry_ME31 = cms.double( 0.0 ),
    readBadChambers = cms.bool( True ),
    NoiseLevel_ME13 = cms.double( 8.0 ),
    NoiseLevel_ME12 = cms.double( 9.0 ),
    NoiseLevel_ME32 = cms.double( 9.0 ),
    NoiseLevel_ME31 = cms.double( 9.0 ),
    XTasymmetry_ME32 = cms.double( 0.0 ),
    ConstSyst_ME41 = cms.double( 0.0 ),
    CSCStripClusterSize = cms.untracked.int32( 3 ),
    CSCStripClusterChargeCut = cms.double( 25.0 ),
    CSCStripPeakThreshold = cms.double( 10.0 ),
    readBadChannels = cms.bool( True ),
    UseParabolaFit = cms.bool( False ),
    XTasymmetry_ME13 = cms.double( 0.0 ),
    XTasymmetry_ME12 = cms.double( 0.0 ),
    wireDigiTag = cms.InputTag( 'hltMuonCSCDigis','MuonCSCWireDigi' ),
    ConstSyst_ME12 = cms.double( 0.0 ),
    ConstSyst_ME13 = cms.double( 0.0 ),
    ConstSyst_ME32 = cms.double( 0.0 ),
    ConstSyst_ME31 = cms.double( 0.0 ),
    UseAverageTime = cms.bool( False ),
    NoiseLevel_ME1a = cms.double( 7.0 ),
    NoiseLevel_ME1b = cms.double( 8.0 ),
    CSCWireClusterDeltaT = cms.int32( 1 ),
    CSCUseStaticPedestals = cms.bool( False ),
    stripDigiTag = cms.InputTag( 'hltMuonCSCDigis','MuonCSCStripDigi' ),
    CSCstripWireDeltaTime = cms.int32( 8 ),
    NoiseLevel_ME21 = cms.double( 9.0 ),
    NoiseLevel_ME22 = cms.double( 9.0 ),
    NoiseLevel_ME41 = cms.double( 9.0 )
)
process.hltCscSegments = cms.EDProducer( "CSCSegmentProducer",
    inputObjects = cms.InputTag( "hltCsc2DRecHits" ),
    algo_psets = cms.VPSet( 
      cms.PSet(  chamber_types = cms.vstring( 'ME1/a',
  'ME1/b',
  'ME1/2',
  'ME1/3',
  'ME2/1',
  'ME2/2',
  'ME3/1',
  'ME3/2',
  'ME4/1',
  'ME4/2' ),
        algo_name = cms.string( "CSCSegAlgoST" ),
        parameters_per_chamber_type = cms.vint32( 2, 1, 1, 1, 1, 1, 1, 1, 1, 1 ),
        algo_psets = cms.VPSet( 
          cms.PSet(  maxRatioResidualPrune = cms.double( 3.0 ),
            yweightPenalty = cms.double( 1.5 ),
            maxRecHitsInCluster = cms.int32( 20 ),
            dPhiFineMax = cms.double( 0.025 ),
            preClusteringUseChaining = cms.bool( True ),
            ForceCovariance = cms.bool( False ),
            hitDropLimit6Hits = cms.double( 0.3333 ),
            NormChi2Cut2D = cms.double( 20.0 ),
            BPMinImprovement = cms.double( 10000.0 ),
            Covariance = cms.double( 0.0 ),
            tanPhiMax = cms.double( 0.5 ),
            SeedBig = cms.double( 0.0015 ),
            onlyBestSegment = cms.bool( False ),
            dRPhiFineMax = cms.double( 8.0 ),
            SeedSmall = cms.double( 2.0E-4 ),
            curvePenalty = cms.double( 2.0 ),
            dXclusBoxMax = cms.double( 4.0 ),
            BrutePruning = cms.bool( True ),
            curvePenaltyThreshold = cms.double( 0.85 ),
            CorrectTheErrors = cms.bool( True ),
            hitDropLimit4Hits = cms.double( 0.6 ),
            useShowering = cms.bool( False ),
            CSCDebug = cms.untracked.bool( False ),
            tanThetaMax = cms.double( 1.2 ),
            NormChi2Cut3D = cms.double( 10.0 ),
            minHitsPerSegment = cms.int32( 3 ),
            ForceCovarianceAll = cms.bool( False ),
            yweightPenaltyThreshold = cms.double( 1.0 ),
            prePrunLimit = cms.double( 3.17 ),
            hitDropLimit5Hits = cms.double( 0.8 ),
            preClustering = cms.bool( True ),
            prePrun = cms.bool( True ),
            maxDPhi = cms.double( 999.0 ),
            maxDTheta = cms.double( 999.0 ),
            Pruning = cms.bool( True ),
            dYclusBoxMax = cms.double( 8.0 )
          ),
          cms.PSet(  maxRatioResidualPrune = cms.double( 3.0 ),
            yweightPenalty = cms.double( 1.5 ),
            maxRecHitsInCluster = cms.int32( 24 ),
            dPhiFineMax = cms.double( 0.025 ),
            preClusteringUseChaining = cms.bool( True ),
            ForceCovariance = cms.bool( False ),
            hitDropLimit6Hits = cms.double( 0.3333 ),
            NormChi2Cut2D = cms.double( 20.0 ),
            BPMinImprovement = cms.double( 10000.0 ),
            Covariance = cms.double( 0.0 ),
            tanPhiMax = cms.double( 0.5 ),
            SeedBig = cms.double( 0.0015 ),
            onlyBestSegment = cms.bool( False ),
            dRPhiFineMax = cms.double( 8.0 ),
            SeedSmall = cms.double( 2.0E-4 ),
            curvePenalty = cms.double( 2.0 ),
            dXclusBoxMax = cms.double( 4.0 ),
            BrutePruning = cms.bool( True ),
            curvePenaltyThreshold = cms.double( 0.85 ),
            CorrectTheErrors = cms.bool( True ),
            hitDropLimit4Hits = cms.double( 0.6 ),
            useShowering = cms.bool( False ),
            CSCDebug = cms.untracked.bool( False ),
            tanThetaMax = cms.double( 1.2 ),
            NormChi2Cut3D = cms.double( 10.0 ),
            minHitsPerSegment = cms.int32( 3 ),
            ForceCovarianceAll = cms.bool( False ),
            yweightPenaltyThreshold = cms.double( 1.0 ),
            prePrunLimit = cms.double( 3.17 ),
            hitDropLimit5Hits = cms.double( 0.8 ),
            preClustering = cms.bool( True ),
            prePrun = cms.bool( True ),
            maxDPhi = cms.double( 999.0 ),
            maxDTheta = cms.double( 999.0 ),
            Pruning = cms.bool( True ),
            dYclusBoxMax = cms.double( 8.0 )
          )
        )
      )
    ),
    algo_type = cms.int32( 1 )
)
process.hltMuonRPCDigis = cms.EDProducer( "RPCUnpackingModule",
    InputLabel = cms.InputTag( "rawDataCollector" ),
    doSynchro = cms.bool( False )
)
process.hltRpcRecHits = cms.EDProducer( "RPCRecHitProducer",
    recAlgoConfig = cms.PSet(  ),
    deadvecfile = cms.FileInPath( "RecoLocalMuon/RPCRecHit/data/RPCDeadVec.dat" ),
    rpcDigiLabel = cms.InputTag( "hltMuonRPCDigis" ),
    maskvecfile = cms.FileInPath( "RecoLocalMuon/RPCRecHit/data/RPCMaskVec.dat" ),
    recAlgo = cms.string( "RPCRecHitStandardAlgo" ),
    deadSource = cms.string( "File" ),
    maskSource = cms.string( "File" )
)
process.hltL2OfflineMuonSeeds = cms.EDProducer( "MuonSeedGenerator",
    SMB_21 = cms.vdouble( 1.043, -0.124, 0.0, 0.183, 0.0, 0.0 ),
    SMB_20 = cms.vdouble( 1.011, -0.052, 0.0, 0.188, 0.0, 0.0 ),
    SMB_22 = cms.vdouble( 1.474, -0.758, 0.0, 0.185, 0.0, 0.0 ),
    OL_2213 = cms.vdouble( 0.117, 0.0, 0.0, 0.044, 0.0, 0.0 ),
    SME_11 = cms.vdouble( 3.295, -1.527, 0.112, 0.378, 0.02, 0.0 ),
    SME_13 = cms.vdouble( -1.286, 1.711, 0.0, 0.356, 0.0, 0.0 ),
    SME_12 = cms.vdouble( 0.102, 0.599, 0.0, 0.38, 0.0, 0.0 ),
    DT_34_2_scale = cms.vdouble( -11.901897, 0.0 ),
    OL_1213_0_scale = cms.vdouble( -4.488158, 0.0 ),
    OL_1222_0_scale = cms.vdouble( -5.810449, 0.0 ),
    DT_13 = cms.vdouble( 0.315, 0.068, -0.127, 0.051, -0.0020, 0.0 ),
    DT_12 = cms.vdouble( 0.183, 0.054, -0.087, 0.028, 0.0020, 0.0 ),
    DT_14 = cms.vdouble( 0.359, 0.052, -0.107, 0.072, -0.0040, 0.0 ),
    CSC_13_3_scale = cms.vdouble( -1.701268, 0.0 ),
    DT_24_2_scale = cms.vdouble( -6.63094, 0.0 ),
    CSC_23 = cms.vdouble( -0.081, 0.113, -0.029, 0.015, 0.0080, 0.0 ),
    CSC_24 = cms.vdouble( 0.0040, 0.021, -0.0020, 0.053, 0.0, 0.0 ),
    OL_2222 = cms.vdouble( 0.107, 0.0, 0.0, 0.04, 0.0, 0.0 ),
    DT_14_2_scale = cms.vdouble( -4.808546, 0.0 ),
    SMB_10 = cms.vdouble( 1.387, -0.038, 0.0, 0.19, 0.0, 0.0 ),
    SMB_11 = cms.vdouble( 1.247, 0.72, -0.802, 0.229, -0.075, 0.0 ),
    SMB_12 = cms.vdouble( 2.128, -0.956, 0.0, 0.199, 0.0, 0.0 ),
    SME_21 = cms.vdouble( -0.529, 1.194, -0.358, 0.472, 0.086, 0.0 ),
    SME_22 = cms.vdouble( -1.207, 1.491, -0.251, 0.189, 0.243, 0.0 ),
    DT_13_2_scale = cms.vdouble( -4.257687, 0.0 ),
    CSC_34 = cms.vdouble( 0.062, -0.067, 0.019, 0.021, 0.0030, 0.0 ),
    SME_22_0_scale = cms.vdouble( -3.457901, 0.0 ),
    DT_24_1_scale = cms.vdouble( -7.490909, 0.0 ),
    OL_1232_0_scale = cms.vdouble( -5.964634, 0.0 ),
    DT_23_1_scale = cms.vdouble( -5.320346, 0.0 ),
    SME_13_0_scale = cms.vdouble( 0.104905, 0.0 ),
    SMB_22_0_scale = cms.vdouble( 1.346681, 0.0 ),
    CSC_12_1_scale = cms.vdouble( -6.434242, 0.0 ),
    DT_34 = cms.vdouble( 0.044, 0.0040, -0.013, 0.029, 0.0030, 0.0 ),
    SME_32 = cms.vdouble( -0.901, 1.333, -0.47, 0.41, 0.073, 0.0 ),
    SME_31 = cms.vdouble( -1.594, 1.482, -0.317, 0.487, 0.097, 0.0 ),
    CSC_13_2_scale = cms.vdouble( -6.077936, 0.0 ),
    crackEtas = cms.vdouble( 0.2, 1.6, 1.7 ),
    SME_11_0_scale = cms.vdouble( 1.325085, 0.0 ),
    SMB_20_0_scale = cms.vdouble( 1.486168, 0.0 ),
    DT_13_1_scale = cms.vdouble( -4.520923, 0.0 ),
    CSC_24_1_scale = cms.vdouble( -6.055701, 0.0 ),
    CSC_01_1_scale = cms.vdouble( -1.915329, 0.0 ),
    DT_23 = cms.vdouble( 0.13, 0.023, -0.057, 0.028, 0.0040, 0.0 ),
    DT_24 = cms.vdouble( 0.176, 0.014, -0.051, 0.051, 0.0030, 0.0 ),
    SMB_12_0_scale = cms.vdouble( 2.283221, 0.0 ),
    SMB_30_0_scale = cms.vdouble( -3.629838, 0.0 ),
    SME_42 = cms.vdouble( -0.0030, 0.0050, 0.0050, 0.608, 0.076, 0.0 ),
    SME_41 = cms.vdouble( -0.0030, 0.0050, 0.0050, 0.608, 0.076, 0.0 ),
    CSC_12_2_scale = cms.vdouble( -1.63622, 0.0 ),
    DT_34_1_scale = cms.vdouble( -13.783765, 0.0 ),
    CSC_34_1_scale = cms.vdouble( -11.520507, 0.0 ),
    OL_2213_0_scale = cms.vdouble( -7.239789, 0.0 ),
    SMB_32_0_scale = cms.vdouble( -3.054156, 0.0 ),
    CSC_12_3_scale = cms.vdouble( -1.63622, 0.0 ),
    SME_21_0_scale = cms.vdouble( -0.040862, 0.0 ),
    OL_1232 = cms.vdouble( 0.184, 0.0, 0.0, 0.066, 0.0, 0.0 ),
    DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
    SMB_10_0_scale = cms.vdouble( 2.448566, 0.0 ),
    EnableDTMeasurement = cms.bool( True ),
    CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
    CSC_23_2_scale = cms.vdouble( -6.079917, 0.0 ),
    scaleDT = cms.bool( True ),
    DT_12_2_scale = cms.vdouble( -3.518165, 0.0 ),
    OL_1222 = cms.vdouble( 0.848, -0.591, 0.0, 0.062, 0.0, 0.0 ),
    CSC_23_1_scale = cms.vdouble( -19.084285, 0.0 ),
    OL_1213 = cms.vdouble( 0.96, -0.737, 0.0, 0.052, 0.0, 0.0 ),
    CSC_02 = cms.vdouble( 0.612, -0.207, 0.0, 0.067, -0.0010, 0.0 ),
    CSC_03 = cms.vdouble( 0.787, -0.338, 0.029, 0.101, -0.0080, 0.0 ),
    CSC_01 = cms.vdouble( 0.166, 0.0, 0.0, 0.031, 0.0, 0.0 ),
    SMB_32 = cms.vdouble( 0.67, -0.327, 0.0, 0.22, 0.0, 0.0 ),
    SMB_30 = cms.vdouble( 0.505, -0.022, 0.0, 0.215, 0.0, 0.0 ),
    SMB_31 = cms.vdouble( 0.549, -0.145, 0.0, 0.207, 0.0, 0.0 ),
    crackWindow = cms.double( 0.04 ),
    CSC_14_3_scale = cms.vdouble( -1.969563, 0.0 ),
    SMB_31_0_scale = cms.vdouble( -3.323768, 0.0 ),
    DT_12_1_scale = cms.vdouble( -3.692398, 0.0 ),
    SMB_21_0_scale = cms.vdouble( 1.58384, 0.0 ),
    DT_23_2_scale = cms.vdouble( -5.117625, 0.0 ),
    SME_12_0_scale = cms.vdouble( 2.279181, 0.0 ),
    DT_14_1_scale = cms.vdouble( -5.644816, 0.0 ),
    beamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    SMB_11_0_scale = cms.vdouble( 2.56363, 0.0 ),
    EnableCSCMeasurement = cms.bool( True ),
    CSC_14 = cms.vdouble( 0.606, -0.181, -0.0020, 0.111, -0.0030, 0.0 ),
    OL_2222_0_scale = cms.vdouble( -7.667231, 0.0 ),
    CSC_13 = cms.vdouble( 0.901, -1.302, 0.533, 0.045, 0.0050, 0.0 ),
    CSC_12 = cms.vdouble( -0.161, 0.254, -0.047, 0.042, -0.0070, 0.0 )
)
process.hltL2MuonSeeds = cms.EDProducer( "L2MuonSeedGenerator",
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'SteppingHelixPropagatorAny' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    InputObjects = cms.InputTag( "hltL1extraParticles" ),
    L1MaxEta = cms.double( 2.5 ),
    OfflineSeedLabel = cms.untracked.InputTag( "hltL2OfflineMuonSeeds" ),
    L1MinPt = cms.double( 0.0 ),
    L1MinQuality = cms.uint32( 1 ),
    GMTReadoutCollection = cms.InputTag( "hltGtDigis" ),
    UseOfflineSeed = cms.untracked.bool( True ),
    Propagator = cms.string( "SteppingHelixPropagatorAny" )
)
process.hltL2Muons = cms.EDProducer( "L2MuonProducer",
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny',
        'hltESPFastSteppingHelixPropagatorOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    InputObjects = cms.InputTag( "hltL2MuonSeeds" ),
    SeedTransformerParameters = cms.PSet( 
      Fitter = cms.string( "hltESPKFFittingSmootherForL2Muon" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      NMinRecHits = cms.uint32( 2 ),
      UseSubRecHits = cms.bool( False ),
      Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
      RescaleError = cms.double( 100.0 )
    ),
    L2TrajBuilderParameters = cms.PSet( 
      DoRefit = cms.bool( False ),
      SeedPropagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
      FilterParameters = cms.PSet( 
        NumberOfSigma = cms.double( 3.0 ),
        FitDirection = cms.string( "insideOut" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        MaxChi2 = cms.double( 1000.0 ),
        MuonTrajectoryUpdatorParameters = cms.PSet( 
          MaxChi2 = cms.double( 25.0 ),
          RescaleErrorFactor = cms.double( 100.0 ),
          Granularity = cms.int32( 0 ),
          ExcludeRPCFromFit = cms.bool( False ),
          UseInvalidHits = cms.bool( True ),
          RescaleError = cms.bool( False )
        ),
        EnableRPCMeasurement = cms.bool( True ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        EnableDTMeasurement = cms.bool( True ),
        RPCRecSegmentLabel = cms.InputTag( "hltRpcRecHits" ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
        EnableCSCMeasurement = cms.bool( True )
      ),
      NavigationType = cms.string( "Standard" ),
      SeedTransformerParameters = cms.PSet( 
        Fitter = cms.string( "hltESPKFFittingSmootherForL2Muon" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        NMinRecHits = cms.uint32( 2 ),
        UseSubRecHits = cms.bool( False ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
        RescaleError = cms.double( 100.0 )
      ),
      DoBackwardFilter = cms.bool( True ),
      SeedPosition = cms.string( "in" ),
      BWFilterParameters = cms.PSet( 
        NumberOfSigma = cms.double( 3.0 ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        FitDirection = cms.string( "outsideIn" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        MaxChi2 = cms.double( 100.0 ),
        MuonTrajectoryUpdatorParameters = cms.PSet( 
          MaxChi2 = cms.double( 25.0 ),
          RescaleErrorFactor = cms.double( 100.0 ),
          Granularity = cms.int32( 2 ),
          ExcludeRPCFromFit = cms.bool( False ),
          UseInvalidHits = cms.bool( True ),
          RescaleError = cms.bool( False )
        ),
        EnableRPCMeasurement = cms.bool( True ),
        BWSeedType = cms.string( "fromGenerator" ),
        EnableDTMeasurement = cms.bool( True ),
        RPCRecSegmentLabel = cms.InputTag( "hltRpcRecHits" ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
        EnableCSCMeasurement = cms.bool( True )
      ),
      DoSeedRefit = cms.bool( False )
    ),
    DoSeedRefit = cms.bool( False ),
    TrackLoaderParameters = cms.PSet( 
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      DoSmoothing = cms.bool( False ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      MuonUpdatorAtVertexParameters = cms.PSet( 
        MaxChi2 = cms.double( 1000000.0 ),
        BeamSpotPosition = cms.vdouble( 0.0, 0.0, 0.0 ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
      ),
      VertexConstraint = cms.bool( True )
    )
)
process.hltL2MuonCandidates = cms.EDProducer( "L2MuonCandidateProducer",
    InputObjects = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
process.hltL1Mu3p5EG12L2Filtered12 = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltL1Mu3p5EG12L1Filtered3p5" ),
    MinPt = cms.double( 12.0 ),
    MinN = cms.int32( 1 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltL3TrajSeedOIState = cms.EDProducer( "TSGFromL2Muon",
    TkSeedGenerator = cms.PSet( 
      propagatorCompatibleName = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
      option = cms.uint32( 3 ),
      maxChi2 = cms.double( 40.0 ),
      errorMatrixPset = cms.PSet( 
        atIP = cms.bool( True ),
        action = cms.string( "use" ),
        errorMatrixValuesPSet = cms.PSet( 
          pf3_V12 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V13 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V11 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          pf3_V14 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V15 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          yAxis = cms.vdouble( 0.0, 1.0, 1.4, 10.0 ),
          pf3_V33 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          zAxis = cms.vdouble( -3.14159, 3.14159 ),
          pf3_V44 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          xAxis = cms.vdouble( 0.0, 13.0, 30.0, 70.0, 1000.0 ),
          pf3_V22 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          pf3_V23 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V45 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V55 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          pf3_V34 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V35 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V25 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V24 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          )
        )
      ),
      propagatorName = cms.string( "hltESPSteppingHelixPropagatorAlong" ),
      manySeeds = cms.bool( False ),
      copyMuonRecHit = cms.bool( False ),
      ComponentName = cms.string( "TSGForRoadSearch" )
    ),
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'hltESPSteppingHelixPropagatorOpposite',
        'hltESPSteppingHelixPropagatorAlong' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' ),
    MuonTrackingRegionBuilder = cms.PSet(  ),
    PCut = cms.double( 2.5 ),
    TrackerSeedCleaner = cms.PSet(  ),
    PtCut = cms.double( 1.0 )
)
process.hltL3TrackCandidateFromL2OIState = cms.EDProducer( "CkfTrajectoryMaker",
    src = cms.InputTag( "hltL3TrajSeedOIState" ),
    reverseTrajectories = cms.bool( True ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    trackCandidateAlso = cms.bool( True ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "hltESPMuonCkfTrajectoryBuilderSeedHit" ),
    maxNSeeds = cms.uint32( 100000 )
)
process.hltL3TkTracksFromL2OIState = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltL3TrackCandidateFromL2OIState" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    alias = cms.untracked.string( "" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    Propagator = cms.string( "PropagatorWithMaterial" )
)
process.hltL3MuonsOIState = cms.EDProducer( "L3MuonProducer",
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'hltESPSmartPropagatorAny',
        'SteppingHelixPropagatorAny',
        'hltESPSmartPropagator',
        'hltESPSteppingHelixPropagatorOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    L3TrajBuilderParameters = cms.PSet( 
      ScaleTECyFactor = cms.double( -1.0 ),
      GlbRefitterParameters = cms.PSet( 
        TrackerSkipSection = cms.int32( -1 ),
        DoPredictionsOnly = cms.bool( False ),
        PropDirForCosmics = cms.bool( False ),
        HitThreshold = cms.int32( 1 ),
        MuonHitsOption = cms.int32( 1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        Chi2CutCSC = cms.double( 150.0 ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        SkipStation = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        TrackerSkipSystem = cms.int32( -1 ),
        DYTthrs = cms.vint32( 30, 15 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      MuonTrackingRegionBuilder = cms.PSet( 
        EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
        EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
        OnDemand = cms.double( -1.0 ),
        Rescale_Dz = cms.double( 3.0 ),
        vertexCollection = cms.InputTag( "pixelVertices" ),
        Rescale_phi = cms.double( 3.0 ),
        Eta_fixed = cms.double( 0.2 ),
        DeltaZ_Region = cms.double( 15.9 ),
        MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
        PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
        Eta_min = cms.double( 0.05 ),
        Phi_fixed = cms.double( 0.2 ),
        DeltaR = cms.double( 0.2 ),
        EscapePt = cms.double( 1.5 ),
        UseFixedRegion = cms.bool( False ),
        PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
        Rescale_eta = cms.double( 3.0 ),
        Phi_min = cms.double( 0.05 ),
        UseVertex = cms.bool( False ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" )
      ),
      RefitRPCHits = cms.bool( True ),
      PCut = cms.double( 2.5 ),
      TrackTransformer = cms.PSet( 
        DoPredictionsOnly = cms.bool( False ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" )
      ),
      GlobalMuonTrackMatcher = cms.PSet( 
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        MinP = cms.double( 2.5 ),
        MinPt = cms.double( 1.0 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Pt_threshold2 = cms.double( 9.99999999E8 ),
        LocChi2Cut = cms.double( 0.0010 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_3 = cms.double( 7.0 ),
        Quality_2 = cms.double( 15.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        Quality_1 = cms.double( 20.0 )
      ),
      PtCut = cms.double( 1.0 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      tkTrajLabel = cms.InputTag( "hltL3TkTracksFromL2OIState" )
    ),
    TrackLoaderParameters = cms.PSet( 
      PutTkTrackIntoEvent = cms.untracked.bool( False ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      SmoothTkTrack = cms.untracked.bool( False ),
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      MuonUpdatorAtVertexParameters = cms.PSet( 
        MaxChi2 = cms.double( 1000000.0 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
      ),
      VertexConstraint = cms.bool( False ),
      DoSmoothing = cms.bool( True )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
process.hltL3TrajSeedOIHit = cms.EDProducer( "TSGFromL2Muon",
    TkSeedGenerator = cms.PSet( 
      PSetNames = cms.vstring( 'skipTSG',
        'iterativeTSG' ),
      L3TkCollectionA = cms.InputTag( "hltL3MuonsOIState" ),
      iterativeTSG = cms.PSet( 
        ErrorRescaling = cms.double( 3.0 ),
        beamSpot = cms.InputTag( "offlineBeamSpot" ),
        MaxChi2 = cms.double( 40.0 ),
        errorMatrixPset = cms.PSet( 
          atIP = cms.bool( True ),
          action = cms.string( "use" ),
          errorMatrixValuesPSet = cms.PSet( 
            pf3_V12 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V13 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V11 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
            ),
            pf3_V14 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V15 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            yAxis = cms.vdouble( 0.0, 1.0, 1.4, 10.0 ),
            pf3_V33 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
            ),
            zAxis = cms.vdouble( -3.14159, 3.14159 ),
            pf3_V44 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
            ),
            xAxis = cms.vdouble( 0.0, 13.0, 30.0, 70.0, 1000.0 ),
            pf3_V22 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
            ),
            pf3_V23 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V45 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V55 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
            ),
            pf3_V34 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V35 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V25 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V24 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            )
          )
        ),
        UpdateState = cms.bool( True ),
        MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
        SelectState = cms.bool( False ),
        SigmaZ = cms.double( 25.0 ),
        ResetMethod = cms.string( "matrix" ),
        ComponentName = cms.string( "TSGFromPropagation" ),
        UseVertexState = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAnyOpposite" )
      ),
      skipTSG = cms.PSet(  ),
      ComponentName = cms.string( "DualByL2TSG" )
    ),
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'PropagatorWithMaterial',
        'hltESPSmartPropagatorAnyOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' ),
    MuonTrackingRegionBuilder = cms.PSet(  ),
    PCut = cms.double( 2.5 ),
    TrackerSeedCleaner = cms.PSet( 
      cleanerFromSharedHits = cms.bool( True ),
      ptCleaner = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      directionCleaner = cms.bool( True )
    ),
    PtCut = cms.double( 1.0 )
)
process.hltL3TrackCandidateFromL2OIHit = cms.EDProducer( "CkfTrajectoryMaker",
    src = cms.InputTag( "hltL3TrajSeedOIHit" ),
    reverseTrajectories = cms.bool( True ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    trackCandidateAlso = cms.bool( True ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "hltESPMuonCkfTrajectoryBuilder" ),
    maxNSeeds = cms.uint32( 100000 )
)
process.hltL3TkTracksFromL2OIHit = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltL3TrackCandidateFromL2OIHit" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    alias = cms.untracked.string( "" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    Propagator = cms.string( "PropagatorWithMaterial" )
)
process.hltL3MuonsOIHit = cms.EDProducer( "L3MuonProducer",
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'hltESPSmartPropagatorAny',
        'SteppingHelixPropagatorAny',
        'hltESPSmartPropagator',
        'hltESPSteppingHelixPropagatorOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    L3TrajBuilderParameters = cms.PSet( 
      ScaleTECyFactor = cms.double( -1.0 ),
      GlbRefitterParameters = cms.PSet( 
        TrackerSkipSection = cms.int32( -1 ),
        DoPredictionsOnly = cms.bool( False ),
        PropDirForCosmics = cms.bool( False ),
        HitThreshold = cms.int32( 1 ),
        MuonHitsOption = cms.int32( 1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        Chi2CutCSC = cms.double( 150.0 ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        SkipStation = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        TrackerSkipSystem = cms.int32( -1 ),
        DYTthrs = cms.vint32( 30, 15 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      MuonTrackingRegionBuilder = cms.PSet( 
        EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
        EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
        OnDemand = cms.double( -1.0 ),
        Rescale_Dz = cms.double( 3.0 ),
        vertexCollection = cms.InputTag( "pixelVertices" ),
        Rescale_phi = cms.double( 3.0 ),
        Eta_fixed = cms.double( 0.2 ),
        DeltaZ_Region = cms.double( 15.9 ),
        MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
        PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
        Eta_min = cms.double( 0.05 ),
        Phi_fixed = cms.double( 0.2 ),
        DeltaR = cms.double( 0.2 ),
        EscapePt = cms.double( 1.5 ),
        UseFixedRegion = cms.bool( False ),
        PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
        Rescale_eta = cms.double( 3.0 ),
        Phi_min = cms.double( 0.05 ),
        UseVertex = cms.bool( False ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" )
      ),
      RefitRPCHits = cms.bool( True ),
      PCut = cms.double( 2.5 ),
      TrackTransformer = cms.PSet( 
        DoPredictionsOnly = cms.bool( False ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" )
      ),
      GlobalMuonTrackMatcher = cms.PSet( 
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        MinP = cms.double( 2.5 ),
        MinPt = cms.double( 1.0 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Pt_threshold2 = cms.double( 9.99999999E8 ),
        LocChi2Cut = cms.double( 0.0010 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_3 = cms.double( 7.0 ),
        Quality_2 = cms.double( 15.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        Quality_1 = cms.double( 20.0 )
      ),
      PtCut = cms.double( 1.0 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      tkTrajLabel = cms.InputTag( "hltL3TkTracksFromL2OIHit" )
    ),
    TrackLoaderParameters = cms.PSet( 
      PutTkTrackIntoEvent = cms.untracked.bool( False ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      SmoothTkTrack = cms.untracked.bool( False ),
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      MuonUpdatorAtVertexParameters = cms.PSet( 
        MaxChi2 = cms.double( 1000000.0 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
      ),
      VertexConstraint = cms.bool( False ),
      DoSmoothing = cms.bool( True )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
process.hltL3TkFromL2OICombination = cms.EDProducer( "L3TrackCombiner",
    labels = cms.VInputTag( 'hltL3MuonsOIState','hltL3MuonsOIHit' )
)
process.hltL3TrajSeedIOHit = cms.EDProducer( "TSGFromL2Muon",
    TkSeedGenerator = cms.PSet( 
      PSetNames = cms.vstring( 'skipTSG',
        'iterativeTSG' ),
      L3TkCollectionA = cms.InputTag( "hltL3TkFromL2OICombination" ),
      iterativeTSG = cms.PSet( 
        firstTSG = cms.PSet( 
          ComponentName = cms.string( "TSGFromOrderedHits" ),
          OrderedHitsFactoryPSet = cms.PSet( 
            ComponentName = cms.string( "StandardHitTripletGenerator" ),
            GeneratorPSet = cms.PSet( 
              useBending = cms.bool( True ),
              useFixedPreFiltering = cms.bool( False ),
              maxElement = cms.uint32( 0 ),
              phiPreFiltering = cms.double( 0.3 ),
              extraHitRPhitolerance = cms.double( 0.06 ),
              useMultScattering = cms.bool( True ),
              ComponentName = cms.string( "PixelTripletHLTGenerator" ),
              extraHitRZtolerance = cms.double( 0.06 ),
              SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) )
            ),
            SeedingLayers = cms.string( "hltESPPixelLayerTriplets" )
          ),
          TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
        ),
        PSetNames = cms.vstring( 'firstTSG',
          'secondTSG' ),
        ComponentName = cms.string( "CombinedTSG" ),
        thirdTSG = cms.PSet( 
          PSetNames = cms.vstring( 'endcapTSG',
            'barrelTSG' ),
          barrelTSG = cms.PSet(  ),
          endcapTSG = cms.PSet( 
            ComponentName = cms.string( "TSGFromOrderedHits" ),
            OrderedHitsFactoryPSet = cms.PSet( 
              maxElement = cms.uint32( 0 ),
              ComponentName = cms.string( "StandardHitPairGenerator" ),
              SeedingLayers = cms.string( "hltESPMixedLayerPairs" ),
              useOnDemandTracker = cms.untracked.int32( 0 )
            ),
            TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
          ),
          etaSeparation = cms.double( 2.0 ),
          ComponentName = cms.string( "DualByEtaTSG" )
        ),
        secondTSG = cms.PSet( 
          ComponentName = cms.string( "TSGFromOrderedHits" ),
          OrderedHitsFactoryPSet = cms.PSet( 
            maxElement = cms.uint32( 0 ),
            ComponentName = cms.string( "StandardHitPairGenerator" ),
            SeedingLayers = cms.string( "hltESPPixelLayerPairs" ),
            useOnDemandTracker = cms.untracked.int32( 0 )
          ),
          TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
        )
      ),
      skipTSG = cms.PSet(  ),
      ComponentName = cms.string( "DualByL2TSG" )
    ),
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'PropagatorWithMaterial' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' ),
    MuonTrackingRegionBuilder = cms.PSet( 
      EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
      EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
      OnDemand = cms.double( -1.0 ),
      Rescale_Dz = cms.double( 3.0 ),
      vertexCollection = cms.InputTag( "pixelVertices" ),
      Rescale_phi = cms.double( 3.0 ),
      Eta_fixed = cms.double( 0.2 ),
      DeltaZ_Region = cms.double( 15.9 ),
      MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
      PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
      Eta_min = cms.double( 0.1 ),
      Phi_fixed = cms.double( 0.2 ),
      DeltaR = cms.double( 0.2 ),
      EscapePt = cms.double( 1.5 ),
      UseFixedRegion = cms.bool( False ),
      PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
      Rescale_eta = cms.double( 3.0 ),
      Phi_min = cms.double( 0.1 ),
      UseVertex = cms.bool( False ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" )
    ),
    PCut = cms.double( 2.5 ),
    TrackerSeedCleaner = cms.PSet( 
      cleanerFromSharedHits = cms.bool( True ),
      ptCleaner = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      directionCleaner = cms.bool( True )
    ),
    PtCut = cms.double( 1.0 )
)
process.hltL3TrackCandidateFromL2IOHit = cms.EDProducer( "CkfTrajectoryMaker",
    src = cms.InputTag( "hltL3TrajSeedIOHit" ),
    reverseTrajectories = cms.bool( False ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    trackCandidateAlso = cms.bool( True ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "hltESPMuonCkfTrajectoryBuilder" ),
    maxNSeeds = cms.uint32( 100000 )
)
process.hltL3TkTracksFromL2IOHit = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltL3TrackCandidateFromL2IOHit" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    alias = cms.untracked.string( "" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    Propagator = cms.string( "PropagatorWithMaterial" )
)
process.hltL3MuonsIOHit = cms.EDProducer( "L3MuonProducer",
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'hltESPSmartPropagatorAny',
        'SteppingHelixPropagatorAny',
        'hltESPSmartPropagator',
        'hltESPSteppingHelixPropagatorOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    L3TrajBuilderParameters = cms.PSet( 
      ScaleTECyFactor = cms.double( -1.0 ),
      GlbRefitterParameters = cms.PSet( 
        TrackerSkipSection = cms.int32( -1 ),
        DoPredictionsOnly = cms.bool( False ),
        PropDirForCosmics = cms.bool( False ),
        HitThreshold = cms.int32( 1 ),
        MuonHitsOption = cms.int32( 1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        Chi2CutCSC = cms.double( 150.0 ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        SkipStation = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        TrackerSkipSystem = cms.int32( -1 ),
        DYTthrs = cms.vint32( 30, 15 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      MuonTrackingRegionBuilder = cms.PSet( 
        EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
        EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
        OnDemand = cms.double( -1.0 ),
        Rescale_Dz = cms.double( 3.0 ),
        vertexCollection = cms.InputTag( "pixelVertices" ),
        Rescale_phi = cms.double( 3.0 ),
        Eta_fixed = cms.double( 0.2 ),
        DeltaZ_Region = cms.double( 15.9 ),
        MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
        PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
        Eta_min = cms.double( 0.05 ),
        Phi_fixed = cms.double( 0.2 ),
        DeltaR = cms.double( 0.2 ),
        EscapePt = cms.double( 1.5 ),
        UseFixedRegion = cms.bool( False ),
        PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
        Rescale_eta = cms.double( 3.0 ),
        Phi_min = cms.double( 0.05 ),
        UseVertex = cms.bool( False ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" )
      ),
      RefitRPCHits = cms.bool( True ),
      PCut = cms.double( 2.5 ),
      TrackTransformer = cms.PSet( 
        DoPredictionsOnly = cms.bool( False ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" )
      ),
      GlobalMuonTrackMatcher = cms.PSet( 
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        MinP = cms.double( 2.5 ),
        MinPt = cms.double( 1.0 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Pt_threshold2 = cms.double( 9.99999999E8 ),
        LocChi2Cut = cms.double( 0.0010 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_3 = cms.double( 7.0 ),
        Quality_2 = cms.double( 15.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        Quality_1 = cms.double( 20.0 )
      ),
      PtCut = cms.double( 1.0 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      tkTrajLabel = cms.InputTag( "hltL3TkTracksFromL2IOHit" )
    ),
    TrackLoaderParameters = cms.PSet( 
      PutTkTrackIntoEvent = cms.untracked.bool( False ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      SmoothTkTrack = cms.untracked.bool( False ),
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      MuonUpdatorAtVertexParameters = cms.PSet( 
        MaxChi2 = cms.double( 1000000.0 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
      ),
      VertexConstraint = cms.bool( False ),
      DoSmoothing = cms.bool( True )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
process.hltL3TrajectorySeed = cms.EDProducer( "L3MuonTrajectorySeedCombiner",
    labels = cms.VInputTag( 'hltL3TrajSeedIOHit','hltL3TrajSeedOIState','hltL3TrajSeedOIHit' )
)
process.hltL3TrackCandidateFromL2 = cms.EDProducer( "L3TrackCandCombiner",
    labels = cms.VInputTag( 'hltL3TrackCandidateFromL2IOHit','hltL3TrackCandidateFromL2OIHit','hltL3TrackCandidateFromL2OIState' )
)
process.hltL3TkTracksFromL2 = cms.EDProducer( "L3TrackCombiner",
    labels = cms.VInputTag( 'hltL3TkTracksFromL2IOHit','hltL3TkTracksFromL2OIHit','hltL3TkTracksFromL2OIState' )
)
process.hltL3MuonsLinksCombination = cms.EDProducer( "L3TrackLinksCombiner",
    labels = cms.VInputTag( 'hltL3MuonsOIState','hltL3MuonsOIHit','hltL3MuonsIOHit' )
)
process.hltL3Muons = cms.EDProducer( "L3TrackCombiner",
    labels = cms.VInputTag( 'hltL3MuonsOIState','hltL3MuonsOIHit','hltL3MuonsIOHit' )
)
process.hltL3MuonCandidates = cms.EDProducer( "L3MuonCandidateProducer",
    InputLinksObjects = cms.InputTag( "hltL3MuonsLinksCombination" ),
    InputObjects = cms.InputTag( "hltL3Muons" ),
    MuonPtOption = cms.string( "Tracker" )
)
process.hltL1Mu3p5EG12L3Filtered22 = cms.EDFilter( "HLTMuonL3PreFilter",
    MaxNormalizedChi2 = cms.double( 9999.0 ),
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL1Mu3p5EG12L2Filtered12" ),
    MinNmuonHits = cms.int32( 0 ),
    MinN = cms.int32( 1 ),
    MinTrackPt = cms.double( 0.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxDXYBeamSpot = cms.double( 9999.0 ),
    MinNhits = cms.int32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MaxDz = cms.double( 9999.0 ),
    MaxPtDifference = cms.double( 9999.0 ),
    MaxDr = cms.double( 2.0 ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    MinDr = cms.double( -1.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinPt = cms.double( 22.0 )
)
process.hltEGRegionalL1Mu3p5EG12 = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    saveTags = cms.bool( False ),
    endcap_end = cms.double( 2.65 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    barrel_end = cms.double( 1.4791 ),
    l1IsolatedTag = cms.InputTag( 'hltL1extraParticles','Isolated' ),
    candIsolatedTag = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    region_phi_size = cms.double( 1.044 ),
    region_eta_size = cms.double( 0.522 ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1Mu3p5EG12" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    candNonIsolatedTag = cms.InputTag( "" ),
    l1NonIsolatedTag = cms.InputTag( 'hltL1extraParticles','NonIsolated' )
)
process.hltEG22EtFilterL1Mu3p5EG12 = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( False ),
    L1NonIsoCand = cms.InputTag( "" ),
    relaxed = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    inputTag = cms.InputTag( "hltEGRegionalL1Mu3p5EG12" ),
    etcutEB = cms.double( 22.0 ),
    ncandcut = cms.int32( 1 ),
    etcutEE = cms.double( 22.0 )
)
process.hltMu22Photon22CaloIdLClusterShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 0.035 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 0.014 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededHLTClusterShape" ),
    candTag = cms.InputTag( "hltEG22EtFilterL1Mu3p5EG12" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltMu22Photon22CaloIdLHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.1 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( 0.15 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededPhotonHcalForHE" ),
    candTag = cms.InputTag( "hltMu22Photon22CaloIdLClusterShapeFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltL1sL1DoubleMu10MuOpen = cms.EDFilter( "HLTLevel1GTSeed",
    saveTags = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_DoubleMu_10_Open" ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreMu17TkMu8 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltL1fL1sDoubleMu10MuOpenL1Filtered0 = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMu10MuOpen" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltL2fL1sDoubleMu10MuOpenL1f0L2Filtered10 = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltL1fL1sDoubleMu10MuOpenL1Filtered0" ),
    MinPt = cms.double( 10.0 ),
    MinN = cms.int32( 1 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltL3fL1sMu10MuOpenL1f0L2f10L3Filtered17 = cms.EDFilter( "HLTMuonL3PreFilter",
    MaxNormalizedChi2 = cms.double( 9999.0 ),
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu10MuOpenL1f0L2Filtered10" ),
    MinNmuonHits = cms.int32( 0 ),
    MinN = cms.int32( 1 ),
    MinTrackPt = cms.double( 0.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxDXYBeamSpot = cms.double( 9999.0 ),
    MinNhits = cms.int32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MaxDz = cms.double( 9999.0 ),
    MaxPtDifference = cms.double( 9999.0 ),
    MaxDr = cms.double( 2.0 ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    MinDr = cms.double( -1.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinPt = cms.double( 17.0 )
)
process.hltPixelTracks = cms.EDProducer( "PixelTrackProducer",
    useFilterWithES = cms.bool( False ),
    FilterPSet = cms.PSet( 
      chi2 = cms.double( 1000.0 ),
      nSigmaTipMaxTolerance = cms.double( 0.0 ),
      ComponentName = cms.string( "PixelTrackFilterByKinematics" ),
      nSigmaInvPtTolerance = cms.double( 0.0 ),
      ptMin = cms.double( 0.1 ),
      tipMax = cms.double( 1.0 )
    ),
    passLabel = cms.string( "Pixel triplet primary tracks with vertex constraint" ),
    FitterPSet = cms.PSet( 
      ComponentName = cms.string( "PixelFitterByHelixProjections" ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      fixImpactParameter = cms.double( 0.0 )
    ),
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "GlobalRegionProducerFromBeamSpot" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originRadius = cms.double( 0.2 ),
        ptMin = cms.double( 0.9 ),
        originHalfLength = cms.double( 24.0 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" )
      )
    ),
    CleanerPSet = cms.PSet(  ComponentName = cms.string( "PixelTrackCleanerBySharedHits" ) ),
    OrderedHitsFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      GeneratorPSet = cms.PSet( 
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        maxElement = cms.uint32( 100000 ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRPhitolerance = cms.double( 0.06 ),
        useMultScattering = cms.bool( True ),
        SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ) ),
        extraHitRZtolerance = cms.double( 0.06 ),
        ComponentName = cms.string( "PixelTripletHLTGenerator" )
      ),
      SeedingLayers = cms.string( "hltESPPixelLayerTriplets" )
    )
)
process.hltMuTrackSeeds = cms.EDProducer( "SeedGeneratorFromProtoTracksEDProducer",
    useEventsWithNoVertex = cms.bool( True ),
    originHalfLength = cms.double( 1.0E9 ),
    useProtoTrackKinematics = cms.bool( False ),
    InputVertexCollection = cms.InputTag( "" ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    InputCollection = cms.InputTag( "hltPixelTracks" ),
    originRadius = cms.double( 1.0E9 )
)
process.hltMuCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltMuTrackSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "hltESPMuTrackJpsiTrajectoryBuilder" )
)
process.hltMuCtfTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltMuCkfTrackCandidates" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    Fitter = cms.string( "hltESPFittingSmootherRK" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    alias = cms.untracked.string( "hltMuCtfTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltDiMuonMerging = cms.EDProducer( "SimpleTrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    promoteTrackQuality = cms.bool( True ),
    MinPT = cms.double( 0.05 ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.0010 ),
    allowFirstHitShare = cms.bool( True ),
    newQuality = cms.string( "confirmed" ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    TrackProducer1 = cms.string( "hltL3TkTracksFromL2" ),
    MinFound = cms.int32( 3 ),
    TrackProducer2 = cms.string( "hltMuCtfTracks" ),
    LostHitPenalty = cms.double( 20.0 ),
    FoundHitBonus = cms.double( 5.0 )
)
process.hltDiMuonLinks = cms.EDProducer( "MuonLinksProducerForHLT",
    pMin = cms.double( 2.5 ),
    InclusiveTrackerTrackCollection = cms.InputTag( "hltDiMuonMerging" ),
    shareHitFraction = cms.double( 0.8 ),
    LinkCollection = cms.InputTag( "hltL3MuonsLinksCombination" ),
    ptMin = cms.double( 2.5 )
)
process.hltGlbTrkMuons = cms.EDProducer( "MuonIdProducer",
    TrackExtractorPSet = cms.PSet( 
      Diff_z = cms.double( 0.2 ),
      inputTrackCollection = cms.InputTag( "hltPFMuonMerging" ),
      BeamSpotLabel = cms.InputTag( "hltOnlineBeamSpot" ),
      ComponentName = cms.string( "TrackExtractor" ),
      DR_Max = cms.double( 1.0 ),
      Diff_r = cms.double( 0.1 ),
      Chi2Prob_Min = cms.double( -1.0 ),
      DR_Veto = cms.double( 0.01 ),
      NHits_Min = cms.uint32( 0 ),
      Chi2Ndof_Max = cms.double( 1.0E64 ),
      Pt_Min = cms.double( -1.0 ),
      DepositLabel = cms.untracked.string( "" ),
      BeamlineOption = cms.string( "BeamSpotFromEvent" )
    ),
    maxAbsEta = cms.double( 3.0 ),
    fillGlobalTrackRefits = cms.bool( False ),
    arbitrationCleanerOptions = cms.PSet( 
      Clustering = cms.bool( True ),
      ME1a = cms.bool( True ),
      ClusterDPhi = cms.double( 0.6 ),
      OverlapDTheta = cms.double( 0.02 ),
      Overlap = cms.bool( True ),
      OverlapDPhi = cms.double( 0.0786 ),
      ClusterDTheta = cms.double( 0.02 )
    ),
    globalTrackQualityInputTag = cms.InputTag( "glbTrackQual" ),
    addExtraSoftMuons = cms.bool( False ),
    debugWithTruthMatching = cms.bool( False ),
    CaloExtractorPSet = cms.PSet( 
      PrintTimeReport = cms.untracked.bool( False ),
      DR_Max = cms.double( 1.0 ),
      DepositInstanceLabels = cms.vstring( 'ecal',
        'hcal',
        'ho' ),
      Noise_HE = cms.double( 0.2 ),
      NoiseTow_EB = cms.double( 0.04 ),
      NoiseTow_EE = cms.double( 0.15 ),
      Threshold_H = cms.double( 0.5 ),
      ServiceParameters = cms.PSet( 
        Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny' ),
        RPCLayers = cms.bool( False ),
        UseMuonNavigation = cms.untracked.bool( False )
      ),
      Threshold_E = cms.double( 0.2 ),
      PropagatorName = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
      DepositLabel = cms.untracked.string( "Cal" ),
      UseRecHitsFlag = cms.bool( False ),
      TrackAssociatorParameters = cms.PSet( 
        muonMaxDistanceSigmaX = cms.double( 0.0 ),
        muonMaxDistanceSigmaY = cms.double( 0.0 ),
        CSCSegmentCollectionLabel = cms.InputTag( "hltCscSegments" ),
        dRHcal = cms.double( 1.0 ),
        dRPreshowerPreselection = cms.double( 0.2 ),
        CaloTowerCollectionLabel = cms.InputTag( "hltTowerMakerForPF" ),
        useEcal = cms.bool( False ),
        dREcal = cms.double( 1.0 ),
        dREcalPreselection = cms.double( 1.0 ),
        HORecHitCollectionLabel = cms.InputTag( "hltHoreco" ),
        dRMuon = cms.double( 9999.0 ),
        propagateAllDirections = cms.bool( True ),
        muonMaxDistanceX = cms.double( 5.0 ),
        muonMaxDistanceY = cms.double( 5.0 ),
        useHO = cms.bool( False ),
        trajectoryUncertaintyTolerance = cms.double( -1.0 ),
        usePreshower = cms.bool( False ),
        DTRecSegment4DCollectionLabel = cms.InputTag( "hltDt4DSegments" ),
        EERecHitCollectionLabel = cms.InputTag( 'hltEcalRecHitAll','EcalRecHitsEE' ),
        dRHcalPreselection = cms.double( 1.0 ),
        useMuon = cms.bool( False ),
        useCalo = cms.bool( True ),
        accountForTrajectoryChangeCalo = cms.bool( False ),
        EBRecHitCollectionLabel = cms.InputTag( 'hltEcalRecHitAll','EcalRecHitsEB' ),
        dRMuonPreselection = cms.double( 0.2 ),
        truthMatch = cms.bool( False ),
        HBHERecHitCollectionLabel = cms.InputTag( "hltHbhereco" ),
        useHcal = cms.bool( False )
      ),
      Threshold_HO = cms.double( 0.5 ),
      Noise_EE = cms.double( 0.1 ),
      Noise_EB = cms.double( 0.025 ),
      DR_Veto_H = cms.double( 0.1 ),
      CenterConeOnCalIntersection = cms.bool( False ),
      ComponentName = cms.string( "CaloExtractorByAssociator" ),
      Noise_HB = cms.double( 0.2 ),
      DR_Veto_E = cms.double( 0.07 ),
      DR_Veto_HO = cms.double( 0.1 ),
      Noise_HO = cms.double( 0.2 )
    ),
    runArbitrationCleaner = cms.bool( False ),
    fillEnergy = cms.bool( False ),
    TrackerKinkFinderParameters = cms.PSet( 
      usePosition = cms.bool( False ),
      diagonalOnly = cms.bool( False )
    ),
    TimingFillerParameters = cms.PSet( 
      UseDT = cms.bool( True ),
      ErrorDT = cms.double( 6.0 ),
      EcalEnergyCut = cms.double( 0.4 ),
      ErrorEB = cms.double( 2.085 ),
      ErrorCSC = cms.double( 7.4 ),
      CSCTimingParameters = cms.PSet( 
        CSCsegments = cms.InputTag( "hltCscSegments" ),
        CSCTimeOffset = cms.double( 0.0 ),
        CSCStripTimeOffset = cms.double( 0.0 ),
        MatchParameters = cms.PSet( 
          CSCsegments = cms.InputTag( "hltCscSegments" ),
          DTsegments = cms.InputTag( "hltDt4DSegments" ),
          DTradius = cms.double( 0.01 ),
          TightMatchDT = cms.bool( False ),
          TightMatchCSC = cms.bool( True )
        ),
        debug = cms.bool( False ),
        UseStripTime = cms.bool( True ),
        CSCStripError = cms.double( 7.0 ),
        CSCWireError = cms.double( 8.6 ),
        CSCWireTimeOffset = cms.double( 0.0 ),
        ServiceParameters = cms.PSet( 
          Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny' ),
          RPCLayers = cms.bool( True )
        ),
        PruneCut = cms.double( 100.0 ),
        UseWireTime = cms.bool( True )
      ),
      DTTimingParameters = cms.PSet( 
        HitError = cms.double( 6.0 ),
        DoWireCorr = cms.bool( False ),
        MatchParameters = cms.PSet( 
          CSCsegments = cms.InputTag( "hltCscSegments" ),
          DTsegments = cms.InputTag( "hltDt4DSegments" ),
          DTradius = cms.double( 0.01 ),
          TightMatchDT = cms.bool( False ),
          TightMatchCSC = cms.bool( True )
        ),
        debug = cms.bool( False ),
        DTsegments = cms.InputTag( "hltDt4DSegments" ),
        PruneCut = cms.double( 10000.0 ),
        RequireBothProjections = cms.bool( False ),
        HitsMin = cms.int32( 5 ),
        DTTimeOffset = cms.double( 2.7 ),
        DropTheta = cms.bool( True ),
        UseSegmentT0 = cms.bool( False ),
        ServiceParameters = cms.PSet( 
          Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny' ),
          RPCLayers = cms.bool( True )
        )
      ),
      ErrorEE = cms.double( 6.95 ),
      UseCSC = cms.bool( True ),
      UseECAL = cms.bool( True )
    ),
    inputCollectionTypes = cms.vstring( 'inner tracks',
      'links' ),
    minCaloCompatibility = cms.double( 0.6 ),
    ecalDepositName = cms.string( "ecal" ),
    minP = cms.double( 0.0 ),
    fillIsolation = cms.bool( False ),
    jetDepositName = cms.string( "jets" ),
    hoDepositName = cms.string( "ho" ),
    writeIsoDeposits = cms.bool( False ),
    maxAbsPullX = cms.double( 4.0 ),
    maxAbsPullY = cms.double( 9999.0 ),
    minPt = cms.double( 8.0 ),
    TrackAssociatorParameters = cms.PSet( 
      muonMaxDistanceSigmaX = cms.double( 0.0 ),
      muonMaxDistanceSigmaY = cms.double( 0.0 ),
      CSCSegmentCollectionLabel = cms.InputTag( "hltCscSegments" ),
      dRHcal = cms.double( 9999.0 ),
      dRPreshowerPreselection = cms.double( 0.2 ),
      CaloTowerCollectionLabel = cms.InputTag( "hltTowerMakerForPF" ),
      useEcal = cms.bool( False ),
      dREcal = cms.double( 9999.0 ),
      dREcalPreselection = cms.double( 0.05 ),
      HORecHitCollectionLabel = cms.InputTag( "hltHoreco" ),
      dRMuon = cms.double( 9999.0 ),
      propagateAllDirections = cms.bool( True ),
      muonMaxDistanceX = cms.double( 5.0 ),
      muonMaxDistanceY = cms.double( 5.0 ),
      useHO = cms.bool( False ),
      trajectoryUncertaintyTolerance = cms.double( -1.0 ),
      usePreshower = cms.bool( False ),
      DTRecSegment4DCollectionLabel = cms.InputTag( "hltDt4DSegments" ),
      EERecHitCollectionLabel = cms.InputTag( 'hltEcalRecHitAll','EcalRecHitsEE' ),
      dRHcalPreselection = cms.double( 0.2 ),
      useMuon = cms.bool( True ),
      useCalo = cms.bool( False ),
      accountForTrajectoryChangeCalo = cms.bool( False ),
      EBRecHitCollectionLabel = cms.InputTag( 'hltEcalRecHitAll','EcalRecHitsEB' ),
      dRMuonPreselection = cms.double( 0.2 ),
      truthMatch = cms.bool( False ),
      HBHERecHitCollectionLabel = cms.InputTag( "hltHbhereco" ),
      useHcal = cms.bool( False )
    ),
    JetExtractorPSet = cms.PSet( 
      PrintTimeReport = cms.untracked.bool( False ),
      ExcludeMuonVeto = cms.bool( True ),
      TrackAssociatorParameters = cms.PSet( 
        muonMaxDistanceSigmaX = cms.double( 0.0 ),
        muonMaxDistanceSigmaY = cms.double( 0.0 ),
        CSCSegmentCollectionLabel = cms.InputTag( "hltCscSegments" ),
        dRHcal = cms.double( 0.5 ),
        dRPreshowerPreselection = cms.double( 0.2 ),
        CaloTowerCollectionLabel = cms.InputTag( "hltTowerMakerForPF" ),
        useEcal = cms.bool( False ),
        dREcal = cms.double( 0.5 ),
        dREcalPreselection = cms.double( 0.5 ),
        HORecHitCollectionLabel = cms.InputTag( "hltHoreco" ),
        dRMuon = cms.double( 9999.0 ),
        propagateAllDirections = cms.bool( True ),
        muonMaxDistanceX = cms.double( 5.0 ),
        muonMaxDistanceY = cms.double( 5.0 ),
        useHO = cms.bool( False ),
        trajectoryUncertaintyTolerance = cms.double( -1.0 ),
        usePreshower = cms.bool( False ),
        DTRecSegment4DCollectionLabel = cms.InputTag( "hltDt4DSegments" ),
        EERecHitCollectionLabel = cms.InputTag( 'hltEcalRecHitAll','EcalRecHitsEE' ),
        dRHcalPreselection = cms.double( 0.5 ),
        useMuon = cms.bool( False ),
        useCalo = cms.bool( True ),
        accountForTrajectoryChangeCalo = cms.bool( False ),
        EBRecHitCollectionLabel = cms.InputTag( 'hltEcalRecHitAll','EcalRecHitsEB' ),
        dRMuonPreselection = cms.double( 0.2 ),
        truthMatch = cms.bool( False ),
        HBHERecHitCollectionLabel = cms.InputTag( "hltHbhereco" ),
        useHcal = cms.bool( False )
      ),
      ServiceParameters = cms.PSet( 
        Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny' ),
        RPCLayers = cms.bool( False ),
        UseMuonNavigation = cms.untracked.bool( False )
      ),
      ComponentName = cms.string( "JetExtractor" ),
      DR_Max = cms.double( 1.0 ),
      PropagatorName = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
      JetCollectionLabel = cms.InputTag( "hltAntiKT5CaloJetsPFEt5" ),
      DR_Veto = cms.double( 0.1 ),
      Threshold = cms.double( 5.0 )
    ),
    fillGlobalTrackQuality = cms.bool( False ),
    minPCaloMuon = cms.double( 1.0E9 ),
    maxAbsDy = cms.double( 9999.0 ),
    fillCaloCompatibility = cms.bool( False ),
    fillMatching = cms.bool( True ),
    MuonCaloCompatibility = cms.PSet( 
      allSiPMHO = cms.bool( False ),
      PionTemplateFileName = cms.FileInPath( "RecoMuon/MuonIdentification/data/MuID_templates_pions_lowPt_3_1_norm.root" ),
      MuonTemplateFileName = cms.FileInPath( "RecoMuon/MuonIdentification/data/MuID_templates_muons_lowPt_3_1_norm.root" ),
      delta_eta = cms.double( 0.02 ),
      delta_phi = cms.double( 0.02 )
    ),
    fillTrackerKink = cms.bool( False ),
    hcalDepositName = cms.string( "hcal" ),
    sigmaThresholdToFillCandidateP4WithGlobalFit = cms.double( 2.0 ),
    inputCollectionLabels = cms.VInputTag( 'hltDiMuonMerging','hltDiMuonLinks' ),
    trackDepositName = cms.string( "tracker" ),
    maxAbsDx = cms.double( 3.0 ),
    ptThresholdToFillCandidateP4WithGlobalFit = cms.double( 200.0 ),
    minNumberOfMatches = cms.int32( 1 )
)
process.hltGlbTrkMuonCands = cms.EDProducer( "L3MuonCandidateProducerFromMuons",
    InputObjects = cms.InputTag( "hltGlbTrkMuons" )
)
process.hltDiMuonGlbFiltered17TrkFiltered8 = cms.EDFilter( "HLTDiMuonGlbTrkFilter",
    saveTags = cms.bool( True ),
    maxNormalizedChi2 = cms.double( 1.0E99 ),
    minMuonHits = cms.int32( -1 ),
    inputCandCollection = cms.InputTag( "hltGlbTrkMuonCands" ),
    minMass = cms.double( 1.0 ),
    trkMuonId = cms.uint32( 0 ),
    requiredTypeMask = cms.uint32( 0 ),
    minPtMuon1 = cms.double( 17.0 ),
    minPtMuon2 = cms.double( 8.0 ),
    minTrkHits = cms.int32( -1 ),
    inputMuonCollection = cms.InputTag( "hltGlbTrkMuons" ),
    minDR = cms.double( 0.1 ),
    allowedTypeMask = cms.uint32( 255 )
)
process.hltDiMuonGlb17Trk8DzFiltered0p2 = cms.EDFilter( "HLT2MuonMuonDZ",
    saveTags = cms.bool( True ),
    originTag1 = cms.InputTag( "hltOriginal1" ),
    originTag2 = cms.InputTag( "hltOriginal2" ),
    MinN = cms.int32( 1 ),
    triggerType1 = cms.int32( 83 ),
    triggerType2 = cms.int32( 83 ),
    MinDR = cms.double( -1.0 ),
    MaxDZ = cms.double( 0.2 ),
    inputTag1 = cms.InputTag( "hltDiMuonGlbFiltered17TrkFiltered8" ),
    inputTag2 = cms.InputTag( "hltDiMuonGlbFiltered17TrkFiltered8" )
)
process.hltL1sMu16Eta2p1 = cms.EDFilter( "HLTLevel1GTSeed",
    saveTags = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleMu16er" ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreMu22TkMu8 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltL1fL1sMu16Eta2p1L1Filtered0 = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sMu16Eta2p1" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.1 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltL2fL1sMu16Eta2p1L1f0L2Filtered16Q = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltL1fL1sMu16Eta2p1L1Filtered0" ),
    MinPt = cms.double( 16.0 ),
    MinN = cms.int32( 1 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.1 ),
    MinNhits = cms.vint32( 0, 1, 0, 1 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 0.9, 1.5, 2.1, 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0, 2, 0, 2 )
)
process.hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered22 = cms.EDFilter( "HLTMuonL3PreFilter",
    MaxNormalizedChi2 = cms.double( 9999.0 ),
    saveTags = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sMu16Eta2p1L1f0L2Filtered16Q" ),
    MinNmuonHits = cms.int32( 0 ),
    MinN = cms.int32( 1 ),
    MinTrackPt = cms.double( 0.0 ),
    MaxEta = cms.double( 2.1 ),
    MaxDXYBeamSpot = cms.double( 9999.0 ),
    MinNhits = cms.int32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MaxDz = cms.double( 9999.0 ),
    MaxPtDifference = cms.double( 9999.0 ),
    MaxDr = cms.double( 2.0 ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    MinDr = cms.double( -1.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinPt = cms.double( 22.0 )
)
process.hltDiMuonGlbFiltered22TrkFiltered8 = cms.EDFilter( "HLTDiMuonGlbTrkFilter",
    saveTags = cms.bool( True ),
    maxNormalizedChi2 = cms.double( 1.0E99 ),
    minMuonHits = cms.int32( -1 ),
    inputCandCollection = cms.InputTag( "hltGlbTrkMuonCands" ),
    minMass = cms.double( 1.0 ),
    trkMuonId = cms.uint32( 0 ),
    requiredTypeMask = cms.uint32( 0 ),
    minPtMuon1 = cms.double( 22.0 ),
    minPtMuon2 = cms.double( 8.0 ),
    minTrkHits = cms.int32( -1 ),
    inputMuonCollection = cms.InputTag( "hltGlbTrkMuons" ),
    minDR = cms.double( 0.1 ),
    allowedTypeMask = cms.uint32( 255 )
)
process.hltDiMuonGlb22Trk8DzFiltered0p2 = cms.EDFilter( "HLT2MuonMuonDZ",
    saveTags = cms.bool( True ),
    originTag1 = cms.InputTag( "hltOriginal1" ),
    originTag2 = cms.InputTag( "hltOriginal2" ),
    MinN = cms.int32( 1 ),
    triggerType1 = cms.int32( 83 ),
    triggerType2 = cms.int32( 83 ),
    MinDR = cms.double( -1.0 ),
    MaxDZ = cms.double( 0.2 ),
    inputTag1 = cms.InputTag( "hltDiMuonGlbFiltered22TrkFiltered8" ),
    inputTag2 = cms.InputTag( "hltDiMuonGlbFiltered22TrkFiltered8" )
)
process.hltPreMu22TkMu22 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltDiMuonGlbFiltered22TrkFiltered22 = cms.EDFilter( "HLTDiMuonGlbTrkFilter",
    saveTags = cms.bool( True ),
    maxNormalizedChi2 = cms.double( 1.0E99 ),
    minMuonHits = cms.int32( -1 ),
    inputCandCollection = cms.InputTag( "hltGlbTrkMuonCands" ),
    minMass = cms.double( 1.0 ),
    trkMuonId = cms.uint32( 0 ),
    requiredTypeMask = cms.uint32( 0 ),
    minPtMuon1 = cms.double( 22.0 ),
    minPtMuon2 = cms.double( 22.0 ),
    minTrkHits = cms.int32( -1 ),
    inputMuonCollection = cms.InputTag( "hltGlbTrkMuons" ),
    minDR = cms.double( 0.1 ),
    allowedTypeMask = cms.uint32( 255 )
)
process.hltDiMuonGlb22Trk22DzFiltered0p2 = cms.EDFilter( "HLT2MuonMuonDZ",
    saveTags = cms.bool( True ),
    originTag1 = cms.InputTag( "hltOriginal1" ),
    originTag2 = cms.InputTag( "hltOriginal2" ),
    MinN = cms.int32( 1 ),
    triggerType1 = cms.int32( 83 ),
    triggerType2 = cms.int32( 83 ),
    MinDR = cms.double( -1.0 ),
    MaxDZ = cms.double( 0.2 ),
    inputTag1 = cms.InputTag( "hltDiMuonGlbFiltered22TrkFiltered22" ),
    inputTag2 = cms.InputTag( "hltDiMuonGlbFiltered22TrkFiltered22" )
)
process.hltPreMu30Ele30CaloIdL = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltL1Mu3p5EG12L3Filtered30 = cms.EDFilter( "HLTMuonL3PreFilter",
    MaxNormalizedChi2 = cms.double( 9999.0 ),
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL1Mu3p5EG12L2Filtered12" ),
    MinNmuonHits = cms.int32( 0 ),
    MinN = cms.int32( 1 ),
    MinTrackPt = cms.double( 0.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxDXYBeamSpot = cms.double( 9999.0 ),
    MinNhits = cms.int32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MaxDz = cms.double( 9999.0 ),
    MaxPtDifference = cms.double( 9999.0 ),
    MaxDr = cms.double( 2.0 ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    MinDr = cms.double( -1.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinPt = cms.double( 30.0 )
)
process.hltEG30EtFilterL1Mu3p5EG12 = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( False ),
    L1NonIsoCand = cms.InputTag( "" ),
    relaxed = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    inputTag = cms.InputTag( "hltEGRegionalL1Mu3p5EG12" ),
    etcutEB = cms.double( 22.0 ),
    ncandcut = cms.int32( 1 ),
    etcutEE = cms.double( 22.0 )
)
process.hltMu3p5Photon30CaloIdLClusterShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 0.035 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 0.014 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededHLTClusterShape" ),
    candTag = cms.InputTag( "hltEG30EtFilterL1Mu3p5EG12" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltMu3p5Photon30CaloIdLHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.1 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( 0.15 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededPhotonHcalForHE" ),
    candTag = cms.InputTag( "hltMu3p5Photon30CaloIdLClusterShapeFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltMu3p5Ele30CaloIdLPixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    saveTags = cms.bool( True ),
    doIsolated = cms.bool( True ),
    L1NonIsoCand = cms.InputTag( "" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "" ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    candTag = cms.InputTag( "hltMu3p5Photon30CaloIdLHEFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltL1SeededStartUpElectronPixelSeeds" )
)
process.hltPreMu40eta2p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered40Q = cms.EDFilter( "HLTMuonL3PreFilter",
    MaxNormalizedChi2 = cms.double( 20.0 ),
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sMu16Eta2p1L1f0L2Filtered16Q" ),
    MinNmuonHits = cms.int32( 0 ),
    MinN = cms.int32( 1 ),
    MinTrackPt = cms.double( 0.0 ),
    MaxEta = cms.double( 2.1 ),
    MaxDXYBeamSpot = cms.double( 0.1 ),
    MinNhits = cms.int32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MaxDz = cms.double( 9999.0 ),
    MaxPtDifference = cms.double( 9999.0 ),
    MaxDr = cms.double( 2.0 ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    MinDr = cms.double( -1.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinPt = cms.double( 40.0 )
)
process.hltPreIsoMu24eta2p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered24Q = cms.EDFilter( "HLTMuonL3PreFilter",
    MaxNormalizedChi2 = cms.double( 20.0 ),
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sMu16Eta2p1L1f0L2Filtered16Q" ),
    MinNmuonHits = cms.int32( 0 ),
    MinN = cms.int32( 1 ),
    MinTrackPt = cms.double( 0.0 ),
    MaxEta = cms.double( 2.1 ),
    MaxDXYBeamSpot = cms.double( 0.1 ),
    MinNhits = cms.int32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MaxDz = cms.double( 9999.0 ),
    MaxPtDifference = cms.double( 9999.0 ),
    MaxDr = cms.double( 2.0 ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    MinDr = cms.double( -1.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinPt = cms.double( 24.0 )
)
process.hltEcalRegionalMuonsFEDs = cms.EDProducer( "EcalRawToRecHitRoI",
    JetJobPSet = cms.VPSet( 
    ),
    sourceTag_es = cms.InputTag( "NotNeededoESfalse" ),
    doES = cms.bool( False ),
    type = cms.string( "candidate" ),
    sourceTag = cms.InputTag( "hltEcalRawToRecHitFacility" ),
    EmJobPSet = cms.VPSet( 
    ),
    CandJobPSet = cms.VPSet( 
      cms.PSet(  bePrecise = cms.bool( False ),
        propagatorNameToBePrecise = cms.string( "" ),
        epsilon = cms.double( 0.01 ),
        regionPhiMargin = cms.double( 0.3 ),
        cType = cms.string( "chargedcandidate" ),
        Source = cms.InputTag( "hltL2MuonCandidates" ),
        Ptmin = cms.double( 0.0 ),
        regionEtaMargin = cms.double( 0.3 )
      )
    ),
    MuonJobPSet = cms.PSet(  ),
    esInstance = cms.untracked.string( "es" ),
    MuJobPSet = cms.PSet(  )
)
process.hltEcalRegionalMuonsRecHit = cms.EDProducer( "EcalRawToRecHitProducer",
    splitOutput = cms.bool( True ),
    rechitCollection = cms.string( "NotNeededsplitOutputTrue" ),
    EErechitCollection = cms.string( "EcalRecHitsEE" ),
    EBrechitCollection = cms.string( "EcalRecHitsEB" ),
    sourceTag = cms.InputTag( "hltEcalRegionalMuonsFEDs" ),
    lazyGetterTag = cms.InputTag( "hltEcalRawToRecHitFacility" )
)
process.hltHoreco = cms.EDProducer( "HcalHitReconstructor",
    digiTimeFromDB = cms.bool( True ),
    S9S1stat = cms.PSet(  ),
    saturationParameters = cms.PSet(  maxADCvalue = cms.int32( 127 ) ),
    tsFromDB = cms.bool( True ),
    samplesToAdd = cms.int32( 4 ),
    correctionPhaseNS = cms.double( 13.0 ),
    HFInWindowStat = cms.PSet(  ),
    digiLabel = cms.InputTag( "hltHcalDigis" ),
    setHSCPFlags = cms.bool( False ),
    firstAuxTS = cms.int32( 4 ),
    setSaturationFlags = cms.bool( False ),
    hfTimingTrustParameters = cms.PSet(  ),
    PETstat = cms.PSet(  ),
    digistat = cms.PSet(  ),
    useLeakCorrection = cms.bool( False ),
    setTimingTrustFlags = cms.bool( False ),
    S8S1stat = cms.PSet(  ),
    correctForPhaseContainment = cms.bool( True ),
    correctForTimeslew = cms.bool( True ),
    setNoiseFlags = cms.bool( False ),
    correctTiming = cms.bool( False ),
    setPulseShapeFlags = cms.bool( False ),
    Subdetector = cms.string( "HO" ),
    dropZSmarkedPassed = cms.bool( True ),
    recoParamsFromDB = cms.bool( True ),
    firstSample = cms.int32( 4 ),
    setTimingShapedCutsFlags = cms.bool( False ),
    timingshapedcutsParameters = cms.PSet(  ),
    pulseShapeParameters = cms.PSet(  ),
    flagParameters = cms.PSet(  ),
    hscpParameters = cms.PSet(  )
)
process.hltTowerMakerForMuons = cms.EDProducer( "CaloTowersCreator",
    EBSumThreshold = cms.double( 0.2 ),
    MomHBDepth = cms.double( 0.2 ),
    UseEtEBTreshold = cms.bool( False ),
    hfInput = cms.InputTag( "hltHfreco" ),
    AllowMissingInputs = cms.bool( False ),
    MomEEDepth = cms.double( 0.0 ),
    EESumThreshold = cms.double( 0.45 ),
    HBGrid = cms.vdouble(  ),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    HBThreshold = cms.double( 0.7 ),
    EcalSeveritiesToBeUsedInBadTowers = cms.vstring(  ),
    UseEcalRecoveredHits = cms.bool( False ),
    MomConstrMethod = cms.int32( 1 ),
    MomHEDepth = cms.double( 0.4 ),
    HcalThreshold = cms.double( -1000.0 ),
    HF2Weights = cms.vdouble(  ),
    HOWeights = cms.vdouble(  ),
    EEGrid = cms.vdouble(  ),
    UseSymEBTreshold = cms.bool( False ),
    EEWeights = cms.vdouble(  ),
    EEWeight = cms.double( 1.0 ),
    UseHO = cms.bool( False ),
    HBWeights = cms.vdouble(  ),
    HF1Weight = cms.double( 1.0 ),
    HF2Grid = cms.vdouble(  ),
    HEDWeights = cms.vdouble(  ),
    HEDGrid = cms.vdouble(  ),
    EBWeight = cms.double( 1.0 ),
    HF1Grid = cms.vdouble(  ),
    EBWeights = cms.vdouble(  ),
    HOWeight = cms.double( 1.0E-99 ),
    HESWeight = cms.double( 1.0 ),
    HESThreshold = cms.double( 0.8 ),
    hbheInput = cms.InputTag( "hltHbhereco" ),
    HF2Weight = cms.double( 1.0 ),
    HF2Threshold = cms.double( 0.85 ),
    HcalAcceptSeverityLevel = cms.uint32( 9 ),
    EEThreshold = cms.double( 0.3 ),
    HOThresholdPlus1 = cms.double( 3.5 ),
    HOThresholdPlus2 = cms.double( 3.5 ),
    HF1Weights = cms.vdouble(  ),
    hoInput = cms.InputTag( "hltHoreco" ),
    HF1Threshold = cms.double( 0.5 ),
    HOThresholdMinus1 = cms.double( 3.5 ),
    HESGrid = cms.vdouble(  ),
    EcutTower = cms.double( -1000.0 ),
    UseRejectedRecoveredEcalHits = cms.bool( False ),
    UseEtEETreshold = cms.bool( False ),
    HESWeights = cms.vdouble(  ),
    EcalRecHitSeveritiesToBeExcluded = cms.vstring( 'kTime',
      'kWeird',
      'kBad' ),
    HEDWeight = cms.double( 1.0 ),
    UseSymEETreshold = cms.bool( False ),
    HEDThreshold = cms.double( 0.8 ),
    EBThreshold = cms.double( 0.07 ),
    UseRejectedHitsOnly = cms.bool( False ),
    UseHcalRecoveredHits = cms.bool( False ),
    HOThresholdMinus2 = cms.double( 3.5 ),
    HOThreshold0 = cms.double( 3.5 ),
    ecalInputs = cms.VInputTag( 'hltEcalRegionalMuonsRecHit:EcalRecHitsEB','hltEcalRegionalMuonsRecHit:EcalRecHitsEE' ),
    UseRejectedRecoveredHcalHits = cms.bool( False ),
    MomEBDepth = cms.double( 0.3 ),
    HBWeight = cms.double( 1.0 ),
    HOGrid = cms.vdouble(  ),
    EBGrid = cms.vdouble(  )
)
process.hltRegionalSeedsForL3MuonIsolation = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "IsolationRegionAroundL3Muon" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originRadius = cms.double( 0.2 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        originHalfLength = cms.double( 15.0 ),
        ptMin = cms.double( 1.0 ),
        deltaPhiRegion = cms.double( 0.24 ),
        measurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
        zVertex = cms.double( 5.0 ),
        deltaEtaRegion = cms.double( 0.24 ),
        rVertex = cms.double( 5.0 ),
        vertexSrc = cms.string( "" ),
        vertexZConstrained = cms.bool( False ),
        vertexZDefault = cms.double( 0.0 ),
        TrkSrc = cms.InputTag( "hltL3Muons" )
      ),
      CollectionsPSet = cms.PSet( 
        recoL2MuonsCollection = cms.InputTag( "" ),
        recoTrackMuonsCollection = cms.InputTag( "cosmicMuons" ),
        recoMuonsCollection = cms.InputTag( "" )
      ),
      RegionInJetsCheckPSet = cms.PSet( 
        recoCaloJetsCollection = cms.InputTag( "ak5CaloJets" ),
        deltaRExclusionSize = cms.double( 0.3 ),
        jetsPtMin = cms.double( 5.0 ),
        doJetsExclusionCheck = cms.bool( True )
      ),
      ToolsPSet = cms.PSet( 
        regionBase = cms.string( "seedOnCosmicMuon" ),
        thePropagatorName = cms.string( "AnalyticalPropagator" )
      )
    ),
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    ClusterCheckPSet = cms.PSet( 
      MaxNumberOfPixelClusters = cms.uint32( 20000 ),
      PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClusters" ),
      MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
      ClusterCollectionLabel = cms.InputTag( "hltSiStripClusters" ),
      doClusterCheck = cms.bool( False )
    ),
    OrderedHitsFactoryPSet = cms.PSet( 
      maxElement = cms.uint32( 100000 ),
      ComponentName = cms.string( "StandardHitPairGenerator" ),
      SeedingLayers = cms.string( "hltESPMixedLayerPairs" ),
      LayerPSet = cms.PSet( 
        TOB = cms.PSet(  TTRHBuilder = cms.string( "WithTrackAngle" ) ),
        layerList = cms.vstring( 'TOB6+TOB5',
          'TOB6+TOB4',
          'TOB6+TOB3',
          'TOB5+TOB4',
          'TOB5+TOB3',
          'TOB4+TOB3',
          'TEC1_neg+TOB6',
          'TEC1_neg+TOB5',
          'TEC1_neg+TOB4',
          'TEC1_pos+TOB6',
          'TEC1_pos+TOB5',
          'TEC1_pos+TOB4' ),
        TEC = cms.PSet( 
          useRingSlector = cms.bool( False ),
          TTRHBuilder = cms.string( "WithTrackAngle" ),
          minRing = cms.int32( 6 ),
          maxRing = cms.int32( 7 )
        )
      )
    ),
    SeedCreatorPSet = cms.PSet( 
      ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
      SeedMomentumForBOFF = cms.double( 5.0 ),
      propagator = cms.string( "PropagatorWithMaterial" ),
      maxseeds = cms.int32( 10000 )
    ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
)
process.hltRegionalCandidatesForL3MuonIsolation = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltRegionalSeedsForL3MuonIsolation" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "hltESPCkfTrajectoryBuilder" )
)
process.hltRegionalTracksForL3MuonIsolation = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltRegionalCandidatesForL3MuonIsolation" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    Propagator = cms.string( "PropagatorWithMaterial" )
)
process.hltL3MuonCombRelIsolations = cms.EDProducer( "L3MuonCombinedRelativeIsolationProducer",
    printDebug = cms.bool( False ),
    CutsPSet = cms.PSet( 
      ConeSizes = cms.vdouble( 0.24 ),
      ComponentName = cms.string( "SimpleCuts" ),
      Thresholds = cms.vdouble( 0.1 ),
      maxNTracks = cms.int32( -1 ),
      EtaBounds = cms.vdouble( 2.411 ),
      applyCutsORmaxNTracks = cms.bool( False )
    ),
    OutputMuIsoDeposits = cms.bool( True ),
    TrackPt_Min = cms.double( -1.0 ),
    CaloExtractorPSet = cms.PSet( 
      DR_Veto_H = cms.double( 0.1 ),
      Vertex_Constraint_Z = cms.bool( False ),
      Threshold_H = cms.double( 0.5 ),
      ComponentName = cms.string( "CaloExtractor" ),
      Threshold_E = cms.double( 0.2 ),
      DR_Max = cms.double( 0.24 ),
      DR_Veto_E = cms.double( 0.07 ),
      Weight_E = cms.double( 1.5 ),
      Vertex_Constraint_XY = cms.bool( False ),
      DepositLabel = cms.untracked.string( "EcalPlusHcal" ),
      CaloTowerCollectionLabel = cms.InputTag( "hltTowerMakerForMuons" ),
      Weight_H = cms.double( 1.0 )
    ),
    inputMuonCollection = cms.InputTag( "hltL3Muons" ),
    TrkExtractorPSet = cms.PSet( 
      DR_VetoPt = cms.double( 0.025 ),
      Diff_z = cms.double( 0.2 ),
      inputTrackCollection = cms.InputTag( "hltRegionalTracksForL3MuonIsolation" ),
      ReferenceRadius = cms.double( 6.0 ),
      BeamSpotLabel = cms.InputTag( "hltOnlineBeamSpot" ),
      ComponentName = cms.string( "PixelTrackExtractor" ),
      DR_Max = cms.double( 0.24 ),
      Diff_r = cms.double( 0.1 ),
      PropagateTracksToRadius = cms.bool( True ),
      Chi2Prob_Min = cms.double( -1.0 ),
      DR_Veto = cms.double( 0.01 ),
      NHits_Min = cms.uint32( 0 ),
      Chi2Ndof_Max = cms.double( 1.0E64 ),
      Pt_Min = cms.double( -1.0 ),
      DepositLabel = cms.untracked.string( "PXLS" ),
      BeamlineOption = cms.string( "BeamSpotFromEvent" ),
      VetoLeadingTrack = cms.bool( True ),
      PtVeto_Min = cms.double( 2.0 )
    )
)
process.hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoFiltered10 = cms.EDFilter( "HLTMuonIsoFilter",
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered24Q" ),
    MinN = cms.int32( 1 ),
    IsolatorPSet = cms.PSet(  ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    DepTag = cms.VInputTag( 'hltL3MuonCombRelIsolations' )
)
process.hltL1sL1Mu12EG7 = cms.EDFilter( "HLTLevel1GTSeed",
    saveTags = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_Mu12_EG7" ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreMu17Ele8CaloIdTCaloIsoVLTrkIdVLTrkIsoVL = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltL1Mu12EG7L1MuFiltered0 = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1Mu12EG7" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltL1Mu12EG7L2MuFiltered0 = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltL1Mu12EG7L1MuFiltered0" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltL1Mu12EG7L3MuFiltered17 = cms.EDFilter( "HLTMuonL3PreFilter",
    MaxNormalizedChi2 = cms.double( 9999.0 ),
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL1Mu12EG7L2MuFiltered0" ),
    MinNmuonHits = cms.int32( 0 ),
    MinN = cms.int32( 1 ),
    MinTrackPt = cms.double( 0.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxDXYBeamSpot = cms.double( 9999.0 ),
    MinNhits = cms.int32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MaxDz = cms.double( 9999.0 ),
    MaxPtDifference = cms.double( 9999.0 ),
    MaxDr = cms.double( 2.0 ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    MinDr = cms.double( -1.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinPt = cms.double( 17.0 )
)
process.hltEGRegionalL1Mu12EG7 = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    saveTags = cms.bool( False ),
    endcap_end = cms.double( 2.65 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    barrel_end = cms.double( 1.4791 ),
    l1IsolatedTag = cms.InputTag( 'hltL1extraParticles','Isolated' ),
    candIsolatedTag = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    region_phi_size = cms.double( 1.044 ),
    region_eta_size = cms.double( 0.522 ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1Mu12EG7" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    candNonIsolatedTag = cms.InputTag( "" ),
    l1NonIsolatedTag = cms.InputTag( 'hltL1extraParticles','NonIsolated' )
)
process.hltEG8EtFilterL1Mu12EG7 = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( False ),
    L1NonIsoCand = cms.InputTag( "" ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    inputTag = cms.InputTag( "hltEGRegionalL1Mu12EG7" ),
    etcutEB = cms.double( 8.0 ),
    ncandcut = cms.int32( 1 ),
    etcutEE = cms.double( 8.0 )
)
process.hltMu17Ele8CaloIdTCaloIsoVLTrkIdVLTrkIsoVLClusterShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 0.031 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 0.011 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededHLTClusterShape" ),
    candTag = cms.InputTag( "hltEG8EtFilterL1Mu12EG7" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltL1SeededPhotonEcalIso = cms.EDProducer( "EgammaHLTEcalRecIsolationProducer",
    etMinEndcap = cms.double( 0.11 ),
    tryBoth = cms.bool( True ),
    ecalBarrelRecHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useNumCrystals = cms.bool( True ),
    etMinBarrel = cms.double( -9999.0 ),
    doRhoCorrection = cms.bool( False ),
    eMinEndcap = cms.double( -9999.0 ),
    intRadiusEndcap = cms.double( 3.0 ),
    jurassicWidth = cms.double( 3.0 ),
    useIsolEt = cms.bool( True ),
    ecalBarrelRecHitCollection = cms.InputTag( "EcalRecHitsEB" ),
    recoEcalCandidateProducer = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    eMinBarrel = cms.double( 0.095 ),
    effectiveAreaEndcap = cms.double( 0.046 ),
    ecalEndcapRecHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" ),
    extRadius = cms.double( 0.3 ),
    intRadiusBarrel = cms.double( 3.0 ),
    subtract = cms.bool( False ),
    rhoScale = cms.double( 1.0 ),
    effectiveAreaBarrel = cms.double( 0.101 ),
    ecalEndcapRecHitCollection = cms.InputTag( "EcalRecHitsEE" ),
    rhoProducer = cms.InputTag( 'hltKT6CaloJets','rho' )
)
process.hltMu17Ele8CaloIdTCaloIsoVLTrkIdVLTrkIsoVLEcalIsoFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.2 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( 0.2 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededPhotonEcalIso" ),
    candTag = cms.InputTag( "hltMu17Ele8CaloIdTCaloIsoVLTrkIdVLTrkIsoVLClusterShapeFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltMu17Ele8CaloIdTCaloIsoVLTrkIdVLTrkIsoVLHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.1 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( 0.15 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededPhotonHcalForHE" ),
    candTag = cms.InputTag( "hltMu17Ele8CaloIdTCaloIsoVLTrkIdVLTrkIsoVLEcalIsoFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltL1SeededPhotonHcalIso = cms.EDProducer( "EgammaHLTHcalIsolationProducersRegional",
    eMinHE = cms.double( 0.8 ),
    hbheRecHitProducer = cms.InputTag( "hltHbhereco" ),
    effectiveAreaBarrel = cms.double( 0.105 ),
    outerCone = cms.double( 0.29 ),
    eMinHB = cms.double( 0.7 ),
    innerCone = cms.double( 0.16 ),
    etMinHE = cms.double( -1.0 ),
    etMinHB = cms.double( -1.0 ),
    rhoProducer = cms.InputTag( 'hltKT6CaloJets','rho' ),
    depth = cms.int32( -1 ),
    doRhoCorrection = cms.bool( False ),
    effectiveAreaEndcap = cms.double( 0.17 ),
    recoEcalCandidateProducer = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    rhoMax = cms.double( 9.9999999E7 ),
    rhoScale = cms.double( 1.0 ),
    doEtSum = cms.bool( True )
)
process.hltMu17Ele8CaloIdTCaloIsoVLTrkIdVLTrkIsoVLHcalIsoFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.2 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( 0.2 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededPhotonHcalIso" ),
    candTag = cms.InputTag( "hltMu17Ele8CaloIdTCaloIsoVLTrkIdVLTrkIsoVLHEFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltMu17Ele8CaloIdTCaloIsoVLTrkIdVLTrkIsoVLPixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    saveTags = cms.bool( False ),
    doIsolated = cms.bool( True ),
    L1NonIsoCand = cms.InputTag( "" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "" ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    candTag = cms.InputTag( "hltMu17Ele8CaloIdTCaloIsoVLTrkIdVLTrkIsoVLHcalIsoFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltL1SeededStartUpElectronPixelSeeds" )
)
process.hltMu17Ele8CaloIdTCaloIsoVLTrkIdVLTrkIsoVLOneOEMinusOneOPFilter = cms.EDFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    saveTags = cms.bool( False ),
    doIsolated = cms.bool( True ),
    electronNonIsolatedProducer = cms.InputTag( "" ),
    barrelcut = cms.double( 999.9 ),
    electronIsolatedProducer = cms.InputTag( "hltPixelMatch3HitElectronsL1Seeded" ),
    ncandcut = cms.int32( 1 ),
    candTag = cms.InputTag( "hltMu17Ele8CaloIdTCaloIsoVLTrkIdVLTrkIsoVLPixelMatchFilter" ),
    endcapcut = cms.double( 999.9 )
)
process.hltMu17Ele8CaloIdTCaloIsoVLTrkIdVLTrkIsoVLDetaFilter = cms.EDFilter( "HLTElectronGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    thrTimesPtEB = cms.double( -1.0 ),
    saveTags = cms.bool( False ),
    thrRegularEE = cms.double( 0.01 ),
    L1IsoCand = cms.InputTag( "hltPixelMatch3HitElectronsL1Seeded" ),
    thrRegularEB = cms.double( 0.01 ),
    lessThan = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( 'hlt3HitElectronL1SeededDetaDphi','Deta' ),
    candTag = cms.InputTag( "hltMu17Ele8CaloIdTCaloIsoVLTrkIdVLTrkIsoVLOneOEMinusOneOPFilter" ),
    thrTimesPtEE = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrOverPtEB = cms.double( -1.0 )
)
process.hltMu17Ele8CaloIdTCaloIsoVLTrkIdVLTrkIsoVLDphiFilter = cms.EDFilter( "HLTElectronGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    thrTimesPtEB = cms.double( -1.0 ),
    saveTags = cms.bool( False ),
    thrRegularEE = cms.double( 0.1 ),
    L1IsoCand = cms.InputTag( "hltPixelMatch3HitElectronsL1Seeded" ),
    thrRegularEB = cms.double( 0.15 ),
    lessThan = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( 'hlt3HitElectronL1SeededDetaDphi','Dphi' ),
    candTag = cms.InputTag( "hltMu17Ele8CaloIdTCaloIsoVLTrkIdVLTrkIsoVLDetaFilter" ),
    thrTimesPtEE = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrOverPtEB = cms.double( -1.0 )
)
process.hltL1Seeded3HitElectronTrackIso = cms.EDProducer( "EgammaHLTElectronTrackIsolationProducers",
    egTrkIsoStripEndcap = cms.double( 0.03 ),
    electronProducer = cms.InputTag( "hltPixelMatch3HitElectronsL1Seeded" ),
    egTrkIsoZSpan = cms.double( 0.15 ),
    useGsfTrack = cms.bool( False ),
    useSCRefs = cms.bool( False ),
    egTrkIsoConeSize = cms.double( 0.3 ),
    trackProducer = cms.InputTag( "hltL1SeededEgammaRegionalCTFFinalFitWithMaterial" ),
    egTrkIsoStripBarrel = cms.double( 0.03 ),
    egTrkIsoVetoConeSizeBarrel = cms.double( 0.03 ),
    egTrkIsoVetoConeSize = cms.double( 0.03 ),
    egTrkIsoRSpan = cms.double( 999999.0 ),
    egTrkIsoVetoConeSizeEndcap = cms.double( 0.03 ),
    recoEcalCandidateProducer = cms.InputTag( "" ),
    beamSpotProducer = cms.InputTag( "hltOnlineBeamSpot" ),
    egTrkIsoPtMin = cms.double( 1.0 ),
    egCheckForOtherEleInCone = cms.untracked.bool( False )
)
process.hltMu17Ele8CaloIdTCaloIsoVLTrkIdVLTrkIsoVLTrackIsoFilter = cms.EDFilter( "HLTElectronGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    thrTimesPtEB = cms.double( -1.0 ),
    saveTags = cms.bool( True ),
    thrRegularEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltPixelMatch3HitElectronsL1Seeded" ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1Seeded3HitElectronTrackIso" ),
    candTag = cms.InputTag( "hltMu17Ele8CaloIdTCaloIsoVLTrkIdVLTrkIsoVLOneOEMinusOneOPFilter" ),
    thrTimesPtEE = cms.double( -1.0 ),
    thrOverPtEE = cms.double( 0.2 ),
    thrOverPtEB = cms.double( 0.2 )
)
process.hltMu17Ele8dZFilter = cms.EDFilter( "HLT2ElectronMuonDZ",
    saveTags = cms.bool( True ),
    originTag1 = cms.InputTag( "hltOriginal1" ),
    originTag2 = cms.InputTag( "hltOriginal2" ),
    MinN = cms.int32( 1 ),
    triggerType1 = cms.int32( 82 ),
    triggerType2 = cms.int32( 83 ),
    MinDR = cms.double( -1.0 ),
    MaxDZ = cms.double( 0.2 ),
    inputTag1 = cms.InputTag( "hltMu17Ele8CaloIdTCaloIsoVLTrkIdVLTrkIsoVLTrackIsoFilter" ),
    inputTag2 = cms.InputTag( "hltL1Mu12EG7L3MuFiltered17" )
)
process.hltL1sL1MuOpenEG12 = cms.EDFilter( "HLTLevel1GTSeed",
    saveTags = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_MuOpen_EG12" ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreMu8Ele17CaloIdTCaloIsoVLTrkIdVLTrkIsoVL = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltL1MuOpenEG12L1Filtered0 = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1MuOpenEG12" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltL1MuOpenEG12L2Filtered5 = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltL1MuOpenEG12L1Filtered0" ),
    MinPt = cms.double( 5.0 ),
    MinN = cms.int32( 1 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltL1MuOpenEG12L3Filtered8 = cms.EDFilter( "HLTMuonL3PreFilter",
    MaxNormalizedChi2 = cms.double( 9999.0 ),
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL1MuOpenEG12L2Filtered5" ),
    MinNmuonHits = cms.int32( 0 ),
    MinN = cms.int32( 1 ),
    MinTrackPt = cms.double( 0.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxDXYBeamSpot = cms.double( 9999.0 ),
    MinNhits = cms.int32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MaxDz = cms.double( 9999.0 ),
    MaxPtDifference = cms.double( 9999.0 ),
    MaxDr = cms.double( 2.0 ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    MinDr = cms.double( -1.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinPt = cms.double( 8.0 )
)
process.hltEGRegionalL1MuOpenEG12 = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    saveTags = cms.bool( False ),
    endcap_end = cms.double( 2.65 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    barrel_end = cms.double( 1.4791 ),
    l1IsolatedTag = cms.InputTag( 'hltL1extraParticles','Isolated' ),
    candIsolatedTag = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    region_phi_size = cms.double( 1.044 ),
    region_eta_size = cms.double( 0.522 ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1MuOpenEG12" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    candNonIsolatedTag = cms.InputTag( "" ),
    l1NonIsolatedTag = cms.InputTag( 'hltL1extraParticles','NonIsolated' )
)
process.hltMu8EG17EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( False ),
    L1NonIsoCand = cms.InputTag( "" ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    inputTag = cms.InputTag( "hltEGRegionalL1MuOpenEG12" ),
    etcutEB = cms.double( 17.0 ),
    ncandcut = cms.int32( 1 ),
    etcutEE = cms.double( 17.0 )
)
process.hltMu8Ele17CaloIdTClusterShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 0.031 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 0.011 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededHLTClusterShape" ),
    candTag = cms.InputTag( "hltMu8EG17EtFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltMu8Ele17CaloIdTCaloIsoVLEcalIsoFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.2 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( 0.2 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededPhotonEcalIso" ),
    candTag = cms.InputTag( "hltMu8Ele17CaloIdTClusterShapeFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltMu8Ele17CaloIdTCaloIsoVLHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.1 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( 0.15 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededPhotonHcalForHE" ),
    candTag = cms.InputTag( "hltMu8Ele17CaloIdTCaloIsoVLEcalIsoFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltMu8Ele17CaloIdTCaloIsoVLHcalIsoFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.2 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( 0.2 ),
    thrRegularEB = cms.double( 999999.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededPhotonHcalIso" ),
    candTag = cms.InputTag( "hltMu8Ele17CaloIdTCaloIsoVLHEFilter" ),
    thrOverE2EE = cms.double( -1.0 )
)
process.hltMu8Ele17CaloIdTCaloIsoVLPixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    saveTags = cms.bool( False ),
    doIsolated = cms.bool( True ),
    L1NonIsoCand = cms.InputTag( "" ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "" ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    candTag = cms.InputTag( "hltMu8Ele17CaloIdTCaloIsoVLHcalIsoFilter" ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltL1SeededStartUpElectronPixelSeeds" )
)
process.hltMu8Ele17CaloIdTCaloIsoVLOneOEMinusOneOPFilter = cms.EDFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    saveTags = cms.bool( False ),
    doIsolated = cms.bool( True ),
    electronNonIsolatedProducer = cms.InputTag( "" ),
    barrelcut = cms.double( 999.9 ),
    electronIsolatedProducer = cms.InputTag( "hltPixelMatch3HitElectronsL1Seeded" ),
    ncandcut = cms.int32( 1 ),
    candTag = cms.InputTag( "hltMu8Ele17CaloIdTCaloIsoVLPixelMatchFilter" ),
    endcapcut = cms.double( 999.9 )
)
process.hltMu8Ele17CaloIdTCaloIsoVLTrkIdVLDetaFilter = cms.EDFilter( "HLTElectronGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    thrTimesPtEB = cms.double( -1.0 ),
    saveTags = cms.bool( False ),
    thrRegularEE = cms.double( 0.01 ),
    L1IsoCand = cms.InputTag( "hltPixelMatch3HitElectronsL1Seeded" ),
    thrRegularEB = cms.double( 0.01 ),
    lessThan = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( 'hlt3HitElectronL1SeededDetaDphi','Deta' ),
    candTag = cms.InputTag( "hltMu8Ele17CaloIdTCaloIsoVLOneOEMinusOneOPFilter" ),
    thrTimesPtEE = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrOverPtEB = cms.double( -1.0 )
)
process.hltMu8Ele17CaloIdTCaloIsoVLTrkIdVLDphiFilter = cms.EDFilter( "HLTElectronGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    thrTimesPtEB = cms.double( -1.0 ),
    saveTags = cms.bool( False ),
    thrRegularEE = cms.double( 0.1 ),
    L1IsoCand = cms.InputTag( "hltPixelMatch3HitElectronsL1Seeded" ),
    thrRegularEB = cms.double( 0.15 ),
    lessThan = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( 'hlt3HitElectronL1SeededDetaDphi','Dphi' ),
    candTag = cms.InputTag( "hltMu8Ele17CaloIdTCaloIsoVLTrkIdVLDetaFilter" ),
    thrTimesPtEE = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrOverPtEB = cms.double( -1.0 )
)
process.hltMu8Ele17CaloIdTCaloIsoVLTrkIdVLTrkIsoVLTrackIsoFilter = cms.EDFilter( "HLTElectronGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    thrTimesPtEB = cms.double( -1.0 ),
    saveTags = cms.bool( True ),
    thrRegularEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltPixelMatch3HitElectronsL1Seeded" ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1Seeded3HitElectronTrackIso" ),
    candTag = cms.InputTag( "hltMu8Ele17CaloIdTCaloIsoVLTrkIdVLDphiFilter" ),
    thrTimesPtEE = cms.double( -1.0 ),
    thrOverPtEE = cms.double( 0.2 ),
    thrOverPtEB = cms.double( 0.2 )
)
process.hltMu8Ele17dZFilter = cms.EDFilter( "HLT2ElectronMuonDZ",
    saveTags = cms.bool( False ),
    originTag1 = cms.InputTag( "hltOriginal1" ),
    originTag2 = cms.InputTag( "hltOriginal2" ),
    MinN = cms.int32( 1 ),
    triggerType1 = cms.int32( 82 ),
    triggerType2 = cms.int32( 83 ),
    MinDR = cms.double( -1.0 ),
    MaxDZ = cms.double( 0.2 ),
    inputTag1 = cms.InputTag( "hltMu8Ele17CaloIdTCaloIsoVLTrkIdVLTrkIsoVLTrackIsoFilter" ),
    inputTag2 = cms.InputTag( "hltL1MuOpenEG12L3Filtered8" )
)
process.hltFEDSelector = cms.EDProducer( "EvFFEDSelector",
    inputTag = cms.InputTag( "rawDataCollector" ),
    fedList = cms.vuint32( 1023 )
)
process.hltTriggerSummaryAOD = cms.EDProducer( "TriggerSummaryProducerAOD",
    processName = cms.string( "@" )
)
process.hltTriggerSummaryRAW = cms.EDProducer( "TriggerSummaryProducerRAW",
    processName = cms.string( "@" )
)

process.HLTL1UnpackerSequence = cms.Sequence( process.hltGtDigis + process.hltGctDigis + process.hltL1GtObjectMap + process.hltL1extraParticles )
process.HLTBeamSpot = cms.Sequence( process.hltScalersRawToDigi + process.hltOnlineBeamSpot + process.hltOfflineBeamSpot )
process.HLTBeginSequence = cms.Sequence( process.hltTriggerType + process.HLTL1UnpackerSequence + process.HLTBeamSpot )
process.HLTDoRegionalEgammaEcalSequence = cms.Sequence( process.hltESRawToRecHitFacility + process.hltEcalRawToRecHitFacility + process.hltEcalRegionalEgammaFEDs + process.hltEcalRegionalEgammaRecHit + process.hltESRegionalEgammaRecHit )
process.HLTMulti5x5SuperClusterL1Seeded = cms.Sequence( process.hltMulti5x5BasicClustersL1Seeded + process.hltMulti5x5SuperClustersL1Seeded + process.hltMulti5x5EndcapSuperClustersWithPreshowerL1Seeded + process.hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Seeded )
process.HLTL1SeededEcalClustersSequence = cms.Sequence( process.hltHybridSuperClustersL1Seeded + process.hltCorrectedHybridSuperClustersL1Seeded + process.HLTMulti5x5SuperClusterL1Seeded )
process.HLTDoLocalHcalWithoutHOSequence = cms.Sequence( process.hltHcalDigis + process.hltHbhereco + process.hltHfreco )
process.HLTPhoton70Sequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1SeededEcalClustersSequence + process.hltL1SeededRecoEcalCandidate + process.hltEGRegionalL1SingleEG30 + process.hltEG70EtFilterL1EG30 + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1SeededPhotonHcalForHE + process.hltEG70HEFilter )
process.HLTEcalActivitySequence = cms.Sequence( process.hltEcalRawToRecHitFacility + process.hltESRawToRecHitFacility + process.hltEcalRegionalRestFEDs + process.hltEcalRegionalESRestFEDs + process.hltEcalRecHitAll + process.hltESRecHitAll + process.hltHybridSuperClustersActivity + process.hltCorrectedHybridSuperClustersActivity + process.hltMulti5x5BasicClustersActivity + process.hltMulti5x5SuperClustersActivity + process.hltMulti5x5SuperClustersWithPreshowerActivity + process.hltCorrectedMulti5x5SuperClustersWithPreshowerActivity + process.hltRecoEcalSuperClusterActivityCandidate + process.hltEcalActivitySuperClusterWrapper )
process.HLTDoublePhoton70UnseededLegSequence = cms.Sequence( process.HLTEcalActivitySequence + process.hltDoubleEG70EtDoubleFilter + process.hltActivityPhotonHcalForHE + process.hltDoubleEG70HEDoubleFilter )
process.HLTEndSequence = cms.Sequence( process.hltBoolEnd )
process.HLTDoublePhoton80Sequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1SeededEcalClustersSequence + process.hltL1SeededRecoEcalCandidate + process.hltEGRegionalL1SingleEG30 + process.hltEG80EtFilterL1EG30 + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1SeededPhotonHcalForHE + process.hltEG80HEFilter + process.HLTEcalActivitySequence + process.hltDoubleIsoEG80EtFilterUnseededTight + process.hltActivityPhotonHcalForHE + process.hltDoublePhoton80EgammaLHEDoubleFilter )
process.HLTSinglePhoton135Sequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1SeededEcalClustersSequence + process.hltL1SeededRecoEcalCandidate + process.hltEGRegionalL1SingleEG30 + process.hltEG135EtFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1SeededPhotonHcalForHE + process.hltPhoton135HEFilter )
process.HLTSinglePhoton150Sequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1SeededEcalClustersSequence + process.hltL1SeededRecoEcalCandidate + process.hltEGRegionalL1SingleEG30 + process.hltEG150EtFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1SeededPhotonHcalForHE + process.hltPhoton150HEFilter )
process.HLTSinglePhoton160Sequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1SeededEcalClustersSequence + process.hltL1SeededRecoEcalCandidate + process.hltEGRegionalL1SingleEG30 + process.hltEG160EtFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1SeededPhotonHcalForHE + process.hltPhoton160HEFilter )
process.HLTSinglePhoton250NoHESequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1SeededEcalClustersSequence + process.hltL1SeededRecoEcalCandidate + process.hltEGRegionalL1SingleEG30 + process.hltEG300EtFilter )
process.HLTSinglePhoton300NoHESequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1SeededEcalClustersSequence + process.hltL1SeededRecoEcalCandidate + process.hltEGRegionalL1SingleEG30 + process.hltEG300EtFilter )
process.HLTDoLocalPixelSequence = cms.Sequence( process.hltSiPixelDigis + process.hltSiPixelClusters + process.hltSiPixelRecHits )
process.HLTDoLocalStripSequence = cms.Sequence( process.hltSiStripExcludedFEDListProducer + process.hltSiStripRawToClustersFacility + process.hltSiStripClusters )
process.HLTPixelMatchElectronL1SeededTrackingSequence = cms.Sequence( process.hltCkfL1SeededTrackCandidates + process.hltCtfL1SeededWithMaterialTracks + process.hltPixelMatchElectronsL1Seeded )
process.HLTEle65CaloIdVTTrkIdTSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1SeededEcalClustersSequence + process.hltL1SeededRecoEcalCandidate + process.hltEGRegionalL1SingleEG20 + process.hltEG65EtFilter + process.hltL1SeededHLTClusterShape + process.hltEG65CaloIdTClusterShapeFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1SeededPhotonHcalForHE + process.hltEG65CaloIdVTHEFilter + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL1SeededStartUpElectronPixelSeeds + process.hltEle65CaloIdVTPixelMatchFilter + process.HLTPixelMatchElectronL1SeededTrackingSequence + process.hltEle65CaloIdVTOneOEMinusOneOPFilter + process.hltElectronL1SeededDetaDphi + process.hltEle65CaloIdVTTrkIdTDetaFilter + process.hltEle65CaloIdVTTrkIdTDphiFilter )
process.HLTEle80CaloIdVTTrkIdTSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1SeededEcalClustersSequence + process.hltL1SeededRecoEcalCandidate + process.hltEGRegionalL1SingleEG20 + process.hltEG80EtFilter + process.hltL1SeededHLTClusterShape + process.hltEG80CaloIdTClusterShapeFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1SeededPhotonHcalForHE + process.hltEG80CaloIdVTHEFilter + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL1SeededStartUpElectronPixelSeeds + process.hltEle80CaloIdVTPixelMatchFilter + process.HLTPixelMatchElectronL1SeededTrackingSequence + process.hltEle80CaloIdVTOneOEMinusOneOPFilter + process.hltElectronL1SeededDetaDphi + process.hltEle80CaloIdVTTrkIdTDetaFilter + process.hltEle80CaloIdVTTrkIdTDphiFilter )
process.HLTEle100CaloIdVTTrkIdTSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1SeededEcalClustersSequence + process.hltL1SeededRecoEcalCandidate + process.hltEGRegionalL1SingleEG20 + process.hltEG100EtFilter + process.hltL1SeededHLTClusterShape + process.hltEG100CaloIdTClusterShapeFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1SeededPhotonHcalForHE + process.hltEG100CaloIdVTHEFilter + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL1SeededStartUpElectronPixelSeeds + process.hltEle100CaloIdVTPixelMatchFilter + process.HLTPixelMatchElectronL1SeededTrackingSequence + process.hltEle100CaloIdVTOneOEMinusOneOPFilter + process.hltElectronL1SeededDetaDphi + process.hltEle100CaloIdVTTrkIdTDetaFilter + process.hltEle100CaloIdVTTrkIdTDphiFilter )
process.HLTPhoton33Sequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1SeededEcalClustersSequence + process.hltL1SeededRecoEcalCandidate + process.hltEGRegionalL1SingleEG22 + process.hltEG33EtFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1SeededPhotonHcalForHE + process.hltEG33HEFilter )
process.HLTDoublePhoton33UnseededLegSequence = cms.Sequence( process.HLTEcalActivitySequence + process.hltDoubleEG33EtDoubleFilter + process.hltActivityPhotonHcalForHE + process.hltDoubleEG33HEDoubleFilter )
process.HLTActivityPixelMatchSequence = cms.Sequence( process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltActivityStartUpElectronPixelSeeds )
process.HLTActivityGsfElectronSequence = cms.Sequence( process.hltActivityCkfTrackCandidatesForGSF + process.hltActivityElectronGsfTracks + process.hltActivityGsfElectrons + process.hltActivityGsfTrackVars )
process.HLTEle33CaloIdTSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1SeededEcalClustersSequence + process.hltL1SeededRecoEcalCandidate + process.hltEGRegionalL1SingleEG22 + process.hltEG33EtFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1SeededPhotonHcalForHE + process.hltEG33CaloIdTHEFilter + process.hltL1SeededHLTClusterShape + process.hltEG33CaloIdTClusterShapeFilter + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL1SeededStartUpElectronPixelSeeds + process.hltEle33CaloIdTPixelMatchFilter )
process.HLTDoubleEle33CaloIdTUnseededLegSequence = cms.Sequence( process.HLTEcalActivitySequence + process.hltDoubleEG33EtDoubleFilter + process.hltActivityPhotonHcalForHE + process.hltDoubleEG33HEDoubleFilter + process.hltDoubleEG33CaloIdTHEDoubleFilter + process.hltActivityPhotonClusterShape + process.hltDoubleEG33CaloIdTClusterShapeDoubleFilter + process.HLTActivityPixelMatchSequence + process.hltDiEle33CaloIdTPixelMatchDoubleFilter )
process.HLTL1SeededEgammaRegionalRecoTrackerSequence = cms.Sequence( process.hltL1SeededEgammaRegionalPixelSeedGenerator + process.hltL1SeededEgammaRegionalCkfTrackCandidates + process.hltL1SeededEgammaRegionalCTFFinalFitWithMaterial )
process.HLTEcalActivityEgammaRegionalRecoTrackerSequence = cms.Sequence( process.hltEcalActivityEgammaRegionalPixelSeedGenerator + process.hltEcalActivityEgammaRegionalCkfTrackCandidates + process.hltEcalActivityEgammaRegionalCTFFinalFitWithMaterial )
process.HLTEle17CaloIdTTrkIdVLCaloIsoVLTrkIsoVLEle8CaloIdTTrkIdVLCaloIsoVLTrkIsoVLSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1SeededEcalClustersSequence + process.hltL1SeededRecoEcalCandidate + process.hltEGRegionalL1DoubleEG137 + process.hltEG17EtFilterDoubleEG137 + process.hltL1SeededHLTClusterShape + process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoClusterShapeFilter + process.hltL1SeededPhotonEcalIsol + process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoEcalIsoFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1SeededPhotonHcalForHE + process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoHEFilter + process.hltL1SeededPhotonHcalIsol + process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoHcalIsoFilter + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL1SeededStartUpElectronPixelSeeds + process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoPixelMatchFilter + process.hltCkf3HitL1SeededTrackCandidates + process.hltCtf3HitL1SeededWithMaterialTracks + process.hltPixelMatch3HitElectronsL1Seeded + process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoOneOEMinusOneOPFilter + process.hlt3HitElectronL1SeededDetaDphi + process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoDetaFilter + process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoDphiFilter + process.HLTL1SeededEgammaRegionalRecoTrackerSequence + process.hltL1Seeded3HitElectronTrackIsol + process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoTrackIsolFilter + process.HLTEcalActivitySequence + process.hltDoubleEG8EtFilterUnseeded + process.hltActivityPhotonClusterShape + process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoClusterShapeDoubleFilter + process.hltActivityPhotonEcalIsol + process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoEcalIsolDoubleFilter + process.hltActivityPhotonHcalForHE + process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoHEDoubleFilter + process.hltActivityPhotonHcalIsol + process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoHcalIsolDoubleFilter + process.hltActivityStartUpElectronPixelSeeds + process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoPixelMatchDoubleFilter + process.hltCkf3HitActivityTrackCandidates + process.hltCtf3HitActivityWithMaterialTracks + process.hltPixelMatch3HitElectronsActivity + process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoOneOEMinusOneOPDoubleFilter + process.hlt3HitElectronActivityDetaDphi + process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoDetaDoubleFilter + process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoDphiDoubleFilter + process.HLTEcalActivityEgammaRegionalRecoTrackerSequence + process.hlt3HitElectronActivityTrackIsol + process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoTrackIsolDoubleFilter + process.hltEle17TightIdLooseIsoEle8TightIdLooseIsoTrackIsolDZ )
process.HLTMuonLocalRecoSequence = cms.Sequence( process.hltMuonDTDigis + process.hltDt1DRecHits + process.hltDt4DSegments + process.hltMuonCSCDigis + process.hltCsc2DRecHits + process.hltCscSegments + process.hltMuonRPCDigis + process.hltRpcRecHits )
process.HLTL2muonrecoNocandSequence = cms.Sequence( process.HLTMuonLocalRecoSequence + process.hltL2OfflineMuonSeeds + process.hltL2MuonSeeds + process.hltL2Muons )
process.HLTL2muonrecoSequence = cms.Sequence( process.HLTL2muonrecoNocandSequence + process.hltL2MuonCandidates )
process.HLTL3muonTkCandidateSequence = cms.Sequence( process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL3TrajSeedOIState + process.hltL3TrackCandidateFromL2OIState + process.hltL3TkTracksFromL2OIState + process.hltL3MuonsOIState + process.hltL3TrajSeedOIHit + process.hltL3TrackCandidateFromL2OIHit + process.hltL3TkTracksFromL2OIHit + process.hltL3MuonsOIHit + process.hltL3TkFromL2OICombination + process.hltL3TrajSeedIOHit + process.hltL3TrackCandidateFromL2IOHit + process.hltL3TkTracksFromL2IOHit + process.hltL3MuonsIOHit + process.hltL3TrajectorySeed + process.hltL3TrackCandidateFromL2 )
process.HLTL3muonrecoNocandSequence = cms.Sequence( process.HLTL3muonTkCandidateSequence + process.hltL3TkTracksFromL2 + process.hltL3MuonsLinksCombination + process.hltL3Muons )
process.HLTL3muonrecoSequence = cms.Sequence( process.HLTL3muonrecoNocandSequence + process.hltL3MuonCandidates )
process.HLTDoEGammaStartupSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1SeededEcalClustersSequence + process.hltL1SeededRecoEcalCandidate )
process.HLTDoEgammaClusterShapeSequence = cms.Sequence( process.hltL1SeededHLTClusterShape )
process.HLTDoEGammaHESequence = cms.Sequence( process.HLTDoLocalHcalWithoutHOSequence + process.hltL1SeededPhotonHcalForHE )
process.HLTTrackerMuonSequence = cms.Sequence( process.HLTDoLocalPixelSequence + process.hltPixelTracks + process.HLTDoLocalStripSequence + process.hltMuTrackSeeds + process.hltMuCkfTrackCandidates + process.hltMuCtfTracks + process.HLTL3muonrecoNocandSequence + process.hltDiMuonMerging + process.hltDiMuonLinks + process.hltGlbTrkMuons + process.hltGlbTrkMuonCands )
process.HLTDoLocalHcalSequence = cms.Sequence( process.hltHcalDigis + process.hltHbhereco + process.hltHfreco + process.hltHoreco )
process.HLTL3muoncaloisorecoSequenceNoBools = cms.Sequence( process.hltEcalRawToRecHitFacility + process.hltEcalRegionalMuonsFEDs + process.hltEcalRegionalMuonsRecHit + process.HLTDoLocalHcalSequence + process.hltTowerMakerForMuons )
process.HLTRegionalCKFTracksForL3Isolation = cms.Sequence( process.hltRegionalSeedsForL3MuonIsolation + process.hltRegionalCandidatesForL3MuonIsolation + process.hltRegionalTracksForL3MuonIsolation )
process.HLTL3muonisorecoSequence = cms.Sequence( process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.HLTRegionalCKFTracksForL3Isolation + process.hltL3MuonCombRelIsolations )
process.HLTMu17Ele8CaloIdTTrkIdVLCaloIsoVLTrkIsoVLSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1SeededEcalClustersSequence + process.hltL1SeededRecoEcalCandidate + process.hltEGRegionalL1Mu12EG7 + process.hltEG8EtFilterL1Mu12EG7 + process.hltL1SeededHLTClusterShape + process.hltMu17Ele8CaloIdTCaloIsoVLTrkIdVLTrkIsoVLClusterShapeFilter + process.hltL1SeededPhotonEcalIso + process.hltMu17Ele8CaloIdTCaloIsoVLTrkIdVLTrkIsoVLEcalIsoFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1SeededPhotonHcalForHE + process.hltMu17Ele8CaloIdTCaloIsoVLTrkIdVLTrkIsoVLHEFilter + process.hltL1SeededPhotonHcalIso + process.hltMu17Ele8CaloIdTCaloIsoVLTrkIdVLTrkIsoVLHcalIsoFilter + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL1SeededStartUpElectronPixelSeeds + process.hltMu17Ele8CaloIdTCaloIsoVLTrkIdVLTrkIsoVLPixelMatchFilter + process.hltCkf3HitL1SeededTrackCandidates + process.hltCtf3HitL1SeededWithMaterialTracks + process.hltPixelMatch3HitElectronsL1Seeded + process.hltMu17Ele8CaloIdTCaloIsoVLTrkIdVLTrkIsoVLOneOEMinusOneOPFilter + process.hlt3HitElectronL1SeededDetaDphi + process.hltMu17Ele8CaloIdTCaloIsoVLTrkIdVLTrkIsoVLDetaFilter + process.hltMu17Ele8CaloIdTCaloIsoVLTrkIdVLTrkIsoVLDphiFilter + process.HLTL1SeededEgammaRegionalRecoTrackerSequence + process.hltL1Seeded3HitElectronTrackIso + process.hltMu17Ele8CaloIdTCaloIsoVLTrkIdVLTrkIsoVLTrackIsoFilter )
process.HLTMu8Ele17CaloIdTCaloIsoVLTrkIdVLTrkIsoVLSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1SeededEcalClustersSequence + process.hltL1SeededRecoEcalCandidate + process.hltEGRegionalL1MuOpenEG12 + process.hltMu8EG17EtFilter + process.hltL1SeededHLTClusterShape + process.hltMu8Ele17CaloIdTClusterShapeFilter + process.hltL1SeededPhotonEcalIso + process.hltMu8Ele17CaloIdTCaloIsoVLEcalIsoFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1SeededPhotonHcalForHE + process.hltMu8Ele17CaloIdTCaloIsoVLHEFilter + process.hltL1SeededPhotonHcalIso + process.hltMu8Ele17CaloIdTCaloIsoVLHcalIsoFilter + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL1SeededStartUpElectronPixelSeeds + process.hltMu8Ele17CaloIdTCaloIsoVLPixelMatchFilter + process.hltCkf3HitL1SeededTrackCandidates + process.hltCtf3HitL1SeededWithMaterialTracks + process.hltPixelMatch3HitElectronsL1Seeded + process.hltMu8Ele17CaloIdTCaloIsoVLOneOEMinusOneOPFilter + process.hlt3HitElectronL1SeededDetaDphi + process.hltMu8Ele17CaloIdTCaloIsoVLTrkIdVLDetaFilter + process.hltMu8Ele17CaloIdTCaloIsoVLTrkIdVLDphiFilter + process.HLTL1SeededEgammaRegionalRecoTrackerSequence + process.hltL1Seeded3HitElectronTrackIso + process.hltMu8Ele17CaloIdTCaloIsoVLTrkIdVLTrkIsoVLTrackIsoFilter )

process.HLT_DoublePhoton70_v3 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG30 + process.hltPreDoublePhoton70 + process.HLTPhoton70Sequence + process.HLTDoublePhoton70UnseededLegSequence + process.HLTEndSequence )
process.HLT_DoublePhoton80_v4 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG30 + process.hltPreDoublePhoton80 + process.HLTDoublePhoton80Sequence + process.HLTEndSequence )
process.HLT_Photon135_v4 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG30 + process.hltPrePhoton135 + process.HLTSinglePhoton135Sequence + process.HLTEndSequence )
process.HLT_Photon150_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG30 + process.hltPrePhoton150 + process.HLTSinglePhoton150Sequence + process.HLTEndSequence )
process.HLT_Photon160_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG30 + process.hltPrePhoton160 + process.HLTSinglePhoton160Sequence + process.HLTEndSequence )
process.HLT_Photon250_NoHE_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG30 + process.hltPrePhoton250NoHE + process.HLTSinglePhoton250NoHESequence + process.HLTEndSequence )
process.HLT_Photon300_NoHE_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG30 + process.hltPrePhoton300NoHE + process.HLTSinglePhoton300NoHESequence + process.HLTEndSequence )
process.HLT_Ele65_CaloIdVT_TrkIdT_v8 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG20 + process.hltPreEle65CaloIdVTTrkIdT + process.HLTEle65CaloIdVTTrkIdTSequence + process.HLTEndSequence )
process.HLT_Ele80_CaloIdVT_TrkIdT_v5 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG20 + process.hltPreEle80CaloIdVTTrkIdT + process.HLTEle80CaloIdVTTrkIdTSequence + process.HLTEndSequence )
process.HLT_Ele100_CaloIdVT_TrkIdT_v5 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG20 + process.hltPreEle100CaloIdVTTrkIdT + process.HLTEle100CaloIdVTTrkIdTSequence + process.HLTEndSequence )
process.HLT_DoubleEle33_CaloIdL_v9 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG22 + process.hltPreDoubleEle33CaloIdL + process.HLTPhoton33Sequence + process.hltL1SeededHLTClusterShape + process.hltEG33CaloIdLClusterShapeFilter + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL1SeededStartUpElectronPixelSeeds + process.hltEle33CaloIdLPixelMatchFilter + process.HLTDoublePhoton33UnseededLegSequence + process.hltActivityPhotonClusterShape + process.hltDoubleEG33CaloIdLClusterShapeDoubleFilter + process.HLTActivityPixelMatchSequence + process.hltDiEle33CaloIdLPixelMatchDoubleFilter + process.HLTEndSequence )
process.HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG22 + process.hltPreDoubleEle33CaloIdLGsfTrkIdVL + process.HLTPhoton33Sequence + process.hltL1SeededHLTClusterShape + process.hltEG33CaloIdLClusterShapeFilter + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL1SeededStartUpElectronPixelSeeds + process.hltEle33CaloIdLPixelMatchFilter + process.HLTDoublePhoton33UnseededLegSequence + process.hltActivityPhotonClusterShape + process.hltDoubleEG33CaloIdLClusterShapeDoubleFilter + process.HLTActivityPixelMatchSequence + process.hltDiEle33CaloIdLPixelMatchDoubleFilter + process.HLTActivityGsfElectronSequence + process.hltDiEle33CaloIdLGsfTrkIdVLDEtaDoubleFilter + process.hltDiEle33CaloIdLGsfTrkIdVLDPhiDoubleFilter + process.HLTEndSequence )
process.HLT_DoubleEle33_CaloIdT_v5 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG22 + process.hltPreDoubleEle33CaloIdT + process.HLTEle33CaloIdTSequence + process.HLTDoubleEle33CaloIdTUnseededLegSequence + process.HLTEndSequence )
process.HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v12 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleEG137 + process.hltPreEle17CaloIdTCaloIsoVLTrkIdVLTrkIsoVLEle8CaloIdTCaloIsoVLTrkIdVLTrkIsoVL + process.HLTEle17CaloIdTTrkIdVLCaloIsoVLTrkIsoVLEle8CaloIdTTrkIdVLCaloIsoVLTrkIsoVLSequence + process.HLTEndSequence )
process.HLT_Mu22_Photon22_CaloIdL_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sL1Mu3p5EG12 + process.hltPreMu22Photon22CaloIdL + process.hltL1Mu3p5EG12L1Filtered3p5 + process.HLTL2muonrecoSequence + process.hltL1Mu3p5EG12L2Filtered12 + process.HLTL3muonrecoSequence + process.hltL1Mu3p5EG12L3Filtered22 + process.HLTDoEGammaStartupSequence + process.hltEGRegionalL1Mu3p5EG12 + process.hltEG22EtFilterL1Mu3p5EG12 + process.HLTDoEgammaClusterShapeSequence + process.hltMu22Photon22CaloIdLClusterShapeFilter + process.HLTDoEGammaHESequence + process.hltMu22Photon22CaloIdLHEFilter + process.HLTEndSequence )
process.HLT_Mu17_TkMu8_v7 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleMu10MuOpen + process.hltPreMu17TkMu8 + process.hltL1fL1sDoubleMu10MuOpenL1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu10MuOpenL1f0L2Filtered10 + process.HLTL3muonrecoSequence + process.hltL3fL1sMu10MuOpenL1f0L2f10L3Filtered17 + process.HLTTrackerMuonSequence + process.hltDiMuonGlbFiltered17TrkFiltered8 + process.hltDiMuonGlb17Trk8DzFiltered0p2 + process.HLTEndSequence )
process.HLT_Mu22_TkMu8_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sMu16Eta2p1 + process.hltPreMu22TkMu8 + process.hltL1fL1sMu16Eta2p1L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sMu16Eta2p1L1f0L2Filtered16Q + process.HLTL3muonrecoSequence + process.hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered22 + process.HLTTrackerMuonSequence + process.hltDiMuonGlbFiltered22TrkFiltered8 + process.hltDiMuonGlb22Trk8DzFiltered0p2 + process.HLTEndSequence )
process.HLT_Mu22_TkMu22_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sMu16Eta2p1 + process.hltPreMu22TkMu22 + process.hltL1fL1sMu16Eta2p1L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sMu16Eta2p1L1f0L2Filtered16Q + process.HLTL3muonrecoSequence + process.hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered22 + process.HLTTrackerMuonSequence + process.hltDiMuonGlbFiltered22TrkFiltered22 + process.hltDiMuonGlb22Trk22DzFiltered0p2 + process.HLTEndSequence )
process.HLT_Mu30_Ele30_CaloIdL_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sL1Mu3p5EG12 + process.hltPreMu30Ele30CaloIdL + process.hltL1Mu3p5EG12L1Filtered3p5 + process.HLTL2muonrecoSequence + process.hltL1Mu3p5EG12L2Filtered12 + process.HLTL3muonrecoSequence + process.hltL1Mu3p5EG12L3Filtered30 + process.HLTDoRegionalEgammaEcalSequence + process.HLTL1SeededEcalClustersSequence + process.hltL1SeededRecoEcalCandidate + process.hltEGRegionalL1Mu3p5EG12 + process.hltEG30EtFilterL1Mu3p5EG12 + process.hltL1SeededHLTClusterShape + process.hltMu3p5Photon30CaloIdLClusterShapeFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1SeededPhotonHcalForHE + process.hltMu3p5Photon30CaloIdLHEFilter + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL1SeededStartUpElectronPixelSeeds + process.hltMu3p5Ele30CaloIdLPixelMatchFilter + process.HLTEndSequence )
process.HLT_Mu40_eta2p1_v8 = cms.Path( process.HLTBeginSequence + process.hltL1sMu16Eta2p1 + process.hltPreMu40eta2p1 + process.hltL1fL1sMu16Eta2p1L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sMu16Eta2p1L1f0L2Filtered16Q + process.HLTL3muonrecoSequence + process.hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered40Q + process.HLTEndSequence )
process.HLT_IsoMu24_eta2p1_v10 = cms.Path( process.HLTBeginSequence + process.hltL1sMu16Eta2p1 + process.hltPreIsoMu24eta2p1 + process.hltL1fL1sMu16Eta2p1L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sMu16Eta2p1L1f0L2Filtered16Q + process.HLTL3muonrecoSequence + process.hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered24Q + process.HLTL3muoncaloisorecoSequenceNoBools + process.HLTL3muonisorecoSequence + process.hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoFiltered10 + process.HLTEndSequence )
process.HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sL1Mu12EG7 + process.hltPreMu17Ele8CaloIdTCaloIsoVLTrkIdVLTrkIsoVL + process.hltL1Mu12EG7L1MuFiltered0 + process.HLTL2muonrecoSequence + process.hltL1Mu12EG7L2MuFiltered0 + process.HLTL3muonrecoSequence + process.hltL1Mu12EG7L3MuFiltered17 + process.HLTMu17Ele8CaloIdTTrkIdVLCaloIsoVLTrkIsoVLSequence + process.hltMu17Ele8dZFilter + process.HLTEndSequence )
process.HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sL1MuOpenEG12 + process.hltPreMu8Ele17CaloIdTCaloIsoVLTrkIdVLTrkIsoVL + process.hltL1MuOpenEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL1MuOpenEG12L2Filtered5 + process.HLTL3muonrecoSequence + process.hltL1MuOpenEG12L3Filtered8 + process.HLTMu8Ele17CaloIdTCaloIsoVLTrkIdVLTrkIsoVLSequence + process.hltMu8Ele17dZFilter + process.HLTEndSequence )
process.HLTriggerFinalPath = cms.Path( process.hltGtDigis + process.hltScalersRawToDigi + process.hltFEDSelector + process.hltTriggerSummaryAOD + process.hltTriggerSummaryRAW )


process.source = cms.Source( "PoolSource",
    fileNames = cms.untracked.vstring(
        'file:RelVal_Raw_GRun.root',
    ),
    secondaryFileNames = cms.untracked.vstring(
    ),
    inputCommands = cms.untracked.vstring(
        'keep *'
    )
)

# En-able HF Noise filters in GRun menu
if 'hltHfreco' in process.__dict__:
    process.hltHfreco.setNoiseFlags = cms.bool( True )

# remove the HLT prescales
if 'PrescaleService' in process.__dict__:
    process.PrescaleService.lvl1DefaultLabel = cms.string( '0' )
    process.PrescaleService.lvl1Labels       = cms.vstring( '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' )
    process.PrescaleService.prescaleTable    = cms.VPSet( )

# CMSSW version specific customizations
import os
cmsswVersion = os.environ['CMSSW_VERSION']

# override the process name
process.setName_('TEST')

# adapt HLT modules to the correct process name
if 'hltTrigReport' in process.__dict__:
    process.hltTrigReport.HLTriggerResults                    = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreExpressCosmicsOutputSmart' in process.__dict__:
    process.hltPreExpressCosmicsOutputSmart.TriggerResultsTag = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreExpressOutputSmart' in process.__dict__:
    process.hltPreExpressOutputSmart.TriggerResultsTag        = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreDQMForHIOutputSmart' in process.__dict__:
    process.hltPreDQMForHIOutputSmart.TriggerResultsTag       = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreDQMForPPOutputSmart' in process.__dict__:
    process.hltPreDQMForPPOutputSmart.TriggerResultsTag       = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreHLTDQMResultsOutputSmart' in process.__dict__:
    process.hltPreHLTDQMResultsOutputSmart.TriggerResultsTag  = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreHLTDQMOutputSmart' in process.__dict__:
    process.hltPreHLTDQMOutputSmart.TriggerResultsTag         = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreHLTMONOutputSmart' in process.__dict__:
    process.hltPreHLTMONOutputSmart.TriggerResultsTag         = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltDQMHLTScalers' in process.__dict__:
    process.hltDQMHLTScalers.triggerResults                   = cms.InputTag( 'TriggerResults', '', 'TEST' )
    process.hltDQMHLTScalers.processname                      = 'TEST'

if 'hltDQML1SeedLogicScalers' in process.__dict__:
    process.hltDQML1SeedLogicScalers.processname              = 'TEST'

# limit the number of events to be processed
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( 100 )
)

# enable the TrigReport and TimeReport
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool( True )
)

# override the GlobalTag, connection string and pfnPrefix
if 'GlobalTag' in process.__dict__:
    process.GlobalTag.connect   = 'frontier://FrontierProd/CMS_COND_31X_GLOBALTAG'
    process.GlobalTag.pfnPrefix = cms.untracked.string('frontier://FrontierProd/')
    from Configuration.AlCa.autoCond import autoCond
    process.GlobalTag.globaltag = autoCond['startup']

if 'MessageLogger' in process.__dict__:
    process.MessageLogger.categories.append('TriggerSummaryProducerAOD')
    process.MessageLogger.categories.append('L1GtTrigReport')
    process.MessageLogger.categories.append('HLTrigReport')

