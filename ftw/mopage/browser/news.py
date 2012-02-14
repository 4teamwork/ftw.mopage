from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName


class ExportNews(BrowserView):

    filename = 'news'
    template = ViewPageTemplateFile('news.xml')

    def __call__(self):
        self.properties = getToolByName(self.context,
                                        'portal_properties').mopage_properties
        if self.request.form.get('plain', 0) != '1':
            self.context.REQUEST.RESPONSE.setHeader(
                'Content-Type',
                'application/xml')
            self.context.REQUEST.RESPONSE.setHeader(
                'Content-disposition',
                'attachment; filename=%s.xml' % self.filename)
        return self.template()

    def cdata(self, text):
        """If you want to fill special chars like & or HTML you have
        to insert a CDATA paragraph.
        """
        return "<![CDATA[%s]]>" % text

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
        brains = catalog(portal_type='News Item')
        items = []
        for brain in brains:
            obj = brain.getObject()
            text_short = obj.getText(mimetype='text/plain')
            if len(text_short) > 200:
                text_short = text_short[:200]
            img = obj.getImage()
            items.append({
                    'id': brain.UID,
                    'title': brain.Title,
                    'text_short': text_short,
                    'description': brain.Description,
                    'image_url': img and img.absolute_url() or '',
                    'categories': brain.Subject,
                    'text': self.cdata(obj.getText() or ' '),
                    'url': brain.getURL(),
                    'datumvon': self.convert_date(brain.effective),
                    'datumbis': self.convert_date(brain.expires)})

        return items
