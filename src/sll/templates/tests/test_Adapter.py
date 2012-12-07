from sll.templates.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_ITopPageMainFeed(self):
        from sll.templates.interfaces import IAdapter
        from sll.templates.interfaces import ITopPageMainFeed
        root = IAdapter(self.portal)
        self.assertEqual(root.get_feed_number(ITopPageMainFeed), 3)

    def test_INewsFeed(self):
        from sll.templates.interfaces import IAdapter
        from sll.templates.interfaces import INewsFeed
        root = IAdapter(self.portal)
        self.assertEqual(root.get_feed_number(INewsFeed), 3)

    def test_IEventFeed(self):
        from sll.templates.interfaces import IAdapter
        from sll.templates.interfaces import IEventFeed
        root = IAdapter(self.portal)
        self.assertEqual(root.get_feed_number(IEventFeed), 3)

    def test_IFolderFeed(self):
        from sll.templates.interfaces import IAdapter
        from sll.templates.interfaces import IFolderFeed
        root = IAdapter(self.portal)
        self.assertEqual(root.get_feed_number(IFolderFeed), 4)

    def test_IFolderFeed__hasattr(self):
        from sll.templates.interfaces import IAdapter
        from sll.templates.interfaces import IFolderFeed
        setattr(self.portal, 'folder_feed_number', 10)
        root = IAdapter(self.portal)
        self.assertEqual(root.get_feed_number(IFolderFeed), 10)

    def test_not_correct_interface(self):
        from sll.templates.interfaces import IAdapter
        from zope.interface import Interface
        root = IAdapter(self.portal)
        with self.assertRaises(ValueError):
            root.get_feed_number(Interface)
