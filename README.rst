**Django Simple Contact** is a pluggable application that renders a simple
contact form to your Django project.

It's a really simple implementation, easy-to-use, that may let you save
a little time in your development.

Installation
------------

1. Clone the source: ``git clone https://github.com/kplaube/django-simple-contact``
2. Put ``simple_contact`` on your path, or install using setuptools: ``python setup.py install``
3. Add ``'simple_contact'`` to your ``INSTALLED_APPS`` in your project's settings.py
4. Add URLs entries: ``url(r'^contact/', include('simple_contact.urls'))``


Templates
---------

Overwrite templates with your markup:

* ``templates/simple_contact/contact_form.html``
* ``templates/simple_contact/contact_email.html``
