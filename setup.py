from setuptools import setup

setup(
    name='FBBot',
    version='0.1a0.dev0',
    author='Lachlan McCarty',
    author_email='lachlan@lachm.com',
    description='Does some of the stuff that the Facebook Graph API doesn\'t',
    long_description='A Python package for doing what the Facebook Graph API '
                     'does not allow (and possibly what it does in the '
                     'future).',
    license='MIT',
    keywords='messenger facebook',
    url='https://github.com/lachm/fbbot',
    packages=[
        'fbbot',
    ],
    install_requires=[
        'beautifulsoup4',
        'requests',
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Communications :: Chat',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
    ]
)
