from Acquisition import aq_inner
from Acquisition import aq_parent
from Products.ATContentTypes.interfaces.document import IATDocument
from Products.ATContentTypes.interfaces.event import IATEvent
from Products.ATContentTypes.interfaces.file import IATFile
from Products.ATContentTypes.interfaces.file import IFileContent
from Products.ATContentTypes.interfaces.image import IATImage
from Products.ATContentTypes.interfaces.image import IImageContent
from Products.ATContentTypes.interfaces.news import IATNewsItem
from Products.CMFEditions.interfaces import IVersioned
from Products.Five.browser import BrowserView
from Products.statusmessages.interfaces import IStatusMessage
from collective.base.interfaces import IAdapter
from plone.app.blob.interfaces import IATBlobFile
from plone.app.blob.interfaces import IATBlobImage
from sll.templates.browser.interfaces import IMicroSiteFeed
from sll.templates.browser.interfaces import ITopPageFeed
from zope.interface import alsoProvides
from zope.interface import directlyProvidedBy
from zope.interface import noLongerProvides

import logging


logger = logging.getLogger(__name__)


class Miscellaneous(BrowserView):

    def feedable_to_top(self):
        return (
            IATDocument.providedBy(
                self.context
            ) or IATEvent.providedBy(
                self.context
            ) or IATNewsItem.providedBy(
                self.context
            )
        ) and not ITopPageFeed.providedBy(self.context)

    def unfeedable_from_top(self):
        return (
            IATDocument.providedBy(
                self.context
            ) or IATEvent.providedBy(
                self.context
            ) or IATNewsItem.providedBy(
                self.context
            )
        ) and ITopPageFeed.providedBy(self.context)

    def feed_to_top(self):
        alsoProvides(self.context, ITopPageFeed)
        self.context.reindexObject(idxs=['object_provides'])
        url = self.context.absolute_url()
        return self.request.response.redirect(url)

    def unfeed_from_top(self):
        noLongerProvides(self.context, ITopPageFeed)
        self.context.reindexObject(idxs=['object_provides'])
        url = self.context.absolute_url()
        return self.request.response.redirect(url)

    def feedable_to_microsite(self):
        return (
            IATDocument.providedBy(
                self.context
            ) or IATEvent.providedBy(
                self.context
            ) or IATNewsItem.providedBy(
                self.context
            )
        ) and not IMicroSiteFeed.providedBy(self.context)

    def unfeedable_from_microsite(self):
        return (
            IATDocument.providedBy(
                self.context
            ) or IATEvent.providedBy(
                self.context
            ) or IATNewsItem.providedBy(
                self.context
            )
        ) and IMicroSiteFeed.providedBy(self.context)

    def feed_to_microsite(self):
        alsoProvides(self.context, IMicroSiteFeed)
        self.context.reindexObject(idxs=['object_provides'])
        url = self.context.absolute_url()
        return self.request.response.redirect(url)

    def unfeed_from_microsite(self):
        noLongerProvides(self.context, IMicroSiteFeed)
        self.context.reindexObject(idxs=['object_provides'])
        url = self.context.absolute_url()
        return self.request.response.redirect(url)

    def clear_interfaces(self):
        context = aq_inner(self.context)
        adapter = IAdapter(context)
        items = {}
        omits = [IVersioned, IATImage, IImageContent, IATFile, IFileContent, IATBlobImage, IATBlobFile]
        for obj in adapter.get_objects():
            if obj.id == 'carousel':
                parent = aq_parent(aq_inner(obj))
                parent.manage_delObjects(['carousel'])
                message = 'Remove carousel folder from {}.'.format('/'.join(parent.getPhysicalPath()))
                logger.info(message)
                IStatusMessage(self.request).addStatusMessage(message, type='info')
            else:
                ifaces = [iface for iface in directlyProvidedBy(obj) if iface not in omits]
                if ifaces:
                    for iface in ifaces:
                        noLongerProvides(obj, iface)
                        identifier = iface.__identifier__
                        if identifier not in items:
                            items[identifier] = 1
                        else:
                            items[identifier] += 1
                    obj.reindexObject(idxs=['object_provides'])

        for key in items:
            message = '{} objects providing {} are cleared.'.format(items[key], key)
            logger.info(message)
            IStatusMessage(self.request).addStatusMessage(message, type='info')
        if not items:
            message = 'No objects need to be cleared.'
            logger.info(message)
            IStatusMessage(self.request).addStatusMessage(message, type='info')
        url = self.context.absolute_url()
        return self.request.response.redirect(url)
