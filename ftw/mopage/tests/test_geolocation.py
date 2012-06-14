from zope.interface.verify import verifyClass
from ftw.mopage.testing import FTWMOPAGE_ZCML_LAYER
from ftw.testing import MockTestCase
from ftw.mopage.interfaces import IMopageGeolocationLookup
from ftw.mopage.adapter import MopageGeolocationLookup
from zope.component import getMultiAdapter
from mocker import ANY


class TestGeolocation(MockTestCase):

    layer = FTWMOPAGE_ZCML_LAYER

    def test_implements_interface(self):

        self.assertTrue(IMopageGeolocationLookup.implementedBy(
            MopageGeolocationLookup))

        verifyClass(IMopageGeolocationLookup,
            MopageGeolocationLookup)

    def test_component_registered(self):

        obj = getMultiAdapter(
            (object(), object()), IMopageGeolocationLookup)
        self.assertEquals(obj.__class__, MopageGeolocationLookup)

    def test_query(self):

        brains = ['brain1', 'brain2']

        ctool = self.mocker.mock()
        self.mock_tool(ctool, 'portal_catalog')

        self.expect(ctool(ANY)).result(brains)

        self.replay()

        obj = getMultiAdapter((object(), object()), IMopageGeolocationLookup)

        result = obj.get_brains()

        self.assertEquals(
            result, ['brain1', 'brain2'])
