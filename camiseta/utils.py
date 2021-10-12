from camiseta.tempfile import *
import pathlib, os
from http.server import HTTPServer, BaseHTTPRequestHandler
import webbrowser

class Save:
    def __init__(self, path='', file_name = ''):
        self.path = path
        self.name = file_name        
        if not os.path.isdir(self.path) and self.path != '':
            return print('Invalid output path {}'.format(self.path))
        else:
            if self.path == '': self.path = pathlib.Path().resolve()

        # Validating file name
        if self.name == '': self.name = 'index.html'
        if not self.name.endswith('.html'): self.name += '.html'
        
        temp_file.seek(0)
        with open('{}/{}'.format(self.path, self.name), 'w') as html:
            html.write(temp_file.read())
        temp_file.close()
        print('Finished. {} saved in {}/{}'.format(self.name, self.path, self.name))

class File:
    def __init__(self, path = ''):
        try:
            self.path = os.path.join(pathlib.Path().resolve(), path)
            with open(self.path, 'r') as file:
                temp_file.write(file.read())
        except:
            print('Error loading file {}. Ignoring.'.format(self.path))

class Server:
    def __init__(self, port = 3500):
        temp_file.seek(0)
        self.port = port
        server = HTTPServer(('', self.port), HelloHandler)
        print('Running')
        webbrowser.open_new_tab('http://127.0.0.1:{}/'.format(self.port))
        server.serve_forever()

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write(temp_file.read().encode())