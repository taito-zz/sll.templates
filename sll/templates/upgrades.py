from Products.CMFCore.utils import getToolByName

import logging


PROFILE_ID = 'profile-sll.templates:default'


def upgrade_1_to_2(context, logger=None):
    """Reimport typeinfo.xml for Document.xml view."""
    if logger is None:
        # Called as upgrade step: define our own logger.
        logger = logging.getLogger(__name__)

    logger.info('Adding monthly-supporter view.')
    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile(PROFILE_ID, 'typeinfo', run_dependencies=False, purge_old=False)
    logger.info('Added monthly-supporter view.')
