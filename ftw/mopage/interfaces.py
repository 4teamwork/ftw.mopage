# pylint: disable=E0211, E0213
# E0211: Method has no argument
# E0213: Method should have "self" as first argument
from zope.interface import Interface


class IMopageXMLDataValidator(Interface):
    """Validates the data received from a MopageXMLDataProvider-Object
    """

    def validate(data):
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


class IMopageXMLWriter(Interface):

    def generate_xml(data):
        """ Start generating the xml and return it as string
        """


class IMopageGeolocationXMLWriter(IMopageXMLWriter):
    """Adapter generate xml for geolocation export
    """


class IMopageEventXMLWriter(IMopageXMLWriter):
    """Adapter generate xml for event export
    """


class IMopageNewsXMLWriter(IMopageXMLWriter):
    """Adapter generate xml for news export
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


class IMopageEventDataProvider(IMopageXMLDataProvider):
    """Adapter provides data to export with
    mopage_event.xml-view
    """


class IMopageNewsDataProvider(IMopageXMLDataProvider):
    """Adapter provides data to export with
    mopage_news.xml-view
    """
