from zope.interface.verify import verifyClass
from ftw.mopage.testing import FTWMOPAGE_ZCML_LAYER
from ftw.testing import MockTestCase
from ftw.mopage.interfaces import IMopageEventLookup
from ftw.mopage.adapter import MopageEventLookup
from zope.component import getMultiAdapter
from mocker import ANY


class TestEvents(MockTestCase):

    layer = FTWMOPAGE_ZCML_LAYER

    def test_implements_interface(self):

        self.replay()

        self.assertTrue(IMopageEventLookup.implementedBy(
            MopageEventLookup))

        verifyClass(IMopageEventLookup, MopageEventLookup)

    def test_component_registered(self):

        self.replay()

        obj = getMultiAdapter((object(), object()), IMopageEventLookup)
        self.assertEquals(obj.__class__, MopageEventLookup)

    def test_query(self):

        brains = ['brain1', 'brain2']

        ctool = self.mocker.mock()
        self.mock_tool(ctool, 'portal_catalog')

        self.expect(ctool(ANY)).result(brains)

        self.replay()

        obj = getMultiAdapter((object(), object()), IMopageEventLookup)

        result = obj.get_brains()

        self.assertEquals(
            result, ['brain1', 'brain2'])
