scirate
------------

Python wrapper for extracting information from Scirate :microscope:

|Build Status| |Coverage Status| |Downloads| |Latest Version| 
|Supported Python versions| |License|

.. image:: https://i.imgur.com/QONau8z.png?1
   :width: 100
   :height: 100

This package provides a Python interface for the `Scirate website <https://scirate.com>`__.

Dependencies
------------

This package depends on the following packages:

- bs4
- lxml
- requests

They can be installed using ``pip``.

::

    sudo pip install -r requirements.txt

If you want to contribute to this package, you will need the ``nose`` package as well.

Installation
------------
The preferred way to install the ``scirate`` package is via ``pip``

::

    sudo pip install scirate


Alternatively to install, you may also run the following command from the top-level package
directory.

::

    sudo python setup.py install


Examples
--------

This package provides a Python interface for interfacing with the Scirate
website. Here are a few examples demonstrating how to access data on 
Scirate.

Clients
~~~~~~~
In order to interface with the content on Scirate, we start off my 
creating a client. This client will be responsible for requesting
information from Scirate and will serve as the intermediary for 
requesting and obtaining data.

.. code:: python

    from scirate.client import ScirateClient
    
    client = ScirateClient()


Papers
~~~~~~

Let us access a paper on Scirate via the arXiv identifier. Say we want to
access information via Scirate on the following `listing 1509.01147 <https://arxiv.org/abs/1509.01147>`__.

We can grab some of the basic information, such as the authors, title, abstract, arXiv category, 
etc.

.. code:: python

    >>> from scirate.paper import SciratePaper
    >>> paper = client.paper("1509.01147")
    >>> "The Information Paradox for Black Holes"
    >>> paper.authors
    >>> ['S. W. Hawking']
    >>> paper.abstract[0:50]
    >>> "I propose that the information loss paradox can be"
    >>> paper.category
    >>> "hep-th"

We can also grab some of the more Scirate-specific metrics. Such as the number of
scites for a given article, who scited the article, etc.

.. code:: python

    >>> paper.scites
    >>> 6
    >>> paper.scitors
    >>> ['Andrew Childs', 'Jonny', 'Mehdi Ahmadi', 'Noon van der Silk', 'Ryan L. Mann', 'Tom Wong']
   
Consult the documentation for further examples of information that can be obtained
from a paper.   
    
Authors
~~~~~~~

You can get information about an author as well.

.. code:: python

    >>> from scirate.author import ScirateAuthor
    >>> author = client.author("Terrance", "Tao", "math.CO")
    >>> author
    >>> "Terrance Tao"
    >>> author.papers[0]
    >>> "An inverse theorem for an inequality of Kneser"
    >>> author.arxiv_ids[0]
    >>> "1711.04337"

Using the arXiv identifier along with what we did in the Papers
section, we can obtain further information about that paper if 
we wish

.. code:: python

    >>> paper = client.paper(author.arxiv_ids[0])
    >>> paper.scites
    >>> 0
    
Note that the mathematician Terrance Tao published on multiple arXiv 
categories. We can look up his papers under the math.NT category as 
well.

.. code:: python

    >>> author = client.author("Terrance", "Tao", "math.NT")
    >>> author.papers[0]
    >>> "Long gaps in sieved sets"
    >>> author.category
    >>> math.NT
    
Categories
~~~~~~~~~~

One may also wish to look at papers under various arXiv identifier
listings on Scirate. For instance, one may wish to find all of the 
papers posted under the 'quant-ph' category posted on September 7, 2017.

.. code:: python

    >>> from scirate.category import ScirateCategory
    >>> category = client.category("quant-ph", "09-07-2017")
    >>> category.papers[0:2]
    >>> ['Quantum Advantage from Conjugated Clifford Circuits', 'Extended Nonlocal Games from Quantum-Classical Games']

Documentation
-------------

Read more about this package
`here <http://scirate.readthedocs.org/en/latest/>`__.


Contribution
------------

If you find an API method that is not supported by this package, feel
free to create a Github issue. Also, you are more than welcome to submit
a pull request for a bug fix or additional feature.


License
-------

`MIT License <http://opensource.org/licenses/mit-license.php>`__

.. |Build Status| image:: http://img.shields.io/travis/vprusso/scirate.svg
   :target: https://travis-ci.org/vprusso/scirate
.. |Coverage Status| image:: http://img.shields.io/coveralls/vprusso/scirate.svg
   :target: https://coveralls.io/r/vprusso/scirate
.. |Downloads| image:: https://img.shields.io/pypi/dm/goodreads.svg
   :target: https://pypi.python.org/pypi/goodreads/
.. |Latest Version| image:: https://img.shields.io/pypi/v/scirate.svg
   :target: https://pypi.python.org/pypi/scirate/
.. |Supported Python versions| image:: https://img.shields.io/pypi/pyversions/scirate.svg
   :target: https://pypi.python.org/pypi/scirate/
.. |License| image:: https://img.shields.io/pypi/l/scirate.svg
   :target: https://pypi.python.org/pypi/scirate/
