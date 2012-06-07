from Acquisition import aq_inner
from Acquisition import aq_parent
from collective.searchevent.browser.viewlet import SearchEventResultsViewlet
from five import grok
from sll.templates.browser.interfaces import ISllTemplatesLayer
from sll.templates.browser.interfaces import IEventsFeedViewletManager
from plone.app.layout.navigation.interfaces import INavigationRoot


grok.templatedir('viewlets')


class SLLSearchEventResultsViewlet(SearchEventResultsViewlet):
    grok.layer(ISllTemplatesLayer)
    grok.template('results')

    def results(self):
        items = []
        for item in super(SLLSearchEventResultsViewlet, self).results():
            parent = aq_parent(aq_inner(item.getObject()))
            items.append(
                {
                    'description': item.Description(),
                    'end': item.end,
                    'parent_description': parent.Description(),
                    'parent_title': parent.Title(),
                    'parent_url': parent.absolute_url(),
                    'start': item.start,
                    'title': item.Title(),
                    'url': item.getURL(),
                }
            )
        return items


class EventsFeedViewlet(SearchEventResultsViewlet):
    grok.context(INavigationRoot)
    grok.layer(ISllTemplatesLayer)
    grok.name('sll.events.feed')
    grok.require('zope2.View')
    grok.template('event-feed')
    grok.viewletmanager(IEventsFeedViewletManager)

    def results(self):
        items = []
        for item in super(EventsFeedViewlet, self).results(limit=3):
            parent = aq_parent(aq_inner(item.getObject()))
            items.append(
                {
                    'description': item.Description(),
                    'end': item.end,
                    'parent_description': parent.Description(),
                    'parent_title': parent.Title(),
                    'parent_url': parent.absolute_url(),
                    'start': item.start,
                    'title': item.Title(),
                    'url': item.getURL(),
                }
            )
        return items
