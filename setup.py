from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = "This package aims to offer trivial but necessary modules for simple and personal python projects."
LONG_DESCRIPTION = "Initially this package only has one module, called read_write_json, that as the name suggests " \
"can only read and write data to json files. Another thing you will notice when looking at the code, is that it is written " \
"in very simple code. The reason for that and it is kind of obvious, is that I am still learning the language, but at the " \
"same time, I have a few personal projects of my own need, and as go deeper into the language and the projects itself I will " \
"increase the package and it's modules."

setup(
  name="trivial_modules", 
  version=VERSION,
  author="Naiara Correa",
  author_email="<seu_email@email.com>",
  description=DESCRIPTION,
  long_description=LONG_DESCRIPTION,
  packages=find_packages(),
  install_requires=[],
  
  keywords=['python', 'read json', 'write json', 'beginners'],
  classifiers= [
    "Development Status :: 1 - Alpha",
    "Intended Audience :: Software Development",
    "Programming Language :: Python :: 3.13",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: Linux",
  ]
)