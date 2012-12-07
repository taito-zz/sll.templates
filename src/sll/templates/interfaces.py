from sll.templates import _
from zope import schema
from zope.interface import Interface


class IBaseFeed(Interface):
    """Base interface for feed on top page"""

    number = schema.Int(
        title=_(u'Number of feeds'),
        min=0,
        default=3)


class ITopPageMainFeed(IBaseFeed):
    """Interface for top page main feed"""


class INewsFeed(IBaseFeed):
    """Interface for top page news feed"""

    path = schema.TextLine(
        title=_(u'Path'),
        default=u'ajankohtaista')


class IEventFeed(IBaseFeed):
    """Interface for top page event feed"""

    path = schema.TextLine(
        title=_(u'Path'),
        default=u'tapahtumat')


class IFolderFeed(IBaseFeed):
    """Interface for feed in folder"""


class IAdapter(Interface):
    """Adapter interface for all the objects"""

    def get_feed_number(interface):  # pragma: no cover
        """Returns number of feed for the interface"""
