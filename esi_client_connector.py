import requests_unixsocket
import json
import urllib.parse
with open('localscan.json') as f:
    scan = json.load(f)
    f.close

class EsiClient:
    def __init__(self, socket_path):
        self.socket_path = urllib.parse.quote(socket_path, safe='')
        self.session = requests_unixsocket.Session()
        try:
            self.session.post('http+unix://' + self.socket_path)
        except requests_unixsocket.requests.exceptions.RequestException as e:
            print(e)
            print('Could not connect to esiclient on defined socket. Please check socket path, if esiclient is running, and possibly permissions.')
            exit(1)

    def submit(self, local_json):
        r = self.session.post('http+unix://' + self.socket_path + '/local', json=local_json)
        if r.headers.get('string-invalid') == 'false':
            return r.json()
        else:
            return None

if __name__ == "__main__":
    client = EsiClient('/tmp/esiclient.sock')
    print(client.submit((scan)))
