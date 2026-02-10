#!/bin/bash

build_plan() {
  if [ "$TOOL" == "hashcat" ] && [ "$ATTACK" == "mask" ]; then
    MASK=""
    for ((i=0;i<LETTERS;i++)); do MASK+="?l"; done
    for ((i=0;i<DIGITS;i++)); do MASK+="?d"; done

    PLAN="hashcat mask attack with mask $MASK"
  fi
}