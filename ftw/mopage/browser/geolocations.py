from ftw.mopage.browser.base import BaseExport
from ftw.mopage import interfaces


class ExportGeoLocations(BaseExport):

    filename = 'geolocations'
    data_provider = interfaces.IMopageGeolocationDataProvider
    data_validator = interfaces.IMopageGeolocationDataValidator
    lookup_provider = interfaces.IMopageGeolocationObjectLookup
    xml_generator = interfaces.IMopageGeolocationXMLGenerator
