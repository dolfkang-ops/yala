import http.server
import socketserver
import webbrowser
import threading
import time

PORT = 8000
DIRECTORY = "."

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def open_browser():
    time.sleep(1)  # wait for server to start
    url = f"http://localhost:{PORT}"
    print(f"Opening browser to {url}...")
    webbrowser.open(url)

if __name__ == "__main__":
    # Disable caching for easier local changes testing
    Handler.extensions_map.update({
        '.html': 'text/html',
        '.css': 'text/css',
        '.js': 'application/javascript',
    })
    
    # Start browser opener thread
    threading.Thread(target=open_browser, daemon=True).start()

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving HTTP on port {PORT} (http://localhost:{PORT})... Press Ctrl+C to stop.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
