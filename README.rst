========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-grains_from_collectors/badge/?style=flat
    :target: https://readthedocs.org/projects/python-grains_from_collectors
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/mcapelli/python-grains_from_collectors.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/mcapelli/python-grains_from_collectors

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/mcapelli/python-grains_from_collectors?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/mcapelli/python-grains_from_collectors

.. |requires| image:: https://requires.io/github/mcapelli/python-grains_from_collectors/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/mcapelli/python-grains_from_collectors/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/mcapelli/python-grains_from_collectors/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/mcapelli/python-grains_from_collectors

.. |version| image:: https://img.shields.io/pypi/v/grains-from-collectors.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/grains-from-collectors

.. |commits-since| image:: https://img.shields.io/github/commits-since/mcapelli/python-grains_from_collectors/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/mcapelli/python-grains_from_collectors/compare/v0.0.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/grains-from-collectors.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/grains-from-collectors

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/grains-from-collectors.svg
    :alt: Supported versions
    :target: https://pypi.org/project/grains-from-collectors

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/grains-from-collectors.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/grains-from-collectors


.. end-badges

An example package. Generated with cookiecutter-pylibrary.
 open the YML file containg the colletor's grains info
 for each collector :
     look for hostname
     look for eth0 ip
 generete the final YAML file containig:
    for each collector :
    look for hostname
    look for eth0 ip

* Free software: BSD 2-Clause License

Installation
============

::

    pip install grains-from-collectors

Documentation
=============


https://python-grains_from_collectors.readthedocs.io/

Usage: main [OPTIONS] INPUT_FILE OUTPUT_FILE

The input file comes from running this command on the C5/Z4 salt master:


::

    salt '*' grains.items --out=yaml --out-file=minion-grains.yml




Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
