from Products.CMFCore.utils import getToolByName
from sll.templates.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_is_package_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('sll.templates'))

    def test_browserlayer(self):
        from sll.templates.browser.interfaces import ISllTemplatesLayer
        from plone.browserlayer import utils
        self.failUnless(ISllTemplatesLayer in utils.registered_layers())

    def test_actions__object_buttons__feed_to_top__title(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        action = getattr(object_buttons, 'feed_to_top')
        self.assertEqual(action.title, 'Feed to Top')

    def test_actions__object_buttons__feed_to_top__description(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        action = getattr(object_buttons, 'feed_to_top')
        self.assertEqual(action.description, 'Make feedable to top page.')

    def test_actions__object_buttons__feed_to_top__url_expr(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        action = getattr(object_buttons, 'feed_to_top')
        self.assertEqual(action.url_expr, 'string:${globals_view/getCurrentObjectUrl}/@@feed-to-top')

    def test_actions__object_buttons__feed_to_top__permissions(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        action = getattr(object_buttons, 'feed_to_top')
        self.assertEqual(action.permissions, ('Manage portal',))

    def test_actions__object_buttons__feed_to_top__visible(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        action = getattr(object_buttons, 'feed_to_top')
        self.assertTrue(action.visible)

    def test_actions__object_buttons__unfeed_from_top__title(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        action = getattr(object_buttons, 'unfeed_from_top')
        self.assertEqual(action.title, 'Unfeed from Top')

    def test_actions__object_buttons__unfeed_from_top__description(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        action = getattr(object_buttons, 'unfeed_from_top')
        self.assertEqual(action.description, 'Make unfeedable from top page.')

    def test_actions__object_buttons__unfeed_from_top__url_expr(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        action = getattr(object_buttons, 'unfeed_from_top')
        self.assertEqual(action.url_expr, 'string:${globals_view/getCurrentObjectUrl}/@@unfeed-from-top')

    def test_actions__object_buttons__unfeed_from_top__permissions(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        action = getattr(object_buttons, 'unfeed_from_top')
        self.assertEqual(action.permissions, ('Manage portal',))

    def test_actions__object_buttons__unfeed_from_top__visible(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        action = getattr(object_buttons, 'unfeed_from_top')
        self.assertTrue(action.visible)

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(
            setup.getVersionForProfile('profile-sll.templates:default'),
            u'1'
        )

    def test_uninstall__package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['sll.templates'])
        self.failIf(installer.isProductInstalled('sll.templates'))

    def t4est_uninstall__browserlayer(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['sll.templates'])
        from sll.templates.browser.interfaces import ISllTemplatesLayer
        from plone.browserlayer import utils
        self.failIf(ISllTemplatesLayer in utils.registered_layers())
