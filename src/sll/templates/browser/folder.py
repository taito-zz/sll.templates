from Products.ATContentTypes.interfaces.folder import IATFolder
from five import grok
from sll.templates.browser.interfaces import ISllTemplatesLayer


class View(grok.View):

    grok.context(IATFolder)
    grok.layer(ISllTemplatesLayer)
    grok.name('sll-view')
    grok.require('zope2.View')
