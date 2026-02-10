#!/bin/bash

estimate_mask() {
  letters=$1
  digits=$2

  combos=$(echo "26^$letters * 10^$digits" | bc)
  echo "Total combinations: $combos"

  cpu_rate=50000   # guesses/sec (conservative)
  gpu_rate=500000000

  cpu_time=$(echo "$combos / $cpu_rate" | bc)
  gpu_time=$(echo "$combos / $gpu_rate" | bc)

  echo "Estimated time (CPU): ~$cpu_time seconds"
  echo "Estimated time (GPU): ~$gpu_time seconds"
}