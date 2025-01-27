import io
import os
from distutils.file_util import copy_file
from setuptools import setup, find_packages


__version__ = None
with open('sendgrid/version.py') as f:
    exec(f.read())

def getRequires():
    deps = ['python_http_client>=3.2.1']
    return deps


dir_path = os.path.abspath(os.path.dirname(__file__))
readme = io.open(os.path.join(dir_path, 'README.rst'), encoding='utf-8').read()

setup(
    name='sendgrid',
    version=str(__version__),
    author='Elmer Thomas, Yamil Asusta',
    author_email='dx@sendgrid.com',
    url='https://github.com/sendgrid/sendgrid-python/',
    packages=find_packages(exclude=["temp*.py", "test", "tests"]),
    include_package_data=True,
    license='MIT',
    description='Twilio SendGrid library for Python',
    long_description=readme,
    install_requires=getRequires(),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
