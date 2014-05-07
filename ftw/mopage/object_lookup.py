from ftw.mopage import interfaces
from Products.CMFCore.utils import getToolByName
from zope.interface import implements


class MopageBaseObjectLookup(object):
    implements(interfaces.IMopageObjectLookup)

    interface = 'ftw.mopage.interfaces.IMopageExporter'

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def _get_brains(self):
        catalog = getToolByName(self.context, 'portal_catalog')

        return catalog({'object_provides': self.interface})

    def get_objects(self):
        return [each.getObject() for each in self._get_brains()]


class MopageEventObjectLookup(MopageBaseObjectLookup):
    implements(interfaces.IMopageEventObjectLookup)

    interface = 'ftw.mopage.interfaces.IMopageEvent'


class MopageNewsObjectLookup(MopageBaseObjectLookup):
    implements(interfaces.IMopageNewsObjectLookup)

    interface = 'ftw.mopage.interfaces.IMopageNews'


class MopageGeolocationObjectLookup(MopageBaseObjectLookup):
    implements(interfaces.IMopageGeolocationObjectLookup)

    interface = 'ftw.mopage.interfaces.IMopageGeolocation'
