#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='{{ cookiecutter.repo_name }}',
    version="0.0.0",
    url='https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.app_name }}',
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.email }}",
    description="{{ cookiecutter.description }}",
    long_description='\n\n'.join([
        open('README.rst').read(),
        open('CHANGELOG.rst').read(),
    ]),
    keywords="django, cms, pages, flatpages",
    license='BSD',
    platforms=['linux'],
    packages=find_packages(exclude=["sandbox*", "tests*"]),
    include_package_data=True,
    install_requires=[
        'Django',
    ],
    # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python',
    ]
)
