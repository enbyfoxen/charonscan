import requests_unixsocket
import json
import urllib.parse
import requests
with open('localscan.json') as f:
    scan = json.load(f)
    f.close()

class EsiClient:
    def __init__(self, socket_path):
        self.socket_path = urllib.parse.quote(socket_path, safe='')
        self.session = requests_unixsocket.Session()

    def submit(self, local_json):
        r = self.session.post('http+unix:://' + self.socket_path + '/local', json=local_json)
        return r.text

if __name__ == "__main__":
    r = requests.post('http://10.0.0.2:8080/local', json=scan)
    print(r.text)