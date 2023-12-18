from setuptools import setup

setup(
    name='pylatestdeb',
    version='1.0.4',
    description='Utility for download latest deb package from AWS S3 bucket',
    url='https://github.com/vadimxL/pylatestdeb',
    author='Malinovsky Vadim',
    author_email='vadim.malinovsky@sentrycs.com',
    license='MIT',
    packages=['pylatestdeb'],
    entry_points={
        'console_scripts': [
            'pylatestdeb = pylatestdeb.run:main'
        ]
    },
    install_requires=['tqdm',
                      'boto3',
                      'oathtool',
                      'diskcache'
                      ],

    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
    ],
)
