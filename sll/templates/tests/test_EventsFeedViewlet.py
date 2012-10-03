from DateTime import DateTime
from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles
from sll.templates.tests.base import IntegrationTestCase


class TestEventsFeedViewlet(IntegrationTestCase):
    """TestCase for class: EventsFeedViewlet"""

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def create_instance(self):
        from sll.templates.browser.viewlet import EventsFeedViewlet
        from zope.publisher.browser import TestRequest
        return EventsFeedViewlet(self.portal, TestRequest(), None, None)

    def test_items__without_ATEvent(self):
        """Test method: items with no ATEvents"""
        instance = self.create_instance()
        self.assertEqual(instance.items(), [])

    def create_event(self, oid, start, end):
        event = self.portal[self.portal.invokeFactory('Event', oid,
            title=oid.capitalize(), startDate=start, endDate=end)]
        event.reindexObject()
        return event

    def test_items__with_ATEvent(self):
        """Test method: items with ATEvent."""
        instance = self.create_instance()
        now = DateTime()
        self.create_event('event1', now - 1, now + 1)
        self.create_event('event2', now + 1, now + 1)
        self.create_event('event3', now + 3, now + 4)
        self.create_event('event4', now + 2, now + 5)
        self.create_event('event5', now + 4, now + 5)
        items = [item['title'] for item in instance.items()]
        self.assertEqual(items, ['Event2', 'Event4', 'Event3'])
