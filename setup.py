from setuptools import setup
from simple_contact import get_version


setup(
    name='django-simple-contact',
    version=get_version(),
    license='GNU Lesser General Public License (LGPL), Version 3',

    description='Contact application for Django project',
    long_description=('Simple Contact is a pluggable contact app for '
                      'Django Web Framework.'),
    keywords='django apps contact form',

    author='Klaus Laube',
    author_email='kplaube@gmail.com',

    url='https://github.com/kplaube/django-simple-contact',
    packages=['simple_contact', ],
    include_package_data=True,
    zip_safe=False,

    classifiers=[
        'Environment :: Plugins',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
