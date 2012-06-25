# coding=UTF-8
from ftw.testing import MockTestCase
from ftw.mopage import data_validator
from mocker import ANY
from ftw.mopage.testing import FTWMOPAGE_ZCML_LAYER


class TestGeolocationValidator(MockTestCase):

    layer = FTWMOPAGE_ZCML_LAYER

    def setUp(self):

        self.request = self.stub_request()
        self.context = self.stub()
        self.data_provider = self.stub()
        self.expect(
            self.data_provider.context.absolute_url()).result('url_to_obj')

        self.data_validator = self.mocker.patch(
            data_validator.MopageGeolocationDataValidator(
                self.context, self.request, self.data_provider))

    def test_validate_geolocation_ok(self):

        data = {
            'id': 'äxx',
            'titel': 'abc123',
            'adresse': 'abc123',
            'plz': 'abc123',
            'ort': 'abc123',
            'land_iso': 'xx',
            'mutationsdatum': 'abc123',
        }

        self.replay()

        result = self.data_validator.validate(data)

        self.assertEquals(result, None)

    def test_validate_geolocation_error(self):

        data = {
            'id': 'äxx',
            'titel': 'abc123',
            'adresse': 'abc123',
            'plz': 'abc123',
            'ort': 'abc123',
            'url_bild': ['abc123'],
            'url_web': "x"*500,
        }

        self.replay()

        self.assertRaises(
            data_validator.MopageValidationError,
            self.data_validator.validate,
            data)


class TestEventValidator(MockTestCase):

    layer = FTWMOPAGE_ZCML_LAYER

    def setUp(self):

        self.request = self.stub_request()
        self.context = self.stub()
        self.data_provider = self.stub()
        self.expect(
            self.data_provider.context.absolute_url()).result('url_to_obj')

        self.data_validator = self.mocker.patch(
            data_validator.MopageEventDataValidator(
                self.context, self.request, self.data_provider))

    def test_validate_event_ok(self):

        data = {
            'id': 'äxx',
            'titel': 'abc123',
            'allday': 'x',
            'von': 'abc123',
            'bis': 'abc123',
        }

        self.replay()

        result = self.data_validator.validate(data)

        self.assertEquals(result, None)

    def test_validate_event_error(self):

        data = {
            'id': 'äxx',
            'titel': 'abc123',
            'textmobile': 'abc123',
            'url_bild': ['abc123'],
            'referenzort': "x"*200,
        }

        self.replay()

        self.assertRaises(
            data_validator.MopageValidationError,
            self.data_validator.validate,
            data)


class TestNewsValidator(MockTestCase):

    layer = FTWMOPAGE_ZCML_LAYER

    def setUp(self):

        self.request = self.stub_request()
        self.context = self.stub()
        self.data_provider = self.stub()
        self.expect(
            self.data_provider.context.absolute_url()).result('url_to_obj')

        self.data_validator = self.mocker.patch(
            data_validator.MopageNewsDataValidator(
                self.context, self.request, self.data_provider))

    def test_validate_news_ok(self):

        data = {
            'id': 'äxx',
            'titel': 'abc123',
            'textmobile': 'abc123',
            'datumvon': 'abc123',
            'mutationsdatum': 'abc123',
        }

        self.replay()

        result = self.data_validator.validate(data)

        self.assertEquals(result, None)

    def test_validate_news_error(self):

        data = {
            'id': 'äxx',
            'titel': 'abc123',
            'textmobile': 'abc123',
            'url_bild': ['abc123'],
            'mutationsdatum': "x"*200,
        }

        self.replay()

        self.assertRaises(
            data_validator.MopageValidationError,
            self.data_validator.validate,
            data)


class TestValidate(MockTestCase):

    layer = FTWMOPAGE_ZCML_LAYER

    def setUp(self):

        self.request = self.stub_request()
        self.context = self.stub()
        self.data_provider = self.stub()

        self.data_validator = self.mocker.patch(
            data_validator.BaseMopageDataValidator(
                self.context, self.request, self.data_provider))

    def test_validate_no_errors(self):

        self.expect(self.data_validator.raise_error()).count(0)
        self.expect(
            self.data_validator.get_validation_queue()).result([lambda:None])

        self.replay()

        result = self.data_validator.validate({'attr': 'value'})

        self.assertEquals(result, None)

    def test_validate_with_errors(self):

        error_container = {}

        self.expect(
            self.data_validator.get_validation_queue()).result(
                [lambda:'error'])
        self.expect(self.data_validator.raise_error(ANY)).call(
            lambda x: error_container.update({'errors': x}))

        self.replay()

        result = self.data_validator.validate({'attr': 'value'})

        self.assertEquals(result, None)
        self.assertEquals(error_container['errors'], ['error'])


class TestRaiseError(MockTestCase):

    layer = FTWMOPAGE_ZCML_LAYER

    def setUp(self):

        self.request = self.stub_request()
        self.context = self.stub()
        self.data_provider = self.stub()
        self.expect(
            self.data_provider.context.absolute_url()).result('url_to_obj')

        self.data_validator = data_validator.BaseMopageDataValidator(
            self.context, self.request, self.data_provider)

    def test_raise_error(self):

        self.replay()

        with self.assertRaises(data_validator.MopageValidationError) as cm:
            self.data_validator.raise_error(['error1', 'error2'])

        exc = cm.exception
        self.assertEqual(str(exc), '\nYou get errors while validating data '
            'of item url_to_obj with following associated data provider: %s'
            '\n\n - error1\n - error2' % self.data_provider)


