from Products.CMFCore.utils import getToolByName
from sll.basetheme.tests.test_setup import get_css_resource
from sll.templates.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_package_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('sll.templates'))

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
        self.assertEqual(action.permissions, ('sll.templates: Manage feed for top',))

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
        self.assertEqual(action.permissions, ('sll.templates: Manage feed for top',))

    def test_actions__object_buttons__unfeed_from_top__visible(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        action = getattr(object_buttons, 'unfeed_from_top')
        self.assertTrue(action.visible)

    def test_actions__object_buttons__feed_to_microsite__title(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        action = getattr(object_buttons, 'feed_to_microsite')
        self.assertEqual(action.title, 'Feed to micro site')

    def test_actions__object_buttons__feed_to_microsite__description(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        action = getattr(object_buttons, 'feed_to_microsite')
        self.assertEqual(action.description, 'Make feedable to micro site.')

    def test_actions__object_buttons__feed_to_microsite__url_expr(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        action = getattr(object_buttons, 'feed_to_microsite')
        self.assertEqual(action.url_expr, 'string:${globals_view/getCurrentObjectUrl}/@@feed-to-microsite')

    def test_actions__object_buttons__feed_to_microsite__permissions(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        action = getattr(object_buttons, 'feed_to_microsite')
        self.assertEqual(action.permissions, ('sll.templates: Manage feed for micro site',))

    def test_actions__object_buttons__feed_to_microsite__visible(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        action = getattr(object_buttons, 'feed_to_microsite')
        self.assertTrue(action.visible)

    def test_actions__object_buttons__unfeed_from_microsite__title(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        action = getattr(object_buttons, 'unfeed_from_microsite')
        self.assertEqual(action.title, 'Unfeed from micro site')

    def test_actions__object_buttons__unfeed_from_microsite__description(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        action = getattr(object_buttons, 'unfeed_from_microsite')
        self.assertEqual(action.description, 'Make unfeedable from micro site.')

    def test_actions__object_buttons__unfeed_from_microsite__url_expr(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        action = getattr(object_buttons, 'unfeed_from_microsite')
        self.assertEqual(action.url_expr, 'string:${globals_view/getCurrentObjectUrl}/@@unfeed-from-microsite')

    def test_actions__object_buttons__unfeed_from_microsite__permissions(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        action = getattr(object_buttons, 'unfeed_from_microsite')
        self.assertEqual(action.permissions, ('sll.templates: Manage feed for micro site',))

    def test_actions__object_buttons__unfeed_from_microsite__visible(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        action = getattr(object_buttons, 'unfeed_from_microsite')
        self.assertTrue(action.visible)

    def test_browserlayer(self):
        from sll.templates.browser.interfaces import ISllTemplatesLayer
        from plone.browserlayer import utils
        self.failUnless(ISllTemplatesLayer in utils.registered_layers())

    def test_cssregistry__sll_basetheme_main__applyPrefix(self):
        resource = get_css_resource(self.portal, '++resource++sll.templates/css/main.css')
        self.assertTrue(resource.getApplyPrefix())

    def test_cssregistry__sll_basetheme_main__authenticated(self):
        resource = get_css_resource(self.portal, '++resource++sll.templates/css/main.css')
        self.assertFalse(resource.getAuthenticated())

    def test_cssregistry__sll_basetheme_main__compression(self):
        resource = get_css_resource(self.portal, '++resource++sll.templates/css/main.css')
        self.assertEqual(resource.getCompression(), 'safe')

    def test_cssregistry__sll_basetheme_main__conditionalcomment(self):
        resource = get_css_resource(self.portal, '++resource++sll.templates/css/main.css')
        self.assertEqual(resource.getConditionalcomment(), '')

    def test_cssregistry__sll_basetheme_main__cookable(self):
        resource = get_css_resource(self.portal, '++resource++sll.templates/css/main.css')
        self.assertTrue(resource.getCookable())

    def test_cssregistry__sll_basetheme_main__enabled(self):
        resource = get_css_resource(self.portal, '++resource++sll.templates/css/main.css')
        self.assertTrue(resource.getEnabled())

    def test_cssregistry__sll_basetheme_main__expression(self):
        resource = get_css_resource(self.portal, '++resource++sll.templates/css/main.css')
        self.assertEqual(resource.getExpression(), '')

    def test_cssregistry__sll_basetheme_main__media(self):
        resource = get_css_resource(self.portal, '++resource++sll.templates/css/main.css')
        self.assertEqual(resource.getMedia(), 'screen')

    def test_cssregistry__sll_basetheme_main__rel(self):
        resource = get_css_resource(self.portal, '++resource++sll.templates/css/main.css')
        self.assertEqual(resource.getRel(), 'stylesheet')

    def test_cssregistry__sll_basetheme_main__rendering(self):
        resource = get_css_resource(self.portal, '++resource++sll.templates/css/main.css')
        self.assertEqual(resource.getRendering(), 'link')

    def test_cssregistry__sll_basetheme_main__title(self):
        resource = get_css_resource(self.portal, '++resource++sll.templates/css/main.css')
        self.assertIsNone(resource.getTitle())

    def test_matadata__dependency__PloneFormGen(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('PloneFormGen'))

    def test_metadata__dependency__collective_contentleadimage(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('collective.contentleadimage'))

    def test_metadata__dependency___collective_cropimage(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('collective.cropimage'))

    def test_metadata__dependency__sll_basetheme(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('sll.basetheme'))

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(
            setup.getVersionForProfile('profile-sll.templates:default'), u'7')

    def test_propertiestool_cli_properties__allowed_types(self):
        properties = getToolByName(self.portal, 'portal_properties')
        cli_properties = getattr(properties, 'cli_properties')
        self.assertEqual(cli_properties.getProperty('allowed_types'), ('Document', 'Event', 'FormFolder'))

    def get_records_proxy(self, interface):
        from plone.registry.interfaces import IRegistry
        from zope.component import getUtility
        return getUtility(IRegistry).forInterface(interface)

    def test_registry__records__IEventFeed(self):
        from sll.templates.interfaces import IEventFeed
        from plone.registry.recordsproxy import RecordsProxy
        self.assertIsInstance(self.get_records_proxy(IEventFeed), RecordsProxy)

    def test_registry__records__IFolderFeed__number(self):
        from sll.templates.interfaces import IFolderFeed
        self.assertEqual(self.get_records_proxy(IFolderFeed).number, 4)

    def test_registry__records__INewsFeed(self):
        from sll.templates.interfaces import INewsFeed
        from plone.registry.recordsproxy import RecordsProxy
        self.assertIsInstance(self.get_records_proxy(INewsFeed), RecordsProxy)

    def test_registry__records__ITopPageMainFeed(self):
        from sll.templates.interfaces import ITopPageMainFeed
        from plone.registry.recordsproxy import RecordsProxy
        self.assertIsInstance(self.get_records_proxy(ITopPageMainFeed), RecordsProxy)

    def test_rolemap__ManageFeedForTop__rolesOfPermission(self):
        permission = "sll.templates: Manage feed for top"
        roles = [item['name'] for item in self.portal.rolesOfPermission(
            permission) if item['selected'] == 'SELECTED']
        roles.sort()
        self.assertEqual(roles, [
            'Manager',
            'Site Administrator'])

    def test_rolemap__ManageFeedForTop__acquiredRolesAreUsedBy(self):
        permission = "sll.templates: Manage feed for top"
        self.assertEqual(self.portal.acquiredRolesAreUsedBy(permission),
            'CHECKED')

    def test_rolemap__ManageFeedForMicroSite__rolesOfPermission(self):
        permission = "sll.templates: Manage feed for micro site"
        roles = [item['name'] for item in self.portal.rolesOfPermission(
            permission) if item['selected'] == 'SELECTED']
        roles.sort()
        self.assertEqual(roles, [
            'Contributor',
            'Manager',
            'Site Administrator'])

    def test_rolemap__ManageFeedForMicroSite__acquiredRolesAreUsedBy(self):
        permission = "sll.templates: Manage feed for micro site"
        self.assertEqual(self.portal.acquiredRolesAreUsedBy(permission),
            'CHECKED')

    def test_rolemap__ManageMakingMicroSite__rolesOfPermission(self):
        permission = "sll.templates: Manage making micro site"
        roles = [item['name'] for item in self.portal.rolesOfPermission(
            permission) if item['selected'] == 'SELECTED']
        roles.sort()
        self.assertEqual(roles, [
            'Manager',
            'Site Administrator'])

    def test_rolemap__ManageMakingMicroSite__acquiredRolesAreUsedBy(self):
        permission = "sll.templates: Manage making micro site"
        self.assertEqual(self.portal.acquiredRolesAreUsedBy(permission),
            'CHECKED')

    def test_typeinfo__Document__view_method(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('Document')
        self.assertEqual(ctype.getProperty('view_methods'), (
            'document_view',
            'sll-view',
            'monthly-supporter'))

    def test_typeinfo__Folder__view_methods(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('Folder')
        self.assertEqual(ctype.getProperty('view_methods'), (
            'folder_summary_view',
            'folder_full_view',
            'folder_tabular_view',
            'atct_album_view',
            'folder_listing',
            'folder_leadimage_view',
            'sll-view'))

    def test_typeinfo__Plone_Site__immediate_view(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('Plone Site')
        self.assertEqual(ctype.getProperty('immediate_view'), 'sll-view')

    def test_typeinfo__Plone_Site__default_view(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('Plone Site')
        self.assertEqual(ctype.getProperty('default_view'), 'sll-view')

    def test_typeinfo__Plone_Site__view_method(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('Plone Site')
        self.assertEqual(ctype.getProperty('view_methods'), ('sll-view',))

    def test_viewlets__top_page_manager(self):
        from zope.component import getUtility
        from plone.app.viewletmanager.interfaces import IViewletSettingsStorage
        storage = getUtility(IViewletSettingsStorage)
        manager = "sll.templates.top.page.manager"
        skinname = "*"
        self.assertEqual(storage.getOrder(manager, skinname), (
            u'sll.templates.main.feed',
            u'sll.templates.news.feed',
            u'sll.templates.event.feed'))

    def test_uninstall__package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['sll.templates'])
        self.failIf(installer.isProductInstalled('sll.templates'))

    def test_uninstall__actions__object_buttons__feed_to_top(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['sll.templates'])
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        self.assertFalse(hasattr(object_buttons, 'feed_to_top'))

    def test_uninstall__actions__object_buttons__unfeed_from_top(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['sll.templates'])
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        self.assertFalse(hasattr(object_buttons, 'unfeed_from_top'))

    def test_uninstall__actions__object_buttons__feed_to_microsite(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['sll.templates'])
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        self.assertFalse(hasattr(object_buttons, 'feed_to_microsite'))

    def test_uninstall__actions__object_buttons__unfeed_from_microsite(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['sll.templates'])
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        self.assertFalse(hasattr(object_buttons, 'unfeed_from_microsite'))

    def test_uninstall__actions__object_buttons__make_microsite(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['sll.templates'])
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        self.assertFalse(hasattr(object_buttons, 'make_microsite'))

    def test_uninstall__actions__object_buttons__unmake_microsite(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['sll.templates'])
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        self.assertFalse(hasattr(object_buttons, 'unmake_microsite'))

    def test_uninstall__browserlayer(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['sll.templates'])
        from sll.templates.browser.interfaces import ISllTemplatesLayer
        from plone.browserlayer import utils
        self.failIf(ISllTemplatesLayer in utils.registered_layers())
