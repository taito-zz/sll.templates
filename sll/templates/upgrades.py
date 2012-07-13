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


def upgrade_2_to_3(context, logger=None):
    """Reimport actions.xml and rolemap.xml."""
    if logger is None:
        # Called as upgrade step: define our own logger.
        logger = logging.getLogger(__name__)

    setup = getToolByName(context, 'portal_setup')

    logger.info('Reimporting rolemap.xml.')
    setup.runImportStepFromProfile(PROFILE_ID, 'rolemap', run_dependencies=False, purge_old=False)
    logger.info('Reimported rolemap.xml')

    logger.info('Reimporting actions.xml.')
    setup.runImportStepFromProfile(PROFILE_ID, 'actions', run_dependencies=False, purge_old=False)
    logger.info('Reimported actions.xml')
