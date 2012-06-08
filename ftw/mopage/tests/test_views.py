from ftw.mopage.testing import FTWMOPAGE_ZCML_LAYER
from ftw.testing import MockTestCase
from mocker import ANY
from zope.interface import Interface
from ftw.mopage.interfaces import IMopageEventDataProvider, \
    IMopageNewsDataProvider, IMopageGeolocationDataProvider
from zope.component import getMultiAdapter
import os
import shutil


class TestViews(MockTestCase):

    layer = FTWMOPAGE_ZCML_LAYER

    def setUp(self):

        self.request_map = []

        self.request = self.stub_request()

        self.site = self.stub()

        self.context = self.stub()
        self.set_parent(self.context, self.site)
        self.expect(self.context.REQUEST.RESPONSE.setHeader(ANY, ANY)).call(
            lambda x, y: self.request_map.append([x, y]))

        self.expect(self.site.getPhysicalRoot()).result('/app/site')

        self.mopage_prop = {
            'partner': 'partner',
            'partnerid': 'partnerid',
            'password': 'password',
            'importid_events': 'importid_events',
            'importid_news': 'importid_news',
            'importid_geolocations': 'importid_geolocations',
            'export_dir': 'var',
        }

        self.file_path = os.path.join(
            os.environ.get('INSTANCE_HOME', ''), 'var')

        self.brain_1 = self.stub()
        self.expect(self.brain_1.getObject()).result(self.brain_1)

        self.data_provider = self.stub()
        self.expect(self.data_provider(ANY, ANY)).result(self.data_provider)

        self.mock_adapter(self.data_provider, IMopageEventDataProvider,
             (Interface, Interface))
        self.mock_adapter(self.data_provider, IMopageNewsDataProvider,
            (Interface, Interface))
        self.mock_adapter(self.data_provider, IMopageGeolocationDataProvider,
            (Interface, Interface))
        self.ptool = self.stub()
        self.expect(self.ptool.mopage_properties).result(self.mopage_prop)

        self.mock_tool(self.ptool, 'portal_properties')

        self.ctool = self.stub()
        self.mock_tool(self.ctool, 'portal_catalog')

    def test_events_download(self):

        self.expect(self.ctool(ANY)).result([self.brain_1])

        self.expect(self.request.form.get('refresh', ANY)).result('0')
        self.expect(self.request.form.get('plain', ANY)).result('0')

        data = {}
        self.expect(self.data_provider.get_data()).result(data)

        self.replay()

        view = getMultiAdapter((self.context, self.request),
                               name='mopage_events.xml')
        result = view()

        file_ = open('/Users/elio_schmutz/Plone/eggs/var/events.xml', 'r')

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

        self.expect(self.request.form.get('refresh', ANY)).result('0')
        self.expect(self.request.form.get('plain', ANY)).result('0')

        data = {}
        self.expect(self.data_provider.get_data()).result(data)

        self.replay()

        view = getMultiAdapter((self.context, self.request),
                               name='mopage_news.xml')
        result = view()

        file_ = open('/Users/elio_schmutz/Plone/eggs/var/news.xml', 'r')

        self.assertTrue(isinstance(file_, file))
        self.assertTrue(file_.read(), result)

        self.assertEquals(
            self.request_map,
            [
                ['Content-Type', 'application/xml'],
                ['Content-disposition', 'attachment; filename=news.xml'],
            ],
        )

    def test_geolocation_download(self):

        self.expect(self.ctool(ANY)).result([self.brain_1])

        self.expect(self.request.form.get('refresh', ANY)).result('0')
        self.expect(self.request.form.get('plain', ANY)).result('0')

        data = {}
        self.expect(self.data_provider.get_data()).result(data)

        self.replay()

        view = getMultiAdapter((self.context, self.request),
                               name='mopage_geolocations.xml')
        result = view()

        file_ = open(
            '/Users/elio_schmutz/Plone/eggs/var/geolocations.xml', 'r')

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
        shutil.rmtree(self.file_path)
