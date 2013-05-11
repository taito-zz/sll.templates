from abita.utils.utils import reimport_profile


PROFILE_ID = 'profile-sll.templates:default'


def reimport_registry(context):
    """Reimport registry"""
    reimport_profile(context, PROFILE_ID, 'plone.app.registry')


def reimport_viewlets(context):
    """Reimport viewlets"""
    reimport_profile(context, PROFILE_ID, 'viewlets')


def reimport_cssregistry(context):
    """Reimport cssregistry"""
    reimport_profile(context, PROFILE_ID, 'cssregistry')
