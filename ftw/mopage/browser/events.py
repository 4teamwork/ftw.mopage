from ftw.mopage.browser.base import BaseExport
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from ftw.mopage.interfaces import \
    IMopageEventDataProvider, IMopageEventQueryProvider


class ExportEvents(BaseExport):

    filename = 'events'
    template = ViewPageTemplateFile('events.xml')
    data_provider = IMopageEventDataProvider
    query_provider = IMopageEventQueryProvider
