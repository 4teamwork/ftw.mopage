from ftw.testing.layer import ComponentRegistryLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from zope.configuration import xmlconfig


class FtwMopageFunctionalLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        from ftw import mopage
        xmlconfig.file('configure.zcml', package=mopage,
                       context=configurationContext)

    def setUpPloneSite(self, portal):

        self.applyProfile(portal, 'ftw.mopage:default')

        from plone.app.testing import setRoles, TEST_USER_ID
        setRoles(portal, TEST_USER_ID, ['Member', 'Contributor', 'Editor'])


FTW_MOPAGE_FIXTURE = FtwMopageFunctionalLayer()
FTW_MOPAGE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(FTW_MOPAGE_FIXTURE, ), name="FtwMopage:Integration")


class FtwMopageZCMLLayer(ComponentRegistryLayer):
    """A layer which only sets up the zcml, but does not start a zope
    instance.
    """

    def setUp(self):
        super(FtwMopageZCMLLayer, self).setUp()
        import ftw.mopage
        self.load_zcml_file('test.zcml', ftw.mopage.tests)
        self.load_zcml_file('configure.zcml', ftw.mopage)


FTWMOPAGE_ZCML_LAYER = FtwMopageZCMLLayer()
