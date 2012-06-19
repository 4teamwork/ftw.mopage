from ftw.testing.layer import ComponentRegistryLayer


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
