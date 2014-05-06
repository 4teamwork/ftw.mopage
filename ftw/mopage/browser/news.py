from ftw.mopage import interfaces
from ftw.mopage.browser.base import BaseExport


class ExportNews(BaseExport):

    filename = 'news'
    data_provider = interfaces.IMopageNewsDataProvider
    data_validator = interfaces.IMopageNewsDataValidator
    lookup_provider = interfaces.IMopageNewsObjectLookup
    xml_generator = interfaces.IMopageNewsXMLGenerator
