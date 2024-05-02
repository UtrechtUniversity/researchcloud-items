# Mock the SURF ResearchCloud user api
# Start a simple http server that simply returns a bit of test JSON

PORT = 8080

import http.server
import socketserver
import json

test_api_response = [
    {
    "username" :"testuser",
    "ssh_keys": ["ssh-rsa bla testuser@local.local"],
    "roles": ["rsc_developers","@all","src_co_wallet","src_ws_admin","src_co_developer","src_co_admin"],
    "research_drive_secret": None,
    "integer_id":2593,
    "services":[]
    }
]

class Server(http.server.SimpleHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
    def do_GET(self):
        self._set_headers()
        self.wfile.write(json.dumps(test_api_response).encode())

with socketserver.TCPServer(("", PORT), Server) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
