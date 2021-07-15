
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
  long_description = fh.read()

classifiers = [
  'Development Status :: 1 - Alpha',
  'Framework :: Terminal',
  'Intended Audience :: Developers',
  'Operating System :: MacOS',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3',
  'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(
  name='lily',
  version='0.1.1',
  description='A python package that generate `.gitignore` file with the required directories and extensions.',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url='https://github.com/mutairibassam/gitignore-generator',
  author='mutairibassam',
  author_email='mutairibassam@gmail.com',
  license='GNU',
  classifiers=classifiers,
  keywords='gitignore',
  packages=find_packages(),
  install_requires=[''],
  extras_require={
    "dev": [
      "pytest>=3.8",
    ]
  }
)
