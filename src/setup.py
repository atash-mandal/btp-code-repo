from setuptools import setup, find_packages
setup(name="visualizer",version='1.2.19',
      description="This is a visualizer pkg",
      long_description="This",
      author='Atash Mandal',
      packages=['visualizer'],
      install_requires=['numpy','matplotlib','scikit-microwave-design'],
      )