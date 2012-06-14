from ftw.mopage.interfaces import IMopageEventLookup, IMopageNewsLookup, \
    IMopageGeolocationLookup
from zope.interface import implements
from Products.CMFCore.utils import getToolByName


class MopageBaseLookup(object):

    interface = 'ftw.mopage.interfaces.IMopageExporter'

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def get_brains(self):
        """Return the brains for the export
        """
        catalog = getToolByName(self.context, 'portal_catalog')

        return catalog({'object_provides': self.interface})


class MopageEventLookup(MopageBaseLookup):
    implements(IMopageEventLookup)

    interface = 'ftw.mopage.interfaces.IMopageEvent'


class MopageNewsLookup(MopageBaseLookup):
    implements(IMopageNewsLookup)

    interface = 'ftw.mopage.interfaces.IMopageNews'


class MopageGeolocationLookup(MopageBaseLookup):
    implements(IMopageGeolocationLookup)

    interface = 'ftw.mopage.interfaces.IMopageGeolocation'
