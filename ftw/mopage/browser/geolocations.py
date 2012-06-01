from ftw.mopage.browser.news import ExportNews
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName


class ExportGeoLocations(ExportNews):

    filename = 'geolocations'
    template = ViewPageTemplateFile('geolocations.xml')

    def items(self):
        catalog = getToolByName(self.context, 'portal_catalog')
        brains = catalog(portal_type='OrgUnit', review_state="published")
        items = []
        for brain in brains:
            obj = brain.getObject()
            opening = ''
            if obj.getShow_opening_hours():
                opening = obj.getOpening_hours().replace('\n', '<br />')
            directions = obj.getDirections().replace('\n', '<br />')
            img = obj.getImage()

            latitude, longitude = obj.getRawGeolocation()

            has_address = obj.getAddress() and obj.getZip() and obj.getCity()

            if has_address or (latitude and longitude):
                items.append({
                    'id': brain.UID,
                    'title': brain.Title,
                    'street': obj.getAddress(),
                    'modified': self.convert_date(brain.modified),
                    'plz': obj.getZip(),
                    'place': obj.getCity(),
                    'country': 'ch',
                    'categories': brain.Subject,
                    'phone': obj.getPhone_office(),
                    'email': obj.getEmail(),
                    'opening': self.cdata(self.make_links_absolute(obj,opening)),
                    'text_short': '', # => no text
                    'company': obj.getAddressTitle(),
                    'firstname': '', # => no firstname
                    'lastname': '', # => no lastname
                    'mobile': obj.getPhone_mobile(),
                    'fax': obj.getFax(),
                    'description': brain.Description,
                    'image_url': img and img.absolute_url() or '',
                    'rubriken':  [rubrik.Title() for rubrik
                                                 in obj.getClassification()],
                    'anfahrt': self.cdata(self.make_links_absolute(obj,directions)),
                    'url': brain.getURL(),
                    'longitude': longitude,
                    'latitude': latitude,
                    })
        return items
