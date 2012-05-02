from Acquisition import aq_inner
from Acquisition import aq_parent
from Products.ATContentTypes.interfaces.document import IATDocument
from Products.ATContentTypes.interfaces.event import IATEvent
from Products.ATContentTypes.interfaces.folder import IATFolder
from Products.ATContentTypes.interfaces.news import IATNewsItem
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.contentlisting.interfaces import IContentListing
from plone.app.layout.navigation.interfaces import INavigationRoot
from plone.app.layout.viewlets.common import PathBarViewlet
from plone.app.layout.viewlets.common import ViewletBase
from sll.templates.browser.interfaces import ITopPageFeed
from zope.component import getMultiAdapter


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


class PathBarViewlet(PathBarViewlet):
    index = ViewPageTemplateFile('viewlets/path_bar.pt')


class SiteActionsViewlet(ViewletBase):
    index = ViewPageTemplateFile('viewlets/site_actions.pt')

    def update(self):
        self.site_actions = self.items()

    def items(self):
        context = aq_inner(self.context)
        portal_state = getMultiAdapter((context, self.request), name="plone_portal_state")
        catalog = getToolByName(context, 'portal_catalog')
        query = {
            'object_provides': IATFolder.__identifier__,
            'path': {
                'query': portal_state.navigation_root_path(),
                'depth': 1,
            },
            'sort_on': 'getObjPositionInParent',
            'Subject': 'actions',
        }
        res = catalog(query)
        return IContentListing(res)


class FooterViewlet(ViewletBase):
    index = ViewPageTemplateFile('viewlets/footer.pt')


class FooterInfoViewlet(ViewletBase):
    index = ViewPageTemplateFile('viewlets/footer_info.pt')

    def items(self):
        context = aq_inner(self.context)
        portal_state = getMultiAdapter((context, self.request), name="plone_portal_state")
        catalog = getToolByName(context, 'portal_catalog')
        query = {
            'object_provides': IATDocument.__identifier__,
            'path': {
                'query': '{0}/info'.format('/'.join(portal_state.portal().getPhysicalPath())),
            },
            'sort_on': 'getObjPositionInParent',
        }
        res = catalog(query)
        if res:
            width = '{0}'.format(100 / len(res))[:2]
            self.width = 'width: {0}%'.format(width)
            items = [
                {
                    'title': item.Title(),
                    'url': item.getURL(),
                    'description': item.Description(),
                    'text': item.getObject().CookedBody(),
                } for item in IContentListing(res)
            ]
            return items


class FooterSubfoldersViewlet(ViewletBase):
    index = ViewPageTemplateFile('viewlets/footer_subfolders.pt')

    def items(self):
        context = aq_inner(self.context)
        portal_state = getMultiAdapter((context, self.request), name="plone_portal_state")
        catalog = getToolByName(context, 'portal_catalog')
        query = {
            'object_provides': IATFolder.__identifier__,
            'path': {
                'query': portal_state.navigation_root_path(),
                'depth': 1,
            },
            'sort_on': 'getObjPositionInParent',
        }
        res = [brain for brain in catalog(query) if not brain.exclude_from_nav]
        ploneview = getMultiAdapter(
            (context, self.request),
            name=u'plone'
        )
        items = [
            {
                'title': item.Title(),
                'url': item.getURL(),
                'description': item.Description(),
                'subfolders': self.subfolders(item, catalog, ploneview),
            } for item in IContentListing(res)
        ]
        return items

    def subfolders(self, item, catalog, ploneview):
        query = {
            'object_provides': IATFolder.__identifier__,
            'path': {
                'query': item.getPath(),
                'depth': 1,
            },
            'sort_on': 'getObjPositionInParent',
        }
        res = [brain for brain in catalog(query) if not brain.exclude_from_nav]
        items = [
            {
                'title': item.Title(),
                'url': item.getURL(),
                'description': item.Description(),
            } for item in IContentListing(res)
        ]
        return items
