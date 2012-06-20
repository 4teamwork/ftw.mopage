from zope.interface.verify import verifyClass
from ftw.mopage.testing import FTWMOPAGE_ZCML_LAYER
from ftw.testing import MockTestCase
from ftw.mopage import interfaces as i
from ftw.mopage import data_provider
from ftw.mopage import object_lookup
from ftw.mopage import data_validator
from ftw.mopage import xml_generator
from zope.component import getMultiAdapter


class TestGeolocationComponents(MockTestCase):

    layer = FTWMOPAGE_ZCML_LAYER

    def test_object_lookup_implements(self):

        self.replay()

        self.assertTrue(i.IMopageGeolocationObjectLookup.implementedBy(
           object_lookup.MopageGeolocationObjectLookup))

        verifyClass(
            i.IMopageGeolocationObjectLookup, object_lookup.MopageGeolocationObjectLookup)

    def test_object_lookup_registered(self):

        self.replay()

        obj = getMultiAdapter((object(), object()), i.IMopageGeolocationObjectLookup)
        self.assertEquals(obj.__class__, object_lookup.MopageGeolocationObjectLookup)

    def test_data_provider_implements(self):
        self.replay()

        self.assertTrue(i.IMopageGeolocationDataProvider.implementedBy(
            data_provider.MopageGeolocationDataProvider))

        verifyClass(
            i.IMopageGeolocationObjectLookup, object_lookup.MopageGeolocationObjectLookup)

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

    def test_xml_generator_implements(self):
        self.replay()

        self.assertTrue(i.IMopageGeolocationXMLGenerator.implementedBy(
           xml_generator.MopageGeolocationXMLGenerator))

        verifyClass(
            i.IMopageGeolocationXMLGenerator,
            xml_generator.MopageGeolocationXMLGenerator,
        )

    def test_xml_generator_registered(self):

        self.replay()

        obj = getMultiAdapter(
            (object(), object()), i.IMopageGeolocationXMLGenerator)
        self.assertEquals(obj.__class__, xml_generator.MopageGeolocationXMLGenerator)


class TestNewsComponents(MockTestCase):

    layer = FTWMOPAGE_ZCML_LAYER

    def test_object_lookup_implements(self):

        self.replay()

        self.assertTrue(i.IMopageNewsObjectLookup.implementedBy(
           object_lookup.MopageNewsObjectLookup))

        verifyClass(i.IMopageNewsObjectLookup, object_lookup.MopageNewsObjectLookup)

    def test_object_lookup_registered(self):

        self.replay()

        obj = getMultiAdapter((object(), object()), i.IMopageNewsObjectLookup)
        self.assertEquals(obj.__class__, object_lookup.MopageNewsObjectLookup)

    def test_data_provider_implements(self):
        self.replay()

        self.assertTrue(i.IMopageNewsDataProvider.implementedBy(
            data_provider.MopageNewsDataProvider))

        verifyClass(i.IMopageNewsObjectLookup, object_lookup.MopageNewsObjectLookup)

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

    def test_xml_generator_implements(self):
        self.replay()

        self.assertTrue(i.IMopageNewsXMLGenerator.implementedBy(
           xml_generator.MopageNewsXMLGenerator))

        verifyClass(i.IMopageNewsXMLGenerator, xml_generator.MopageNewsXMLGenerator)

    def test_xml_generator_registered(self):

        self.replay()

        obj = getMultiAdapter((object(), object()), i.IMopageNewsXMLGenerator)
        self.assertEquals(obj.__class__, xml_generator.MopageNewsXMLGenerator)


class TestEventComponents(MockTestCase):

    layer = FTWMOPAGE_ZCML_LAYER

    def test_object_lookup_implements(self):

        self.replay()

        self.assertTrue(i.IMopageEventObjectLookup.implementedBy(
           object_lookup.MopageEventObjectLookup))

        verifyClass(i.IMopageEventObjectLookup, object_lookup.MopageEventObjectLookup)

    def test_object_lookup_registered(self):

        self.replay()

        obj = getMultiAdapter((object(), object()), i.IMopageEventObjectLookup)
        self.assertEquals(obj.__class__, object_lookup.MopageEventObjectLookup)

    def test_data_provider_implements(self):
        self.replay()

        self.assertTrue(i.IMopageEventDataProvider.implementedBy(
            data_provider.MopageEventDataProvider))

        verifyClass(i.IMopageEventObjectLookup, object_lookup.MopageEventObjectLookup)

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

    def test_xml_generator_implements(self):
        self.replay()

        self.assertTrue(i.IMopageEventXMLGenerator.implementedBy(
           xml_generator.MopageEventXMLGenerator))

        verifyClass(i.IMopageEventXMLGenerator, xml_generator.MopageEventXMLGenerator)

    def test_xml_generator_registered(self):

        self.replay()

        obj = getMultiAdapter((object(), object()), i.IMopageEventXMLGenerator)
        self.assertEquals(obj.__class__, xml_generator.MopageEventXMLGenerator)
