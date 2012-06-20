from ftw.mopage import interfaces
from zope.interface import implements


class BaseMopageDataProvider(object):
    implements(interfaces.IMopageDataProvider)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def get_data(self):
        """ Return data
        """
        return {}


class MopageEventDataProvider(BaseMopageDataProvider):
    implements(interfaces.IMopageEventDataProvider)


class MopageNewsDataProvider(BaseMopageDataProvider):
    implements(interfaces.IMopageNewsDataProvider)


class MopageGeolocationDataProvider(BaseMopageDataProvider):
    implements(interfaces.IMopageGeolocationDataProvider)
