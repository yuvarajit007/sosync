#!/usr/bin/env python3
"""
SOSync Web Server Runner
Lightweight local HTTP server for the SOSync Emergency Response Platform.
"""
import http.server
import socketserver
import os
import sys

# Force UTF-8 stdout if available
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

def run():
    os.chdir(DIRECTORY)
    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print("============================================================")
            print(f"[*] SOSync Emergency Response System is LIVE at:")
            print(f"[*] http://localhost:{PORT}")
            print("============================================================")
            print(f"Serving files from: {DIRECTORY}")
            print("Press Ctrl+C to stop the server.")
            httpd.serve_forever()
    except OSError as e:
        if getattr(e, 'errno', None) in (98, 10048):
            alt_port = PORT + 1
            print(f"Port {PORT} in use, trying http://localhost:{alt_port}")
            with socketserver.TCPServer(("", alt_port), Handler) as httpd:
                print(f"[*] AegisSOS Emergency Response System is LIVE at http://localhost:{alt_port}")
                httpd.serve_forever()
        else:
            raise

if __name__ == '__main__':
    run()
