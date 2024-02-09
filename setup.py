from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='gerstlix',
  version='0.0.1',
  author='travkacode',
  author_email='tt-tt-19@mail.ru',
  description='Library for simplified access to the Gerstlix API',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/TravkaCodeDeveloper/gerstlix_python',
  packages=find_packages(),
  install_requires=[
    'requests>=2.25.1',
    'json>=1.6.3'
],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='gerstlix api python',
  project_urls={
    'GitHub': 'https://github.com/TravkaCodeDeveloper/gerstlix_python'
  },
  python_requires='>=3.9'
)