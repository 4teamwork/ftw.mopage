from xml.dom import minidom
from Products.CMFCore.utils import getToolByName
from ftw.mopage.interfaces import IMopageGeolocationXMLWriter, \
    IMopageNewsXMLWriter, IMopageEventXMLWriter
from zope.interface import implements


class BaseMopageXMLWriter(object):
    """ Used to generate a mopage xml
    """

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.data = None
        self.xml = None

    def set_base_xml(self):

        self.xml = minidom.Document()
        self.generate_header()

    def generate_xml(self, data):

        self.set_base_xml()
        self.data = data

    def generate_header(self):

        properties = getToolByName(self.context, 'portal_properties')
        properties = properties.mopage_properties

        header = self.xml.createElement('import')

        header.setAttribute('partner', properties.partner)
        header.setAttribute('partnerid', properties.partnerid)
        header.setAttribute('passwort', properties.password)
        header.setAttribute('importid', '1')

        self.xml.appendChild(header)

    def create_node(
        self, tag_name, parent_node, content='', allow_empty=False, **kwargs):
        """ Create a new minidom node
        """

        if not allow_empty and not content:
            return

        node = self.xml.createElement(tag_name)

        for key, value in kwargs.items():
            node.setAttribute(key, value)

        parent_node.appendChild(node)

        return node

    def get_item_node(self):

        item = self.createElement('item')
        item.setAttribute('suchbar', 1)
        item.setAttribute('status', 1)

        return item


class MopageGeolocationXMLWriter(BaseMopageXMLWriter):
    implements(IMopageGeolocationXMLWriter)

    def generate_xml(self, data):
        super(MopageGeolocationXMLWriter, self).generate_xml(data)

        if not self.data:
            return self.xml.toxml()

        for item in self.data:

            xml_node = self.get_item_node()
            xml_node.setAttribute(
                'mutationsdatum', self.data.get('mutationsdatum'))

            self.create_node('id', xml_node, self.data.get('id'))
            self.create_node('titel', xml_node, self.data.get('titel'))
            self.create_node('adresse', xml_node, self.data.get('adresse'))
            self.create_node('plz', xml_node, self.data.get('plz'))
            self.create_node('ort', xml_node, self.data.get('ort'))
            self.create_node('land_iso', xml_node, self.data.get('land_iso'))
            for rubrik in self.data.get('rubrik'):
                self.create_node('rubrik', xml_node, rubrik)
            self.create_node('telefon1', xml_node, self.data.get('telefon1'))
            self.create_node('email', xml_node, self.data.get('email'))
            self.create_node(
                'oeffnungszeiten', xml_node, self.data.get('oeffnungszeiten'))
            self.create_node(
                'textmobile', xml_node, self.data.get('textmobile'))
            self.create_node('url_web', xml_node, self.data.get('url_web'))
            self.create_node(
                'url_mobile', xml_node, self.data.get('url_mobile'))
            self.create_node('firma', xml_node, self.data.get('firma'))
            self.create_node('vorname', xml_node, self.data.get('vorname'))
            self.create_node('name', xml_node, self.data.get('name'))
            self.create_node('sex', xml_node, self.data.get('sex'))
            self.create_node('abteilung', xml_node, self.data.get('abteilung'))
            self.create_node('telefon2', xml_node, self.data.get('telefon2'))
            self.create_node('telefon3', xml_node, self.data.get('telefon3'))
            self.create_node('mobile', xml_node, self.data.get('mobile'))
            self.create_node('fax', xml_node, self.data.get('fax'))
            self.create_node(
                'adresse_zusatz', xml_node, self.data.get('adresse_zusatz'))
            self.create_node('land', xml_node, 'ch')
            self.create_node('textlead', xml_node, self.data.get('textlead'))
            self.create_node('url_bild', xml_node, self.data.get('url_bild'))
            self.create_node('oev', xml_node, self.data.get('oev'))
            self.create_node('longitude', xml_node, self.data.get('longitude'))
            self.create_node('latitude', xml_node, self.data.get('latitude'))
            self.create_node('text', xml_node, self.data.get('text'))

            self.xml.appendChild(xml_node)

        return self.xml.toxml()


class MopageNewsXMLWriter(BaseMopageXMLWriter):
    implements(IMopageNewsXMLWriter)

    def generate_xml(self, data):
        super(MopageNewsXMLWriter, self).generate_xml(data)

        if not self.data:
            return self.xml.toxml()

        for item in self.data:

            xml_node = self.get_item_node()
            xml_node.setAttribute('datumvon', self.data.get('datumvon'))
            xml_node.setAttribute(
                'mutationsdatum', self.data.get('mutationsdatum'))

            self.create_node('id', xml_node, self.data.get('id'))
            self.create_node('titel', xml_node, self.data.get('titel'))
            self.create_node(
                'textmobile', xml_node, self.data.get('textmobile'))
            self.create_node('textlead', xml_node, self.data.get('textlead'))
            self.create_node('url_bild', xml_node, self.data.get('url_bild'))
            for rubrik in self.data.get('rubrik'):
                self.create_node('rubrik', xml_node, rubrik)
            self.create_node('text', xml_node, self.data.get('text'))
            self.create_node('url_web', xml_node, self.data.get('url_web'))
            self.create_node(
                'url_mobile', xml_node, self.data.get('url_mobile'))

            self.xml.appendChild(xml_node)

        return self.xml.toxml()


class MopageEventXMLWriter(BaseMopageXMLWriter):
    implements(IMopageEventXMLWriter)

    def generate_xml(self, data):
        super(MopageEventXMLWriter, self).generate_xml(data)

        if not self.data:
            return self.xml.toxml()

        for item in self.data:

            xml_node = self.get_item_node()

            self.create_node('id', xml_node, self.data.get('id'))
            self.create_node('titel', xml_node, self.data.get('titel'))
            termin = self.create_node('termin', xml_node, allow_empty=True)
            termin.setAttribute('allday', self.data.get('allday'))
            self.create_node('von', termin, self.data.get('von'))
            self.create_node('bis', termin, self.data.get('bis'))
            xml_node.appendChild(termin)
            self.create_node(
                'referenzort', xml_node, self.data.get('referenzort'))
            self.create_node(
                'textmobile', xml_node, self.data.get('textmobile'))
            for rubrik in self.data.get('rubrik'):
                self.create_node('rubrik', xml_node, rubrik)
            self.create_node('textlead', xml_node, self.data.get('textlead'))
            self.create_node('url_bild', xml_node, self.data.get('url_bild'))
            self.create_node('url_web', xml_node, self.data.get('url_web'))
            self.create_node(
                'url_mobile', xml_node, self.data.get('url_mobile'))
            self.create_node('text', xml_node, self.data.get('text'))

            self.xml.appendChild(xml_node)

        return self.xml.toxml()
