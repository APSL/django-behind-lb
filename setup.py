import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-behind-lb',
    version='1.0',
    packages=['behind_lb'],
    include_package_data=True,
    license='Public Domain',
    description='A very efficient and simple Django middleware to obtain the real IP address from the headers sent by a trusted load balancer',
    long_description=README,
    url='http://www.apsl.net/',
    author='Ricardo Galli',
    author_email='gallir@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
