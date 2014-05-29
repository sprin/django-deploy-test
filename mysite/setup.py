from setuptools import setup

setup(
    name='myapp',
    version='0.1',
    install_requires=[
        'Django==1.7b4',
        'gunicorn==18.0',
        'psycopg2==2.5.3',
        'dj-database-url==0.3.0'
    ],
    dependency_links=[
        'https://www.djangoproject.com/download/1.7.b4/tarball/#egg=Django-1.7b4',
    ],
)
