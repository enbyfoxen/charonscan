import psycopg2
from configparser import ConfigParser
import json

def __config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for entry in params:
            db[entry[0]] = entry[1]
    
    else:
        raise Exception('Section {0} not found in {1} file'.format(section, filename))

    return db   

def __connect():
    conn = None
    try:
        # read connection parameters
        params = __config()
 
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        # return connection
        return conn
    except(Exception, psycopg2.DataError) as error:
        print(error)
        exit()

def get_scan(scan_id):
    cur = conn.cursor() #define cursor
    cmd = 'SELECT * FROM dscan_data WHERE scan_id = %s' # SQL query, get all columns from scan_data where scan_id matches
    cur.execute(cmd, (scan_id, ))
    dat = cur.fetchone()
    cur.close()
    if dat == None: # check if response is empty (doesnt exist)
        return None
    else:
        # put data into json format before returning it.
        data = { 
        "scan_UUID" : dat[0],
        "scan_data" : dat[1],
        "datetime_created" : dat[2].strftime("%Y-%m-%d %H:%M:%S"),
        "typelist" : dat[3],
        "grouplist" : dat[4],
        "catlist" : dat[5],
        "system" : dat[6]
        }
        data = json.dumps(data)
        return data
        
def get_local_scan(scan_id):
    cur = conn.cursor()
    cmd = 'SELECT * FROM localscan_data WHERE scan_id = %s'
    cur.execute(cmd, (scan_id, ))
    dat = cur.fetchone()
    cur.close()
    if dat == None:
        return None
    else:
        data = {
            "scan_UUID" : dat[0],
            "scan_data" : dat[1],
            "datetime_created" : dat[2].strftime("%Y-%m-%d %H:%M:%S")
        }
        data = json.dumps(data)
        return data

def add_local_scan(scan_id, scan_data, creation_time):
    json_scan_data = json.dumps(scan_data)
    cur = conn.cursor()
    cmd = 'INSERT INTO localscan_data VALUES (%s, %s, %s)'
    cur.execute(cmd, (str(scan_id), json_scan_data, creation_time))
    conn.commit()
    cur.close()

def add_scan(scan_id, scan_data, creation_time, typelist, grouplist, catlist, system):
    json_data = json.dumps(scan_data) # dump scan data to json
    json_typelist = json.dumps(typelist)
    json_grouplist = json.dumps(grouplist)
    json_catlist = json.dumps(catlist)
    cur = conn.cursor()
    # write data to database
    cmd = 'INSERT INTO dscan_data VALUES (%s, %s, %s, %s, %s, %s, %s)'
    cur.execute(cmd, (str(scan_id), json_data, creation_time, json_typelist, json_grouplist, json_catlist, system))
    conn.commit()
    cur.close()


# define connection globally
global conn
# assigned connection
conn = __connect()
