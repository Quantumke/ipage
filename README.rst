======================
Django Azure Template
======================

Django project template for Windows Azure, let you deploy Django on Windows Azure in just a few steps.


Install Django
===============

.. code-block:: sh

    $ pip install django


Start project
==============

.. code-block:: sh

    $ django-admin.py startproject <project_name> --template=https://github.com/tzangms/django-azure-template/zipball/master


Modify web.config
=================

Replace {{ project_name }} in *web.config* to your own project_name.


Install requirements
=====================

Using Windows Azure, your have to install all the dependencies into *site-packages* directory, you can use pip with -t args to do this. shown as below.

.. code-block:: sh

    $ pip install django wsgiref -t site-packages


Commit and Deploy
=================

Commit your code include the site-packages directory. and setup the deploy in Windows Azure with any VCS, then you should see your Django project running in a few minutes.
