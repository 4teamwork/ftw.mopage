from ftw.mopage.interfaces import IMopageGeolocationDataValidator, IMopageNewsDataValidator, IMopageEventDataValidator
from zope.interface import implements

class MopageValidationError(Exception):
    """ Raised when a the data is not valid
    """


class BaseMopageDataValidator(object):

    required_attributes = []

    def __init__(self, context, request, data_provider):
        self.context = context
        self.request = request
        self.data_provider = data_provider
        self.data = self.data_provider.get_data()

    def validate(self):

        queue = self.get_validation_queue() + self.get_additional_validations()

        for job in queue:
            job()

    def get_validation_queue(self):

        return [
            self.check_empty_data,
            self.check_correct_instance,
            self.check_required_attributes,
        ]

    def get_additional_validations(self):

        return []

    def check_empty_data(self):
        if not self.data:
            raise MopageEventDataValidator(
                'The given data_provider does not return any data.'
                )

    def check_correct_instance(self):
        if not isinstance(self.data, dict):
            raise MopageEventDataValidator(
                'The data_provider must return a dict with data.'
                )

    def check_required_attributes(self):
        """ Check for required attributes
        """

        for attr in self.required_attributes:
            if not attr in self.data.keys():
                raise MopageEventDataValidator(
                    'The following attribute is required. Please ' \
                    + 'specify it in your data_provider: %s' % attr
                    )


class MopageEventDataValidator(BaseMopageDataValidator):
    implements(IMopageEventDataValidator)


    def get_validation_queue(self):
        super(MopageEventDataValidator, self).validate()
        """
        """


class MopageNewsDataValidator(BaseMopageDataValidator):
    implements(IMopageNewsDataValidator)

    required_attributes = ['id', 'titel', 'textmobile']

    def validate(self):
        super(MopageNewsDataValidator, self).validate()
        """
        """

class MopageGeolocationDataValidator(BaseMopageDataValidator):
    implements(IMopageGeolocationDataValidator)


    def validate(self):
        super(MopageGeolocationDataValidator, self).validate()
        """
        """