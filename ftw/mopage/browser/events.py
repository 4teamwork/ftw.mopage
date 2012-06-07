from ftw.mopage.browser.news import ExportNews
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from ftw.mopage.interfaces import \
    IMopageEventDataProvider, IMopageEventQueryProvider


class ExportEvents(ExportNews):

    filename = 'events'
    template = ViewPageTemplateFile('events.xml')
    data_provider = IMopageEventDataProvider
    query_provider = IMopageEventQueryProvider
