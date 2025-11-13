from setuptools import setup, find_packages

requires = [
    'pyramid',
    'waitress',
    'pyramid_debugtoolbar',
    'pyramid_mako',
]

setup(name='tutorial',
      version='0.0',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = tutorial:main
      """,
)