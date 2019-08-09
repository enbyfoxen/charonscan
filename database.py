import psycopg2
from configparser import ConfigParser

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
      
        # create a cursor
        cur = conn.cursor()
        # return cursor for use
        return conn, cur
    except(Exception, psycopg2.DataError) as error:
        print(error)
        exit()

def get_scan(scan_id):
    cmd = 'SELECT * FROM dscan_data WHERE scan_id = %s'
    cur.execute(cmd, (scan_id, ))
    dat = cur.fetchone()
    return(dat)

def add_scan(scan_id, scan_data, creation_time):
    cmd = 'INSERT INTO dscan_data VALUES (%s, %s, %s)'
    cur.execute(cmd, (scan_id, scan_data, creation_time))
    conn.commit()


# define connection and cursor globablly
global conn
global cur
# unpack tuple and assign connection and cursor
(conn, cur) = __connect()
