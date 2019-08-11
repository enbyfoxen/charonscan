from flask import Flask
from validate_uuid import validate_uuid4
import database
from flask import abort
from flask import request
import dscan_parser
import uuid
import datetime
from flask import jsonify

app = Flask(__name__)

@app.route('/api/scan/<path:path>')
def get_dscan(path):
    if validate_uuid4(path) == False:
        return abort(400)
    else:
        res = database.get_scan(path)
        if res == None:
            return abort(404)
        else:
            response = app.response_class(
                response=res,
                mimetype='application/json'
            )
            return response
        
@app.route('/api/post', methods = ['POST'])
def api_post():
    if request.headers['Content-Type'] == 'application/json':
        data = request.get_json()
        if data == None:
            abort(400)
        else:
            scan = dscan_parser.parse_dscan(str(request.json['string']))
        if scan.__len__() < 1:
            abort(400)
        scan_id = uuid.uuid4()
        creation_time = datetime.datetime.now()
        database.add_scan(scan_id, scan, creation_time)
        data = {"scan_id" : scan_id}
        return jsonify(data)
    else:
        abort(415)



if __name__ == "__main__":
    app.run(debug=True)
