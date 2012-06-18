from ftw.mopage.interfaces import IMopageGeolocationDataValidator, \
    IMopageNewsDataValidator, IMopageEventDataValidator
from zope.interface import implements


class MopageValidationError(Exception):
    """ Raised when a the data is not valid
    """


class Property(object):

    def __init__(self, name, required, type_, length, **kwargs):

        self.properties = {
            'name': name,
            'required': required,
            'type_': type_,
            'length': length,
        }

        self.properties.update(kwargs)

    def __call__(self, name):
        return self.properties.get(name, '')


class BaseMopageDataValidator(object):

    def __init__(self, context, request, data_provider):
        self.context = context
        self.request = request
        self.data_provider = data_provider
        self.data = None
        self.attributes = []

    def validate(self, data):
        """ Validates the given data

        """
        self.data = data

        if not self.data:
            return

        self.attributes = self.get_attributes()

        queue = self.get_validation_queue()

        validated = [job() for job in queue]

        error_msgs = filter(None, validated)

        if error_msgs:
            self.raise_error(error_msgs)

    def get_attributes(self):
        return []

    def raise_error(self, error_msgs):

        entry_msg = ('\nYou get errors while validating data of item %s with '
             'following associated data provider: %s\n') % (
                self.data_provider.context.absolute_url(),
                self.data_provider,
            )

        error_msg = '\n - '.join([entry_msg] + error_msgs)

        raise MopageValidationError(error_msg)

    def get_validation_queue(self):
        """Return a list of validation methods found in the validator class.
        """

        def is_validation_method(attr):

            return attr.startswith('validate_') and \
                hasattr(getattr(self, attr), '__call__')

        method_names = filter(is_validation_method, dir(self))
        methods = [getattr(self, name) for name in method_names]

        return methods

    def validate_not_empty_data(self):
        if not self.data:
            return 'The given data_provider does not return any data.'

    def validate_correct_instance(self):
        if not isinstance(self.data, dict):
            return 'The data_provider must return a dict with data.'

    def validate_required_attributes(self):
        """ Check for required attributes
        """

        errors = []

        for prop in self.attributes:

            required = prop('required')
            available = prop('name') in self.data.keys()
            has_data = self.data.get(prop)

            if required and not available and not has_data:
                errors.append(prop('name'))

        if errors:
            return ('The following attribute are required. Please specify '
            'them in your data_provider: %s') % ', '.join(errors)

    def validate_attribute_type(self):
        """ Check for attibutes containing text
        """

        errors = []

        for prop in self.attributes:

            value = self.data.get(prop('name'))

            if value and not type(value) == prop('type_'):
                errors.append(('%s: type: %s') % (prop('name'), prop('type_')))

        if errors:
            return ('The following attributes have a bad type: %s') % (
                ', '.join(errors))

    def validate_attribute_length(self):
        """ Check for attibutes containing text
        """

        errors = []

        def length_validator(value, length, name):
            if not len(value) <= length:
                errors.append(('%s: max: %s') % (name, length))

        for prop in self.attributes:
            value = self.data.get(prop('name'))

            if isinstance(value, (str, unicode)):
                length_validator(value, prop('length'), prop('name'))

            if isinstance(value, (list, tuple, set)):
                subprop = prop('elements')
                for subvalue in value:
                    length_validator(subvalue, subprop('length'), prop('name'))

        if errors:
            return ('Text is too long in following attributes: %s.') % (
                ', '.join(errors))

    def validate_unused_attributes(self):
        """ Check the data for unused attributes.
        """

        given_attrs = self.data.keys()
        availabel_attrs = [attr('name') for attr in self.attributes]

        errors = []

        for attr in given_attrs:
            if not attr in availabel_attrs:
                errors.append(attr)

        if errors:
            return ('You have defined unused attributes: %s.') % (
                ', '.join(errors))


class MopageEventDataValidator(BaseMopageDataValidator):
    implements(IMopageEventDataValidator)

    def get_attributes(self):
        return [
            Property('id', True, str, 50),
            Property('titel', True, str, 100),
            Property('von', True, str, 255),
            Property('bis', True, str, 255),
            Property('referenzort', False, str, 50),
            Property('textmobile', False, str, 10000),
            Property('rubrik', False, list, 0,
                elements=Property('', False, str, 100)),
            Property('textlead', False, str, 1000),
            Property('url_bild', False, str, 225),
            Property('url_web', False, str, 255),
            Property('url_mobile', False, str, 255),
            Property('text', False, str, 30000),
        ]


class MopageNewsDataValidator(BaseMopageDataValidator):
    implements(IMopageNewsDataValidator)

    def get_attributes(self):
        return [
            Property('id', True, str, 50),
            Property('titel', True, str, 100),
            Property('textmobile', True, str, 10000),
            Property('datumvon', True, str, 60),
            Property('mutationsdatum', True, str, 100),
            Property('textlead', False, str, 1000),
            Property('url_bild', False, str, 225),
            Property('rubrik', False, list, 0,
                elements=Property('', False, str, 100)),
            Property('text', False, str, 30000),
            Property('url_web', False, str, 1000),
            Property('url_mobile', False, str, 1000),
        ]


class MopageGeolocationDataValidator(BaseMopageDataValidator):
    implements(IMopageGeolocationDataValidator)

    def get_attributes(self):
        return [
            Property('id', True, str, 50),
            Property('titel', True, str, 100),
            Property('adresse', True, str, 255),
            Property('plz', True, str, 50),
            Property('ort', True, str, 255),
            Property('land_iso', True, str, 2),
            Property('mutationsdatum', True, str, 100),
            Property('rubrik', False, list, 0,
                elements=Property('', False, str, 100)),
            Property('telefon1', False, str, 255),
            Property('email', False, str, 500),
            Property('oeffnungszeiten', False, str, 255),
            Property('textmobile', False, str, 10000),
            Property('url_web', False, str, 255),
            Property('url_mobile', False, str, 255),
            Property('firma', False, str, 255),
            Property('vorname', False, str, 255),
            Property('name', False, str, 255),
            Property('sex', False, str, 1),
            Property('abteilung', False, str, 255),
            Property('telefon2', False, str, 255),
            Property('telefon3', False, str, 255),
            Property('mobile', False, str, 255),
            Property('fax', False, str, 255),
            Property('adresse_zusatz', False, str, 255),
            Property('land', False, str, 255),
            Property('textlead', False, str, 1000),
            Property('url_bild', False, str, 255),
            Property('oev', False, str, 255),
            Property('longitude', False, float, 0),
            Property('latitude', False, float, 0),
            Property('text', False, str, 30000),
        ]
