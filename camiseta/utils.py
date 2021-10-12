from camiseta.tempfile import *
import pathlib, os

class Doc:
    def __init__(self, path='', file_name = ''):
        self.path = path
        self.name = file_name

        # Validating path
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
