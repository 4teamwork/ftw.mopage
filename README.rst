Introduction
============

``ftw.mopage`` provides a plone xml interface for the moPage CMS of
anthrazit.

The package registers tree views:

- mopage_news.xml
- mopage_events.xml
- mopage_geolocations.xml

If you call a view, a new xml will be generated on the filesystem and
will be downloaded.


Requirements
============

The package is compatible with `Plone`_ 4.x.


Installing
==========

Add ``ftw.mopage`` to your buildout configuration:

::

  [instance]
  eggs =
    ftw.mopage


Marker Interfaces
=================

- IMopageExporter

 - IMopageEvent

 - IMopageGeolocation

 - IMopageNews


Adapters Interfaces
===================

- IMopageObjectLookup (context, request)

 - IMopageEventObjectLookup

 - IMopageNewsObjectLookup

 - IMopageGeolocationObjectLookup


- IMopageDataProvider (context, request)

 - IMopageGeolocationDataProvider

 - IMopageEventDataProvider

 - IMopageNewsDataProvider

- IMopageDataValidator (context, request, dataprovider)

 - IMopageGeolocationDataValidator

 - IMopageEventDataValidator

 - IMopageNewsDataValidator

- IMopageXMLGenerator (context, request)

 - IMopageGeolocationXMLGenerator

 - IMopageEventXMLGenerator

 - IMopageNewsXMLGenerator


Implementation
==============

If you call export view, the following steps will be execute in the given
order:


Get Objects
-----------

1. Get MopageObjectLookup multiadapter
2. Call get_brains method of MopageObjectLookup

Get Data
--------

3. Get MopageDataProvider multiadapter with every object
4. Call get_data method of MopageDataProviders

Validate Data
-------------

5. Get MopageDataValidator multiadapter of every objects dataprovider
6. Call validate method of MopageDataValidator

Abort or Continue
-----------------

7. If the MopageDataValidator raises an error, we abort the export
8. If the MopageDataValidator validation is valid, we continue exporting data

Create the xml string
---------------------

9. Get MopageXMLGenerator multiadapter
10. Call generate_xml_string method of MopageXMLGenerator

Return the string
-----------------

11. Return the xml string as xml download file


Usage
=====

You need to mark your content types as MopageExporters.

To get the data of a MopageExporter, you need to override the specific
MopageDataProvider to implement the dataexport.


Mark new content type as a specific MopageExporter
--------------------------------------------------

::


    >>> from zope.interface import implements
    >>> from Products.ATContentTypes.content.file import ATFile
    >>> from ftw.mopage.interfaces import IMopageNews


    >>> class File(ATFile):
    ...     implements(IFile, IMopageNews)


Mark existing content type as a specific MopageExporter
-------------------------------------------------------

configure.zcml:

::


    <configure
        xmlns="http://namespaces.zope.org/zope"
        xmlns:five="http://namespaces.zope.org/five">

        <five:implements
            class="Products.ATContentTypes.content.file.ATFile"
            interface="ftw.mopage.interfaces.IMopageNews"
        />

    </configure>


Override specific MopageDataProvider
------------------------------------

configure.zcml:

::


    <configure
        xmlns="http://namespaces.zope.org/zope">

         <adapter
           for="ftw.mopage.interfaces.IMopageNews
                example.customization.browser.interfaces.IExampleCustomizatio"
           factory=".data_provider.NewsDataProvider"
           provides="ftw.mopage.interfaces.IMopageNewsDataProvider"
          />

    </configure>


data_provider.py:

::


    >>> from ftw.mopage.data_provider import MopageNewsDataProvider


    >>> class NewsDataProvider(MopageNewsDataProvider):

    ...     def get_data(self):
    ...
    ...         data = {
    ...             'id': 'äxx',
    ...             'titel': 'abc123',
    ...             'textmobile': 'abc123',
    ...             'datumvon': 'abc123',
    ...             'mutationsdatum': 'abc123',
    ...         }
    ...
    ...         return data


Additional information
======================

In the docs-directory you find the official moPage interface documentation
on Anthrazit-side.


Links
-----

- Github: https://github.com/4teamwork/ftw.mopage
- Issues: https://github.com/4teamwork/ftw.mopage/issues
- Pypi: http://pypi.python.org/pypi/ftw.mopage
- Continuous integration: https://jenkins.4teamwork.ch/search?q=ftw.mopage


Copyright
=========

This package is copyright by `4teamwork <http://www.4teamwork.ch/>`_.

``ftw.mopage`` is licensed under GNU General Public License, version 2.

.. _Plone: http://www.plone.org/
