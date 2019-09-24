import dscan_parser
import json
from datetime import datetime

with open('scratchpad/dscan.json') as f:
    scanjson = json.load(f)
    f.close()

scanstring = scanjson['string']

start = datetime.now()
parsed = dscan_parser.parse_dscan(scanstring)
end = datetime.now()
delta = end - start
print(delta)