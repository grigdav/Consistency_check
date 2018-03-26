-- MySQL dump 10.13  Distrib 5.7.21, for Linux (x86_64)
--
-- Host: localhost    Database: Consistency_check
-- ------------------------------------------------------
-- Server version	5.7.21-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `t_f4ge_enodeb_m`
--

DROP TABLE IF EXISTS `Dumper_enodebfunction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Dumper_enodebfunction` (
  `field_enodeb_id` varchar(45) NOT NULL,
  `field_enodeb_stnNodes` varchar(45) DEFAULT NULL,
  `field_enodeb_tcuNodes` varchar(45) DEFAULT NULL,
  `field_enodeb_nnsfMode` varchar(45) DEFAULT NULL,
  `field_enodeb_timePhaseMaxDeviation` varchar(45) DEFAULT NULL,
  `field_enodeb_forcedSiTunnelingActive` varchar(45) DEFAULT NULL,
  `field_enodeb_pwsPersistentStorage` varchar(45) DEFAULT NULL,
  `field_enodeb_x2WhiteList` varchar(45) DEFAULT NULL,
  `field_enodeb_upIpAddressRef` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary9` varchar(45) DEFAULT NULL,
  `field_enodeb_eNodeBPlmnId` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary7` varchar(45) DEFAULT NULL,
  `field_enodeb_dscpLabel` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary8` varchar(45) DEFAULT NULL,
  `field_enodeb_userLabel` varchar(45) DEFAULT NULL,
  `field_enodeb_rrcConnReestActive` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary21` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary22` varchar(45) DEFAULT NULL,
  `field_enodeb_x2retryTimerStart` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary25` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary26` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary23` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary24` varchar(45) DEFAULT NULL,
  `field_enodeb_x2SetupTwoWayRelations` varchar(45) DEFAULT NULL,
  `field_enodeb_licCapDistrMethod` varchar(45) DEFAULT NULL,
  `field_enodeb_timeAndPhaseSynchCritical` varchar(45) DEFAULT NULL,
  `field_enodeb_ulSchedulerDynamicBWAllocationEnabled` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary2` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary1` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary3` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary6` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary10` varchar(45) DEFAULT NULL,
  `field_enodeb_s1RetryTimer` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary5` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary11` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary12` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary13` varchar(45) DEFAULT NULL,
  `field_enodeb_randUpdateInterval` varchar(45) DEFAULT NULL,
  `field_enodeb_x2IpAddrViaS1Active` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary16` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary18` varchar(45) DEFAULT NULL,
  `field_enodeb_maxRandc` varchar(45) DEFAULT NULL,
  `field_enodeb_sctpRef` varchar(45) DEFAULT NULL,
  `field_enodeb_minRandc` varchar(45) DEFAULT NULL,
  `field_enodeb_s1HODirDataPathAvail` varchar(45) DEFAULT NULL,
  `field_enodeb_mfbiSupport` varchar(45) DEFAULT NULL,
  `field_enodeb_dnsLookupOnTai` varchar(45) DEFAULT NULL,
  `field_enodeb_dnsLookupTimer` varchar(45) DEFAULT NULL,
  `field_enodeb_x2BlackList` varchar(45) DEFAULT NULL,
  `field_enodeb_initPreschedulingEnable` varchar(45) DEFAULT NULL,
  `field_enodeb_tOutgoingHoExecCdma1xRtt` varchar(45) DEFAULT NULL,
  `field_enodeb_csfbMeasFromIdleMode` varchar(45) DEFAULT NULL,
  `field_enodeb_eNBId` varchar(45) DEFAULT NULL,
  `field_enodeb_x2retryTimerMaxAuto` varchar(45) DEFAULT NULL,
  `field_enodeb_biasThpWifiMobility` varchar(45) DEFAULT NULL,
  `field_enodeb_releaseInactiveUesMpLoadLevel` varchar(45) DEFAULT NULL,
  `field_enodeb_dnsSelectionS1X2Ref` varchar(45) DEFAULT NULL,
  `field_enodeb_tS1HoCancelTimer'` varchar(45) DEFAULT NULL,
  `field_enodeb_combCellSectorSelectThreshRx` varchar(45) DEFAULT NULL,
  `field_enodeb_combCellSectorSelectThreshTx` varchar(45) DEFAULT NULL,
  `field_enodeb_releaseInactiveUesInactTime` varchar(45) DEFAULT NULL,
  `field_enodeb_plmnBorderNode` varchar(45) DEFAULT NULL,
  `field_enodeb_timePhaseMaxDeviationMbms` varchar(45) DEFAULT NULL,
  `field_enodeb_timePhaseMaxDeviationOtdoa` varchar(45) DEFAULT NULL,
  `field_enodeb_licUlBbPercentileConf` varchar(45) DEFAULT NULL,
  `field_enodeb_licUlPrbPercentileConf` varchar(45) DEFAULT NULL,
  `field_enodeb_release` varchar(45) DEFAULT NULL,
  `field_enodeb_licDlPrbPercentileConf` varchar(45) DEFAULT NULL,
  `field_enodeb_timePhaseMaxDeviationTdd` varchar(45) DEFAULT NULL,
  `field_enodeb_timePhaseMaxDeviationSib16` varchar(45) DEFAULT NULL,
  `field_enodeb_timeAndPhaseSynchAlignment` varchar(45) DEFAULT NULL,
  `field_enodeb_mtRreWithoutNeighborActive` varchar(45) DEFAULT NULL,
  `field_enodeb_licDlBbPercentileConf` varchar(45) DEFAULT NULL,
  `field_enodeb_licConnectedUsersPercentileConf` varchar(45) DEFAULT NULL,
  `field_enodeb_timePhaseMaxDeviationCdma2000` varchar(45) DEFAULT NULL,
  `field_enodeb_ulMaxWaitingTimeGlobal` varchar(45) DEFAULT NULL,
  `field_enodeb_softLockRwRWaitTimerInternal` varchar(45) DEFAULT NULL,
  `field_enodeb_enabledUlTrigMeas` varchar(45) DEFAULT NULL,
  `field_enodeb_dlMaxWaitingTimeGlobal` varchar(45) DEFAULT NULL,
  `field_enodeb_tddVoipDrxProfileId` varchar(45) DEFAULT NULL,
  `field_enodeb_mfbiSupportPolicy` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary28` varchar(45) DEFAULT NULL,
  `field_enodeb_measuringEcgiWithAgActive` varchar(45) DEFAULT NULL,
  `field_enodeb_checkEmergencySoftLock` varchar(45) DEFAULT NULL,
  `field_enodeb_softLockRwRWaitTimerOperator` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary32` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary33` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary34` varchar(45) DEFAULT NULL,
  `field_enodeb_tRelocOverall` varchar(45) DEFAULT NULL,
  `field_enodeb_alignTtiBundWUlTrigSinr` varchar(45) DEFAULT NULL,
  `field_enodeb_useBandPrioritiesInSCellEval` varchar(45) DEFAULT NULL,
  `field_enodeb_prioritizeAdditionalBands` varchar(45) DEFAULT NULL,
  `field_enodeb_caAwareMfbiIntraCellHo` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary40` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary39` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary35` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary36` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary37` varchar(45) DEFAULT NULL,
  `field_enodeb_gtpuErrorIndicationDscp` varchar(45) DEFAULT NULL,
  `field_enodeb_s1GtpuEchoFailureAction` varchar(45) DEFAULT NULL,
  `field_enodeb_s1GtpuEchoEnable` varchar(45) DEFAULT NULL,
  `field_enodeb_x2GtpuEchoDscp` varchar(45) DEFAULT NULL,
  `field_enodeb_x2GtpuEchoEnable` varchar(45) DEFAULT NULL,
  `field_enodeb_s1GtpuEchoDscp` varchar(45) DEFAULT NULL,
  `field_enodeb_useBandPrioritiesInSib1` varchar(45) DEFAULT NULL,
  `field_enodeb_eranVlanPortRef` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary51` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary50` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary54` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary53` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary52` varchar(45) DEFAULT NULL,
  `field_enodeb_timePhaseMaxDeviationIeNbCa` varchar(45) DEFAULT NULL,
  `field_enodeb_sctpX2Ref` varchar(45) DEFAULT NULL,
  `field_enodeb_timePhaseMaxDeviationEdrx` varchar(45) DEFAULT NULL,
  `field_enodeb_interEnbCaTunnelDscp` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary43` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary41` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary42` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary49` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary47` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary48` varchar(45) DEFAULT NULL,
  `field_enodeb_upX2IpAddressRef` varchar(45) DEFAULT NULL,
  `field_enodeb_altNasBackTo` varchar(45) DEFAULT NULL,
  `field_enodeb_ipsecEpAddressRef` varchar(45) DEFAULT NULL,
  `field_enodeb_csmMinHighHitThreshold` varchar(45) DEFAULT NULL,
  `field_enodeb_csfbUseRegisteredLai` varchar(45) DEFAULT NULL,
  `field_enodeb_interEnbUlCompTunnelDscp` varchar(45) DEFAULT NULL,
  `field_enodeb_extendedWaitTimeNb` varchar(45) DEFAULT NULL,
  `field_enodeb_inactivitySupervisionTimerNb` varchar(45) DEFAULT NULL,
  `field_enodeb_inactivitySupervisionTimerNb_1` varchar(45) DEFAULT NULL,
  `field_enodeb_inactivitySupervisionTimerNb_2` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary55` varchar(45) DEFAULT NULL,
  `field_enodeb_maxNrOfInterEnbUlCompLbm` varchar(45) DEFAULT NULL,
  `field_enodeb_timePhaseMaxDeviationTdd6` varchar(45) DEFAULT NULL,
  `field_enodeb_timePhaseMaxDeviationTdd5` varchar(45) DEFAULT NULL,
  `field_enodeb_timePhaseMaxDeviationTdd7` varchar(45) DEFAULT NULL,
  `field_enodeb_timePhaseMaxDeviationTdd2` varchar(45) DEFAULT NULL,
  `field_enodeb_timePhaseMaxDeviationTdd1` varchar(45) DEFAULT NULL,
  `field_enodeb_timePhaseMaxDeviationTdd4` varchar(45) DEFAULT NULL,
  `field_enodeb_timePhaseMaxDeviationTdd3` varchar(45) DEFAULT NULL,
  `field_enodeb_timePhaseMaxDevIeNBUlComp` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary58` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary57` varchar(45) DEFAULT NULL,
  `field_enodeb_zzzTemporary56` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`field_enodeb_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_f4ge_enodeb_m`
--

LOCK TABLES `t_f4ge_enodeb_m` WRITE;
/*!40000 ALTER TABLE `t_f4ge_enodeb_m` DISABLE KEYS */;
/*!40000 ALTER TABLE `t_f4ge_enodeb_m` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-02-26 13:11:56
