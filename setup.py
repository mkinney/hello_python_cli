from setuptools import setup
#from setuptools import find_packages

setup(
   name='hello',
   version='0.0.1',
   description='Simple python example',
   author='Mike Kinney',
   author_email='mike.kinney@gmail.com',
   packages=['hello_module'],
   #packages=find_packages(exclude=['tests']),
   install_requires=[],
   scripts=['hello'],
#   entry_points={
#    'console_scripts': (
#        'hello = main',
#    ),
#   },
)
        # 'hello = hello.main:__main__',
