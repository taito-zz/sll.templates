=============
sll.templates
=============

sll.templates provides templates for SLL site.

.. image:: https://secure.travis-ci.org/taito/sll.templates.png
    :target: http://travis-ci.org/taito/sll.templates

- Put feed back image to plone site root with id: feed-back.png

Currently tested with
---------------------

- Plone-4.3.6
- Python-2.7.10

Change log
----------

1.11.4 (2015-08-24)
===================

- Fix clear_interfaces to work for most interfaces and remove carousel folder. [taito]

1.11 (2015-08-10)
=================

- Fix test. [taito]

1.10 (2015-08-10)
=================

- Add dependency to Products.CMFPlacefulWorkflow for test. [taito]
- Add link to remove interfaces from objects underneath folder. [taito]

1.9 (2013-05-11)
================

- Removed dependency from five.grok. [taito]
- Tested with Plone-4.3. [taito]

1.8 (2013-03-23)
================

- Updated from abita.adapter to collective.base:
  Fist uninstall abita.adapter and then install collective.base. [taito]

1.7.1 (2013-02-03)
==================

- Fixed feed view for unpublished feeds. [taito]

1.7 (2013-01-31)
================

- Use effective date instead of modified date for feed views. [taito]

1.6 (2013-01-11)
================

- Made feed back image dynamic. [taito]

1.5.2 (2013-01-07)
==================

- Updated template and styles. [taito]

1.5.1 (2012-12-11)
==================

- Fixed bug in number of news and event feed when some to them are fed to main feed. [taito]

1.5 (2012-12-10)
================

- Moved customized search event viewlet and monthly support template to sll.theme package. [taito]

1.4 (2012-12-09)
================

- Fixed feed in micro site. [taito]

1.3 (2012-12-09)
================

- United event and news feed templates. [taito]

1.2 (2012-12-07)
================

- Updated to more flexible feed. [taito]

1.1 (2012-11-30)
================

- Moved micro site functionality to package: collective.microsite. [taito]
- Added testing integration to Travis CI. [taito]

1.0 (2012-11-14)
================

- Tested with Plone-4.2.2. [taito]

0.9.2 (2012-11-13)
==================

- Fixed event feed on micro site's top page to feed only from the micro site. [taito]

0.9.1 (2012-10-31)
==================

- Updated Finnish translations. [taito]

0.9 (2012-10-31)
================

- Added action to make and unmake micro site. [taito]

0.8 (2012-10-03)
================

- Changed event feed query criteria to show only upcoming events, but not on-going ones. [taito]
- Added link to cropped images in feeds. [taito]

0.7.1 (2012-09-24)
==================

- Added content lead image related property. [taito]

0.7 (2012-09-19)
================

- Initial release. [taito]
