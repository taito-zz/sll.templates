from sll.basetheme.browser.interfaces import INavigationRootView
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.interface import implements


class TopPageView(BrowserView):
    """View class for site and micro site top page."""
    implements(INavigationRootView)
    __call__ = ViewPageTemplateFile('templates/top-page.pt')


class FolderView(BrowserView):
    """View class for folder"""
    __call__ = ViewPageTemplateFile('templates/folder.pt')


class BaseDocumentView(BrowserView):

    def image(self):
        return self.context.getField('leadImage').tag(self.context)

    def text(self):
        return self.context.CookedBody()


class DocumentView(BaseDocumentView):
    __call__ = ViewPageTemplateFile('templates/document.pt')
