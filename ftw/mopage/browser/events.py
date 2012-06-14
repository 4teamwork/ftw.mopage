from ftw.mopage.browser.base import BaseExport
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from ftw.mopage.interfaces import \
    IMopageEventDataProvider, IMopageEventDataValidator, IMopageEventLookup


class ExportEvents(BaseExport):

    filename = 'events'
    template = ViewPageTemplateFile('events.xml')
    data_provider = IMopageEventDataProvider
    data_validator = IMopageEventDataValidator
    lookup_provider = IMopageEventLookup
