from ftw.mopage.browser.base import BaseExport
from ftw.mopage import interfaces as i


class ExportGeoLocations(BaseExport):

    filename = 'geolocations'
    data_provider = i.IMopageGeolocationDataProvider
    data_validator = i.IMopageGeolocationDataValidator
    lookup_provider = i.IMopageGeolocationObjectLookup
    xml_generator = i.IMopageGeolocationXMLGenerator
