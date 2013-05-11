from zope.interface import Interface
from zope.viewlet.interfaces import IViewletManager


class ISllTemplatesLayer(Interface):
    """Marker interface for browserlayer."""


class ITopPageFeed(Interface):
    """Marker interface for top page feed."""


class IMicroSiteFeed(Interface):
    """Marker interface for micro site feed."""


# Viewlet manager

class ITopPageViewletManager(IViewletManager):
    """Viewlet manager interface for TopPageViewletManager"""


class IFolderViewletManager(IViewletManager):
    """Viewlet manager interface for FolderViewletManager"""
