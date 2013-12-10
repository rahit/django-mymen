import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-rahit-user',
    version='0.0.1',
    description='Registration and Auth module',
    long_description=README,
    author='Tahsin Hassan Rahit',
    author_email='tahsin.rahit@gmail.com',
    url='http://github.com/rahit/django-rahit-user',
    packages=['mymen'],
    install_requires=['Django >=1.5'],
    include_package_data=True,
    license='MIT License',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
