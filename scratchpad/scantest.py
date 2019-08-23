import regex
import json

### REGEX PATTERNS ###
system_extractor = regex.compile(r'^(.+) - ')
#### REGEX PATTERNS END ###

### Here we load static files like lookup tables. ###
### They should not be modified, they are intended for global use by multiple functions ###
with open('static/group_lookup.json') as f:
    group_lookup = json.load(f)
    f.close()
with open('static/category_lookup.json') as f:
    cat_lookup = json.load(f)
    f.close()
with open('static/ships.json', encoding='utf-8') as f:
    ships = json.load(f)
    f.close()
with open('static/groups.json') as f:
    groups = json.load(f)
    f.close()
with open ('static/solarsystemnames.json') as f:
    systems = json.load(f)
    f.close()

with open('misc/testdata.json') as f:
    testdata = json.load(f)
    f.close()

scan = testdata['scan_data']

def find_system(parsed_scan):
    system_object_list = []
    system_pattern_matches = []
    system_name_matches = []
    for entry in parsed_scan:
        if cat_lookup[group_lookup[entry['item_name']]] == 'Structure':
            system_object_list.append(entry['name_str'])
    
    for entry in system_object_list:
        res = regex.search(system_extractor, entry)
        system_pattern_matches.append(res.group(1))    

    for entry in system_pattern_matches:
        if entry in systems:
            system_name_matches.append(entry)

    top_count = 0
    top_match = None
    for entry in system_name_matches:
        count = system_name_matches.count(entry)
        if count > top_count:
            top_match = entry
            top_count = count

    return top_match

print(find_system(scan))