class TestValidationMethods(MockTestCase):

    layer = FTWMOPAGE_ZCML_LAYER

    def setUp(self):

        self.request = self.stub_request()
        self.context = self.stub()
        self.data_provider = self.stub()
        self.expect(self.data_provider.absolute_url()).result('url_to_obj')

        self.data_validator = self.mocker.patch(
            data_validator.BaseMopageDataValidator(
                self.context, self.request, self.data_provider))

    def test_validate_no_data(self):

        self.replay()

        result = self.data_validator.validate({})

        self.assertEquals(result, None)

    def test_validate_correct_instance_ok(self):

        self.expect(self.data_validator.data).result({}).count(0, None)

        self.replay()

        result = self.data_validator._validate_correct_instance()

        self.assertEquals(result, None)

    def test_validate_correct_instance_error(self):

        self.expect(self.data_validator.data).result([]).count(0, None)

        self.replay()

        result = self.data_validator._validate_correct_instance()

        self.assertEquals(
            result, 'The data_provider must return a dict with data.')

    def test_validate_required_attributes_ok(self):

        self.expect(self.data_validator.attributes).result(
            [
                data_validator.Property('id', True, str, 50),
                data_validator.Property('titel', True, str, 100),
            ])

        self.expect(self.data_validator.data).result({
            'id': 'id',
            'titel': 'titee',
        }).count(0, None)

        self.replay()

        result = self.data_validator._validate_required_attributes()

        self.assertEquals(
            result, None)

    def test_validate_required_attributes_error(self):

        self.expect(self.data_validator.attributes).result(
            [
                data_validator.Property('id', True, str, 50),
                data_validator.Property('titel', True, str, 100),
                data_validator.Property('name', True, str, 100),
                data_validator.Property('titel', False, str, 100),
            ])

        self.expect(self.data_validator.data).result({
            'id': 'id',
        }).count(0, None)

        self.replay()

        result = self.data_validator._validate_required_attributes()

        self.assertEquals(
            result, 'The following attribute are required. Please specify '
            'them in your data_provider: titel, name')

    def test_validate_attribute_type_ok(self):

        self.expect(self.data_validator.attributes).result(
            [
                data_validator.Property('id', True, str, 50),
                data_validator.Property('titel', True, list, 100),
            ])

        self.expect(self.data_validator.data).result({
            'id': 'id',
            'titel': ['list'],
        }).count(0, None)

        self.replay()

        result = self.data_validator._validate_attribute_type()

        self.assertEquals(result, None)

    def test_validate_attribute_type_error(self):

        self.expect(self.data_validator.attributes).result(
            [
                data_validator.Property('id', True, str, 50),
                data_validator.Property('titel', True, list, 100),
                data_validator.Property('name', True, dict, 100),
            ])

        self.expect(self.data_validator.data).result({
            'id': 'id',
            'titel': 'list',
            'name': 'dict',
        }).count(0, None)

        self.replay()

        result = self.data_validator._validate_attribute_type()

        self.assertEquals(
            result, 'The following attributes have a bad type: '
                'titel: type: <type \'list\'>, name: type: <type \'dict\'>')

    def test_validate_attribute_length_ok(self):

        self.expect(self.data_validator.attributes).result(
            [
                data_validator.Property('id', True, str, 10),
                data_validator.Property(
                    'titel',
                    True,
                    list,
                    0,
                    elements=data_validator.Property(
                        '', True, str, 10), ),

            ])

        self.expect(self.data_validator.data).result({
            'id': 'id',
            'titel': ['list1', 'list2'],
        }).count(0, None)

        self.replay()

        result = self.data_validator._validate_attribute_length()

        self.assertEquals(result, None)

    def test_validate_attribute_length_error(self):

        self.expect(self.data_validator.attributes).result(
            [
                data_validator.Property('id', True, str, 10),
                data_validator.Property(
                    'titel',
                    True,
                    list,
                    0,
                    elements=data_validator.Property(
                        '', True, str, 10), ),

            ])

        self.expect(self.data_validator.data).result({
            'id': 'too_long_id',
            'titel': ['too_long_list_element', 'list2'],
        }).count(0, None)

        self.replay()

        result = self.data_validator._validate_attribute_length()

        self.assertEquals(
            result, 'Text is too long in following attributes: '
                'id: max: 10, titel: max: 10.')

    def test_validate_unused_attributes_ok(self):

        self.expect(self.data_validator.attributes).result(
            [
                data_validator.Property('id', True, str, 50),
                data_validator.Property('titel', True, list, 100),
            ])

        self.expect(self.data_validator.data).result({
            'id': 'id',
            'titel': 'titel',
        }).count(0, None)

        self.replay()

        result = self.data_validator._validate_unused_attributes()

        self.assertEquals(result, None)

    def test_validate_unused_attributes_error(self):

        self.expect(self.data_validator.attributes).result(
            [
                data_validator.Property('id', True, str, 50),
                data_validator.Property('titel', True, list, 100),
            ])

        self.expect(self.data_validator.data).result({
            'id': 'id',
            'titel': 'titel',
            'badman': 'badman',
            'superman': 'superman',
        }).count(0, None)

        self.replay()

        result = self.data_validator._validate_unused_attributes()

        self.assertEquals(result, 'You have defined unused attributes: '
            'badman, superman.')
