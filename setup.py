#!/usr/bin/env python3
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='export_torrent_cache',
    version='0.1',
    python_requires='>=3.6',
    py_modules=['export_torrent_cache',],
    license='MIT',
    author='codeclem',
    author_email='25412578+codeclem@users.noreply.github.com',
    url='https://github.com/codeclem/export_torrent_cache',
    install_requires=['torrent_parser',],
    entry_points={
        'console_scripts': ['export_torrent_cache=export_torrent_cache:main']
    },
    description='Export/backup the cache directory of a torrent client, restoring original filenames and organized by tracker',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
