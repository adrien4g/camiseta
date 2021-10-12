from camiseta.tempfile import *

class Meta:
    def __init__(self, prop):
        self.prop = prop
        temp_file.write('<meta {}/>'.format(self.prop))

class Css:
    def __init__(self, attribute, style):
        temp_file.write(attribute + '{' + style + '}')

class Text:
    def __init__(self, text):
        self.text = text
        temp_file.write(self.text)