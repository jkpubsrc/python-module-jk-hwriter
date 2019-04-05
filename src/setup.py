from setuptools import setup


def readme():
	with open("README.rst") as f:
		return f.read()


setup(name="jk_hwriter",
	version="0.2019.4.5",
	description="This python module provides a single class: A buffer that can be used to create indented output. This is useful for producing pretty printed texts for XML, HTML or programming languages.",
	author="Jürgen Knauth",
	author_email="pubsrc@binary-overflow.de",
	license="Apache 2.0",
	url="https://github.com/jkpubsrc/python-module-jk-hwriter",
	download_url="https://github.com/jkpubsrc/python-module-jk-hwriter/tarball/0.2019.1.22",
	keywords=[
		"html",
		"xml",
		"json",
		"java",
		"python",
		"c#",
		"development",
		"html5",
		],
	packages=[
		"jk_hwriter",
		],
	install_requires=[
	],
	include_package_data=True,
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: Apache Software License",
	],
	long_description=readme(),
	zip_safe=False)

