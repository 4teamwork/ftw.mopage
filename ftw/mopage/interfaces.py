# pylint: disable=E0211, E0213
# E0211: Method has no argument
# E0213: Method should have "self" as first argument
from zope.interface import Interface


class IMopageExporter(Interface):
    """
    Markerinterface for Exportable objects with ftw.mopage
    """


class IMopageEvent(IMopageExporter):
    """
    Specific Markerinterface for MopageEvents
    """


class IMopageGeolocation(IMopageExporter):
    """
    Specific Markerinterface for MopageGeolocations
    """


class IMopageNews(IMopageExporter):
    """
    Specific Markerinterface for News
    """


class IMopageDataValidator(Interface):
    """
    Adapter to validate the received data of the data provider.

    To be sure the data received over a data provider is valid,
    we use this validator.

    The Validator raises a MopageValidationError when the data is not valid.
    """

    def validate(data):
        """
        Start the validation of data.
        """

    def get_attributes():
        """
        Return a list with all attributes to validate
        """

    def get_validation_queue():
        """
        Return a list with callable methods containing validation
        functions.
        """


class IMopageGeolocationDataValidator(IMopageDataValidator):
    """
    Specific validation adapter used for geolocations.
    """


class IMopageEventDataValidator(IMopageDataValidator):
    """
    Specific validation adapter used for events.
    """


class IMopageNewsDataValidator(IMopageDataValidator):
    """
    Specific validation adapter used for news.
    """


class IMopageXMLGenerator(Interface):
    """
    Adapter to generate xmls with minidom.
    """

    def generate_xml_string(data):
        """
        Return a string of a xmlfile generated with 'data'
        """


class IMopageGeolocationXMLGenerator(IMopageXMLGenerator):
    """
    Specific adapter used to generate a xml for geolocations.
    """


class IMopageEventXMLGenerator(IMopageXMLGenerator):
    """
    Specific adapter used to generate a xml for events.
    """


class IMopageNewsXMLGenerator(IMopageXMLGenerator):
    """
    Specific adapter used to generate a xml for news.
    """


class IMopageObjectLookup(Interface):
    """
    Adapter to lookup objects providing data for the xml export
    """

    def get_brains():
        """
        Return brains providing data for the xml export
        """


class IMopageEventObjectLookup(IMopageObjectLookup):
    """
    Specific adapter to lookup objects providing event data for xml export
    """


class IMopageNewsObjectLookup(IMopageObjectLookup):
    """
    Specific adapter to lookup objects providing news data for xml export
    """


class IMopageGeolocationObjectLookup(IMopageObjectLookup):
    """
    Specific adapter to lookup objects providing geolocation
    data for xml export
    """


class IMopageDataProvider(Interface):
    """
    Adapter provides data to export in xml
    """

    def get_data():
        """
        Return required data in a dict
        """


class IMopageGeolocationDataProvider(IMopageDataProvider):
    """
    Specific adapter provides geolocation data to export in xml
    """


class IMopageEventDataProvider(IMopageDataProvider):
    """
    Specific adapter provides event data to export in xml
    """


class IMopageNewsDataProvider(IMopageDataProvider):
    """
    Specific adapter provides news data to export in xml
    """
