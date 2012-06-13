from zope.interface.verify import verifyClass
from ftw.mopage.testing import FTWMOPAGE_ZCML_LAYER
from ftw.testing import MockTestCase
from ftw.mopage.interfaces import IMopageEventQueryProvider
from ftw.mopage.query_provider MopageEventQueryProvider
from zope.component import getMultiAdapter


class TestEvents(MockTestCase):

    layer = FTWMOPAGE_ZCML_LAYER

    def test_implements_interface(self):

        self.replay()

        self.assertTrue(IMopageEventQueryProvider.implementedBy(
            MopageEventQueryProvider))

        verifyClass(IMopageEventQueryProvider, MopageEventQueryProvider)

    def test_component_registered(self):

        self.replay()

        obj = getMultiAdapter((object(), object()), IMopageEventQueryProvider)
        self.assertEquals(obj.__class__, MopageEventQueryProvider)

    def test_query(self):

        self.replay()

        obj = getMultiAdapter((object(), object()), IMopageEventQueryProvider)

        result = obj.get_query()
        self.assertEquals(
            result, {'object_provides': 'ftw.mopage.interfaces.IMopageEvent'})
