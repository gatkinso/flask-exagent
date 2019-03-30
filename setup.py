"""
Flask-Agent
-------------

This is the description for Flask-Agent
"""
from setuptools import setup


setup(
    name='Flask-Exagent',
    version='1.0',
    url='https://github.com/gatkinso/flask-exagent/',
    license='BSD',
    author='Geoffrey Atkinson',
    author_email='geoffrey_atkinso@hotmail.com',
    description='A Flask Exchange sniffer agent',
    long_description=__doc__,
    py_modules=['flask_exagent'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)