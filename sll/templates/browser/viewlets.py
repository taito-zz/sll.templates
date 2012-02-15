from Acquisition import aq_inner
from Acquisition import aq_parent
from Products.ATContentTypes.interfaces.document import IATDocument
from Products.ATContentTypes.interfaces.event import IATEvent
from Products.ATContentTypes.interfaces.news import IATNewsItem
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.contentlisting.interfaces import IContentListing
from plone.app.layout.viewlets.common import ViewletBase
from sll.policy.browser.interfaces import ITopPageFeed
from zope.component import getMultiAdapter
from plone.app.layout.navigation.interfaces import INavigationRoot


class FeedViewlet(ViewletBase):
    index = ViewPageTemplateFile('viewlets/feed.pt')

    def items(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        limit = 4
        query = {
            # 'object_provides': ITopPageFeed.__identifier__,
            'sort_on': 'modified',
            'sort_order': 'reverse',
            'sort_limit': limit,
            'path': '/'.join(context.getPhysicalPath()),
            'path': {
                'query': '/'.join(context.getPhysicalPath()),
            },
            'object_provides': [
                IATDocument.__identifier__,
                IATEvent.__identifier__,
                IATNewsItem.__identifier__,
            ],
        }
        if INavigationRoot.providedBy(context):
            limit = 3
            query['object_provides'] = ITopPageFeed.__identifier__
            query['sort_limit'] = limit
        res = catalog(query)[:limit]
        ploneview = getMultiAdapter(
            (context, self.request),
            name=u'plone'
        )
        items = [
            {
                'title': item.Title(),
                'url': item.getURL(),
                'parent': aq_parent(item.getObject()).Title(),
                'parent_url': aq_parent(item.getObject()).absolute_url(),
                'description': self.description(item),
                'object': item.getObject(),
                'image': self.image(item),
                'date': ploneview.toLocalizedTime(item.ModificationDate()),
            } for item in IContentListing(res)
        ]
        return items

    def description(self, item):
        desc = item.Description()
        length = 200
        if len(desc) > length:
            ploneview = getMultiAdapter(
                (self.context, self.request),
                name=u'plone'
            )
            desc = ploneview.cropText(desc, length)
        return desc

    def image(self, item):
        obj = item.getObject()
        field_name = 'image' if obj.getField('image') else 'leadImage'
        html = obj.restrictedTraverse('cropped-image')(field_name, 'feed')
        if html is None:
            portal_state = getMultiAdapter(
                (self.context, self.request),
                name=u'plone_portal_state'
            )
            image_url = '{0}/++theme++sll.theme/images/feed-fallback.png'.format(portal_state.portal_url())
            html = '<div class="crop" style="width:170px;height:150px;">'
            html += '<img src="{0}" alt="{1}" title="{1}" />'.format(
                image_url,
                item.Title()
            )
            html += '</div>'
        return html


class NewsEventsFeedViewlet(ViewletBase):
    index = ViewPageTemplateFile('viewlets/news_events_feed.pt')


class SimpleFeedViewlet(ViewletBase):
    index = ViewPageTemplateFile('viewlets/simple_feed.pt')

    def feeds(self, identifier, limit=3):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        query = {
            'object_provides': identifier,
            'sort_on': 'modified',
            'sort_order': 'reverse',
            'sort_limit': limit,
        }
        res = catalog(query)[:limit]
        ploneview = getMultiAdapter(
            (context, self.request),
            name=u'plone'
        )
        items = [
            {
                'title': item.Title(),
                'url': item.getURL(),
                'parent': aq_parent(item.getObject()).Title(),
                'parent_url': aq_parent(item.getObject()).absolute_url(),
                'date': ploneview.toLocalizedTime(item.ModificationDate()),
            } for item in IContentListing(res)
        ]
        return items


class NewsFeedViewlet(SimpleFeedViewlet):

    def items(self):
        return self.feeds(IATNewsItem.__identifier__)


class EventsFeedViewlet(SimpleFeedViewlet):

    def items(self):
        return self.feeds(IATEvent.__identifier__)
