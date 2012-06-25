# coding=UTF-8
from ftw.testing import MockTestCase
from ftw.mopage import xml_generator
from lxml import etree
from StringIO import StringIO
from ftw.mopage.testing import FTWMOPAGE_ZCML_LAYER
from os import path


def validate_xml(dtd_path, xml_string):

    file_ = open(dtd_path)
    dtd_source = StringIO(file_.read())

    dtd = etree.DTD(dtd_source)

    xml = etree.XML(xml_string)

    result = dtd.validate(xml)
    if result:
        return None

    return dtd.error_log


class TestXMLGenerator(MockTestCase):

    layer = FTWMOPAGE_ZCML_LAYER

    def setUp(self):

        self.request = self.stub_request()
        self.context = self.stub()

        self.mopage_prop = self.create_dummy(
            partner='partner',
            partnerid='partnerid',
            password='password',
            importid_news='importid_news',
            importid_event='importid_event',
            importid_geolocation='importid_geolocation',
        )

        self.ptool = self.stub()
        self.expect(self.ptool.mopage_properties).result(self.mopage_prop)
        self.mock_tool(self.ptool, 'portal_properties')

        self.news_xml_generator = xml_generator.MopageNewsXMLGenerator(
                self.context, self.request)

        self.event_xml_generator = xml_generator.MopageEventXMLGenerator(
                self.context, self.request)

        self.geolocation_xml_generator = xml_generator.MopageGeolocationXMLGenerator(
                self.context, self.request)

    def test_geolocation_valid(self):
        data = [
            {
                'id': 'newsidä',
                'titel': 'newstitel',
                'adresse': 'adresse',
                'plz': 'plz',
                'ort': 'ort',
                'land_iso': 'land_iso',
                'mutationsdatum': 'mutationsdatum',
                'rubrik': ['rubirk1', 'rubrik2'],
                'telefon1': 'telefon1',
                'email': 'email',
                'oeffnungszeiten': 'oeffnungszeiten',
                'textmobile': 'textmobile',
                'url_web': 'url_web',
                'url_mobile': 'url_mobile',
                'firma': 'firma',
                'vorname': 'vorname',
                'name': 'name',
                'sex': 'sex',
                'abteilung': 'abteilung',
                'telefon2': 'telefon2',
                'telefon3': 'telefon3',
                'mobile': 'mobile',
                'fax': 'fax',
                'adresse_zusatz': 'adresse_zusatz',
                'land': 'land',
                'textlead': 'textlead',
                'url_bild': 'url_bild',
                'oev': 'oev',
                'longitude': 'longitude',
                'latitude': 'latitude',
                'text': 'text',
            },
            {
                'id': 'newsidä',
                'titel': 'newstitel',
                'adresse': 'adresse',
                'plz': 'plz',
                'ort': 'ort',
                'land_iso': 'land_iso',
                'mutationsdatum': 'mutationsdatum',
                'rubrik': ['rubirk1', 'rubrik2'],
                'telefon1': 'telefon1',
                'email': 'email',
                'oeffnungszeiten': 'oeffnungszeiten',
                'textmobile': 'textmobile',
                'url_web': 'url_web',
                'url_mobile': 'url_mobile',
                'firma': 'firma',
                'vorname': 'vorname',
                'name': 'name',
                'sex': 'sex',
                'abteilung': 'abteilung',
                'telefon2': 'telefon2',
                'telefon3': 'telefon3',
                'mobile': 'mobile',
                'fax': 'fax',
                'adresse_zusatz': 'adresse_zusatz',
                'land': 'land',
                'textlead': 'textlead',
                'url_bild': 'url_bild',
                'oev': 'oev',
                'longitude': 'longitude',
                'latitude': 'latitude',
                'text': 'text',
            },
        ]

        self.replay()

        xml = self.geolocation_xml_generator.generate_xml_string(data)

        result = validate_xml(
            path.join(path.dirname(__file__), 'geolocations.dtd'), xml)

        self.assertEquals(result, None)

    def test_geolocation_invalid(self):
        data = [
            {
                'id': 'newsidä',
                'adresse': 'adresse',
                'plz': 'plz',
                'ort': 'ort',
                'land_iso': 'land_iso',
                'mutationsdatum': 'mutationsdatum',
                'rubrik': ['rubirk1', 'rubrik2'],
                'telefon1': 'telefon1',
                'email': 'email',
                'oeffnungszeiten': 'oeffnungszeiten',
                'textmobile': 'textmobile',
                'url_web': 'url_web',
                'url_mobile': 'url_mobile',
                'firma': 'firma',
                'vorname': 'vorname',
                'name': 'name',
                'sex': 'sex',
                'abteilung': 'abteilung',
                'telefon2': 'telefon2',
                'telefon3': 'telefon3',
                'mobile': 'mobile',
                'fax': 'fax',
                'adresse_zusatz': 'adresse_zusatz',
                'land': 'land',
                'textlead': 'textlead',
                'url_bild': 'url_bild',
                'oev': 'oev',
                'longitude': 'longitude',
                'latitude': 'latitude',
                'text': 'text',
            },
        ]

        self.replay()

        xml = self.geolocation_xml_generator.generate_xml_string(data)

        result = validate_xml(
            path.join(path.dirname(__file__), 'geolocations.dtd'), xml)

        self.assertNotEquals(result, None)

    def test_event_valid(self):
        data = [
            {
                'id': 'newsidä',
                'titel': 'newstitel',
                'textmobile': 'textmobile',
                'allday': '1',
                'von': 'von',
                'bis': 'bis',
                'mutationsdatum': 'mutationsdatum',
                'textlead': 'textlead',
                'referenzort': 'refort',
                'url_bild': 'url_bild',
                'rubrik': ['rubirk1', 'rubrik2'],
                'text': 'text',
                'url_web': 'url_web',
                'url_mobile': 'url_mobile',
            },
            {
                'id': 'newsidä',
                'titel': 'newstitel',
                'textmobile': 'textmobile',
                'allday': '1',
                'von': 'von',
                'bis': 'bis',
                'mutationsdatum': 'mutationsdatum',
                'textlead': 'textlead',
                'referenzort': 'refort',
                'url_bild': 'url_bild',
                'rubrik': ['rubirk1', 'rubrik2'],
                'text': 'text',
                'url_web': 'url_web',
                'url_mobile': 'url_mobile',
            },
        ]

        self.replay()

        xml = self.event_xml_generator.generate_xml_string(data)

        result = validate_xml(
            path.join(path.dirname(__file__), 'events.dtd'), xml)

        self.assertEquals(result, None)

    def test_event_invalid(self):
        data = [
            {
                'id': 'newsidä',
                'textmobile': 'textmobile',
                'allday': '1',
                'von': 'von',
                'bis': 'bis',
                'mutationsdatum': 'mutationsdatum',
                'textlead': 'textlead',
                'referenzort': 'refort',
                'url_bild': 'url_bild',
                'rubrik': ['rubirk1', 'rubrik2'],
                'text': 'text',
                'url_web': 'url_web',
                'url_mobile': 'url_mobile',
            },
        ]

        self.replay()

        xml = self.event_xml_generator.generate_xml_string(data)

        result = validate_xml(
            path.join(path.dirname(__file__), 'events.dtd'), xml)

        self.assertNotEquals(result, None)

    def test_news_valid(self):
        data = [
            {
                'id': 'newsidä',
                'titel': 'newstitel',
                'textmobile': 'textmobile',
                'datumvon': 'datumvon',
                'mutationsdatum': 'mutationsdatum',
                'textlead': 'textlead',
                'url_bild': 'url_bild',
                'rubrik': ['rubirk1', 'rubrik2'],
                'text': 'text',
                'url_web': 'url_web',
                'url_mobile': 'url_mobile',
            },
            {
                'id': 'newsid',
                'titel': 'newstitel',
                'textmobile': 'textmobile',
                'datumvon': 'datumvon',
                'mutationsdatum': 'mutationsdatum',
                'textlead': 'textlead',
                'url_bild': 'url_bild',
                'rubrik': ['rubirk1', 'rubrik2'],
                'text': 'text',
                'url_web': 'url_web',
                'url_mobile': 'url_mobile',
            },
        ]

        self.replay()

        xml = self.news_xml_generator.generate_xml_string(data)

        result = validate_xml(
            path.join(path.dirname(__file__), 'news.dtd'), xml)

        self.assertEquals(result, None)

    def test_news_invalid(self):

        data = [
            {
            'id': 'newsidä',
            'textmobile': 'textmobile',
            'datumvon': 'datumvon',
            'mutationsdatum': 'mutationsdatum',
            'textlead': 'textlead',
            'url_bild': 'url_bild',
            'rubrik': ['rubirk1', 'rubrik2'],
            'text': 'text',
            'url_web': 'url_web',
            'url_mobile': 'url_mobile',
            },
        ]

        self.replay()

        xml = self.news_xml_generator.generate_xml_string(data)

        result = validate_xml(
            path.join(path.dirname(__file__), 'news.dtd'), xml)

        self.assertNotEquals(result, None)
