from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='flareworks',
  version='0.2',
  description=' FlareWorks is a simple, easy and fast micro web framework for python 3.x. ',
  long_description=open('README.MD').read(),
  long_description_content_type='text/markdown',
  url='',  
  author='HdlJohanna',
  author_email='hdljohanna@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='wsgi flare server flareworks http', 
  packages=find_packages(),
  install_requires=[] 
)
