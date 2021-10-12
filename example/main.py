from camiseta import *

with Html(True):
    with Head():
        Meta('charset="UTF-8"')
        with Style():
            File('example/style.css')

    with Body():
        with Tag('header'):
            for i in ['Home', 'Contato', 'Sobre']:
                with A('{}'.format(i)):
                    with Tag('p', 'header_p'):
                        Text(i)

        with Tag('div', 'app'):
            for i in range(0, 25):
                with Tag('div', 'box'):
                    with Tag('p', 'box_name'):
                        Text('Container Name')
                    Img('https://miro.medium.com/max/336/0*rmv6pZTW2hfP2XYd.png', 'docker-logo', Class='container_logo')
                    with Tag('p', 'box_image'):
                        Text('Container Image')


Server()