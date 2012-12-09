from Acquisition import aq_inner
from Acquisition import aq_parent
from DateTime import DateTime
from Products.ATContentTypes.interfaces import IATDocument
from Products.ATContentTypes.interfaces import IATEvent
from Products.ATContentTypes.interfaces import IATFolder
from Products.ATContentTypes.interfaces import IATNewsItem
from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot
from Products.PloneFormGen.interfaces import IPloneFormGenForm
from abita.adapter.interfaces import IBaseAdapter
from five import grok
from plone.app.layout.navigation.interfaces import INavigationRoot
from plone.app.viewletmanager.manager import OrderedViewletManager
from plone.memoize import view
from plone.registry.interfaces import IRegistry
from sll.templates.browser.interfaces import IMicroSiteFeed
from sll.templates.browser.interfaces import ISllTemplatesLayer
from sll.templates.browser.interfaces import ITopPageFeed
from sll.templates.interfaces import IAdapter
from sll.templates.interfaces import IEventFeed
from sll.templates.interfaces import IFolderFeed
from sll.templates.interfaces import INewsFeed
from sll.templates.interfaces import ITopPageMainFeed
from zope.component import getMultiAdapter
from zope.component import getUtility


grok.templatedir('viewlets')


class BaseViewletManager(OrderedViewletManager, grok.ViewletManager):
    """Base class for viewlet manager"""
    grok.baseclass()
    grok.layer(ISllTemplatesLayer)


class TopPageViewletManager(BaseViewletManager):
    """Viewlet manager for top page"""
    grok.context(INavigationRoot)
    grok.name('sll.templates.top.page.manager')


class BaseViewlet(grok.Viewlet):
    """Base class for viewlet"""
    grok.baseclass()
    grok.layer(ISllTemplatesLayer)
    grok.require('zope2.View')

    interface = ITopPageMainFeed

    def _description(self, item):
        desc = item.Description()
        length = 200
        if len(desc) > length:
            ploneview = getMultiAdapter(
                (self.context, self.request),
                name=u'plone'
            )
            desc = ploneview.cropText(desc, length)
        return desc

    def _image(self, item):
        obj = item.getObject()
        field_name = 'image' if obj.getField('image') else 'leadImage'
        html = obj.restrictedTraverse('cropped-image')(field_name, 'feed')
        if html is None:
            portal_state = getMultiAdapter(
                (self.context, self.request),
                name=u'plone_portal_state'
            )
            image_url = '{}/++resource++sll.templates/images/feed-fallback.png'.format(portal_state.portal_url())
            html = '<div class="crop" style="width:170px;height:150px;">'
            html += '<img src="{0}" alt="{1}" title="{1}" />'.format(
                image_url,
                item.Title()
            )
            html += '</div>'
        return html

    def _items(self, **query):
        adapter = IAdapter(self.context)
        sort_limit = adapter.get_feed_number(self.interface)
        if sort_limit:
            query['sort_limit'] = sort_limit
        base = IBaseAdapter(self.context)
        res = []
        for item in base.get_content_listing(**query):
            obj = item.getObject()
            if not isinstance(self, BaseNewsEventFeedViewlet) or not ITopPageFeed.providedBy(obj):
                parent = aq_parent(aq_inner(obj))
                res.append({
                    'title': item.Title(),
                    'url': item.getURL(),
                    'parent_title': parent.Title(),
                    'parent_url': parent.absolute_url(),
                    'date': self._date(item),
                    'image': self._image(item),
                    'description': self._description(item),
                })
        if sort_limit:
            return res[:sort_limit]
        return res

    def _date(self, item):
        base = IBaseAdapter(self.context)
        localized_time = base.ulocalized_time()
        if self.interface == IEventFeed:
            start = item.start
            end = item.end
            start_dt = localized_time(start, long_format=True, context=self.context)
            if start.Date() == end.Date():
                if start == end:
                    dt = start_dt
                else:
                    end_time = localized_time(end, time_only=True)
                    dt = u'{} - {}'.format(start_dt, end_time)
            else:
                if start.h_24() == start.minute() == end.h_24() == end.minute() == 0:
                    start_dt = localized_time(start, long_format=False, context=self.context)
                    end_dt = localized_time(end, long_format=False, context=self.context)
                else:
                    end_dt = localized_time(end, long_format=True, context=self.context)
                dt = u'{} - {}'.format(start_dt, end_dt)
            return dt
        else:
            return localized_time(item.modified, long_format=False, context=self.context)


class BaseTopPageFeedViewlet(BaseViewlet):
    """Base class for feed viewlet for TopPageViewletManager"""
    grok.baseclass()
    grok.context(INavigationRoot)
    grok.viewletmanager(TopPageViewletManager)


class MainFeedViewlet(BaseTopPageFeedViewlet):
    """Viewlet class for main feed which has cropped images"""
    grok.name('sll.templates.main.feed')
    grok.template('main-feed')

    def items(self):
        query = {
            'sort_on': 'modified',
            'sort_order': 'descending',
        }
        if IPloneSiteRoot.providedBy(self.context):
            query['object_provides'] = ITopPageFeed.__identifier__
        else:
            query['object_provides'] = IMicroSiteFeed.__identifier__
        return self._items(**query)


class BaseNewsEventFeedViewlet(BaseTopPageFeedViewlet):
    """Base class for NewsViewlet and EventViewlet"""
    grok.baseclass()
    grok.template('event-news-feed')

    @view.memoize
    def records(self):
        return getUtility(IRegistry).forInterface(self.interface)

    @view.memoize
    def link(self):
        base = IBaseAdapter(self.context)
        path = '{}/{}'.format(
            '/'.join(self.context.getPhysicalPath()),
            self.records().path)
        query = {'path': {'query': path, 'depth': 0}}
        brain = base.get_brain(**query)
        if brain:
            return {
                'title': brain.Title,
                'url': brain.getURL(),
            }


class NewsFeedViewlet(BaseNewsEventFeedViewlet):
    """Viewlet class for news feed"""
    grok.name('sll.templates.news.feed')

    interface = INewsFeed

    def items(self):
        query = {
            'object_provides': IATNewsItem.__identifier__,
            'sort_on': 'modified',
            'sort_order': 'descending',
        }
        return self._items(**query)


class EventFeedViewlet(BaseNewsEventFeedViewlet):
    """Viewlet class for event feed"""
    grok.name('sll.templates.event.feed')

    interface = IEventFeed

    def items(self):
        now = DateTime()
        query = {
            'object_provides': IATEvent.__identifier__,
            'sort_on': 'start',
            'start': {
                'query': [now, ],
                'range': 'min',
            },
        }
        return self._items(**query)


class FolderViewletManager(BaseViewletManager):
    """Viewlet manager for folder"""
    grok.context(IATFolder)
    grok.name('sll.templates.folder.manager')


class FolderFeedViewlet(BaseViewlet):
    """Viewlet for folder feed"""
    grok.context(IATFolder)
    grok.name('sll.templates.folder.feed')
    grok.template('main-feed')
    grok.viewletmanager(FolderViewletManager)

    interface = IFolderFeed

    def items(self):
        query = {
            'sort_on': 'modified',
            'sort_order': 'descending',
            'object_provides': [
                IATDocument.__identifier__,
                IATEvent.__identifier__,
                IATNewsItem.__identifier__,
                IPloneFormGenForm.__identifier__]
        }
        return self._items(**query)


# class SLLSearchEventResultsViewlet(SearchEventResultsViewlet):
#     grok.layer(ISllTemplatesLayer)
#     grok.template('results')

#     def parent(self, item):
#         return aq_parent(aq_inner(item.getObject()))
