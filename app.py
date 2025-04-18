from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = f"Accessed at {datetime.now()}\n"
        with open("log.txt", "a") as f:
            f.write(message)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from Docker container with logs!")

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 80), SimpleHandler)
    print("Server started on port 80...")
    server.serve_forever()
