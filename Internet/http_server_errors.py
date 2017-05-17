# http_server_errors.py
from http.server import BaseHTTPRequestHandler


class ErrorHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_error(404)


if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8084), ErrorHandler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()

