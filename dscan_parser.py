import regex
import json
#load list of types to compare against, so we dont let any illegal types through
with open('static/typelist.json', encoding='utf-8') as f:
    typeset = set(json.load(f))
    f.close()
### REGEX PATTERNS ###
dscan_splitter = regex.compile(r'\d+\t[^\t]+\t[^\t]+\t(?:[\d,]+ (?:km|m)|-)', flags = regex.MULTILINE | regex.VERSION1) # find every line that is a valid D-Scan line
dscan_extractor = regex.compile(r'(\d+)\t([^\t]+)\t([^\t]+)\t((?:[\d,]+ (?:km|m))|-)', flags = regex.VERSION1) # extract all the values (item_id, name_string, item_name, range) from each D-Scan line
range_extractor = regex.compile(r'(\d*)( km| m)') # split up the range value
#### REGEX PATTERNS END ###

def parse_dscan(dscan):

    dscan_lines = regex.findall(dscan_splitter, dscan)

    dscan_lines_entries = []
    for entry in dscan_lines: # create a list of all valid D-Scan lines
        tmp = regex.findall(dscan_extractor, entry)
        dscan_lines_entries.append(tmp)

    dscan_data = []

    for entry in dscan_lines_entries: # take the list of D-Scan lines, take the values and add them to a dictionary. Add that dictionary to a list.
        if entry[0][2] in typeset:
            if entry[0][3] == '-': # set range to -1 if the range is not displayed (signified by '-' in the D-Scan line)
                range = -1
            else:
                range_match = regex.search(range_extractor, entry[0][3]) # take the range value, remove the commas from it, if its displayed in km convert to m.
                range_value = range_match.group(1)
                range_value.replace(",", "")
                if range_match.group(2) == " km":
                    range = int(range_value) * 1000
                else:
                    range = int(range_value)    
                
            dscan_entry = { # generate dictionary
                "itemID": int(entry[0][0]),
                "name_str": entry[0][1],
                "item_name": entry[0][2],
                "range": range
            }

            dscan_data.append(dscan_entry)
    return(dscan_data)