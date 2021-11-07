#!/bin/bash

random_size=(10 100 1000 10000)

for size in ${random_size[*]}
do
  for ((iteration=1; iteration < 10; iteration++))
  do
      python main.py -r "$size" -o /dev/null
      echo '-----------------------------'
  done
  echo 'size: '"$size"" tested"
  echo '----------------------------------------------------------'
done
