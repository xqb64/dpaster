import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='thepaster',
    version='3.0.1',
    author='xvm32',
    author_email='dedmauz69@gmail.com',
    description=('client interface for https://dpaste.com/ pastebin'),
    license='MIT',
    keywords='client interface for https://dpaste.com/ pastebin',
    url='https://github.com/xvm32/dpaster',
    packages=['dpaster'],
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'console_scripts': [
            'dpaster = dpaster.application:cli'
        ],
    },
    install_requires=[
          'requests',
          'pygments',
          'pyperclip',
          'click'
      ],
)
