from zope.interface import Interface
from zope.viewlet.interfaces import IViewletManager


class ISllTemplatesLayer(Interface):
    """Marker interface for browserlayer."""


class ITopViewletManager(IViewletManager):
    """A viewlet manager for Portal Top Page."""


class ISimpleFeedViewletManager(IViewletManager):
    """Base Simple Feed manager for News and Events feed."""


class INewsFeedViewletManager(ISimpleFeedViewletManager):
    """News Feed Viewlet Manager."""


class IEventsFeedViewletManager(ISimpleFeedViewletManager):
    """Events Feed Viewlet Manager."""
