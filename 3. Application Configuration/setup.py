from setuptools import setup

# Daftar dependencies yang dibutuhkan
requires = [
    'pyramid',
    'waitress',
    'pyramid_debugtoolbar', # <-- TAMBAHKAN BARIS INI
]

setup(name='tutorial',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = tutorial:main
      """,
)