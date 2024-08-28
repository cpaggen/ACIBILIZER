-------------------------------------------------------------- TO RUN THIS SCRIPT -----------------------------------------------------------

-> install the packages in "requirements.txt" -- only "PyYaml" is required.

-> ensure "jsontoyml.py" is in the same directory as "required_maps.py"

-> run the following command in the terminal: python jsontoyml.py <<PATH TO JSON CONFIG>> <<PATH TO SAVE PLAYBOOK>> <<PATH TO ACI INVENTORY>>

--------------------------------------------------------- KNOWN BUGS / MISSING FEATURES -----------------------------------------------------

-> only supports fv/vz classes

-> values for "use_proxy", "use_ssl", "validate_certs" in "hosts - vars" currently hardcoded as "no", "yes", "no"

-> can potentially run into issues if a task includes any of the following: "spanDestGrp", "spanSrcGrp", "spanSrc", "mgmtMaintP",
									    "spanRsSrcToPathEp", "dhcpRelayP", "infraRsVlanNs",
									    "fvRsSecInherited", "l1PhysIf", "l2extInstP", "mgmtOoB"