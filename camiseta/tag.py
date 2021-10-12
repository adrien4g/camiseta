from camiseta.tempfile import *

class Html:
    def __init__(self, ignore_doctype = False):
        self.ignore_doctype = ignore_doctype

    def __enter__(self):
        self.prefix = ''
        if not self.ignore_doctype:
            self.prefix = '<!DOCTYPE html>'
        temp_file.write('{}<html>'.format(self.prefix))

    def __exit__(self, type, value, traceback):
        temp_file.write('</html>')

class Head:
    def __enter__(self):
        temp_file.write('<head>')

    def __exit__(self, type, value, traceback):
        temp_file.write('</head>')

class Style:
    def __enter__(self):
        temp_file.write('<style>')

    def __exit__(self, type, value, traceback):
        temp_file.write('</style>')

class Body:
    def __enter__(self):
        temp_file.write('<body>')

    def __exit__(self, type, value, traceback):
        temp_file.write('</body>')

class Tag:
    def __init__(self, tag, Class = '', id = '', props = ''):
        self.tag = tag
        self.attr_class = Class
        self.attr_id = id
        self.props = props
        
        if self.attr_id != '': self.attr_id = 'id="{}"'.format(self.attr_id)
        if self.attr_class != '': self.attr_class = 'class="{}"'.format(self.attr_class)
    
    def __enter__(self):
        temp_file.write('<{} {} {} {}>'.format(self.tag,self.attr_id, self.attr_class, self.props))

    def __exit__(self, type, value, traceback):
        temp_file.write('</{}>'.format(self.tag))

class Img:
    def __init__(self, src, alt, width = '', height = '', Class = '', id = ''):
        self.src = src
        self.alt = alt
        self. width = width
        self.height = height
        self.attr_class = Class
        self.attr_id = id

        if self.width != '': self.width = 'width="{}"'.format(self.width)
        if self.height != '': self.height = 'height="{}"'.format(self.height)

        if self.attr_id != '': self.attr_id = 'id="{}"'.format(self.attr_id)
        if self.attr_class != '': self.attr_class = 'class="{}"'.format(self.attr_class)

        temp_file.write('<img src="{}" alt="{}" {} {} {} {}>'.format(self.src, self.alt, self.width, self.height, self.attr_id, self.attr_class))

class A:
    def __init__(self, href, target='_blank'):
        self.href = href
        self.target = target

    def __enter__(self):
        temp_file.write('<a href="{}" target="{}">'.format(self.href, self.target))

    def __exit__(self, type, value, traceback):
        temp_file.write('</a>')