# Django Simple Contact

[![Build Status](https://travis-ci.org/kplaube/django-simple-contact.svg?branch=master)](https://travis-ci.org/kplaube/django-simple-contact)
[![Coverage Status](https://coveralls.io/repos/github/kplaube/django-simple-contact/badge.svg?branch=master)](https://coveralls.io/github/kplaube/django-simple-contact?branch=master)
[![PyPI version](https://badge.fury.io/py/django-simple-contact.svg)](https://badge.fury.io/py/django-simple-contact)

**Django Simple Contact** is a pluggable application that renders a simple
contact form to your [Django](https://www.djangoproject.com/) project.

It's a really simple implementation, easy-to-use, that may let you save
a little time in your development.

## Installation

Using [pip](https://pypi.python.org/pypi/pip):

```
$ pip install django-simple-contact
```

Using the source code:

```
$ git clone https://github.com/kplaube/django-simple-contact
$ cd django-simple-contact/
$ python setup develop
```

Configuring:

- Add `simple_contact` to `INSTALLED_APPS` in your `settings.py`.
- Add the URL entries: `path('contact/', include('simple_contact.urls'))`

## Templates

If you want your own markup (of course you do!), it's possible by overwritting the following templates:

- `templates/simple_contact/contact_form.html`
- `templates/simple_contact/contact_email.html`

## Tests

Tests are a good idea, and we do our best to make it "as seamless as possible":

```
$ python setup.py test
```

It'll solve the project's dependencies and run the test suite.
