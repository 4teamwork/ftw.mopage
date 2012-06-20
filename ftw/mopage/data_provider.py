from ftw.mopage.interfaces import IMopageGeolocationDataProvider, \
    IMopageNewsDataProvider, IMopageEventDataProvider
from zope.interface import implements


class BaseMopageDataProvider(object):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def get_data(self):
        """ Return data
        """
        return {}


class MopageEventDataProvider(BaseMopageDataProvider):
    implements(IMopageEventDataProvider)


class MopageNewsDataProvider(BaseMopageDataProvider):
    implements(IMopageNewsDataProvider)


class MopageGeolocationDataProvider(BaseMopageDataProvider):
    implements(IMopageGeolocationDataProvider)
