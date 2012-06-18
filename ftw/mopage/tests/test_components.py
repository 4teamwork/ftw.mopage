from zope.interface.verify import verifyClass
from ftw.mopage.testing import FTWMOPAGE_ZCML_LAYER
from ftw.testing import MockTestCase
from ftw.mopage import interfaces as i
from ftw.mopage import data_provider
from ftw.mopage import data_lookup
from ftw.mopage import data_validator
from ftw.mopage import xml_writer
from zope.component import getMultiAdapter


class TestGeolocationComponents(MockTestCase):

    layer = FTWMOPAGE_ZCML_LAYER

    def test_data_lookup_implements(self):

        self.replay()

        self.assertTrue(i.IMopageGeolocationLookup.implementedBy(
           data_lookup.MopageGeolocationLookup))

        verifyClass(
            i.IMopageGeolocationLookup, data_lookup.MopageGeolocationLookup)

    def test_data_lookup_registered(self):

        self.replay()

        obj = getMultiAdapter((object(), object()), i.IMopageGeolocationLookup)
        self.assertEquals(obj.__class__, data_lookup.MopageGeolocationLookup)

    def test_data_provider_implements(self):
        self.replay()

        self.assertTrue(i.IMopageGeolocationDataProvider.implementedBy(
            data_provider.MopageGeolocationDataProvider))

        verifyClass(
            i.IMopageGeolocationLookup, data_lookup.MopageGeolocationLookup)

    def test_data_validator_implements(self):

        self.replay()

        self.assertTrue(i.IMopageGeolocationDataValidator.implementedBy(
           data_validator.MopageGeolocationDataValidator))

        verifyClass(
            i.IMopageGeolocationDataValidator,
            data_validator.MopageGeolocationDataValidator)

    def test_data_validator_registered(self):

        provider = self.providing_stub(i.IMopageGeolocationDataProvider)

        self.replay()

        obj = getMultiAdapter(
            (object(), object(), provider), i.IMopageGeolocationDataValidator)
        self.assertEquals(
            obj.__class__, data_validator.MopageGeolocationDataValidator)

    def test_xml_writer_implements(self):
        self.replay()

        self.assertTrue(i.IMopageGeolocationXMLWriter.implementedBy(
           xml_writer.MopageGeolocationXMLWriter))

        verifyClass(
            i.IMopageGeolocationXMLWriter,
            xml_writer.MopageGeolocationXMLWriter,
        )

    def test_xml_writer_registered(self):

        self.replay()

        obj = getMultiAdapter(
            (object(), object()), i.IMopageGeolocationXMLWriter)
        self.assertEquals(obj.__class__, xml_writer.MopageGeolocationXMLWriter)


class TestNewsComponents(MockTestCase):

    layer = FTWMOPAGE_ZCML_LAYER

    def test_data_lookup_implements(self):

        self.replay()

        self.assertTrue(i.IMopageNewsLookup.implementedBy(
           data_lookup.MopageNewsLookup))

        verifyClass(i.IMopageNewsLookup, data_lookup.MopageNewsLookup)

    def test_data_lookup_registered(self):

        self.replay()

        obj = getMultiAdapter((object(), object()), i.IMopageNewsLookup)
        self.assertEquals(obj.__class__, data_lookup.MopageNewsLookup)

    def test_data_provider_implements(self):
        self.replay()

        self.assertTrue(i.IMopageNewsDataProvider.implementedBy(
            data_provider.MopageNewsDataProvider))

        verifyClass(i.IMopageNewsLookup, data_lookup.MopageNewsLookup)

    def test_data_validator_implements(self):

        self.replay()

        self.assertTrue(i.IMopageNewsDataValidator.implementedBy(
           data_validator.MopageNewsDataValidator))

        verifyClass(
            i.IMopageNewsDataValidator,
            data_validator.MopageNewsDataValidator)

    def test_data_validator_registered(self):

        provider = self.providing_stub(i.IMopageNewsDataProvider)

        self.replay()

        obj = getMultiAdapter(
            (object(), object(), provider), i.IMopageNewsDataValidator)
        self.assertEquals(
            obj.__class__, data_validator.MopageNewsDataValidator)

    def test_xml_writer_implements(self):
        self.replay()

        self.assertTrue(i.IMopageNewsXMLWriter.implementedBy(
           xml_writer.MopageNewsXMLWriter))

        verifyClass(i.IMopageNewsXMLWriter, xml_writer.MopageNewsXMLWriter)

    def test_xml_writer_registered(self):

        self.replay()

        obj = getMultiAdapter((object(), object()), i.IMopageNewsXMLWriter)
        self.assertEquals(obj.__class__, xml_writer.MopageNewsXMLWriter)


class TestEventComponents(MockTestCase):

    layer = FTWMOPAGE_ZCML_LAYER

    def test_data_lookup_implements(self):

        self.replay()

        self.assertTrue(i.IMopageEventLookup.implementedBy(
           data_lookup.MopageEventLookup))

        verifyClass(i.IMopageEventLookup, data_lookup.MopageEventLookup)

    def test_data_lookup_registered(self):

        self.replay()

        obj = getMultiAdapter((object(), object()), i.IMopageEventLookup)
        self.assertEquals(obj.__class__, data_lookup.MopageEventLookup)

    def test_data_provider_implements(self):
        self.replay()

        self.assertTrue(i.IMopageEventDataProvider.implementedBy(
            data_provider.MopageEventDataProvider))

        verifyClass(i.IMopageEventLookup, data_lookup.MopageEventLookup)

    def test_data_validator_implements(self):

        self.replay()

        self.assertTrue(i.IMopageEventDataValidator.implementedBy(
           data_validator.MopageEventDataValidator))

        verifyClass(
            i.IMopageEventDataValidator,
            data_validator.MopageEventDataValidator)

    def test_data_validator_registered(self):

        provider = self.providing_stub(i.IMopageEventDataProvider)

        self.replay()

        obj = getMultiAdapter(
            (object(), object(), provider), i.IMopageEventDataValidator)
        self.assertEquals(
            obj.__class__, data_validator.MopageEventDataValidator)

    def test_xml_writer_implements(self):
        self.replay()

        self.assertTrue(i.IMopageEventXMLWriter.implementedBy(
           xml_writer.MopageEventXMLWriter))

        verifyClass(i.IMopageEventXMLWriter, xml_writer.MopageEventXMLWriter)

    def test_xml_writer_registered(self):

        self.replay()

        obj = getMultiAdapter((object(), object()), i.IMopageEventXMLWriter)
        self.assertEquals(obj.__class__, xml_writer.MopageEventXMLWriter)
