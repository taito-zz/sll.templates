from Acquisition import aq_inner
from Acquisition import aq_parent
from collective.searchevent.browser.viewlet import SearchEventResultsViewlet
# from collective.searchevent.browser.interfaces import ISearchEventResultsViewletManager
from five import grok
from sll.templates.browser.interfaces import ISllTemplatesLayer


grok.templatedir('viewlets')


class SearchEventResultsViewlet(SearchEventResultsViewlet):
    grok.template('results')
    # grok.viewletmanager(ISearchEventResultsViewletManager)
    grok.layer(ISllTemplatesLayer)

    def results(self):
        items = []
        for item in super(SearchEventResultsViewlet, self).results():
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
