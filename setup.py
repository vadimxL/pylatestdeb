from setuptools import setup

setup(
    name='pylatestdeb',
    version='1.0',
    description='A example Python package',
    url='https://github.com/vadimxL/pylatestdeb',
    author='Malinovsky Vadim',
    author_email='vadim.malinovsky@sentrycs.com',
    license='BSD 2-clause',
    packages=['pylatestdeb'],
    install_requires=['tqdm',
                      'boto3',
                      'oathtool',
                      'diskcache'
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.12',
    ],
)