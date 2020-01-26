from setuptools import setup

setup(
    name='WordSearchKata',
    packages=[
      ],
    include_package_data=True,
    install_requires=[],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest', 'pytest-cov', 'coverage'
    ],
)