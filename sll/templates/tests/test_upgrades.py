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
