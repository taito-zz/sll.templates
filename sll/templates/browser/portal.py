from five import grok
from sll.templates.browser.interfaces import ISllTemplatesLayer
# from Products.CMFCore.interfaces._content import ISiteRoot
from plone.app.layout.navigation.interfaces import INavigationRoot


class View(grok.View):

    # grok.context(ISiteRoot)
    grok.context(INavigationRoot)
    grok.layer(ISllTemplatesLayer)
    grok.require('zope2.View')
    grok.name('sll-view')
