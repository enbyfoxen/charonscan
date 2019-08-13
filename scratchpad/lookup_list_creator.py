import json

with open('../groupIDlookup.json', encoding="utf-8") as f:
    groupID_lookup = json.load(f)
    f.close()

with open('../groupnamelookup.json') as f:
    groupName_lookup = json.load(f)
    f.close()

    lookup_list = {}

for key, value in groupID_lookup.items():
    lookup_list[key] = groupName_lookup[value]

with open('lookuplist.json', 'w') as f:
    json.dump(lookup_list, f)
    f.close()

