from Acquisition import aq_inner
from Products.ATContentTypes.interfaces.document import IATDocument
from Products.ATContentTypes.interfaces.event import IATEvent
from Products.ATContentTypes.interfaces.news import IATNewsItem
from Products.Five.browser import BrowserView
from Products.statusmessages.interfaces import IStatusMessage
from collective.base.interfaces import IAdapter
from hexagonit.socialbutton.interfaces import ISocialButtonHidden
from sll.templates.browser.interfaces import IMicroSiteFeed
from sll.templates.browser.interfaces import ITopPageFeed
from zope.interface import alsoProvides
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

    def _no_longer_provide(self, iface):
        context = aq_inner(self.context)
        adapter = IAdapter(context)
        objs = adapter.get_objects(iface)

        for obj in objs:
            noLongerProvides(obj, iface)
            obj.reindexObject(idxs=['object_provides'])

        message = '{} objects providing {} are cleared.'.format(len(objs), iface.__identifier__)
        logger.info(message)
        IStatusMessage(self.request).addStatusMessage(message, type='info')

    def clear_interfaces(self):
        self._no_longer_provide(ITopPageFeed)
        self._no_longer_provide(IMicroSiteFeed)
        self._no_longer_provide(ISocialButtonHidden)
        url = self.context.absolute_url()
        return self.request.response.redirect(url)
