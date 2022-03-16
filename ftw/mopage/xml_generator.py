from ftw.mopage import interfaces
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import safe_unicode
from xml.dom import minidom
from zope.interface import implements


class BaseMopageXMLGenerator(object):
    implements(interfaces.IMopageXMLGenerator)

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.data = None
        self.xml = None

    def generate_xml_string(self, data):
        return ''

    def _set_base_xml(self):
        """ Create a base xml with a default header
        """

        self.xml = minidom.Document()
        self._generate_header()

    def _generate_header(self):
        """ Generates the header for the xml file
        """

        properties = self._get_mopage_properties()

        header = self.xml.createElement('import')

        self._set_attribute(header, 'partner', properties.partner)
        self._set_attribute(header, 'partnerid', properties.partnerid)
        self._set_attribute(header, 'passwort', properties.password)
        self._set_attribute(header, 'importid', self._get_import_id())

        self.xml.appendChild(header)

    def _create_node(
        self, tag_name, parent_node, content='', allow_empty=False, **kwargs
    ):
        """ Create a new minidom node and append it to the parent node
        """

        if not allow_empty and not content:
            return

        node = self.xml.createElement(tag_name)

        for key, value in kwargs.items():
            self._set_attribute(node, key, self._convert_to_string(value))

        node.appendChild(self.xml.createCDATASection(
            self._convert_to_string(content)))

        parent_node.appendChild(node)

        return node

    def _convert_to_string(self, value):
        """ Convert the given value into a string
        """
        return safe_unicode(value)

    def _get_item_node(self):
        """ Return a node to create a new item
        """

        item = self.xml.createElement('item')
        self._set_attribute(item, 'suchbar', '1')
        self._set_attribute(item, 'status', '1')

        return item

    def _set_attribute(self, node, name, value):
        """ Set a attribute on a node
        """
        if not name or not value:
            return

        node.setAttribute(name, value)

    def _get_import_id(self):
        """ Return required importid attribute for the mopage export
        """
        return '1'

    def _get_mopage_properties(self):
        properties = getToolByName(self.context, 'portal_properties')
        return properties.mopage_properties


class MopageGeolocationXMLGenerator(BaseMopageXMLGenerator):
    implements(interfaces.IMopageGeolocationXMLGenerator)

    def generate_xml_string(self, data):

        self._set_base_xml()
        self.data = data

        for item in self.data:

            xml_node = self._get_item_node()
            self._set_attribute(
                xml_node, 'mutationsdatum', item.get('mutationsdatum'))
            self._create_node('id', xml_node, item.get('id'))
            self._create_node('titel', xml_node, item.get('titel'))
            self._create_node('adresse', xml_node, item.get('adresse'))
            self._create_node('plz', xml_node, item.get('plz'))
            self._create_node('ort', xml_node, item.get('ort'))
            self._create_node('land_iso', xml_node, item.get('land_iso'))
            for rubrik in item.get('rubrik', []):
                self._create_node('rubrik', xml_node, rubrik)
            self._create_node('telefon1', xml_node, item.get('telefon1'))
            self._create_node('email', xml_node, item.get('email'))
            self._create_node(
                'oeffnungszeiten', xml_node, item.get('oeffnungszeiten'),
            )
            self._create_node(
                'textmobile', xml_node, item.get('textmobile'))
            self._create_node('url_web', xml_node, item.get('url_web'))
            self._create_node(
                'url_mobile', xml_node, item.get('url_mobile'))
            self._create_node('firma', xml_node, item.get('firma'))
            self._create_node('vorname', xml_node, item.get('vorname'))
            self._create_node('name', xml_node, item.get('name'))
            self._create_node('sex', xml_node, item.get('sex'))
            self._create_node('abteilung', xml_node, item.get('abteilung'))
            self._create_node('telefon2', xml_node, item.get('telefon2'))
            self._create_node('telefon3', xml_node, item.get('telefon3'))
            self._create_node('mobile', xml_node, item.get('mobile'))
            self._create_node('fax', xml_node, item.get('fax'))
            self._create_node(
                'adresse_zusatz', xml_node, item.get('adresse_zusatz'))
            self._create_node('land', xml_node, 'ch')
            self._create_node('textlead', xml_node, item.get('textlead'))
            self._create_node('url_bild', xml_node, item.get('url_bild'))
            self._create_node('oev', xml_node, item.get('oev'))
            self._create_node('longitude', xml_node, item.get('longitude'))
            self._create_node('latitude', xml_node, item.get('latitude'))
            self._create_node('text', xml_node, item.get('text'))

            self.xml.firstChild.appendChild(xml_node)

        return self.xml.toxml(encoding='utf-8')

    def _get_import_id(self):
        return self._get_mopage_properties().importid_geolocation


class MopageNewsXMLGenerator(BaseMopageXMLGenerator):
    implements(interfaces.IMopageNewsXMLGenerator)

    def generate_xml_string(self, data):

        self._set_base_xml()
        self.data = data

        for item in self.data:

            xml_node = self._get_item_node()
            self._set_attribute(xml_node, 'datumvon', item.get('datumvon'))
            self._set_attribute(
                xml_node, 'mutationsdatum', item.get('mutationsdatum'))
            self._create_node('id', xml_node, item.get('id'))
            self._create_node('titel', xml_node, item.get('titel'))
            self._create_node(
                'textmobile', xml_node, item.get('textmobile'))
            self._create_node(
                'textlead', xml_node, item.get('textlead'))
            self._create_node('url_bild', xml_node, item.get('url_bild'))
            for rubrik in item.get('rubrik', []):
                self._create_node('rubrik', xml_node, rubrik)
            self._create_node('text', xml_node, item.get('text'))
            self._create_node('url_web', xml_node, item.get('url_web'))
            self._create_node(
                'url_mobile', xml_node, item.get('url_mobile'))

            self.xml.firstChild.appendChild(xml_node)

        return self.xml.toxml(encoding='utf-8')

    def _get_import_id(self):
        return self._get_mopage_properties().importid_news


class MopageEventXMLGenerator(BaseMopageXMLGenerator):
    implements(interfaces.IMopageEventXMLGenerator)

    def generate_xml_string(self, data):

        self._set_base_xml()
        self.data = data

        for item in self.data:

            xml_node = self._get_item_node()

            self._create_node('id', xml_node, item.get('id'))
            self._create_node('titel', xml_node, item.get('titel'))
            termin = self._create_node('termin', xml_node, allow_empty=True)
            self._set_attribute(termin, 'allday', str(item.get('allday')))
            self._create_node('von', termin, item.get('von'))
            self._create_node('bis', termin, item.get('bis'))
            xml_node.appendChild(termin)
            self._create_node(
                'referenzort', xml_node, item.get('referenzort'))
            self._create_node(
                'textmobile', xml_node, item.get('textmobile'))
            for rubrik in item.get('rubrik', []):
                self._create_node('rubrik', xml_node, rubrik)
            self._create_node(
                'textlead', xml_node, item.get('textlead'))
            self._create_node('url_bild', xml_node, item.get('url_bild'))
            self._create_node('url_web', xml_node, item.get('url_web'))
            self._create_node(
                'url_mobile', xml_node, item.get('url_mobile'))
            self._create_node('text', xml_node, item.get('text'))

            self.xml.firstChild.appendChild(xml_node)

        return self.xml.toxml(encoding='utf-8')

    def _get_import_id(self):
        return self._get_mopage_properties().importid_event
