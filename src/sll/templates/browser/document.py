from Products.ATContentTypes.interfaces.document import IATDocument
from five import grok
from sll.templates.browser.interfaces import ISllTemplatesLayer


class View(grok.View):

    grok.context(IATDocument)
    grok.layer(ISllTemplatesLayer)
    grok.require('zope2.View')
    grok.name('sll-view')

    def image(self):
        return self.context.getField('leadImage').tag(self.context)

    def text(self):
        return self.context.CookedBody()
