# _*_ coding: utf-8 _*_

from setuptools import setup
setup(
  name="ci_example",
  version='1.0.0',
  url='https://github.com/andrleite/continuous-integration',
  author='Andre Leite',
  author_email='andrleite@gmai.com',
  description='Continuous Integration Example',
  packages=['ci_example', 'tests'],
  test_suite='tests',
)