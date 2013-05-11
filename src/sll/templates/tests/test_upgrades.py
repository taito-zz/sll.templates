from sll.templates.tests.base import IntegrationTestCase

import mock


class TestCase(IntegrationTestCase):
    """TestCase for Plone upgrades."""

    @mock.patch('sll.templates.upgrades.reimport_profile')
    def test_reimport_registry(self, reimport_profile):
        from sll.templates.upgrades import reimport_registry
        reimport_registry(self.portal)
        reimport_profile.assert_called_with(self.portal, 'profile-sll.templates:default', 'plone.app.registry')

    @mock.patch('sll.templates.upgrades.reimport_profile')
    def test_reimport_viewlets(self, reimport_profile):
        from sll.templates.upgrades import reimport_viewlets
        reimport_viewlets(self.portal)
        reimport_profile.assert_called_with(self.portal, 'profile-sll.templates:default', 'viewlets')

    @mock.patch('sll.templates.upgrades.reimport_profile')
    def test_reimport_cssregistry(self, reimport_profile):
        from sll.templates.upgrades import reimport_cssregistry
        reimport_cssregistry(self.portal)
        reimport_profile.assert_called_with(self.portal, 'profile-sll.templates:default', 'cssregistry')
