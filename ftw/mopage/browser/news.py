from ftw.mopage import interfaces as i
from ftw.mopage.browser.base import BaseExport


class ExportNews(BaseExport):

    filename = 'news'
    data_provider = i.IMopageNewsDataProvider
    data_validator = i.IMopageNewsDataValidator
    lookup_provider = i.IMopageNewsObjectLookup
    xml_generator = i.IMopageNewsXMLGenerator
