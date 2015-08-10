PROFILE_ID = 'profile-sll.templates:default'


def reimport_actions(setup):
    """Reimport actions"""
    setup.runImportStepFromProfile(PROFILE_ID, 'actions', run_dependencies=False, purge_old=False)
