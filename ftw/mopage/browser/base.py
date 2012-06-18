import os
from Products.statusmessages.interfaces import IStatusMessage
from Products.Five.browser import BrowserView
from zope.component import getMultiAdapter


class BaseExport(BrowserView):

    filename = None
    template = None
    data_provider = None
    data_validator = None
    lookup_provider = None

    def __call__(self):

        file_path = self.get_file_path(
            self.properties.export_dir, self.filename)

        if self.request.form.get('refresh', None) == '1':

            # refresh xml => do not download
            self.refresh(file_path)

            msg = u'Cache flushed for %s' % self.filename
            IStatusMessage(self.request).addStatusMessage(msg, type='info')

            return self.request.response.redirect(self.context.absolute_url())

        return self.download(file_path)

    def get_file_path(self, export_dir, filename):
        """ Return the path of the file. If the path does not exist, we
        create it.
        """
        path = os.path.join(
            os.environ.get('INSTANCE_HOME', ''), '%s/' % export_dir)

        if not os.path.exists(path):
            os.makedirs(path)

        file_path = os.path.join(path, '%s.xml' % filename)

        return file_path

    def refresh(self, file_path):
        """ Refresh or create the xml file
        """

        file_content = self.get_xml()
        xml_file = open(file_path, 'w')
        xml_file.write(file_content.encode('utf8'))
        xml_file.close()

        return True

    def download(self, file_path):
        """ Download the xml file
        """

        if not os.path.isfile(file_path):
            # If we there is no file, we create it
            self.refresh(file_path)

        xml_file = open(file_path, 'r+')
        tmp = xml_file.read()
        xml_file.close()

        self.context.REQUEST.RESPONSE.setHeader(
            'Content-Type',
            'application/xml')

        if self.request.form.get('plain', 0) != '1':
            self.context.REQUEST.RESPONSE.setHeader(
                'Content-disposition',
                'attachment; filename=%s.xml' % self.filename)

        return tmp

    def get_xml(self):

        xml_writer = getMultiAdapter(
            (self.context, self.request), self.xml_writer)

        return xml_writer.generate_xml(self.get_data)

    def get_data(self):
        """Gets the news from catalog and prepares the
        attributes for the xml.
        """

        lookup_provider = getMultiAdapter(
            (self.context, self.request), self.lookup_provider)

        brains = lookup_provider.get_brains()

        data = []
        for brain in brains:
            obj = brain.getObject()

            data_provider = getMultiAdapter(
                (obj, self.request), self.data_provider)

            data = data_provider.get_data()

            data_validator = getMultiAdapter(
                (
                    self.context,
                    self.request,
                    data_provider,
                ),
                self.data_validator)

            data_validator.validate(data)

            data.append(data_provider.get_data())

        return data
