from hexagonit.testing.browser import Browser
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import TEST_USER_PASSWORD
from plone.app.testing import setRoles
from plone.testing import layered
from sll.templates.tests.base import FUNCTIONAL_TESTING
from sll.templates.browser.interfaces import ITopPageFeed
from zope.testing import renormalizing
from zope.interface import alsoProvides


import doctest
import manuel.codeblock
import manuel.doctest
import manuel.testing
import re
import transaction
import unittest2 as unittest

FLAGS = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS | doctest.REPORT_NDIFF | doctest.REPORT_ONLY_FIRST_FAILURE

CHECKER = renormalizing.RENormalizing([
    # Normalize the generated UUID values to always compare equal.
    (re.compile(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'), '<UUID>'),
])


def setUp(self):
    layer = self.globs['layer']
    # Update global variables within the tests.
    self.globs.update({
        'portal': layer['portal'],
        'portal_url': layer['portal'].absolute_url(),
        'browser': Browser(layer['app']),
        'TEST_USER_ID': TEST_USER_ID,
        'TEST_USER_NAME': TEST_USER_NAME,
        'TEST_USER_PASSWORD': TEST_USER_PASSWORD,
        'SITE_OWNER_NAME': SITE_OWNER_NAME,
        'SITE_OWNER_PASSWORD': SITE_OWNER_PASSWORD,
    })

    portal = self.globs['portal']
    browser = self.globs['browser']
    portal_url = self.globs['portal_url']
    browser.setBaseUrl(portal_url)

    browser.handleErrors = True
    portal.error_log._ignored_exceptions = ()

    setRoles(portal, TEST_USER_ID, ['Manager'])

    folder = portal[
        portal.invokeFactory(
            'Folder',
            'folder',
            title='Title of Folder',
            description='Description of Folder.',
        )
    ]
    folder.reindexObject()

    ids = ['01', '02']
    for oid in ids:
        obj = folder[
            folder.invokeFactory(
                'Document',
                'doc{0}'.format(oid),
                title='Title of Document{0}'.format(oid),
                description='Description of Document{0}'.format(oid),
                text='<p>This is the body text of Document{0}.</p>'.format(oid),
            )
        ]
        alsoProvides(obj, ITopPageFeed)
        obj.reindexObject()

    transaction.commit()


def DocFileSuite(testfile, flags=FLAGS, setUp=setUp, layer=FUNCTIONAL_TESTING):
    """Returns a test suite configured with a test layer.

    :param testfile: Path to a doctest file.
    :type testfile: str

    :param flags: Doctest test flags.
    :type flags: int

    :param setUp: Test set up function.
    :type setUp: callable

    :param layer: Test layer
    :type layer: object

    :rtype: `manuel.testing.TestSuite`
    """
    m = manuel.doctest.Manuel(optionflags=flags, checker=CHECKER)
    m += manuel.codeblock.Manuel()

    return layered(
        manuel.testing.TestSuite(m, testfile, setUp=setUp, globs=dict(layer=layer)),
        layer=layer)


def test_suite():
    return unittest.TestSuite([
        DocFileSuite('functional/folder.txt'),
        DocFileSuite('functional/portal.txt'),
        ])
