# Borderless Lotus Press
A simple Developer Blog for personal use which provides the next functionallity (TO BE DONE):
* Developers can add new entries to the devBlog.
* Regular users can comment on the entries.
* The entries use markdown.

![Lotus Logo][logo]

[logo]: https://github.com/panteleevnikita/borderless_lotus_press/blob/master/static/images/logo.png "Lotus"

Lista de recursos de usar: 
* [Cosmo para bootstrap 4](https://bootswatch.com/4-alpha/cosmo/)
    - Implementado.
    
* A eligir uno de lso dos siguientes (u otra opción que nos proporcione una funcionalidad similar):
    - [Campo de markdown para django](https://github.com/adi-/django-markdownx)
    - [pypandoc - Alternativa para markdown personalizado](https://pypi.python.org/pypi/pypandoc)
    
* [Despliegue con ngnix](http://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)
    - Tener en cuenta el donde se va a despliegar la aplicación y en que momento.
* [Informacion sobre venv - entorno virtual](https://docs.python.org/3/library/venv.html)
* [Framework de pruebas unitarias de python](https://docs.python.org/3/library/unittest.html)
    - Seria interesante tenerlo sobre todo para las transformaciones a .md
* [Automatizacion de construccion](http://pybuilder.github.io/)
    - Para añadir la libreria que trate el .md lo primero y otras cosas como uwsgi, unittest o django mismo como dependencia.
