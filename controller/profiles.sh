#!/bin/bash

load_profile() {
  case "$1" in
    bank_bill)
      TOOL="hashcat"
      ATTACK="mask"
      LETTERS=4
      DIGITS=4
      ;;
    statement)
      TOOL="pdfrip"
      ATTACK="date"
      ;;
    custom)
      TOOL=""
      ATTACK=""
      ;;
    *)
      echo "Unknown profile"
      exit 1
  esac
}