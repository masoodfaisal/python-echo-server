import http.server
import os


host = '0.0.0.0'
port = 8080

class EchoRequestHandler(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        print("GET not implemented")
        
        
    def do_POST(self):
        
        content_length = int(self.headers.get('Content-Length'))
        
        print(self.rfile.read(content_length))
        
        self.send_response(200)
    
    do_PUT = do_POST
    do_DELETE = do_GET

def main():
    try:
        print("Starting server at http://{}:{}\n".format(host, port))
        httpd = http.server.HTTPServer((host, port), EchoRequestHandler)
        httpd.serve_forever()
    finally:
        print("Server closed")

if __name__ == "__main__":
    main()