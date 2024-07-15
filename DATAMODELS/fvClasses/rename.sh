#!/bin/bash
shopt -s nullglob
for file in *
do
  if [ -f "$file" ];then
    newFile="fv${file}"
    mv "$file" "$newFile"
  fi
done
