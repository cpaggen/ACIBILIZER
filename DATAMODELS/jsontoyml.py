import os
import json
from mappings import classToAnsible, ansibleToClass # need to get the mapping to ansible from json
import yaml
import pprint
from isConfigurableMap import isConfigurableMap # need to get the 
from defaultClassAttrValues import defaults
from exceptionDict import exceptions
from requiredParamsAliasesMap import requiredParamsAliases, reverse_alias_map
from paramAliasMap import paramAliasMap


PATH_TO_SAVE = ""

### start of the main function ###
reverseAliases = reverse_alias_map(requiredParamsAliases)

# this will be refactored at some stage, maybe some OOP or just cleaned, for now it does what I need it to

def reconstruct_yml(data, out_dir=None):
    save_path = "ansible_reconstructed.yml" if out_dir is None else os.path.join(out_dir, "ansible_reconstructed.yml")

    # here define default arguments (to delete)
    default_args = ['', "", "::", ":all:"]

    # invisible_arguments
    invisible_args = ["annotation", "dn"] # adjust as needed

    # define exception list
    exception_list = ['aci_access_span_src_group',
                        'aci_bd',
                        'aci_bd_dhcp_label',
                        'aci_bd_subnet',
                        'aci_domain_to_vlan_pool',
                        'aci_epg_subnet',
                        'aci_fabric_span_src_group',
                        'aci_tenant_span_src_group',
                        'aci_tenant_span_src_group_src']
    
    # here define duplicates list - handle dupes in values of class mappings
    # key (class) : value (dict) -> key (parent class) : value (correct mapping)

    duplicate_list = ['spanDestGrp', 'spanSrcGrp', 'spanSrc',
                      'mgmtMaintP', 'spanRsSrcToPathEp', 'fvSubnet',
                      'fvRsPathAtt', 'vzBrCP', 'dhcpRelayP',
                      'infraRsVlanNs', 'fvRsSecInherited', 'l1PhysIf',
                      'l2extInstP', 'mgmtOoB']

    # TO DO
    # finish this mapping
    duplicate_map = {
        # 'spanDestGrp': None,
        # 'spanSrcGrp': None,
        # 'spanSrc': None,
        # 'mgmtMaintP': None,
        # 'spanRsSrcToPathEp': None,
        'fvSubnet': {'aci_epg': 'aci_epg_subnet',
                     'aci_bd': 'aci_bd_subnet'},
        # 'fvRsPathAtt': None,
        'vzBrCP': "aci_contract",
        # 'dhcpRelayP': None,
        # 'infraRsVlanNs': None,
        # 'fvRsSecInherited': None,
        # 'l1PhysIf': None,
        # 'l2extInstP': None,
        # 'mgmtOoB': None
        }
    
    def map_json_to_ansible(json_data, key, map):
        try:
            new_key = map[key]
            json_data[new_key] = json_data.pop(key) # replace with ansible term
        except(KeyError): # no match found, skip
            pass

    def remove_isNotConfigurable(key, delete_key_list):
        try:
            if isConfigurableMap[key] == False:
                delete_key_list.append(key)
            else:
                pass
        except(KeyError):
            pass

    # helper method to navigate the exception dictionary
    def map_if_duplicate(child, parent = None):
        out = None
        try:
            out = duplicate_map[child][parent]
        except(KeyError):
            out = duplicate_map[child] # means there is no exception with the parent
        return out

    # simple method to check if a key in in the exception list
    # need to run this stuff before mapping anything - mapping is ambiguous
    def isduplicate(key):
        return key in duplicate_list

    def isdefault(parent_key, key, value, map):
        try:
            return value == map[parent_key][key] # means attribute has a default value
        except(KeyError):
            return False
        
    def isexception(key): # checks if key in exceptions
        try:
            return classToAnsible[key] in exception_list
        except(KeyError):
            return False

    def isfullydefault(val, parent_key, default_map, second_default_map):
        try:
            # convert defaults to sets 
            default_values_set = set(default_map[parent_key].values())
            second_default_values_set = set(second_default_map)
            
            # combine default args and default mapping
            combined_default_values_set = default_values_set.union(second_default_values_set)
            
            # to set 
            val_set = set(val)
            
            # check if subset
            return val_set.issubset(combined_default_values_set)
        except KeyError: # anything which is not "fv" is here atm
            return True # change based on desired behavior
        
    def save_to_yaml(save_path, data):
        # save_path = os.path.join(save_path, "ansible_reconstructed.yml")
        with open("ansible_reconstructed.yml", 'w') as file:
            yaml.dump(a, file, default_flow_style = False, sort_keys = False)
        print(f"YAML file has been saved to ansible_reconstructed.yml")

    # process data recursively
    # we need to track many parent-child keys, including some of sublists etc
    def process(data, parent_key:str = None, children_parent_key:str = None, attribute_parent_key:str = None, default_map:dict = defaults, dn:dict = {}) -> dict:
        """

        Handles mapping of 
        - classes to ansible
        - class parameters to ansible

        Gets rid of the "attributes" field found in the JSON config 

        Gets rid of any fields with default values

        Handles duplicates in mappings

        """

        changes = []

        yml_tasks = [] # we will also need a list of the nested dictionaries for yml correct format

        if isinstance(data, dict):
            keys_to_delete = [] # maintain this list outside any loop, prevents "changed size" errors

            for key, value in data.items():

                # handle dn - name of parent in child, grandchild etc etc
                if isinstance(value, dict) and "children" in value.keys():
                    try:
                        dn_key = reverseAliases[classToAnsible[key]]["name"][:-1]
                        dn_val = data[key]['attributes']["name"]
                        dn[dn_key] = dn_val
                    except(KeyError):
                        pass

                # all CLASSES are handled, exceptions..
                # TO DO -> handle exceptions like "changes"
                # also not quite sure everything we are looking for is exclusively under "children" ...
                if key == "children":
                    children_parent_key = parent_key

                    # children ALWAYS contains a nested list of nested dictionaries
                    for item in value:
                        for chld_key, chld_value in item.items():

                            # the last element of each tuple in "changes" is an integer
                            # this is ONLY TO IDENTIFY WHICH TYPE OF CHANGE IS NEEDED

                            # handle duplicate mappings FIRST
                            if isduplicate(chld_key):
                                changes.append((children_parent_key, chld_key, chld_value, 0))

                # all PARAMETERS are processed and mapped if needed
                elif key == "attributes": # these are all the parameters of the classes
                    attribute_parent_key = parent_key

                    # check if all attributes are default; if so, skip processing entirely
                    # empty dictionaries function will take care of it
                    if not isfullydefault(value.values(), parent_key, defaults, default_args):

                        if isexception(parent_key):

                            # TYPE 1 EXCEPTIONS -> ADD PARAMS WHICH ARE FOUND IN SUBCLASSES (handled same as type2 actually)
                            try:
                                for param, path in exceptions[classToAnsible[parent_key]].items():
                                    for item in data['children']: # it seems "children" is almost always found here
                                        if path[0] in item.keys():
                                            changes.append((parent_key, param, item[path[0]][path[1]][path[2]], 2))

                                            #######
                                            # path[0] is the exception class we need to get rid of, maybe through the changes system
                                            #######

                            except(KeyError) as e:
                                print(f"KeyError encountered: {e}")
                                pass

                        # TYPE 2 -> fix the dn attributes missing from children classes
                        if len(dn) > 0:
                            # assuming dn can only be a stack 2 long
                            if len(dn) > 2:
                                dn_list = list(dn.items())
                                dn_list.pop(1)
                                dn = dict(dn_list)
                            for dn_key, dn_val in dn.items():
                                changes.append((attribute_parent_key, dn_key, dn_val, 2))

                        # TYPE 2 CHANGES -> ATTRIBUTES FIELD REMOVAL, REMOVAL OF DEFAULTS
                        # append all non default params to "changes" - mapping and deletion is done here
                        for attr_key, attr_value in value.items(): # here empty values are also handled, eg if default then don't change
                            if attr_key not in invisible_args and attr_value not in default_args and not isdefault(attribute_parent_key, attr_key, attr_value, default_map):

                                # proper to fv_subnet once again?
                                # new exception found with "ip" -> creates a mask
                                if attr_key == "ip":
                                    attr_key = "gateway"
                                    changes.append((attribute_parent_key, 'mask', int(attr_value[-2:]), 2))

                                attr_value = attr_value if attr_key != "gateway" else attr_value[:-3]

                                changes.append((attribute_parent_key, attr_key, attr_value, 2)) # appends a tuple

                        # atm hardcoding "present" into yml, change later if needed
                        changes.append((attribute_parent_key, 'state', 'present', 2))

                    keys_to_delete.append("attributes") # can append key too

                # any exception will be caught here and will crash the entire program
                # therefore we want no exceptions
                if isinstance(value, (dict, list)):
                    try:
                        process(value, key, attribute_parent_key, dn)
                    except (KeyError) as e:
                        print(f"Error processing key {key}: {e}")
                        pass

                if isinstance(value, dict) and not value:
                    keys_to_delete.append(key)

                remove_isNotConfigurable(key, keys_to_delete) # change to boolean check? 

            # any modification to the dict can only be made outside the loops
            for key in keys_to_delete:
                try:
                    del data[key]
                except(KeyError):
                    pass

            # use the mapping function
            for key in list(data.keys()):
                if key not in duplicate_list: # mapping done elsewhere for dupes
                    map_json_to_ansible(data, key, classToAnsible)

        elif isinstance(data, list):
            for item in data:
                if isinstance(item, (dict, list)):
                    process(item, parent_key, attribute_parent_key, dn)

        # accessing keys in "data" instead of passing through a parent_key works
        # BECAUSE OF RECURSION, we are handling nested dictionaries as "data" everytime !!!!!!
        for change in changes:
            parent_key, child_key, child_value, change_type = change  # "change" is a 3x tuple
            if change_type == 2: # ATTRIBUTES parent key
                try:
                    new_key = reverseAliases[classToAnsible[parent_key]][child_key]
                    # at the moment no use for the required tag, can change later on if we need it somehow
                    if new_key[-1] == "*":
                        new_key = new_key[:-1]

                    data[new_key] = child_value
                    if child_key in data and new_key != child_key: # UNSURE if this is necessary anymore ..
                        del data[child_key]
                except KeyError:
                    data[child_key] = child_value

            # DOUBLE CHECK logic here, otherwise seems to work as expected
            # also can get rid of the whole "CHILDREN" key and move all upwards when we need it, only issue is how does this translate in yml
            # FOR NOW keep "children" key as it helps with ordering everything correctly
            elif change_type == 0: # CHILDREN parent key, DUPLICATE CASES
                try:
                    new_key = map_if_duplicate(child_key, classToAnsible[parent_key])
                    data['children'][0][new_key] = child_value
                    if child_key in data['children'][0]: # is this always the case? 0 idx? double check logic
                        del data['children'][0][child_key]
                except(KeyError):
                    pass

        return data

    # this function gets rid of empty structures in the output, think of {} for example
    # code is from GPT
    def remove_empty_dicts(data):
        if isinstance(data, dict):
            return {k: remove_empty_dicts(v) for k, v in data.items() if remove_empty_dicts(v)} # see return of function for why this works
        elif isinstance(data, list):
            for idx, item in enumerate(data):
                if isinstance(item, dict) and len(item) == 0:
                    data.pop(idx)
                else:
                    data[idx] = remove_empty_dicts(item)
            return data
        else:
            return data # this basically evaluates to false when the structure is None

    # handle reconstruction of yml with recursion

