from zope.interface import Interface


class IMopageXMLDataValidator(Interface):
    """Validates the data received from a MopageXMLDataProvider-Object
    """

    def validate():
        """Start validation
        """


class IMopageGeolocationDataValidator(IMopageXMLDataValidator):
    """Adapter validates data to export in mopage_geolocations.xml
    """


class IMopageEventDataValidator(IMopageXMLDataValidator):
    """Adapter validates data to export in mopage_events.xml
    """


class IMopageNewsDataValidator(IMopageXMLDataValidator):
    """Adapter validates data to export in mopage_news.xml
    """


class IMopageExporter(Interface):
    """Markerinterface for Exportable objects with ftw.mopage
    """


class IMopageEvent(IMopageExporter):
    """Markerinterface for MopageEvents
    """


class IMopageGeolocation(IMopageExporter):
    """Markerinterface for MopageGelocation
    """


class IMopageNews(IMopageExporter):
    """Markerinterface for MopageNews
    """


class IMopageBaseLookup(Interface):
    """Adapter providing the query for mopage exports
    """

    def get_brains():
        """Return the catalogquery
        """


class IMopageEventLookup(IMopageBaseLookup):
    """Adapter providing the query to export mopage events
    """


class IMopageNewsLookup(IMopageBaseLookup):
    """Adapter providing the query to export mopage news
    """


class IMopageGeolocationLookup(IMopageBaseLookup):
    """Adapter providing the query to export mopage geolocations
    """


class IMopageXMLDataProvider(Interface):
    """Adapter provides data to export in xml
    """

    def get_data():
        """ Return required data in a dict
        """


class IMopageGeolocationDataProvider(IMopageXMLDataProvider):
    """Adapter provides geolocationdata to export with
    mopage_geolocation.xml-view
    """

    def get_data():
        """
        Needs to provide following keys in the dict:

        - id
        - title
        - street
        - modified
        - plz
        - place
        - country
        - categories
        - phone
        - email
        - opening
        - text_short
        - company
        - firstname
        - lastname
        - mobile
        - fax
        - description
        - image_url
        - rubriken
        - anfahrt
        - url
        - longitude
        - latitude
        """


class IMopageEventDataProvider(IMopageXMLDataProvider):
    """Adapter provides data to export with
    mopage_event.xml-view
    """

    def get_data():
        """
        Needs to provide following keys in the dict:

        - id
        - title
        - modified
        - allday
        - start
        - end
        - reference (reference to geolocation data id)
        - text
        - categories
        - description
        - image_url
        - url

        """


class IMopageNewsDataProvider(IMopageXMLDataProvider):
    """Adapter provides data to export with
    mopage_news.xml-view
    """

    def get_data():
        """
        Needs to provide following keys in the dict:

        - id
        - title
        - description
        - text_short
        - text
        - image_url
        - categories
        - url
        - modified
        - datumvon
        - datumbis
        """
