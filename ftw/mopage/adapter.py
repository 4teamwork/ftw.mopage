from ftw.mopage.interfaces import IMopageEventQueryProvider, IMopageNewsQueryProvider, IMopageGeolocationQueryProvider
from zope.interface import implements


class BaseMopageQueryProvider(object):

    interface = 'ftw.mopage.interfaces.IMopageExporter'

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def get_query(self):
        """Return the query for the export
        """
        return {'object_provides': self.interface}


class MopageEventQueryProvider(BaseMopageQueryProvider):
    implements(IMopageEventQueryProvider)

    interface = 'ftw.mopage.interfaces.IMopageEvent'


class MopageNewsQueryProvider(BaseMopageQueryProvider):
    implements(IMopageNewsQueryProvider)

    interface = 'ftw.mopage.interfaces.IMopageNews'


class MopageGeolocationQueryProvider(BaseMopageQueryProvider):
    implements(IMopageGeolocationQueryProvider)

    interface = 'ftw.mopage.interfaces.IMopageGeolocation'
