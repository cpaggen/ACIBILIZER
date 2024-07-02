#!/bin/bash

echo "[" > aci_modules.json
ansible-doc --list | grep cisco.aci | grep -oP "^\S+" | \
while read MODULE; do
    ansible-doc $MODULE -j >> aci_modules.json
    echo "," >> aci_modules.json
done
sed '$ s/.$/]/' aci_modules.json > aci_modules.tmp && mv aci_modules.tmp aci_modules.json
jq . aci_modules.json > aci_modules.tmp && mv aci_modules.tmp aci_modules.json

