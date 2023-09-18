from setuptools import setup

requires = [
    'pyramid==2.0.2',
        'waitress==2.1.2',
        'SQLAlchemy==2.0.20',
        'pyramid-mako==1.1.0',
]
dev_requires = [
       
        'pytest==7.4.2',
        'pytest-cov==4.1.0',
        'pytest-pyramid==1.0.2',
        'WebTest==3.0.0',
    ]
setup(
   name='slashdb-demo',
   install_requires=requires,
   extras_require={
      'dev': dev_requires,
   },
   entry_points={
    'console_scripts': [
        'start_server = main:main',
    ],
},
)