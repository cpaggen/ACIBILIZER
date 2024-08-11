import os
import json
from mappings import CLASS_TO_ANSIBLE_MAP # need to get the mapping to ansible from json
import yaml
from isConfigurableMap import ACI_MODULE_IS_CONFIGURABLE_MAP # need to get the 
from defaultClassAttrValues import ACI_MODULE_ATTRIBUTES_DEFAULT_VALUES
from exceptionDict import ACI_MODULE_DEPENDENCIES_FROM_CHILDREN
from requiredParamsAliasesMap import ACI_MODULE_ALIASES_TO_ATTRIBUTES_MAP
import time
import re

# define all the paths here
PATH_TO_SAVE        = "./VALIDATION/output.yml"
PATH_TO_JSON        = "./TENANT_EXAMPLE/tenantLeopoldo.json"
PATH_TO_CREDENTIALS = ""
PATH_TO_INVENTORY   = "./VALIDATION/aciInventory.ini"
PATH_TO_FINAL       = "./VALIDATION/output-final.yml"

### start of the main function ###

# this will be refactored at some stage, maybe some OOP or just cleaned, for now it does what I need it to

def reconstruct_yml(data, out_dir=None, inventory = None):
    save_path = "ansible_reconstructed.yml" if out_dir is None else os.path.join(out_dir, "ansible_reconstructed.yml")

    # aci classes have some parameters which are default for all classes
    ATTRIBUTES_COMMON_DEFAULT_VALUES = ['', "", "::", ":all:", "unknown"]

    # invisible_arguments - be sure to have them "pre-mapping"
    INVISIBLE_ARGUMENTS = ["annotation", "dn", "rn", "uid", "modTs", "monPolDn",
                       "seg", "pcTag", "userdom", "tDn", "filter_nam",
                       "mac", "preferred", "numPorts", "encap"] # adjust as needed

    # define exception list - dependencies
    ACI_CLASSES_WITH_DEPENDENCIES_IN_CHILD = ['aci_access_span_src_group',
                        'aci_bd',
                        'aci_bd_dhcp_label',
                        'aci_bd_subnet',
                        'aci_domain_to_vlan_pool',
                        'aci_epg_subnet',
                        'aci_fabric_span_src_group',
                        'aci_tenant_span_src_group',
                        'aci_tenant_span_src_group_src',
                        'aci_epg']
    
    # here define duplicates list - handle dupes in values of class mappings
    # key (class) : value (dict) -> key (parent class) : value (correct mapping)
    ACI_CLASSES_WITH_MULTIPLE_MAPPINGS = ['spanDestGrp', 'spanSrcGrp', 'spanSrc',
                      'mgmtMaintP', 'spanRsSrcToPathEp', 'fvSubnet',
                      'fvRsPathAtt', 'vzBrCP', 'dhcpRelayP',
                      'infraRsVlanNs', 'fvRsSecInherited', 'l1PhysIf',
                      'l2extInstP', 'mgmtOoB']

    # TO DO
    # finish this mapping
    ACI_CLASSES_WITH_MULTIPLE_MAPPINGS_MAP = {
        # 'spanDestGrp': None,
        # 'spanSrcGrp': None,
        # 'spanSrc': None,
        # 'mgmtMaintP': None,
        # 'spanRsSrcToPathEp': None,
        'fvSubnet': {'aci_epg': 'aci_epg_subnet',
                     'aci_bd': 'aci_bd_subnet'},
        'fvRsPathAtt': 'aci_static_binding_to_epg',
        'vzBrCP': "aci_contract",
        # 'dhcpRelayP': None,
        # 'infraRsVlanNs': None,
        # 'fvRsSecInherited': None,
        # 'l1PhysIf': None,
        # 'l2extInstP': None,
        # 'mgmtOoB': None
        }
    
    def _map_json_to_ansible(json_data, key, map):
        """
        Maps classes as found in json config to aci terminology
        """
        try:
            new_key = map[key]
            json_data[new_key] = json_data.pop(key) # replace with ansible term
        except(KeyError): # no match found, skip
            pass

    def _remove_isNotConfigurable(key, delete_key_list):
        """
        Appends all non-configurable classes to deletion list
        """
        try:
            if ACI_MODULE_IS_CONFIGURABLE_MAP[key] == False:
                delete_key_list.append(key)
            else:
                pass
        except(KeyError):
            pass

    # helper method to navigate the exception dictionary - KEYS
    def _map_if_duplicate(child, parent = None):
        """
        Maps classes with multiple mappings using their parent class
        """
        out = None
        try:
            out = ACI_CLASSES_WITH_MULTIPLE_MAPPINGS_MAP[child][parent]
        except(KeyError, TypeError):
            out = ACI_CLASSES_WITH_MULTIPLE_MAPPINGS_MAP[child] # means there is no exception with the parent
        return out

    # maps entire dictionary - used for change of type 0
    def _map_if_duplicate_value(key, value):
        """
        Maps values
        """
        out = {}
        for subkey in value:
            try:
                new_key = ACI_MODULE_ALIASES_TO_ATTRIBUTES_MAP[key][subkey]
                out[new_key] = value[subkey]
            except KeyError:
                out[subkey] = value[subkey]
        return out

    # simple method to check if a key in in the exception list
    # need to run this stuff before mapping anything - mapping is ambiguous
    def _isduplicate(key):
        """
        
        """
        return key in ACI_CLASSES_WITH_MULTIPLE_MAPPINGS

    def _isdefault(parent_key, key, value, map):
        try:
            return value == map[parent_key][key] # means attribute has a default value
        except(KeyError):
            return False

    def _isexception(key): # checks if key in exceptions
        try:
            return CLASS_TO_ANSIBLE_MAP[key] in ACI_CLASSES_WITH_DEPENDENCIES_IN_CHILD
        except(KeyError):
            return False

    def _isfullydefault(val, parent_key, ACI_MODULE_ATTRIBUTES_DEFAULT_VALUES, second_default_map):
        try:
            # convert defaults to sets 
            default_values_set = set(ACI_MODULE_ATTRIBUTES_DEFAULT_VALUES[parent_key].values())
            second_default_values_set = set(second_default_map)
            
            # combine default args and default mapping
            combined_default_values_set = default_values_set.union(second_default_values_set)
            
            # to set 
            val_set = set(val)
            
            # check if subset
            return val_set.issubset(combined_default_values_set)
        except KeyError: # anything which is not "fv" is here atm
            return True # change based on desired behavior

    def _save_to_yaml(save_path, data):
        # save_path = os.path.join(save_path, "ansible_reconstructed.yml")
        with open("ansible_reconstructed.yml", 'w') as file:
            yaml.dump(a, file, default_flow_style = False, sort_keys = False)
        print(f"YAML file has been saved to ansible_reconstructed.yml")
    
    def _parse_ini_file(file_path):
        with open(file_path, 'r') as file:
            content = file.read()

        # get host username and password
        host_pattern = r'\[aci\]\s*([\d\.]+)'
        username_pattern = r'aci_username\s*=\s*(\S+)'
        password_pattern = r'aci_password\s*=\s*(\S+)'

        host = re.search(host_pattern, content)
        aci_username = re.search(username_pattern, content)
        aci_password = re.search(password_pattern, content)

        host = host.group(1) if host else None
        aci_username = aci_username.group(1) if aci_username else None
        aci_password = aci_password.group(1) if aci_password else None

        return host, aci_username, aci_password

    # process data recursively
    # we need to track many parent-child keys, including some of sublists etc
    def _process(data,
                parent_key:str = None,
                grandparent_key:str = None) -> dict:
        """
        #### `_process(data, parent_key=None, grandparent_key=None, default_map=defaults, dn={}, dn_key_stack=[])`

        **Arguments:**
        - `data` (dict or list): The data to process.
        
        **Arguments handled in recursion:**
        - `parent_key` (str): Key of the parent item. Defaults to `None`.
        - `grandparent_key` (str): Key of the grandparent item. Defaults to `None`.
    
        **Returns:**
        - `dict`: The processed data with attributes mapped and cleaned, and the "attributes" keys removed.
        """

        changes = []

        if isinstance(data, dict):
            keys_to_delete = [] # maintain this list outside any loop, prevents "changed size" errors

            for key, value in data.items():

                # all CLASSES are handled, exceptions..
                # TO DO -> handle exceptions like "changes"
                # also not quite sure everything we are looking for is exclusively under "children" ...
                if key == "children":

                    # children ALWAYS contains a nested list of nested dictionaries
                    for sublist in value:
                        for child_key, child_value in sublist.items():

                            # the last element of each tuple in "changes" is an integer
                            # this is ONLY TO IDENTIFY WHICH TYPE OF CHANGE IS NEEDED

                            # handle duplicate mappings FIRST
                            if _isduplicate(child_key):
                                changes.append((parent_key, child_key, child_value, 0))

                # all PARAMETERS are processed and mapped if needed
                elif key == "attributes": # these are all the parameters of the classes

                    # check if all attributes are default; if so, skip processing entirely
                    # empty dictionaries function will take care of it
                    if not _isfullydefault(value.values(), parent_key, ACI_MODULE_ATTRIBUTES_DEFAULT_VALUES, ATTRIBUTES_COMMON_DEFAULT_VALUES):

                        if _isexception(parent_key):
                            # TYPE 2 EXCEPTIONS -> ADD PARAMS WHICH ARE FOUND IN SUBCLASSES
                            try:
                                for param, path in ACI_MODULE_DEPENDENCIES_FROM_CHILDREN[CLASS_TO_ANSIBLE_MAP[parent_key]].items():
                                    for sublist in data['children']: # it seems "children" is always found here
                                        if path[0] in sublist.keys():
                                            changes.append((parent_key, param, sublist[path[0]][path[1]][path[2]], 2))

                                            #######
                                            # path[0] is the exception class we need to get rid of, maybe through the changes system
                                            #######

                            except(KeyError) as e:
                                # print(f"KeyError encountered: {e}")
                                pass

                        # append all non default params to "changes" - mapping and deletion is done here
                        for attr_key, attr_value in value.items(): # here empty values are also handled, eg if default then don't change

                            # these changes occur within the key itself, not a parent, and therefore it is handled as "type 1"
                            # could possibly handle with exceptions_list but risky..
                            if parent_key == "fvRsDomAtt" and attr_key == "tDn": # bypass the skip tDn
                                changes.append((parent_key, "tDn", attr_value, 1))

                            if parent_key == "fvRsPathAtt" and attr_key == "tDn":
                                changes.append((parent_key, "tDn", attr_value, 1))

                            if parent_key == "fvRsPathAtt" and attr_key == "encap":
                                changes.append((parent_key, attr_key, attr_value, 1))

                            # handle fvRsProv and fvRsCons
                            if parent_key == "fvRsCons":
                                changes.append((parent_key, "contract_type", "consumer", 2))
                            
                            if parent_key == "fvRsProv":
                                changes.append((parent_key, "contract_type", "provider", 2))

                            # TYPE 2 CHANGES -> ATTRIBUTES FIELD REMOVAL, REMOVAL OF DEFAULTS
                            if attr_key not in INVISIBLE_ARGUMENTS and attr_value not in ATTRIBUTES_COMMON_DEFAULT_VALUES and not _isdefault(parent_key, attr_key, attr_value, ACI_MODULE_ATTRIBUTES_DEFAULT_VALUES):

                                # proper to fv_subnet once again?
                                # new exception found with "ip" -> creates a mask, gateway
                                if attr_key == "ip":
                                    attr_key = "gateway"
                                    changes.append((parent_key, 'mask', int(attr_value[-2:]), 2))

                                attr_value = attr_value if attr_key != "gateway" else attr_value[:-3]

                                changes.append((parent_key, attr_key, attr_value, 2)) # appends a tuple

                        # atm hardcoding "present" into yml, change later if needed
                        changes.append((parent_key, 'state', 'present', 2))

                    keys_to_delete.append("attributes") # can append key too

                # any exception will be caught here and will crash the entire program
                # therefore we want no exceptions
                if isinstance(value, (dict, list)):
                    try:
                        _process(data = value, parent_key = key, grandparent_key = parent_key)

                    except (KeyError) as e:
                        print(f"Error processing key {key}: {e}")
                        pass

                if isinstance(value, dict) and not value:
                    keys_to_delete.append(key)

                _remove_isNotConfigurable(key, keys_to_delete) # change to boolean check? 

            # any modification to the dict can only be made outside the loops
            for key in keys_to_delete:
                try:
                    del data[key]
                except(KeyError):
                    pass

            # use the mapping function
            for key in list(data.keys()):
                if not _isduplicate(key): # mapping done elsewhere for dupes - changes of type 0 
                    _map_json_to_ansible(data, key, CLASS_TO_ANSIBLE_MAP)

        elif isinstance(data, list):
            for item in data:
                if isinstance(item, (dict, list)):
                    _process(data = item, parent_key = parent_key, grandparent_key = grandparent_key)

        # accessing keys in "data" instead of passing through a parent_key works
        # BECAUSE OF RECURSION, we are handling nested dictionaries as "data" everytime !!!!!!
        for change in changes:
            parent_key, child_key, child_value, change_type = change  # "change" is a 3x tuple
            if change_type == 2: # ATTRIBUTES parent key
                try:
                    new_key = ACI_MODULE_ALIASES_TO_ATTRIBUTES_MAP[CLASS_TO_ANSIBLE_MAP[parent_key]][child_key]

                    # at the moment no use for the required tag, can change later on if we need it somehow
                    if new_key[-1] == "*":
                        new_key = new_key[:-1]

                    data[new_key] = child_value
                    if child_key in data and new_key != child_key: # UNSURE if this is necessary anymore ..
                        del data[child_key]
                except KeyError:
                    data[child_key] = child_value

            # changes within same class (not associated with a parent)
            elif change_type == 1:

                if parent_key == "fvRsDomAtt":
                    if "vmm" in change[2].split("/")[1]:
                        dom_type_val = "vmm"
                        vm_provider_val = change[2].split("/")[1].split("-")[1].lower()
                        dom_val = change[2].split("/")[2][4:]

                    elif "phys" in change[2].split("/")[1]:
                        dom_type_val = "phys"
                        dom_val = change[2].split("/")[1].split("-")[1]

                    elif "l2dom" in change[2].split("/")[1]:
                        dom_type_val = "l2dom"

                    data["domain_type"] = dom_type_val

                    try:
                        data["vm_provider"] = vm_provider_val
                        data["domain"] = dom_val
                    except(UnboundLocalError):
                        pass

                if parent_key == "fvRsPathAtt" and child_key == "tDn":
                    data["leafs"] = change[2].split("/")[2].split("-")[1]
                    data["interface"] = change[2].split("-")[3].replace("[", "").replace("]", "")
                    data["pod_id"] = change[2].split("/")[1].split("-")[1]

                if parent_key == "fvRsPathAtt" and child_key == "encap":
                    data["encap_id"] = child_value.split("-")[1]
                    if child_key in data:
                        del data[child_key]

            # handle all duplicates
            elif change_type == 0: # CHILDREN parent key, DUPLICATE CASES

                # seems forcing the "children" index to be 0 causes issues..
                try:
                    new_key = _map_if_duplicate(child_key, CLASS_TO_ANSIBLE_MAP[parent_key])
                    new_value = _map_if_duplicate_value(new_key, child_value)

                    # iterate to find correct index.. slow but works
                    for child in data['children']:
                        if child_key in child:
                            child[new_key] = new_value
                            del child[child_key]
                            break

                except KeyError:
                    pass

        return data

    # this function gets rid of empty structures in the output, think of {} for example
    # code is from GPT
    def _remove_empty_dicts(data):
        if isinstance(data, dict):
            return {k: _remove_empty_dicts(v) for k, v in data.items() if _remove_empty_dicts(v)} # see out of function for why this works
        elif isinstance(data, list):
            for idx, item in enumerate(data):
                if isinstance(item, dict) and len(item) == 0:
                    data.pop(idx)
                else:
                    data[idx] = _remove_empty_dicts(item)
            return data
        else:
            return data # this basically evaluates to false when the structure is None

    # this function gathers all hierarchical parameter names - further used in reconstruct function
    # returns a dictionary with list values and string keys
    def _get_parent_attributes(data, 
                          parent_key=None, 
                          grandparent_key=None, 
                          great_grandparent_key=None, 
                          great_great_grandparent_key=None, 
                          parent_name=None, 
                          grandparent_name=None, 
                          great_grandparent_name=None, 
                          great_great_grandparent_name=None, 
                          changes=None):
        
        """
        #### `get_parent_attributes(data, parent_key=None, grandparent_key=None, great_grandparent_key=None, great_great_grandparent_key=None, parent_name=None, grandparent_name=None, great_grandparent_name=None, great_great_grandparent_name=None, changes=None)`

        **Arguments:**
        - `data` (dict or list): Data structure to gather hierarchical parameter names from.
        
        **Arguments handled in recursion:**
        - `parent_key` (str): Key of the current parent item. Defaults to `None`.
        - `grandparent_key` (str): Key of the grandparent item. Defaults to `None`.
        - `great_grandparent_key` (str): Key of the great-grandparent item. Defaults to `None`.
        - `great_great_grandparent_key` (str): Key of the great-great-grandparent item. Defaults to `None`.
        - `parent_name` (str): Name of the current parent item. Defaults to `None`.
        - `grandparent_name` (str): Name of the grandparent item. Defaults to `None`.
        - `great_grandparent_name` (str): Name of the great-grandparent item. Defaults to `None`.
        - `great_great_grandparent_name` (str): Name of the great-great-grandparent item. Defaults to `None`.
        - `changes` (dict): Dictionary to accumulate hierarchical parameter names. Defaults to `{}`.

        **Returns:**
        - `dict`: A dictionary containing aci classes along with a list of required attributes found in parent keys.
        """
        
        # this dict ensures we are not missing any params
        # for example aci_epg needs a bd, but this function does not find a bd otherwise

        if changes is None:
            changes = {}

        if isinstance(data, dict):
            for key, value in data.items():
                try:
                    current_name = ACI_MODULE_ALIASES_TO_ATTRIBUTES_MAP[key]["name"][:-1]  # remove mandatory tag
                except KeyError:
                    current_name = None

                if parent_key == "children": # need to append all this info for later use - iterate over pairwise, will work just fine
                    change = [i for i in [parent_name, grandparent_name, great_grandparent_name, great_great_grandparent_name, grandparent_key, great_great_grandparent_key] if i is not None]
                    changes[key] = change if "tenant" in change else change + ["tenant", "aci_tenant"] # need to be careful this is a len 6

                # could make it more clear somehow.. 
                _get_parent_attributes(value, key, parent_key, grandparent_key, great_grandparent_key, 
                                    current_name, parent_name, grandparent_name, great_grandparent_name, changes)

        elif isinstance(data, list):
            for item in data:
                _get_parent_attributes(item, parent_key, grandparent_key, great_grandparent_key, great_great_grandparent_key, 
                                    parent_name, grandparent_name, great_grandparent_name, great_great_grandparent_name, changes)

        return changes

    # handle reconstruction of yml with recursion
    # TO DO -> ADD REMVOVAL OF "fvRs" CLASSES, too hard to handle above due to recursive issues
    def _rebuild_yml(data, dn_parent_map={}, dn_attributes_map=None, credentials_file=None, yml_list=[], parent_key=None, grandparent_key=None, ini_inventory = inventory):
        """
        #### `rebuild_yml(data, dn_parent_map={}, dn_attributes_map=None, credentials_file=None, yml_list=[], parent_key=None, grandparent_key=None, ini_inventory=None)`

        **Arguments:**
        - `data` (dict/json): The data to be reconstructed into YAML.
        - `dn_parent_map` (dict): Mapping of distinguished names to their parent attributes. Defaults to `{}`.
        - `ini_inventory` (str): Path to the inventory file. Defaults to `None`.
        - `credentials_file` (str): Path to the credentials file. Defaults to `None`.
        
        **Arguments handled in recursion:**
        - `dn_attributes_map` (dict): Mapping of DN attributes. Defaults to `None`.
        - `yml_list` (list): List to accumulate YAML entries. Defaults to `[]`.
        - `parent_key` (str): Key of the parent item. Defaults to `None`.
        - `grandparent_key` (str): Key of the grandparent item. Defaults to `None`.

        **Returns:**
        - `list`: A list containing the reconstructed YAML structure ready for output.
        """

        entry_dict = {}

        tcp_flags_map = {"ack": "acknowledgment", "est": "established", "fin": "finish", "rst": "reset", "syn": "synchronize"}

        # get the params in .ini inventory
        hosts, username, password = _parse_ini_file(ini_inventory)

        if isinstance(data, dict):
            for key, value in data.items():

                # get dn attributes
                try:
                    parent_attribute = ACI_MODULE_ALIASES_TO_ATTRIBUTES_MAP[key]["name"][:-1]  # only applies to required params
                    dn_parent_map[key] = data[key][parent_attribute]

                except KeyError:
                    pass

                nested_dictionary = {}

                # here restructuring is handled
                if parent_key == "children" or parent_key is None:

                    # bad trick to get rid of all non-aci modules
                    if key[:3] == "aci":
                        pass
                    else:
                        break

                    # set name to something generic

                    key_name = key

                    # try:
                    #     key_name = key.split("_")[1] if len(key.split("_")) == 2 else key.split("_")[2]
                    # except(IndexError):
                    #     key_name = key

                    sentence = f"Task - Create {key_name.upper()}"

                    entry_dict["name"] = sentence

                    # add yml anchor
                    nested_dictionary['<<'] = "*aci_login"

                    # this does handle parents, not siblings however
                    if key in dn_attributes_map:
                        try:
                            if len(dn_attributes_map[key]) == 2:
                                nested_dictionary[dn_attributes_map[key][0]] = dn_parent_map[dn_attributes_map[key][1]]

                            elif len(dn_attributes_map[key]) == 4:
                                nested_dictionary[dn_attributes_map[key][0]] = dn_parent_map[dn_attributes_map[key][2]]
                                nested_dictionary[dn_attributes_map[key][1]] = dn_parent_map[dn_attributes_map[key][3]]

                            # the only case in which this is 6 is when we find no "tenant", then we simply add one like so
                            elif len(dn_attributes_map[key]) == 6:
                                nested_dictionary[dn_attributes_map[key][0]] = dn_parent_map[dn_attributes_map[key][2]]
                                nested_dictionary[dn_attributes_map[key][1]] = dn_parent_map[dn_attributes_map[key][3]]
                                nested_dictionary[dn_attributes_map[key][4]] = dn_parent_map[dn_attributes_map[key][5]]

                        except KeyError:
                            pass

                    for subkey, subvalue in data[key].items():
                        if subkey != "children":
                            # add the check for tcp_flags here..? 
                            if subkey == 'tcp_flags':
                                nested_dictionary[subkey] = [tcp_flags_map[i] for i in subvalue.split(",")]
                            else:
                                nested_dictionary[subkey] = subvalue

                    # if key in dn_attributes_map and key in 

                    entry_dict["cisco.aci." + key] = nested_dictionary
                    entry_dict["delegate_to"] = "localhost"

                    yml_list.append(entry_dict)

                if isinstance(value, dict):
                    _rebuild_yml(value, dn_parent_map, dn_attributes_map, credentials_file, yml_list, key, parent_key)

                elif isinstance(value, list):
                    for item in value:
                        _rebuild_yml(item, dn_parent_map, dn_attributes_map, credentials_file, yml_list, key, parent_key)

        elif isinstance(data, list):
            for item in data:
                _rebuild_yml(item, dn_parent_map, dn_attributes_map, credentials_file, yml_list, parent_key, grandparent_key)

        return [{
            "hosts": hosts,
            "connection": "local",
            "vars": {
                "aci_login": {
                    "hostname": "{{ inventory_hostname }}",
                    "username": username,
                    "password": password,
                    "use_proxy": "no",
                    "use_ssl": "yes",
                    "validate_certs": "no"
                }
            },
            "tasks": yml_list
        }]

    # process the initial data
    processed_data_1 = _process(data)
    processed_data_2 = _remove_empty_dicts(processed_data_1)
    required_attributes_from_parents_map = _get_parent_attributes(processed_data_2)
    processed_data_3 = _rebuild_yml(data = processed_data_2, dn_attributes_map = required_attributes_from_parents_map)

    return processed_data_3

if __name__ == "__main__":
    start_time = time.time()
    with open(PATH_TO_JSON, 'r') as file:
        y = json.load(file)

    out = reconstruct_yml(y, inventory = PATH_TO_INVENTORY)

    # save_path = os.path.join(save_path, "ansible_reconstructed.yml")
    with open(PATH_TO_SAVE, 'w') as file:
        file.write("---\n") # at start of file
        yaml.dump(out, file, default_flow_style = False, sort_keys = False)

    # remove single quotes from YAML anchors
    with open(PATH_TO_SAVE, 'r') as fin:
        lines = fin.readlines()

    with open(PATH_TO_FINAL, "wt") as fout:
        for line in lines:
            modified_line = line.replace("'<<': '*aci_login'", "<<: *aci_login")
            modified_line = modified_line.replace("aci_login:", "aci_login: &aci_login")
            modified_line = modified_line.replace("'yes'", "yes").replace("'no'", "no")
            fout.write(modified_line)

    # time 
    end_time = time.time()
    elapsed_time_ms = (end_time - start_time) * 1000

    print(f"YAML file has been saved to {PATH_TO_FINAL}")
    print(f"Completed in {elapsed_time_ms:.2f} ms")
