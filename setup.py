from setuptools import setup, find_packages


setup(name='granny',
      version='2012.1',
      packages=find_packages(exclude=['test', 'bin']),
      scripts=['bin/granny'],
      zip_safe=False,
      install_requires=['setuptools'],
      )
