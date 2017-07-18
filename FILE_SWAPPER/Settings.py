from WorkerManager import WorkerType
import Utils

#################################################################################################################
# GLOBALS 

# Intermediate swap space sizing parameters (in MB):
minswapsize = 10#500               # In MB
maxswapsize = 50#1000              # In MB
gBS = Utils.MBtoBytes(1)           # In bytes
gPartExt = "endpart"
gWorkerType = WorkerType.thread
gPerlMerger = "merge.pl"




