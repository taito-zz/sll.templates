from Acquisition import aq_inner
from Acquisition import aq_parent
from Products.ATContentTypes.interfaces.document import IATDocument
from collective.searchevent.browser.template import SearchResultsView
from five import grok
from sll.templates.browser.interfaces import ISllTemplatesLayer
from zope.interface import Interface


grok.templatedir('templates')


class MonthlySupporterView(grok.View):

    grok.context(IATDocument)
    grok.layer(ISllTemplatesLayer)
    grok.name('monthly-supporter')
    grok.require('zope2.View')
    grok.template('monthly-supporter')

    def image(self):
        return self.context.getField('leadImage').tag(self.context)

    def text(self):
        return self.context.CookedBody()


class SearchResultsView(grok.View, SearchResultsView):

    grok.context(Interface)
    grok.layer(ISllTemplatesLayer)
    grok.name('search-results')
    grok.require('zope2.View')
    grok.template('search-results')

    def results(self):
        items = []
        for item in super(SearchResultsView, self).results():
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
