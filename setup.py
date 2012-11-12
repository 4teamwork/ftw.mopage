from setuptools import setup, find_packages

version = '1.0'

tests_require = [
    'ftw.testing',
    'plone.app.testing',
    'lxml',
    ]

setup(name='ftw.mopage',
      version=version,
      description="Provides moPage integration for Plone.",
      long_description=open("README.rst").read() + "\n" + \
          open("docs/HISTORY.txt").read(),

      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],

      keywords='',
      author='4teamwork GmbH',
      author_email='mailto:info@4teamwork.ch',
      url='https://github.com/4teamwork/ftw.mopage',
      license='GPL2',

      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ftw'],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
        'setuptools',
        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),

      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
