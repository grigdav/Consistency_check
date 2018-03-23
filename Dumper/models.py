# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models
#from django.core.validators import MaxValueValidator

class ENodeBFunction(models.Model):
    field_enodeb_id                                     = models.CharField("Station ID", primary_key=True, max_length=45)
    field_enodeb_stnnodes                               = models.CharField(db_column='field_enodeb_stnNodes', max_length=45, blank=True, null=True, default='')  # Field name made lowercase.
    field_enodeb_tcunodes                               = models.CharField(db_column='field_enodeb_tcuNodes', max_length=45, blank=True, null=True, default='')  # Field name made lowercase.
    field_enodeb_nnsfmode                               = models.CharField(db_column='field_enodeb_nnsfMode', max_length=45, blank=True, null=True, default='')  # Field name made lowercase.
    field_enodeb_timephasemaxdeviation                  = models.CharField(db_column='field_enodeb_timePhaseMaxDeviation', max_length=45, blank=True, null=True, default='')  # Field name made lowercase.
    field_enodeb_forcedsitunnelingactive                = models.CharField(db_column='field_enodeb_forcedSiTunnelingActive', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_pwspersistentstorage                   = models.CharField(db_column='field_enodeb_pwsPersistentStorage', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_x2whitelist                            = models.CharField(db_column='field_enodeb_x2WhiteList', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_upipaddressref                         = models.CharField(db_column='field_enodeb_upIpAddressRef', max_length=191, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary9                          = models.CharField(db_column='field_enodeb_zzzTemporary9', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_enodebplmnid                           = models.CharField(db_column='field_enodeb_eNodeBPlmnId', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary7                          = models.CharField(db_column='field_enodeb_zzzTemporary7', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_dscplabel                              = models.CharField(db_column='field_enodeb_dscpLabel', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary8                          = models.CharField(db_column='field_enodeb_zzzTemporary8', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_userlabel                              = models.CharField(db_column='field_enodeb_userLabel', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_rrcconnreestactive                     = models.CharField(db_column='field_enodeb_rrcConnReestActive', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary21                         = models.CharField(db_column='field_enodeb_zzzTemporary21', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary22                         = models.CharField(db_column='field_enodeb_zzzTemporary22', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_x2retrytimerstart                      = models.CharField(db_column='field_enodeb_x2retryTimerStart', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary25                         = models.CharField(db_column='field_enodeb_zzzTemporary25', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary26                         = models.CharField(db_column='field_enodeb_zzzTemporary26', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary23                         = models.CharField(db_column='field_enodeb_zzzTemporary23', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary24                         = models.CharField(db_column='field_enodeb_zzzTemporary24', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_x2setuptwowayrelations                 = models.CharField(db_column='field_enodeb_x2SetupTwoWayRelations', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_liccapdistrmethod                      = models.CharField(db_column='field_enodeb_licCapDistrMethod', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_timeandphasesynchcritical              = models.CharField(db_column='field_enodeb_timeAndPhaseSynchCritical', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_ulschedulerdynamicbwallocationenabled  = models.CharField(db_column='field_enodeb_ulSchedulerDynamicBWAllocationEnabled', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary2                          = models.CharField(db_column='field_enodeb_zzzTemporary2', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary1                          = models.CharField(db_column='field_enodeb_zzzTemporary1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary3                          = models.CharField(db_column='field_enodeb_zzzTemporary3', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary6                          = models.CharField(db_column='field_enodeb_zzzTemporary6', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary10                         = models.CharField(db_column='field_enodeb_zzzTemporary10', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_s1retrytimer                           = models.CharField(db_column='field_enodeb_s1RetryTimer', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary5                          = models.CharField(db_column='field_enodeb_zzzTemporary5', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary11                         = models.CharField(db_column='field_enodeb_zzzTemporary11', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary12                         = models.CharField(db_column='field_enodeb_zzzTemporary12', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary13                         = models.CharField(db_column='field_enodeb_zzzTemporary13', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_randupdateinterval                     = models.CharField(db_column='field_enodeb_randUpdateInterval', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_x2ipaddrvias1active                    = models.CharField(db_column='field_enodeb_x2IpAddrViaS1Active', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary16                         = models.CharField(db_column='field_enodeb_zzzTemporary16', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary18                         = models.CharField(db_column='field_enodeb_zzzTemporary18', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_maxrandc                               = models.CharField(db_column='field_enodeb_maxRandc', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_sctpref                                = models.CharField(db_column='field_enodeb_sctpRef', max_length=191, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_minrandc                               = models.CharField(db_column='field_enodeb_minRandc', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_s1hodirdatapathavail                   = models.CharField(db_column='field_enodeb_s1HODirDataPathAvail', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_mfbisupport                            = models.CharField(db_column='field_enodeb_mfbiSupport', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_dnslookupontai                         = models.CharField(db_column='field_enodeb_dnsLookupOnTai', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_dnslookuptimer                         = models.CharField(db_column='field_enodeb_dnsLookupTimer', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_x2blacklist                            = models.CharField(db_column='field_enodeb_x2BlackList', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_initpreschedulingenable                = models.CharField(db_column='field_enodeb_initPreschedulingEnable', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_toutgoinghoexeccdma1xrtt               = models.CharField(db_column='field_enodeb_tOutgoingHoExecCdma1xRtt', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_csfbmeasfromidlemode                   = models.CharField(db_column='field_enodeb_csfbMeasFromIdleMode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_enbid                                  = models.CharField(db_column='field_enodeb_eNBId', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_x2retrytimermaxauto                    = models.CharField(db_column='field_enodeb_x2retryTimerMaxAuto', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_biasthpwifimobility                    = models.CharField(db_column='field_enodeb_biasThpWifiMobility', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_releaseinactiveuesmploadlevel          = models.CharField(db_column='field_enodeb_releaseInactiveUesMpLoadLevel', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_dnsselections1x2ref                    = models.CharField(db_column='field_enodeb_dnsSelectionS1X2Ref', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_ts1hocanceltimer_field                 = models.CharField(db_column="field_enodeb_tS1HoCancelTimer'", max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    field_enodeb_combcellsectorselectthreshrx           = models.CharField(db_column='field_enodeb_combCellSectorSelectThreshRx', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_combcellsectorselectthreshtx           = models.CharField(db_column='field_enodeb_combCellSectorSelectThreshTx', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_releaseinactiveuesinacttime            = models.CharField(db_column='field_enodeb_releaseInactiveUesInactTime', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_plmnbordernode                         = models.CharField(db_column='field_enodeb_plmnBorderNode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_timephasemaxdeviationmbms              = models.CharField(db_column='field_enodeb_timePhaseMaxDeviationMbms', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_timephasemaxdeviationotdoa             = models.CharField(db_column='field_enodeb_timePhaseMaxDeviationOtdoa', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_liculbbpercentileconf                  = models.CharField(db_column='field_enodeb_licUlBbPercentileConf', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_liculprbpercentileconf                 = models.CharField(db_column='field_enodeb_licUlPrbPercentileConf', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_release                                = models.CharField(max_length=45, blank=True, null=True)
    field_enodeb_licdlprbpercentileconf                 = models.CharField(db_column='field_enodeb_licDlPrbPercentileConf', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_timephasemaxdeviationtdd               = models.CharField(db_column='field_enodeb_timePhaseMaxDeviationTdd', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_timephasemaxdeviationsib16             = models.CharField(db_column='field_enodeb_timePhaseMaxDeviationSib16', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_timeandphasesynchalignment             = models.CharField(db_column='field_enodeb_timeAndPhaseSynchAlignment', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_mtrrewithoutneighboractive             = models.CharField(db_column='field_enodeb_mtRreWithoutNeighborActive', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_licdlbbpercentileconf                  = models.CharField(db_column='field_enodeb_licDlBbPercentileConf', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_licconnecteduserspercentileconf        = models.CharField(db_column='field_enodeb_licConnectedUsersPercentileConf', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_timephasemaxdeviationcdma2000          = models.CharField(db_column='field_enodeb_timePhaseMaxDeviationCdma2000', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_ulmaxwaitingtimeglobal                 = models.CharField(db_column='field_enodeb_ulMaxWaitingTimeGlobal', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_softlockrwrwaittimerinternal           = models.CharField(db_column='field_enodeb_softLockRwRWaitTimerInternal', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_enabledultrigmeas                      = models.CharField(db_column='field_enodeb_enabledUlTrigMeas', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_dlmaxwaitingtimeglobal                 = models.CharField(db_column='field_enodeb_dlMaxWaitingTimeGlobal', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_tddvoipdrxprofileid                    = models.CharField(db_column='field_enodeb_tddVoipDrxProfileId', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_mfbisupportpolicy                      = models.CharField(db_column='field_enodeb_mfbiSupportPolicy', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary28                         = models.CharField(db_column='field_enodeb_zzzTemporary28', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_measuringecgiwithagactive              = models.CharField(db_column='field_enodeb_measuringEcgiWithAgActive', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_checkemergencysoftlock                 = models.CharField(db_column='field_enodeb_checkEmergencySoftLock', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_softlockrwrwaittimeroperator           = models.CharField(db_column='field_enodeb_softLockRwRWaitTimerOperator', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary32                         = models.CharField(db_column='field_enodeb_zzzTemporary32', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary33                         = models.CharField(db_column='field_enodeb_zzzTemporary33', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary34                         = models.CharField(db_column='field_enodeb_zzzTemporary34', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_trelocoverall                          = models.CharField(db_column='field_enodeb_tRelocOverall', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_alignttibundwultrigsinr                = models.CharField(db_column='field_enodeb_alignTtiBundWUlTrigSinr', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_usebandprioritiesinscelleval           = models.CharField(db_column='field_enodeb_useBandPrioritiesInSCellEval', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_prioritizeadditionalbands              = models.CharField(db_column='field_enodeb_prioritizeAdditionalBands', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_caawaremfbiintracellho                 = models.CharField(db_column='field_enodeb_caAwareMfbiIntraCellHo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary40                         = models.CharField(db_column='field_enodeb_zzzTemporary40', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary39                         = models.CharField(db_column='field_enodeb_zzzTemporary39', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary35                         = models.CharField(db_column='field_enodeb_zzzTemporary35', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary36                         = models.CharField(db_column='field_enodeb_zzzTemporary36', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary37                         = models.CharField(db_column='field_enodeb_zzzTemporary37', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_gtpuerrorindicationdscp                = models.CharField(db_column='field_enodeb_gtpuErrorIndicationDscp', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_s1gtpuechofailureaction                = models.CharField(db_column='field_enodeb_s1GtpuEchoFailureAction', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_s1gtpuechoenable                       = models.CharField(db_column='field_enodeb_s1GtpuEchoEnable', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_x2gtpuechodscp                         = models.CharField(db_column='field_enodeb_x2GtpuEchoDscp', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_x2gtpuechoenable                       = models.CharField(db_column='field_enodeb_x2GtpuEchoEnable', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_s1gtpuechodscp                         = models.CharField(db_column='field_enodeb_s1GtpuEchoDscp', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_usebandprioritiesinsib1                = models.CharField(db_column='field_enodeb_useBandPrioritiesInSib1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_eranvlanportref                        = models.CharField(db_column='field_enodeb_eranVlanPortRef', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary51                         = models.CharField(db_column='field_enodeb_zzzTemporary51', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary50                         = models.CharField(db_column='field_enodeb_zzzTemporary50', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzzTemporary54                         = models.CharField(db_column='field_enodeb_zzzTemporary54', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary53                         = models.CharField(db_column='field_enodeb_zzzTemporary53', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary52                         = models.CharField(db_column='field_enodeb_zzzTemporary52', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_timephasemaxdeviationienbca            = models.CharField(db_column='field_enodeb_timePhaseMaxDeviationIeNbCa', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_sctpx2ref                              = models.CharField(db_column='field_enodeb_sctpX2Ref', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_timephasemaxdeviationedrx              = models.CharField(db_column='field_enodeb_timePhaseMaxDeviationEdrx', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_interenbcatunneldscp                   = models.CharField(db_column='field_enodeb_interEnbCaTunnelDscp', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary43                         = models.CharField(db_column='field_enodeb_zzzTemporary43', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary41                         = models.CharField(db_column='field_enodeb_zzzTemporary41', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary42                         = models.CharField(db_column='field_enodeb_zzzTemporary42', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary49                         = models.CharField(db_column='field_enodeb_zzzTemporary49', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary47                         = models.CharField(db_column='field_enodeb_zzzTemporary47', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary48                         = models.CharField(db_column='field_enodeb_zzzTemporary48', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_upx2ipaddressref                       = models.CharField(db_column='field_enodeb_upX2IpAddressRef', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_altnasbackto                           = models.CharField(db_column='field_enodeb_altNasBackTo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_ipsecepaddressref                      = models.CharField(db_column='field_enodeb_ipsecEpAddressRef', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_csmminhighhitthreshold                 = models.CharField(db_column='field_enodeb_csmMinHighHitThreshold', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_csfbuseregisteredlai                   = models.CharField(db_column='field_enodeb_csfbUseRegisteredLai', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_interenbulcomptunneldscp               = models.CharField(db_column='field_enodeb_interEnbUlCompTunnelDscp', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_extendedwaittimenb                     = models.CharField(db_column='field_enodeb_extendedWaitTimeNb', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_inactivitysupervisiontimernb           = models.CharField(db_column='field_enodeb_inactivitySupervisionTimerNb', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_inactivitysupervisiontimernb_1         = models.CharField(db_column='field_enodeb_inactivitySupervisionTimerNb_1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_inactivitysupervisiontimernb_2         = models.CharField(db_column='field_enodeb_inactivitySupervisionTimerNb_2', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary55                         = models.CharField(db_column='field_enodeb_zzzTemporary55', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_maxnrofinterenbulcomplbm               = models.CharField(db_column='field_enodeb_maxNrOfInterEnbUlCompLbm', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_timephasemaxdeviationtdd6              = models.CharField(db_column='field_enodeb_timePhaseMaxDeviationTdd6', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_timephasemaxdeviationtdd5              = models.CharField(db_column='field_enodeb_timePhaseMaxDeviationTdd5', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_timephasemaxdeviationtdd7              = models.CharField(db_column='field_enodeb_timePhaseMaxDeviationTdd7', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_timephasemaxdeviationtdd2              = models.CharField(db_column='field_enodeb_timePhaseMaxDeviationTdd2', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_timephasemaxdeviationtdd1              = models.CharField(db_column='field_enodeb_timePhaseMaxDeviationTdd1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_timephasemaxdeviationtdd4              = models.CharField(db_column='field_enodeb_timePhaseMaxDeviationTdd4', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_timephasemaxdeviationtdd3              = models.CharField(db_column='field_enodeb_timePhaseMaxDeviationTdd3', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_timephasemaxdevienbulcomp              = models.CharField(db_column='field_enodeb_timePhaseMaxDevIeNBUlComp', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary58                         = models.CharField(db_column='field_enodeb_zzzTemporary58', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary57                         = models.CharField(db_column='field_enodeb_zzzTemporary57', max_length=45, blank=True, null=True)  # Field name made lowercase.
    field_enodeb_zzztemporary56                         = models.CharField(db_column='field_enodeb_zzzTemporary56', max_length=45, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.field_enodeb_id

class AdmissionControll(models.Model):
    field_enodeb_id                                     = models.CharField("Station ID", primary_key=True, max_length=45)
    field_enodeb_resourceReservationForDifferentiation  = models.CharField(db_column='field_enodeb_resourceReservationForDifferentiation', max_length=45, blank=True, null=True, default='')
    field_enodeb_zzzTemp20                              = models.CharField(db_column='field_enodeb_zzzTemp20', max_length=45, blank=True, null=True)
    field_enodeb_zzzTemp21                              = models.CharField(db_column='field_enodeb_zzzTemp21', max_length=45, blank=True, null=True)
    field_enodeb_zzzTemporary7                          = models.CharField(db_column='field_enodeb_zzzTemporary7', max_length=45, blank=True, null=True)
    field_enodeb_dlMbmsGbrRatio                         = models.CharField(db_column='field_enodeb_dlMbmsGbrRatio', max_length=45, blank=True, null=True)
    field_enodeb_dlAdmOverloadThr                       = models.CharField(db_column='field_enodeb_dlAdmOverloadThr', max_length=45, blank=True, null=True)
    field_enodeb_paArpOverride                          = models.CharField(db_column='field_enodeb_paArpOverride', max_length=45, blank=True, null=True)
    field_enodeb_ulAdmDifferentiationThr                = models.CharField(db_column='field_enodeb_ulAdmDifferentiationThr', max_length=45, blank=True, null=True)
    field_enodeb_resourceReservationForPAState          = models.CharField(db_column='field_enodeb_resourceReservationForPAState', max_length=45, blank=True, null=True)
    field_enodeb_ulTransNwBandwidth                     = models.CharField(db_column=' field_enodeb_ulTransNwBandwidth', max_length=45, blank=True, null=True)
    field_enodeb_nrOfPaConnReservationsPerCell          = models.CharField(db_column='field_enodeb_nrOfPaConnReservationsPerCell', max_length=45, blank=True, null=True)
    field_enodeb_zzTemp4                                = models.CharField(db_column='field_enodeb_zzTemp4', max_length=45, blank=True, null=True)
    field_enodeb_zzzTemp5                               = models.CharField(db_column='field_enodeb_zzzTemp5', max_length=45, blank=True, null=True)
    field_enodeb_zzzTemp2                               = models.CharField(db_column='field_enodeb_zzzTemp2', max_length=45, blank=True, null=True)
    field_enodeb_zzzTemp3                               = models.CharField(db_column='field_enodeb_zzzTemp3', max_length=45, blank=True, null=True)
    field_enodeb_arpBasedPreEmptionState                = models.CharField(db_column='field_enodeb_arpBasedPreEmptionState', max_length=45, blank=True, null=True)
    field_enodeb_zzzTemp10                              = models.CharField(db_column='field_enodeb_zzzTemp10', max_length=45, blank=True, null=True)
    field_enodeb_zzzTemp1                               = models.CharField(db_column='field_enodeb_zzzTemp1', max_length=45, blank=True, null=True)
    field_enodeb_zzzTemp11                              = models.CharField(db_column='field_enodeb_zzzTemp11', max_length=45, blank=True, null=True)
    field_enodeb_zzzTemp12                              = models.CharField(db_column='field_enodeb_zzzTemp12', max_length=45, blank=True, null=True)
    field_enodeb_dlTransNwBandwidth                     = models.CharField(db_column='field_enodeb_dlTransNwBandwidth', max_length=45, blank=True, null=True)
    field_enodeb_ulAdmOverloadThr                       = models.CharField(db_column='field_enodeb_ulAdmOverloadThr', max_length=45, blank=True, null=True)
    field_enodeb_zzzTemp8                               = models.CharField(db_column='field_enodeb_zzzTemp8', max_length=45, blank=True, null=True)
    field_enodeb_zzzTemp9                               = models.CharField(db_column='field_enodeb_zzzTemp9', max_length=45, blank=True, null=True)
    field_enodeb_zzzTemp6                               = models.CharField(db_column='field_enodeb_zzzTemp6', max_length=45, blank=True, null=True)
    field_enodeb_zzzTemp7                               = models.CharField(db_column='field_enodeb_zzzTemp7', max_length=45, blank=True, null=True)
    field_enodeb_admNrRbDifferentiationThr              = models.CharField(db_column='field_enodeb_admNrRbDifferentiationThr', max_length=45, blank=True, null=True)
    field_enodeb_zzzTemporary2                          = models.CharField(db_column='field_enodeb_zzzTemporary2', max_length=45, blank=True, null=True)
    field_enodeb_zzzTemporary1                          = models.CharField(db_column='field_enodeb_zzzTemporary1', max_length=45, blank=True, null=True)
    field_enodeb_admNrRrcDifferentiationThr             = models.CharField(db_column='field_enodeb_admNrRrcDifferentiationThr', max_length=45, blank=True, null=True)
    field_enodeb_zzzTemporary4                          = models.CharField(db_column='field_enodeb_zzzTemporary4', max_length=45, blank=True, null=True)
    field_enodeb_zzzTemporary3                          = models.CharField(db_column='field_enodeb_zzzTemporary3', max_length=45, blank=True, null=True)
    field_enodeb_zzzTemporary6                          = models.CharField(db_column='field_enodeb_zzzTemporary6', max_length=45, blank=True, null=True)
    field_enodeb_zzzTemporary5                          = models.CharField(db_column='field_enodeb_zzzTemporary5', max_length=45, blank=True, null=True)
    field_enodeb_zzzTemp14                              = models.CharField(db_column='field_enodeb_zzzTemp14', max_length=45, blank=True, null=True)
    field_enodeb_zzzTemp13                              = models.CharField(db_column='field_enodeb_zzzTemp13', max_length=45, blank=True, null=True)
    field_enodeb_zzzTemp16                              = models.CharField(db_column='field_enodeb_zzzTemp16', max_length=45, blank=True, null=True)
    field_enodeb_admResourceMinQciPrio                  = models.CharField(db_column='field_enodeb_admResourceMinQciPrio', max_length=45, blank=True, null=True)
    field_enodeb_zzzTemp15                              = models.CharField(db_column='field_enodeb_zzzTemp15', max_length=45, blank=True, null=True)
    field_enodeb_zzzTemp18                              = models.CharField(db_column='field_enodeb_zzzTemp18', max_length=45, blank=True, null=True)
    field_enodeb_zzzTemp17                              = models.CharField(db_column='field_enodeb_zzzTemp17', max_length=45, blank=True, null=True)
    field_enodeb_nrOfRbReservationsPerPaConn            = models.CharField(db_column='field_enodeb_nrOfRbReservationsPerPaConn', max_length=45, blank=True, null=True)
    field_enodeb_dlAdmDifferentiationThr                = models.CharField(db_column='field_enodeb_dlAdmDifferentiationThr', max_length=45, blank=True, null=True)
    field_enodeb_zzzTemp19                              = models.CharField(db_column='field_enodeb_zzzTemp19', max_length=45, blank=True, null=True)
    field_enodeb_zzzTemporary22                         = models.CharField(db_column='field_enodeb_zzzTemporary22', max_length=45, blank=True, null=True)
    field_enodeb_zzzTemporary25                         = models.CharField(db_column='field_enodeb_zzzTemporary25', max_length=45, blank=True, null=True)
    field_enodeb_zzzTemporary26                         = models.CharField(db_column='field_enodeb_zzzTemporary26', max_length=45, blank=True, null=True)
    field_enodeb_zzzTemporary23                         = models.CharField(db_column='field_enodeb_zzzTemporary23', max_length=45, blank=True, null=True)
    field_enodeb_zzzTemporary24                         = models.CharField(db_column='field_enodeb_zzzTemporary24', max_length=45, blank=True, null=True)
    field_enodeb_lbAtoThresholdLevel2                   = models.CharField(db_column='field_enodeb_lbAtoThresholdLevel2', max_length=45, blank=True, null=True)
    field_enodeb_lbAtoThresholdLevel1                   = models.CharField(db_column='field_enodeb_lbAtoThresholdLevel1', max_length=45, blank=True, null=True)

    def __str__(self):
        return self.field_enodeb_id