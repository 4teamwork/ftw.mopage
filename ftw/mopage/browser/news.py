from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from ftw.mopage.interfaces import \
    IMopageNewsDataProvider, IMopageNewsDataValidator, IMopageNewsLookup
from ftw.mopage.browser.base import BaseExport


class ExportNews(BaseExport):

    filename = 'news'
    template = ViewPageTemplateFile('news.xml')
    data_provider = IMopageNewsDataProvider
    data_validator = IMopageNewsDataValidator
    lookup_provider = IMopageNewsLookup
