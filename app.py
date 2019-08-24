from flask import Flask
from validate_uuid import validate_uuid4
import database
from flask import abort
from flask import request
import dscan_parser
import uuid
import datetime
from flask import jsonify
import json
import regex
### REGEX PATTERNS ###
system_extractor = regex.compile(r'^(.+) - ')
#### REGEX PATTERNS END ###
app = Flask(__name__)

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

# used to get scan data from API by UUID
@app.route('/api/scan/<path:path>')
def get_dscan(path): 
    if validate_uuid4(path) == False: # check if the string after scan/ is a valid UUID. If it isnt, abort
        return abort(400)
    else:
        res = database.get_scan(path) # make database call, if it comes back empty abort with 404.
        if res == None:
            return abort(404)
        else:
            response = app.response_class( # else, return json data from database call.
                response=res,
                mimetype='application/json'
            )
            return response

# used to add scans to database

### I REALLY NEED TO MAKE THIS CLEANER, BASICALLY HAVING THE SAME CODE FOR BOTH OPTIONS IS KINDA SHIT ###
@app.route('/api/post', methods = ['POST'])
def api_post():
    if request.headers['Content-Type'] == 'application/json': # check if the mimetype is json
        data = request.get_json() # retrieve json data
        if data == None: # abort if the client sent empty data
            abort(400)

        elif 'string' not in data:  # abort if the client sent data in the wrong format
            abort(400)

        else:
            scan = dscan_parser.parse_dscan(str(request.json['string'])) # parse scan data
        if scan.__len__() < 1: # abort if the parser comes back empty (we dont want empty scans in the database)
            abort(400)

        scan_id = store_scan(scan) # call function that stores the scan and returns the scan ID, send scan ID to client
        return scan_id
    
    elif request.headers['Content-Type'] == 'text/plain': # check if the mimetype is text/plain and the charset utf-8
        data = request.get_data(as_text=True) # get the plaintext data as text
        scan = dscan_parser.parse_dscan(data) # parse the scan data
        if scan.__len__() < 1: # abort if the parser comes back empty (we dont want empty scans in the database)
            abort(400)

        scan_id = store_scan(scan)  # call function that stores the scan and returns the scan ID, send scan ID to client
        return scan_id
    
    else: # if client sent neither json nor plain/text, abort with 415 (Unsupported Media Type)
        print(request.headers['Content-Type'])
        abort(415)

@app.route('/scan/<path:path>')
def serve_scan(path):
    return app.send_static_file('page.html')

@app.route('/post')
def postpage():
    return app.send_static_file('postscan.html')

### static json data ###
@app.route('/data/ships.json')
def get_dpsShips():
    return jsonify(ships)

@app.route('/data/groups.json')
def get_groups():
    return jsonify(groups)  
def store_scan(parsed_scan):
    scan_id = uuid.uuid4() # generate a random UUID to use as scan ID
    creation_time = datetime.datetime.now() # store current time as creation time
    typelist = make_typelist(parsed_scan) # call typelist function 
    grouplist = make_grouplist(typelist)
    catlist = make_catlist(grouplist)
    system = find_system(parsed_scan)
    database.add_scan(scan_id, parsed_scan, creation_time, typelist, grouplist, catlist, system) # make database call to create entry, pass scan ID, scan data and creation time
    datareturn = str(scan_id)
    return datareturn

def make_typelist(scan): # create a dictionary of each item name and how often it occurs
    typelist = {}
    for entry in scan:
        if entry['item_name'] in typelist:
            typelist[entry['item_name']] += 1

        else:
            typelist[entry['item_name']] = 1
    
    return typelist

def make_grouplist(typelist): # gets list of shiptypes and their numbers, uses lookup table to convert it to a list of shipgroups and their numbers
    global group_lookup
    grouplist = {}
    for key, value in typelist.items():
        if group_lookup[key] in grouplist:
            grouplist[group_lookup[key]] += value
        
        else:
            grouplist[group_lookup[key]] = value
    return grouplist

def make_catlist(grouplist):
    global cat_lookup
    catlist = {}
    for key, value in grouplist.items():
        if cat_lookup[key] in catlist:
            catlist[cat_lookup[key]] += value

        else:
            catlist[cat_lookup[key]] = value
    return catlist

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

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = '5000')
