from zope.interface.verify import verifyClass
from ftw.mopage.testing import FTWMOPAGE_ZCML_LAYER
from ftw.testing import MockTestCase
from ftw.mopage.interfaces import IMopageGeolocationQueryProvider
from ftw.mopage.adapter import MopageGeolocationQueryProvider
from zope.component import getMultiAdapter


class TestGeolocation(MockTestCase):

    layer = FTWMOPAGE_ZCML_LAYER

    def test_implements_interface(self):

        self.assertTrue(IMopageGeolocationQueryProvider.implementedBy(
            MopageGeolocationQueryProvider))

        verifyClass(IMopageGeolocationQueryProvider,
            MopageGeolocationQueryProvider)

    def test_component_registered(self):

        obj = getMultiAdapter(
            (object(), object()), IMopageGeolocationQueryProvider)
        self.assertEquals(obj.__class__, MopageGeolocationQueryProvider)

    def test_query(self):

        obj = getMultiAdapter(
            (object(), object()), IMopageGeolocationQueryProvider)

        result = obj.get_query()

        self.assertEquals(
            result,
            {'object_provides': 'ftw.mopage.interfaces.IMopageGeolocation'})
