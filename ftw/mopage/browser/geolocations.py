from ftw.mopage.browser.news import ExportNews
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from ftw.mopage.interfaces import \
    IMopageGeolocationDataProvider, IMopageGeolocationQueryProvider


class ExportGeoLocations(ExportNews):

    filename = 'geolocations'
    template = ViewPageTemplateFile('geolocations.xml')
    data_provider = IMopageGeolocationDataProvider
    query_provider = IMopageGeolocationQueryProvider
