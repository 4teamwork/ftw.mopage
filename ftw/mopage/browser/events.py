from ftw.mopage.browser.news import ExportNews
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName


class ExportEvents(ExportNews):

    filename = 'events'
    template = ViewPageTemplateFile('events.xml')

    def items(self):
        """Gets all events from catalog and prepares the
        attributes for the xml.
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        brains = catalog(portal_type='Event', review_state="published")
        items = []
        for brain in brains:
            obj = brain.getObject()
            items.append({
                    'id': brain.UID,
                    'title': brain.Title,
                    'effective': self.convert_date(brain.effective),
                    'allday': self.is_allday(brain.start, brain.end),
                    'start': self.convert_date(brain.start),
                    'end': self.convert_date(brain.end),
                    'place': '',#obj.getLocation(), => ist geolocation gemeint
                    'text': self.cdata(self.make_links_absolute(obj, obj.getText())),
                    'categories': obj.getEventType(),
                    'description': brain.Description,
                    'image_url': '', # => no image in event
                    'url': brain.getURL()})

        return items
