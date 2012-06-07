import os
from Products.statusmessages.interfaces import IStatusMessage
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from zope.component import getMultiAdapter


class BaseExport(BrowserView):

    filename = None
    template = None
    data_provider = None
    query_provider = None

    def __call__(self):
        self.properties = getToolByName(self.context,
                                        'portal_properties').mopage_properties

        file_path = os.path.join(os.environ.get('INSTANCE_HOME', ''),
                                 'var/%s.xml' % self.filename)

        if self.request.form.get('refresh', None) == '1' or \
           not os.path.isfile(file_path):
            # refresh xml => do not download
            file_content = self.template()
            xml_file = open(file_path, 'w')
            xml_file.write(file_content.encode('utf8'))
            xml_file.close()
            msg = u'Cache flushed for %s' % self.filename
            IStatusMessage(self.request).addStatusMessage(msg, type='info')
            return self.request.response.redirect(self.context.absolute_url())
        else:
            # download file
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

    def items(self):
        """Gets the news from catalog and prepares the
        attributes for the xml.
        """

        query_provider = getMultiAdapter(
            (self.context, self.request), self.query_provider)

        catalog = getToolByName(self.context, 'portal_catalog')
        brains = catalog(query_provider.get_query())

        items = []
        for brain in brains:
            obj = brain.getObject()
            data_provider = getMultiAdapter(
                (obj, self.request), self.data_provider)

            data = data_provider.get_data()

            if not data:
                continue

            items.append(data)

        return items
