from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from zope.component import getMultiAdapter
import os


class BaseExport(BrowserView):

    filename = None
    template = None
    data_provider = None
    data_validator = None
    lookup_provider = None

    def __call__(self):

        return self.download()

    def get_file_path(self):
        """ Return the path of the file. If the path does not exist, we
        create it.
        """

        properties = getToolByName(self.context, 'portal_properties')
        properties = properties.mopage_properties

        export_dir = properties.export_dir

        path = os.path.join(
            os.environ.get('INSTANCE_HOME', ''), '%s/' % export_dir)

        if not os.path.exists(path):
            os.makedirs(path)

        file_path = os.path.join(path, '%s.xml' % self.filename)

        return file_path

    def refresh(self):
        """ Refresh or create the xml file
        """

        file_content = self.get_xml()
        xml_file = open(self.get_file_path(), 'w')
        xml_file.write(file_content)
        xml_file.close()

        return True

    def download(self):
        """ Download the xml file
        """
        path = self.get_file_path()
        self.refresh()

        xml_file = open(path, 'r+')
        tmp = xml_file.read()
        xml_file.close()

        self.context.REQUEST.RESPONSE.setHeader(
            'Content-Type',
            'application/xml')

        self.context.REQUEST.RESPONSE.setHeader(
            'Content-disposition',
            'attachment; filename=%s.xml' % self.filename)

        return tmp

    def get_xml(self):
        """ Return the generated xml as string
        """

        xml_generator = getMultiAdapter(
            (self.context, self.request), self.xml_generator)

        return xml_generator.generate_xml_string(self.get_data())

    def get_data(self):
        """ Return the received and validated data of all data providers in
        a list
        """

        lookup_provider = getMultiAdapter(
            (self.context, self.request), self.lookup_provider)

        objects = lookup_provider.get_objects()

        xml_data = []
        for obj in objects:

            data_provider = getMultiAdapter(
                (obj, self.request), self.data_provider)

            data = data_provider.get_data()
            if not data:
                continue

            data_validator = getMultiAdapter(
                (
                    self.context,
                    self.request,
                    data_provider,
                ),
                self.data_validator)

            data_validator.validate(data)

            xml_data.append(data_provider.get_data())

        return xml_data
