"""
Flask-Arango
-------------

Flask extension that provides integration with the Arango graph database using
the pyArango library. Under initial development.

"""
from setuptools import setup


setup(
    name='Flask-Arango',
    version='0.1.1',
    url='https://github.com/grucin/flask-arango',
    license='Apache License, 2.0',
    author='Grzegorz Rucinski',
    author_email='grucin@gmail.com',
    description='Flask extension providing integration with Arango.',
    long_description=__doc__,
    py_modules=['flask_arango'],
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'Flask >= 0.10',
        'pyArango >= 1.0.3'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
