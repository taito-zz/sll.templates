from five import grok
from plone.app.layout.navigation.interfaces import INavigationRoot
from sll.templates.browser.interfaces import ISllTemplatesLayer


class View(grok.View):

    grok.context(INavigationRoot)
    grok.layer(ISllTemplatesLayer)
    grok.require('zope2.View')
    grok.name('sll-view')
