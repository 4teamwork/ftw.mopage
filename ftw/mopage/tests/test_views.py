# coding=UTF-8
from ftw.mopage.testing import FTWMOPAGE_ZCML_LAYER
from ftw.testing import MockTestCase
from mocker import ANY
from zope.interface import Interface
from ftw.mopage.interfaces import IMopageEventDataProvider, \
    IMopageNewsDataProvider, IMopageGeolocationDataProvider
from zope.component import getMultiAdapter
import os
import shutil
from tempfile import gettempdir
from plone.memoize import ram


class TestViews(MockTestCase):

    layer = FTWMOPAGE_ZCML_LAYER

    def setUp(self):
        super(TestViews, self).setUp()

        self._ori_instance_home = os.environ.get('INSTANCE_HOME', '')
        os.environ['INSTANCE_HOME'] = gettempdir()

        self.request_map = []

        self.request = self.stub_request()

        self.site = self.stub()

        self.context = self.stub()
        self.set_parent(self.context, self.site)
        self.expect(self.context.REQUEST.RESPONSE.setHeader(ANY, ANY)).call(
            lambda x, y: self.request_map.append([x, y]))

        self.expect(self.site.getPhysicalRoot()).result('/app/site')

        self.mopage_prop = self.create_dummy(
            partner='pärtner',
            partnerid='partnerid',
            password='password',
            export_dir='var',
            importid_news='importid_news',
            importid_event='importid_event',
            importid_geolocation='importid_geolocation',
        )
        self.file_path = os.path.join(
            os.environ.get('INSTANCE_HOME', ''), 'var')

        self.brain_1 = self.stub()
        self.expect(self.brain_1.getObject()).result(self.brain_1)

        self.ptool = self.stub()
        self.expect(self.ptool.mopage_properties).result(self.mopage_prop)
        self.mock_tool(self.ptool, 'portal_properties')

        self.ctool = self.stub()
        self.mock_tool(self.ctool, 'portal_catalog')

        # DataProvider adapters
        self.news_data_provider = self.providing_stub(
            [IMopageNewsDataProvider])
        self.expect(self.news_data_provider(ANY, ANY)).result(
            self.news_data_provider)
        self.expect(
            self.news_data_provider.context.absolute_url()).result(
                'url_to_obj')

        self.event_data_provider = self.providing_stub(
            [IMopageEventDataProvider])
        self.expect(self.event_data_provider(ANY, ANY)).result(
            self.event_data_provider)
        self.expect(
            self.event_data_provider.context.absolute_url()).result(
                'url_to_obj')

        self.geolocation_data_provider = self.providing_stub(
            [IMopageGeolocationDataProvider])
        self.expect(self.geolocation_data_provider(ANY, ANY)).result(
            self.geolocation_data_provider)
        self.expect(
            self.geolocation_data_provider.context.absolute_url()).result(
                'url_to_obj')

        # Registering DataProvider adapters
        self.mock_adapter(self.event_data_provider, IMopageEventDataProvider,
             (Interface, Interface))
        self.mock_adapter(self.news_data_provider, IMopageNewsDataProvider,
            (Interface, Interface))
        self.mock_adapter(
            self.geolocation_data_provider, IMopageGeolocationDataProvider,
            (Interface, Interface))

    def test_events_download(self):

        self.expect(self.ctool(ANY)).result([self.brain_1])

        data = {
            'id': 'äxx',
            'titel': 'abc123',
            'allday': 'x',
            'von': 'abc123',
            'bis': 'abc123',
        }

        self.expect(self.event_data_provider.get_data()).result(data)

        self.replay()

        view = getMultiAdapter((self.context, self.request),
                               name='mopage_events.xml')
        result = view()

        file_ = open(os.path.join(self.file_path, 'events.xml'), 'r')

        self.assertTrue(isinstance(file_, file))
        self.assertTrue(file_.read(), result)

        self.assertEquals(
            self.request_map,
            [
                ['Content-Type', 'application/xml'],
                ['Content-disposition', 'attachment; filename=events.xml'],
            ],
        )

    def test_news_download(self):

        self.expect(self.ctool(ANY)).result([self.brain_1])

        data = {
            'id': 'äxx',
            'titel': 'abc123',
            'textmobile': 'abc123',
            'datumvon': 'abc123',
            'mutationsdatum': 'abc123',
        }

        self.expect(self.news_data_provider.get_data()).result(data)

        self.replay()

        view = getMultiAdapter((self.context, self.request),
                               name='mopage_news.xml')
        result = view()

        file_ = open(os.path.join(self.file_path, 'news.xml'), 'r')

        self.assertTrue(isinstance(file_, file))
        self.assertTrue(file_.read(), result)

        self.assertEquals(
            self.request_map,
            [
                ['Content-Type', 'application/xml'],
                ['Content-disposition', 'attachment; filename=news.xml'],
            ],
        )

        result = view()

    def test_geolocation_download(self):

        self.expect(self.ctool(ANY)).result([self.brain_1])

        self.expect(self.request.form.get('plain', ANY)).result('0')

        data = {
            'id': 'äxx',
            'titel': 'abc123',
            'adresse': 'abc123',
            'plz': 'abc123',
            'ort': 'abc123',
            'land_iso': 'xx',
            'mutationsdatum': 'abc123',
        }
        self.expect(self.geolocation_data_provider.get_data()).result(data)

        self.replay()

        view = getMultiAdapter((self.context, self.request),
                               name='mopage_geolocations.xml')
        result = view()

        file_ = open(os.path.join(self.file_path, 'geolocations.xml'), 'r')

        self.assertTrue(isinstance(file_, file))
        self.assertTrue(file_.read(), result)

        self.assertEquals(
            self.request_map,
            [
                ['Content-Type', 'application/xml'],
                [
                    'Content-disposition',
                    'attachment; filename=geolocations.xml',
                ],
            ],
        )

    def tearDown(self):
        os.environ['INSTANCE_HOME'] = self._ori_instance_home
        shutil.rmtree(self.file_path)
