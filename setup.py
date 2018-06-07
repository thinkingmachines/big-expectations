from setuptools import setup
from setuptools import find_packages

setup(name='big-expectations',
      version='0.0.1',
      description='Great Expectations for BigQuery',
      url='https://github.com/thinkingmachines/big-expectations',
      author='Thinking Machines',
      author_email='hello@thinkingmachin.es',
      license='MIT',
      install_requires=[
            'great_expectations',
            'pybigquery'
      ],
      packages=find_packages(),
      zip_safe=False)
