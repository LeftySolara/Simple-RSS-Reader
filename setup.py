try:
	from setuptools import setup
except:
	from distutils.core import setup

config = {
	"description": "Simple RSS/Atom feed reader",
	"author": "Jalen Adams",
	"url": "https://github.com/leftysolara",
	"author_email": "leftysolara@gmail.com",
	"version": "0.1",
	"install_requires": ["nose","feedparser"],
	"packages": ["RSS Reader"],
	"scripts": ["file_ops.py","manage_links.py","reader.py"],
	"name": "Simple RSS Reader"
}

setup(**config)