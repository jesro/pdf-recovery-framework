#!/bin/bash
source /app/controller/profiles.sh
source /app/controller/estimator.sh
source /app/controller/planner.sh
source /app/controller/executor.sh

clear
echo "PDF Recovery Framework"
echo "----------------------"
echo "1) Bank bill"
echo "2) Statement"
echo "3) Custom"
read -p "Choose profile: " p

case $p in
  1) load_profile bank_bill ;;
  2) load_profile statement ;;
  3) load_profile custom ;;
  *) exit 1 ;;
esac

if [ "$ATTACK" == "mask" ]; then
  estimate_mask $LETTERS $DIGITS
fi

build_plan
execute_plan