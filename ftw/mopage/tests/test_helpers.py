from DateTime import DateTime
from ftw.mopage import helpers
from ftw.mopage.testing import FTWMOPAGE_ZCML_LAYER
from ftw.testing import MockTestCase
from mocker import ANY


class TestMakeLinksAbsolute(MockTestCase):

    layer = FTWMOPAGE_ZCML_LAYER

    def setUp(self):

        self.obj = self.stub()

    def test_no_links_in_text(self):

        self.replay()

        result = helpers.make_links_absolute(self.obj, 'text with no links')

        self.assertEquals(result, 'text with no links')

    def test_with_links_in_text(self):

        self.expect(self.obj.restrictedTraverse('rel_link', ANY)).result(
            self.obj)
        self.expect(self.obj.absolute_url()).result('absolute_link')

        self.replay()

        result = helpers.make_links_absolute(
            self.obj, 'text with <a href="rel_link">My Link</a>')

        self.assertEquals(
            result, 'text with <a href="absolute_link">My Link</a>')

    def test_with_links_in_text_but_not_found(self):

        self.expect(
            self.obj.restrictedTraverse('rel_link', ANY)).result(None)

        text = 'text with <a href="rel_link">My Link</a>'
        self.replay()

        result = helpers.make_links_absolute(self.obj, text)

        self.assertEquals(result, text)


class TestConvertDate(MockTestCase):

    layer = FTWMOPAGE_ZCML_LAYER

    def test_no_date(self):

        self.replay()

        result = helpers.convert_date('')

        self.assertEquals(result, '')

    def test_with_date(self):

        self.replay()

        result = helpers.convert_date(DateTime('31.01.2012 00:00:00'))

        self.assertEquals(result, '2012-01-31 00:00:00')

class TestIsAllday(MockTestCase):

    layer = FTWMOPAGE_ZCML_LAYER

    def test_no_args(self):

        self.replay()

        result = helpers.is_allday()

        self.assertEquals(result, True)

    def test_bad_args(self):

        self.replay()

        result = helpers.is_allday(object(), object())

        self.assertEquals(result, True)

    def test_is_allday(self):

        self.replay()

        result = helpers.is_allday(
            DateTime('2012-12-01 00:00:00'), DateTime('2012-12-03 00:00:00'))

        self.assertEquals(result, True)

    def test_not_allday(self):

        self.replay()

        result = helpers.is_allday(
            DateTime('2012-12-01 00:00:00'), DateTime('2012-12-03 00:02:00'))

        self.assertEquals(result, False)
