
application: DCT_WIBCE_ADS_Application
configrepo: wibce-integration-tools
branch: develop
startstopsnaphsot: PSG_start_stop
only_changed: false
versions:
- component: DCT_Utilities_Component
  version: 1.19
- component: DCT_MW_JDK_Component
  version: 8u271

startstopversions:
- component: abc
  version: 123
steps:
- import
- deploy
- stop
- activate
- start
environment:
- ddev
- dsit

