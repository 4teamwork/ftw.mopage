from ftw.mopage import interfaces
from ftw.mopage.browser.base import BaseExport


class ExportEvents(BaseExport):

    filename = 'events'
    data_provider = interfaces.IMopageEventDataProvider
    data_validator = interfaces.IMopageEventDataValidator
    lookup_provider = interfaces.IMopageEventObjectLookup
    xml_generator = interfaces.IMopageEventXMLGenerator
