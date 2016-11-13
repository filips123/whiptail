import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

try:
    readme = read('README.rst')
    changes = read('whiptailPy', 'CHANGES.txt')
except:
    readme = "Use whiptail to display dialog boxes from shell scripts"
    changes = ""
version = 1.0

setup(
    name='whiptailPy',
    version=version,
    description="Use whiptail to display dialog boxes from shell scripts",
    long_description=readme + '\n\n' + changes,
    keywords='whiptail',
    author='filips',
    author_email='filip.stamcar@hotmail.com',
    url='https://github.com/fillips/whiptail',
    py_modules=['whiptailPy'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
    ],
)
