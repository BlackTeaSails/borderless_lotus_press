# Borderless Lotus Press
A simple Developer Blog for personal use which provides the next functionallity (TO BE DONE):
* Developers can add new entries to the devBlog.
* Regular users can comment on the entries.
* The entries use markdown.

Lista de recursos de utiles: 
* [Cosmo para bootstrap 4](https://bootswatch.com/4-alpha/cosmo/)
    - Implementado.
    
* A eligir uno de lso dos siguientes (u otra opción que nos proporcione una funcionalidad similar):
    - [Campo de markdown para django](https://github.com/adi-/django-markdownx)
    - [pypandoc - Alternativa para markdown personalizado](https://pypi.python.org/pypi/pypandoc)
    
* [Despliegue con ngnix](http://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)
    - Tener en cuenta el donde se va a despliegar la aplicación y en que momento.
* [Informacion sobre venv - entorno virtual](https://docs.python.org/3/library/venv.html)
* Test Unitarios para Django
    - [Framework de pruebas unitarias de python](https://docs.python.org/3/library/unittest.html)
    - [Interfaz de las pruebas unitarias de unittest para django](https://docs.djangoproject.com/en/1.11/topics/testing/overview/)
    - [Medida de cobertura de las pruebas en django](http://django-testing-docs.readthedocs.io/en/latest/coverage.html)

    - Seria interesante tenerlo sobre todo para las transformaciones a .md
* Automatización de la construcción
    - [Automatizacion de construccion](http://pybuilder.github.io/)
    - Python posee su propia implementacion para las pruebas, pero no para automatización de los tests ni la construccion de las dependencias. :/
    - Para añadir la libreria que trate el .md lo primero y otras cosas como uwsgi, unittest o django mismo como dependencia.
    
* [Articulo sobre estrategia de ramas](http://nvie.com/posts/a-successful-git-branching-model/)


* Una alternativa posible es usar ansible para instalar las dependencias y ejecutar las tareas de testing de django:
    - [manage.py de django con Ansible (incluye test)](http://docs.ansible.com/ansible/django_manage_module.html)
    - [Pip con ansible (incluye venv)](http://docs.ansible.com/ansible/pip_module.html)

![Lotus Logo][logo]

[logo]: https://github.com/panteleevnikita/borderless_lotus_press/blob/master/static/images/logo.png "Lotus"
