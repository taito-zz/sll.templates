from Products.CMFCore.utils import getToolByName
from sll.templates.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = getToolByName(self.portal, 'portal_quickinstaller')

    def test_is_sll_theme_installed(self):
        self.failUnless(self.installer.isProductInstalled('sll.templates'))

    def test_is_plone_app_theming_installed(self):
        self.failUnless(self.installer.isProductInstalled('plone.app.theming'))

    def test_uninstall(self):
        self.installer.uninstallProducts(['sll.templates'])
        self.failIf(self.installer.isProductInstalled('sll.templates'))

    def test_browserlayer(self):
        from sll.templates.browser.interfaces import ISllTemplatesLayer
        from plone.browserlayer import utils
        self.failUnless(ISllTemplatesLayer in utils.registered_layers())