# TO DO -> ADD REMVOVAL OF "fvRs" CLASSES, too hard to handle above due to recursive issues

    def rebuild_yml(data, credentials_file = None, yml_list = [], parent_key = None, grandparent_key = None):

        entry_dict = {}

        if isinstance(data, dict):
            for key, value in data.items():

                nested_dictionary = {}

                # here restructuring is handled
                if parent_key == "children" or parent_key == None:

                    # bad trick to get rid of all non-aci modules
                    if key[:3] == "aci":
                        pass
                    else:
                        break

                    # set name to something generic
                    key_name = key.split("_")[1] if len(key.split("_")) == 2 else key.split("_")[2]
                    if parent_key != None:
                        grandparent_key_name = grandparent_key.split("_")[1] if len(grandparent_key.split("_")) == 2 else grandparent_key.split("_")[2:]
                        sentence = f"add a {key_name.upper()} to the {grandparent_key_name.upper()}"
                    else:
                        sentence = f"create {key_name} on ACI using {key} module"

                    entry_dict["name"] = sentence
                    for subkey, subvalue in data[key].items():
                        if subkey != "children":
                            # print(key, subkey, subvalue)
                            nested_dictionary[subkey] = subvalue
                    entry_dict["cisco.aci." + key] = nested_dictionary
                    entry_dict["delegate_to"] = "localhost"

                    yml_list.append(entry_dict)

                if isinstance(value, dict):
                    rebuild_yml(value, parent_key = key, grandparent_key = parent_key)

                elif isinstance(value, list):
                    for item in value:
                        rebuild_yml(item, parent_key = key, grandparent_key = parent_key)

        elif isinstance(data, list):
            for item in data:
                rebuild_yml(item, parent_key = key, grandparent_key = parent_key)

        return yml_list

    # process the initial data
    a = process(data)

    # delete the empty dictionaries
    b = remove_empty_dicts(a)

    fin = rebuild_yml(b)

    return fin

if __name__ == "__name__":
    
    with open("tn-nils-4.json", 'r') as file:
        y = json.load(file)

    out = reconstruct_yml(y)

    # save_path = os.path.join(save_path, "ansible_reconstructed.yml")
    with open("ansible_reconstructed.yml", 'w') as file:
        yaml.dump(out, file, default_flow_style = False, sort_keys = False)
    print(f"YAML file has been saved to ansible_reconstructed.yml")

    print(f"YAML file has been saved to {PATH_TO_SAVE}")
