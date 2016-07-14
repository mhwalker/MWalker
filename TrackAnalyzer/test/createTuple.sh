#!/bin/bash



MAINDIR=`pwd`
SCRIPTDIR=`pwd`/scripts
LOGDIR=$MAINDIR/logs
CMSDIR=$CMSSW_BASE/src


condorFile=$SCRIPTDIR/submitJobsTUPLE.sh

ALGOS=(iter0 iter1 iter2 iter3 iter4 iter5 iter6 iter7)
#ALGOS=(iter5)
#ALGOS=(iter0 iter1 iter3)

if [ -e $condorFile ]
then
    rm -rf $condorFile
fi
touch $condorFile
chmod a+x $condorFile

filelist=files0.list

i=0
while read line
  do
  for algo in "${ALGOS[@]}"
  do
    runScript=$SCRIPTDIR/runJobsTUPLE_${i}_${algo}.sh
    if [ -e $runScript ]
	then
	rm -rf $runScript
    fi
    touch $runScript
    chmod a+x $runScript
    
  
    echo "#BSUB -o $LOGDIR/tuple_${algo}_${i}.out" >> $runScript
    echo "#BSUB -e $LOGDIR/tuple_${algo}_${i}.err" >> $runScript
    echo "#BSUB -L /bin/bash" >> $runScript
    echo "cd $CMSDIR" >> $runScript
    echo "export SCRAM_ARCH=$SCRAM_ARCH" >> $runScript
    echo 'eval `scramv1 runtime -sh`' >> $runScript
    echo "cd $MAINDIR" >> $runScript
    
    echo "cmsRun runTuple.py $line $i $algo" >> $runScript
    
    echo "bsub -R \"pool>30000\" -q 1nd < $runScript" >> $condorFile
  done
  let i++  
done < $filelist
