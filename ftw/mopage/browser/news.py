import os
import re
from DateTime import DateTime
from Products.statusmessages.interfaces import IStatusMessage
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
#from urlparse import urlparse, urljoin


A_HREF_RE = re.compile(r'<a[^>]*?href="([^"]*)', re.IGNORECASE|re.DOTALL)


class ExportNews(BrowserView):

    filename = 'news'
    template = ViewPageTemplateFile('news.xml')

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

    def cdata(self, text):
        """If you want to fill special chars like & or HTML you have
        to insert a CDATA paragraph.
        """
        return "<![CDATA[%s]]>" % text

    def make_links_absolute(self, obj, text):
        """Converts relative links to absolute.
        """
        matches = A_HREF_RE.findall(text)
        for m in matches:
            target = obj.restrictedTraverse(m, None) 
            if target:
                text = text.replace('href="%s"' % m, 'href="%s"' % target.absolute_url())
        return text

    def convert_date(self, date):
        """Returns the date in format: 2011-2-15 12:55:34
        """
        return '%s %s' % (date.Date().replace('/', '-'),
                          date.Time())

    def is_allday(self, *kw):
        """Checks if all kw (DateTime) .Time() is '00:00:00'.
        """
        for date in kw:
            if date.Time() != '00:00:00':
                return False
        return True

    def items(self):
        """Gets the news from catalog and prepares the
        attributes for the xml.
        """

        catalog = getToolByName(self.context, 'portal_catalog')
        brains = catalog(portal_type='Paragraph', review_state="published",
                         path={'query':self.properties.news_path, 'depth':1},
                         expires={'query':DateTime(), 'range':'min'})

        items = []
        for brain in brains:
            obj = brain.getObject()
            img = obj.getImage()
            text_short = obj.getText(mimetype='text/plain')
            if len(text_short) > 200:
                text_short = text_short[:200]
            items.append({
                    'id': brain.UID,
                    'title': brain.Title,
                    'description': brain.Description,
                    'text_short': text_short,
                    'text': self.cdata(self.make_links_absolute(obj, obj.getText()) or ' '),
                    'image_url': img and img.absolute_url() or '',
                    'categories': brain.Subject,
                    'url': brain.getURL(),
                    'modified': self.convert_date(brain.modified),
                    'datumvon': self.convert_date(brain.effective),
                    'datumbis': self.convert_date(brain.expires)})
        return items
