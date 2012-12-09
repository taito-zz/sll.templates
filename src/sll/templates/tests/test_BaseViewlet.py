from sll.templates.tests.base import IntegrationTestCase
from zope.publisher.browser import TestRequest

import mock


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def create_instance(self):
        from sll.templates.browser.viewlet import MainFeedViewlet
        return MainFeedViewlet(self.portal, TestRequest(), None, None)

    def test__image(self):
        instance = self.create_instance()
        item = mock.Mock()
        obj = item.getObject()
        obj.restrictedTraverse().return_value = 'HTML'
        self.assertEqual(instance._image(item), 'HTML')
