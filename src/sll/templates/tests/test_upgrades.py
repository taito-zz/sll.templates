from Products.CMFCore.utils import getToolByName
from sll.templates.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone upgrades."""

    def setUp(self):
        self.portal = self.layer['portal']
        from plone.app.testing import TEST_USER_ID
        from plone.app.testing import setRoles
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_upgrades_1_to_2(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('Document')
        ctype.manage_changeProperties(view_methods=('document_view', ))
        self.assertEqual(
            ctype.getProperty('view_methods'),
            (
                'document_view',
            )
        )

        from sll.templates.upgrades import upgrade_1_to_2
        upgrade_1_to_2(self.portal)

        self.assertEqual(
            ctype.getProperty('view_methods'),
            (
                'document_view',
                'sll-view',
                'monthly-supporter',
            )
        )

    def test_update_actions(self):

        permission = "sll.templates: Manage feed for top"
        self.portal.manage_permission(permission, roles=['Manager'])
        roles = [
            item['name'] for item in self.portal.rolesOfPermission(
                permission
            ) if item['selected'] == 'SELECTED'
        ]
        roles.sort()
        self.assertEqual(
            roles,
            [
                'Manager',
            ]
        )
        self.assertEqual(
            self.portal.acquiredRolesAreUsedBy(permission),
            ''
        )

        permission = "sll.templates: Manage feed for micro site"
        self.portal.manage_permission(permission, roles=['Manager'])
        roles = [
            item['name'] for item in self.portal.rolesOfPermission(
                permission
            ) if item['selected'] == 'SELECTED'
        ]
        roles.sort()
        self.assertEqual(
            roles,
            [
                'Manager',
            ]
        )
        self.assertEqual(
            self.portal.acquiredRolesAreUsedBy(permission),
            ''
        )

        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        object_buttons.manage_delObjects(ids=['feed_to_microsite', 'unfeed_from_microsite'])
        self.assertFalse(hasattr(object_buttons, 'feed_to_microsite'))
        self.assertFalse(hasattr(object_buttons, 'unfeed_from_microsite'))

        from sll.templates.upgrades import update_actions
        update_actions(self.portal)

        permission = "sll.templates: Manage feed for top"
        roles = [
            item['name'] for item in self.portal.rolesOfPermission(
                permission
            ) if item['selected'] == 'SELECTED'
        ]
        roles.sort()
        self.assertEqual(
            roles,
            [
                'Manager',
                'Site Administrator',
            ]
        )
        self.assertEqual(
            self.portal.acquiredRolesAreUsedBy(permission),
            'CHECKED'
        )

        permission = "sll.templates: Manage feed for micro site"
        roles = [
            item['name'] for item in self.portal.rolesOfPermission(
                permission
            ) if item['selected'] == 'SELECTED'
        ]
        roles.sort()
        self.assertEqual(
            roles,
            [
                'Contributor',
                'Manager',
                'Site Administrator',
            ])
        self.assertEqual(
            self.portal.acquiredRolesAreUsedBy(permission),
            'CHECKED')

        self.assertTrue(hasattr(object_buttons, 'feed_to_microsite'))
        self.assertTrue(hasattr(object_buttons, 'unfeed_from_microsite'))
