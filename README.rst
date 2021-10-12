Camiseta
________
A framework made with python to generate html files easily.

Install
_______

``pip3 install camiseta``

Basic example
_____________
.. code:: python

    from camiseta import *
    
    with Html():
        with Body():
            with Tag('h1', Class='title'):
                Text('Hello Camiseta :D')
    Server()
    

How to use
____

use ``with`` to set child elements
Example:

.. code:: python

    with Tag('div'):
        with Tag('h1'):
            Text('Hello!')
            
    #Output
    '''<div>
        <h1>
            Hello!
        <h1>
    </div>'''

    Tag('div')
    Tag('h1')
    Text('Hello")

    #Output
    '''<div></div>
        <h1><h1>
        Hello!
    '''

Tags
~~~~

.. list-table::

  * - Tag
    - Return
    - Parameters
    
  * - Html()
    - <html> </html>
    - ignore_doctype = False

  * - Head()
    - <head> </head>
    - None

  * - Style()
    - <style> </style>
    - None

  * - Body()
    - <body> </body>
    - None

  * - Tag('tag')
    - <tag> </tag>
    - id = 'id' | Class = 'class'
  
  * - Img()
    - <img> </img>
    - src = 'image.com' | alt = 'alt' | width = '260px' | heigth = '300px' | id = 'id' | Class = 'class'
  
  * - A()
    - <a> </a>
    - href = 'link.com' | target = '_blank'
    
Adding <meta> to head
~~~~~~~~~~~~~~~~~~~
.. code:: python

    from camiseta import *

    with Html():
        with Head():
            Meta('charset="UTF-8"')
            
insert css
~~~~~~~~~~
.. code:: python

    from camiseta import *

    with Html():
        with Head():
            Style():
                Css('.box', """
                    background-color: Red;
                    border-radius: 25px;
                    """)
                # Importing css from file
                File('style.css')


HTTP server with your html response
___________________________________
To acess the html file you need to use the function ``Server``

.. code:: python

    from camiseta import *

    with Html():
        with Body():
            pass
    Server()

Parameters
~~~~~~~~~~

.. list-table::

  * - Name
    - Default value
    
  * - port
    - 3500

Exporting html
______________

To save the html file you need to use the function ``Save``

.. code:: python

    from camiseta import *

    with Html():
        with Body():
            pass
    Save()

Parameters
~~~~~~~~~~

.. list-table::

  * - Name
    - Default value
    
  * - path
    - Root of your project
    
  * - file_name
    - index.html

Example in example/example.py
___________

.. code:: python

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
                        Img('https://miro.medium.com/max/336/0*rmv6pZTW2hfP2XYd.png', alt='docker-logo', Class='container_logo')
                        with Tag('p', 'box_image'):
                            Text('Container Image')
    
    Server()