cc-django-app
=============

A cookiecutter_ template for a re-usable Django app that is running on Travis
for CI using py.test as the testrunner. It set ups the project with a BSD
(3-clause) license.

.. _cookiecutter: https://github.com/audreyr/cookiecutter

Usage
------

Run the following command to setup up cookie cutter in a virtualenv for your
project. Let's call it ``fancypants``::

    $ mkvirtualenv fancypants
    $ pip install cookiecutter
    $ cookiecutter https://github.com/elbaschid/cc-django-app.git

Answer the questions on the commandline and you are all done.

You might want to set the project directory as your default for the virtualenv
by doing::

    $ cd fancypants
    $ setvirtualenvproject
