from setuptools import setup, find_packages

setup(
    name='wgforge2018_igorxxl8',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['wgforge.wargaming.com_access.log']},
    entry_points={
        'console_scripts': [
            'task1 = IGOR_TURCEVICH_WGFORGE2018.TASK1.task1:main'
        ]
    },
    test_suite='tests'
)
