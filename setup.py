from setuptools import setup

setup(
    name='django-configurations-webpack',
    version='2020.5.26',
    install_requires=[
        'django-configurations',
        'django-cors-headers',
        'django-webpack-loader',
        'setuptools',
    ],
    packages=[
        'django_configurations_webpack',
    ],
)
