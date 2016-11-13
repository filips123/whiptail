import os
from setuptools import setup

def read(fname):
return open(os.path.join(os.path.dirname(__file__), fname)).read()

readme = read('README.rst')
changes = read('CHANGES.txt')
version_file = 'whiptail.py'
version = 1.0

setup(
    name='whiptail',
    version=version,
    description="Use whiptail to display dialog boxes from shell scripts",
    long_description=readme + '\n\n' + changes,
    keywords='whiptail',
    author='Marwan Alsabbagh / filips',
    author_email='marwan.alsabbagh@gmail.com / filip.stamcar@hotmail.com',
    url='https://github.com/fillips/whiptail',
    license='BSD',
    py_modules=['whiptail'],
    namespace_packages=[],
    include_package_data=True,
    platforms='Linux',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],
)
