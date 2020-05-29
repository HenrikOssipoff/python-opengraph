.. image:: https://travis-ci.org/HenrikOssipoff/python-opengraph.svg?branch=master
    :target: https://travis-ci.org/HenrikOssipoff/python-opengraph
.. image:: https://coveralls.io/repos/HenrikOssipoff/python-opengraph/badge.svg?branch=master
  :target: https://coveralls.io/r/HenrikOssipoff/python-opengraph?branch=master

❗ This repository is no longer maintained in any way. PRs will not be responded to ❗

Python module to parse Open Graph metadata on web pages. For more information on the Open Graph Protocol, see http://ogp.me/.

Compatability
=============
- Python 2.7
- Python 3.3, 3.4
- PyPy

Other versions may work, but testing is only done against the above versions.

Dependencies
============
- Beautiful Soup 4
- Requests

Installation
============
.. code:: python

    pip install python-opengraph

Example loading from URL
========================
.. code:: python

    from opengraph import OpenGraph

    og = OpenGraph(url='http://someurl.com')
    og.title  # would yield the 'title' open graph element
