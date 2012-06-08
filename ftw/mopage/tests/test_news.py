from zope.interface.verify import verifyClass
from ftw.mopage.testing import FTWMOPAGE_ZCML_LAYER
from ftw.testing import MockTestCase
from ftw.mopage.interfaces import IMopageNewsQueryProvider
from ftw.mopage.adapter import MopageNewsQueryProvider
from zope.component import getMultiAdapter


class TestNews(MockTestCase):

    layer = FTWMOPAGE_ZCML_LAYER

    def test_implements_interface(self):

        self.assertTrue(
            IMopageNewsQueryProvider.implementedBy(MopageNewsQueryProvider))

        verifyClass(IMopageNewsQueryProvider, MopageNewsQueryProvider)

    def test_component_registered(self):

        obj = getMultiAdapter((object(), object()), IMopageNewsQueryProvider)
        self.assertEquals(obj.__class__, MopageNewsQueryProvider)

    def test_query(self):

        obj = getMultiAdapter((object(), object()), IMopageNewsQueryProvider)

        result = obj.get_query()

        self.assertEquals(
            result, {'object_provides': 'ftw.mopage.interfaces.IMopageNews'})
