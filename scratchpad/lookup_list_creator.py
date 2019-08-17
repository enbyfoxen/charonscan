import json

with open('../groupName_catID.json', encoding="utf-8") as f:
    groupID_lookup = json.load(f)
    f.close()

with open('../catID_catName.json') as f:
    groupName_lookup = json.load(f)
    f.close()

    lookup_list = {}

for key, value in groupID_lookup.items():
    lookup_list[key] = groupName_lookup[value]

with open('lookuplist.json', 'w') as f:
    json.dump(lookup_list, f)
    f.close()

