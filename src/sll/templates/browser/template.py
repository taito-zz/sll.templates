from Products.ATContentTypes.interfaces import IATDocument
from Products.ATContentTypes.interfaces import IATFolder
from five import grok
from plone.app.layout.navigation.interfaces import INavigationRoot
from sll.templates.browser.interfaces import ISllTemplatesLayer


grok.templatedir('templates')


class BaseView(grok.View):
    """Base class for View"""
    grok.baseclass()
    grok.layer(ISllTemplatesLayer)
    grok.name('sll-view')
    grok.require('zope2.View')


class TopPageView(BaseView):
    """View class for site and micro site top page."""
    grok.context(INavigationRoot)
    grok.template('top-page')


class FolderView(BaseView):
    """View class for folder"""
    grok.context(IATFolder)
    grok.template('folder')


class BaseDocumentView(BaseView):
    grok.baseclass()
    grok.context(IATDocument)

    def image(self):
        return self.context.getField('leadImage').tag(self.context)

    def text(self):
        return self.context.CookedBody()


class DocumentView(BaseDocumentView):
    grok.template('document')
