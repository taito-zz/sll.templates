from Products.ATContentTypes.interfaces.document import IATDocument
from five import grok
from sll.templates.browser.interfaces import ISllTemplatesLayer


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
