from ftw.mopage.browser.base import BaseExport
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from ftw.mopage.interfaces import IMopageGeolocationDataProvider, \
    IMopageGeolocationDataValidator,IMopageGeolocationLookup


class ExportGeoLocations(BaseExport):

    filename = 'geolocations'
    template = ViewPageTemplateFile('geolocations.xml')
    data_provider = IMopageGeolocationDataProvider
    data_validator = IMopageGeolocationDataValidator
    lookup_provider = IMopageGeolocationLookup
