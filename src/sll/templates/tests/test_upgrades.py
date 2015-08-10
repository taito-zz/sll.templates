import mock
import unittest


class TestCase(unittest.TestCase):
    """TestCase for upgrades."""

    def test_reimport_actions(self):
        from sll.templates.upgrades import reimport_actions
        setup = mock.Mock()
        reimport_actions(setup)
        setup.runImportStepFromProfile.assert_called_with('profile-sll.templates:default', 'actions', run_dependencies=False, purge_old=False)
