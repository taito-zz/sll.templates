from sll.templates.tests.base import IntegrationTestCase

import mock


class TestFeedViewlet(IntegrationTestCase):
    """TestCase testing FeedViewlet class."""

    def setUp(self):
        self.portal = self.layer['portal']

    def createViewlet(self):
        from sll.templates.browser.viewlets import FeedViewlet
        from zope.publisher.browser import TestRequest
        return FeedViewlet(self.portal, TestRequest(), None, None)

    def test_viewlet__subclass(self):
        from sll.templates.browser.viewlets import FeedViewlet
        from plone.app.layout.viewlets.common import ViewletBase
        self.assertTrue(issubclass(FeedViewlet, ViewletBase))

    def test_viewlet__instance(self):
        from sll.templates.browser.viewlets import FeedViewlet
        viewlet = self.createViewlet()
        self.assertTrue(isinstance(viewlet, FeedViewlet))

    @mock.patch('sll.templates.browser.viewlets.getMultiAdapter')
    def test_viewlet__description(self, getMultiAdapter):
        viewlet = self.createViewlet()
        item = mock.Mock()
        desc = 'AAA ' * 51
        item.Description.return_value = desc
        viewlet.description(item)
        getMultiAdapter().cropText.assert_called_with(desc, 200)

    @mock.patch('sll.templates.browser.viewlets.getMultiAdapter')
    def test_viewlet__image(self, getMultiAdapter):
        viewlet = self.createViewlet()
        item = mock.Mock()
        item.getObject().restrictedTraverse().return_value = None
        getMultiAdapter().portal_url.return_value = 'URL'
        item.Title.return_value = 'TITLE'
        self.assertEqual(
            viewlet.image(item),
            '<div class="crop" style="width:170px;height:150px;"><img src="URL/++theme++sll.theme/images/feed-fallback.png" alt="TITLE" title="TITLE" /></div>'
        )

    @mock.patch('sll.templates.browser.viewlets.getMultiAdapter')
    def test_viewlet__image_html_not_None(self, getMultiAdapter):
        viewlet = self.createViewlet()
        item = mock.Mock()
        item.getObject().restrictedTraverse().return_value = '<html>'
        getMultiAdapter().portal_url.return_value = 'URL'
        item.Title.return_value = 'TITLE'
        self.assertEqual(
            viewlet.image(item),
            '<html>'
        )
