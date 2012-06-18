from ftw.mopage.browser.base import BaseExport
from ftw.mopage.interfaces import \
    IMopageEventDataProvider, IMopageEventDataValidator, IMopageEventLookup


class ExportEvents(BaseExport):

    filename = 'events'
    data_provider = IMopageEventDataProvider
    data_validator = IMopageEventDataValidator
    lookup_provider = IMopageEventLookup
