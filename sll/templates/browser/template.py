from Acquisition import aq_inner
from Acquisition import aq_parent
from Products.ATContentTypes.interfaces.document import IATDocument
from Products.ATContentTypes.interfaces.folder import IATFolder
from Products.CMFCore.utils import getToolByName
from five import grok
from plone.app.contentlisting.interfaces import IContentListing
from sll.templates.browser.interfaces import ISllTemplatesLayer
from zope.component import getMultiAdapter


grok.templatedir('templates')


class DevelopmentWorkView(grok.View):

    grok.context(IATFolder)
    grok.layer(ISllTemplatesLayer)
    grok.name('development-work')
    grok.require('cmf.ManagePortal')
    grok.template('development-work')
