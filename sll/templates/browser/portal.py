from five import grok
from sll.templates.browser.interfaces import ISllTemplatesLayer
from plone.app.layout.navigation.interfaces import INavigationRoot


class View(grok.View):

    grok.context(INavigationRoot)
    grok.layer(ISllTemplatesLayer)
    grok.require('zope2.View')
    grok.name('sll-view')
