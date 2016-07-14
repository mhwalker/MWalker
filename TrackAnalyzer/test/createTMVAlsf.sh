#!/bin/bash

#ITERATIONS=(0 1 2 3 4 5 6)
#ITERATIONS=(0 1 3 4 6)
ITERATIONS=(2 5 7)
#ITERATIONS=(5)
#VARIABLES=(absd0 absdz absdzPV absd0PV ndof nlayers nlayers3D nlayerslost chi2n chi2n_no1Dmod eta relpterr nhits minlost lostmidfrac pt)
VARIABLES=(ndof nlayers nlayers3D nlayerslost chi2n chi2n_no1Dmod eta relpterr nhits minlost lostmidfrac pt)


for iter in "${ITERATIONS[@]}"
do
  TMVAType="PURITYV02ITER${iter}"
  MAINDIR=`pwd`
  SCRIPTDIR=`pwd`/${TMVAType}
  LOGDIR=$MAINDIR/logs
  ROOTDIR=$MAINDIR/root
  CMSDIR="$MAINDIR/../"
  
  mkdir $SCRIPTDIR
  macro=run_TMVA.C
  cp TMVA_TEMPLATE.C $SCRIPTDIR/$macro
  
#ln -s $MAINDIR/TMVARegGui.C $SCRIPTDIR/TMVARegGui.C
  ln -s $MAINDIR/tmvaglob.C $SCRIPTDIR/tmvaglob.C
  
  
  sed -i "s/TMVA_TEMPLATE(/run_TMVA(/" $SCRIPTDIR/$macro
###V00##
  
  
  SPECTATORS=()
#SPECTATORS=(mass pt eta CAT4 classifier sinthetaCM costhetaCM tanPhi)
#CUT="sqrt(pow(inner_outer_x - outer_inner_x,2) + pow(inner_outer_y - outer_inner_y,2) + pow(inner_outer_z - outer_inner_z,2))*(sqrt(outer_inner_x*outer_inner_x + outer_inner_y*outer_inner_y) < sqrt(inner_outer_x*inner_outer_x + inner_outer_y*inner_outer_y) ? -1.0 : 1.0) > -4 && inner_nMissingOuter > 2 && sqrt(delta3d_x*delta3d_x+delta3d_y*delta3d_y) > 15"
  BKGCUT="fake == 1"
  SIGCUT="fake == 0"
  CUT="iter==${iter}"
  
  sed -i "/ADD CUT/ a   TCut mycut=\"$CUT\";" $SCRIPTDIR/$macro
  
  
  INPUTTREE=purityTree
  
  for i in ${VARIABLES[@]}; do
      sed -i "/ADD VARIABLES/ a   factory->AddVariable(\"$i\",'F');" $SCRIPTDIR/$macro
  done
  for i in ${SPECTATORS[@]}; do
      sed -i "/ADD SPECTATORS/ a   factory->AddSpectator(\"$i\",'F');" $SCRIPTDIR/$macro
  done
#for i in ${TARGETS[@]}; do
#    sed -i "/ADD TARGETS/ a   factory->AddTarget(\"$i\");" $SCRIPTDIR/$macro
#done
  
  
  file=f_input
  fname=../purityTree_iter${iter}.root
  tree=tree
  sed -i "/ADD SIGNAL/ a factory->SetInputTrees($tree,\"$SIGCUT\",\"$BKGCUT\");" $SCRIPTDIR/$macro
  sed -i "/ADD INPUT/ a TTree* $tree = (TTree*)${file}->Get(\"$INPUTTREE\");" $SCRIPTDIR/$macro
  sed -i "/ADD INPUT/ a TFile* $file = new TFile(\"$fname\");" $SCRIPTDIR/$macro
  
#nEvents=1000
#nJobs=1000
  
  condorFile=$SCRIPTDIR/submitTMVAlocal.condor
  
  if [ -e $condorFile ]
      then
      rm -rf $condorFile
  fi
  touch $condorFile
  
  runScript=$SCRIPTDIR/runScript.sh
  if [ -e $runScript ]
      then
      rm -rf $runScript
  fi
  touch $runScript
  chmod a+x $runScript
  
  echo "date" >> $runScript
  echo "#BSUB -o $SCRIPTDIR/${TMVAType}.out" >> $runScript
  echo "#BSUB -e $SCRIPTDIR/${TMVAType}.err" >> $runScript
  echo "#BSUB -L /bin/bash" >> $runScript
  echo "source /cvmfs/cms.cern.ch/cmsset_default.sh" >> $runScript  
  echo "cd $CMSSW_BASE/src" >> $runScript
  echo 'eval `scramv1 runtime -sh`' >> $runScript
#echo "cmsenv" >> $runScript
#  echo "cmscvsroot CMSSW" >> $runScript
  echo 'echo "CVSROOT is "$CVSROOT' >> $runScript
  echo 'echo "PWD is: "`pwd`' >> $runScript
  
  echo "cd $SCRIPTDIR" >> $runScript
  echo "root -q -b -l $macro\(\\\"${TMVAType}.root\\\"\)" >> $runScript
  
  echo "bsub -R \"pool>30000\" -q 1nd < $runScript" >> $condorFile
  
done