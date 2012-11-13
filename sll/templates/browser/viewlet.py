from Acquisition import aq_inner
from Acquisition import aq_parent
from DateTime import DateTime
from Products.ATContentTypes.interfaces.event import IATEvent
from Products.CMFCore.utils import getToolByName
from collective.searchevent.browser.viewlet import SearchEventResultsViewlet
from collective.searchevent.interfaces import IItemDateTime
from five import grok
from plone.app.contentlisting.interfaces import IContentListing
from plone.app.layout.navigation.interfaces import INavigationRoot
from sll.templates.browser.interfaces import IEventsFeedViewletManager
from sll.templates.browser.interfaces import ISllTemplatesLayer


grok.templatedir('viewlets')


class SLLSearchEventResultsViewlet(SearchEventResultsViewlet):
    grok.layer(ISllTemplatesLayer)
    grok.template('results')

    def parent(self, item):
        return aq_parent(aq_inner(item.getObject()))


class EventsFeedViewlet(grok.Viewlet):
    grok.context(INavigationRoot)
    grok.layer(ISllTemplatesLayer)
    grok.name('sll.events.feed')
    grok.require('zope2.View')
    grok.template('event-feed')
    grok.viewletmanager(IEventsFeedViewletManager)

    def items(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        now = DateTime()
        query = {
            'object_provides': IATEvent.__identifier__,
            'path': '/'.join(context.getPhysicalPath()),
            'sort_limit': 3,
            'sort_on': 'start',
            'start': {
                'query': [now, ],
                'range': 'min',
            },
        }
        items = []
        for item in IContentListing(catalog(query)):
            parent = aq_parent(aq_inner(item.getObject()))
            items.append({
                'datetime': self._datetime(item),
                'description': item.Description(),
                'parent_description': parent.Description(),
                'parent_title': parent.Title(),
                'parent_url': parent.absolute_url(),
                'title': item.Title(),
                'url': item.getURL(),
            })
        return items

    def _datetime(self, item):
        return IItemDateTime(item)()
