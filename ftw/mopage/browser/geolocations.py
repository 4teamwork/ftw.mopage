from ftw.mopage.browser.base import BaseExport
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from ftw.mopage.interfaces import \
    IMopageGeolocationDataProvider, IMopageGeolocationLookup


class ExportGeoLocations(BaseExport):

    filename = 'geolocations'
    template = ViewPageTemplateFile('geolocations.xml')
    data_provider = IMopageGeolocationDataProvider
    lookup_provider = IMopageGeolocationLookup
