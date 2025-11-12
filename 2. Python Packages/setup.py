from setuptools import setup

# Daftar dependencies yang dibutuhkan
requires = [
    'pyramid',
    'waitress',
]

setup(name='tutorial',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = tutorial:main
      """,
)