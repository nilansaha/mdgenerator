from setuptools import setup

long_description = '''
mdgenerator is a package to generate different kind of markdown texts

* Following details the functionality provided by the package:

	- Generate File Structure Trees in Markdown
	- Generate Tables in Markdown from pandas dataframe or python arrays
'''

setup(
	name='mdgenerator',
	version='0.1.0',
	author='Nilan Saha',
	description = 'Package to generate different kind of markdown texts',
	long_description = long_description,
	license = 'Apache 2.0',
	packages = ['mdgenerator'],
	entry_points = {
		'console_scripts': [
			'mdgenerator = mdgenerator.cli:main'
		]
	}
)
