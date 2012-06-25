# -*- coding: utf-8 -*-
import unittest2 as unittest
from ftw.mopage.testing import FTW_MOPAGE_INTEGRATION_TESTING
from Products.CMFCore.utils import getToolByName


class InstallTestCase(unittest.TestCase):

    layer = FTW_MOPAGE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_installed(self):
        qi = getattr(self.portal, 'portal_quickinstaller')
        self.assertTrue(qi.isProductInstalled('ftw.mopage'))

    def test_propertiestool(self):

        ptool = getToolByName(self.portal, 'portal_properties')

        properties = ptool.mopage_properties

        self.assertTrue(hasattr(properties, 'title'))
        self.assertTrue(hasattr(properties, 'partner'))
        self.assertTrue(hasattr(properties, 'partnerid'))
        self.assertTrue(hasattr(properties, 'password'))
        self.assertTrue(hasattr(properties, 'export_dir'))
        self.assertTrue(hasattr(properties, 'importid_event'))
        self.assertTrue(hasattr(properties, 'importid_news'))
        self.assertTrue(hasattr(properties, 'importid_geolocation'))
