from ftw.mopage.browser.base import BaseExport
from ftw.mopage import interfaces as i


class ExportEvents(BaseExport):

    filename = 'events'
    data_provider = i.IMopageEventDataProvider
    data_validator = i.IMopageEventDataValidator
    lookup_provider = i.IMopageEventLookup
    xml_writer = i.IMopageEventXMLWriter
