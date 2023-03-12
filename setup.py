from setuptools import setup, find_packages

with open('./requirement.txt') as f:
  required = f.read().splitlines()

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Information Technology',
  'Operating System :: Unix',
  'Operating System :: MacOS :: MacOS X',
  'Operating System :: Microsoft :: Windows',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3.6'
]

setup(
  name='JSJumble',
  version='1.0.0',
  description='Tool for obfuscate, compress, and collect Static files.',
  long_description=open('pypi.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  long_description_content_type='text/markdown',
  url='https://github.com/GoodDay360/pygesture',  
  author='GoodDay360',
  author_email='istartgame31@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['pygesture','library','module','gesture_recognition'], 
  packages=find_packages(exclude=["dist","git","pygesture.egg-info","assets"]),
  install_requires=required,
)