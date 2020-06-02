
from setuptools import setup


setup(name='writer-snap',


      version='0.1dev1',
      description='A test snap to write configuration into a TOML file',

      author='Muhammad Yahya & Felix Forster @ OLI Systems 2020',
      url='https://github.com/olisystems/intersnap-com-demo.git',
      packages=['writer_main.writer_pkg', 'writer_main'],
      install_requires=['click', 'toml', ],

      classifiers=[
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "Topic :: Utilities",
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: Operating System :: POSIX :: Linux", ],

      entry_points={
          'console_scripts': [
              'writer-snap = writer_main.writer_main:init'
          ]
      },

      )
