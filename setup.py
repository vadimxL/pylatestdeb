from setuptools import setup

setup(
    name='pylatestdeb',
    version='1.0',
    description='A example Python package',
    url='https://github.com/shuds13/pyexample',
    author='Malinovsky Vadim',
    author_email='shudson@anl.gov',
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
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)