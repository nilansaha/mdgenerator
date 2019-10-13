# MD Generator (mdgenerator)

mdgenerator is a package to generate different kinds of markdown texts

Following details the functionality provided by the package:

- Generate File Structure Trees in Markdown
- Generate Tables in Markdown from pandas dataframe or python arrays

## Installation

There are two ways to install mdgenerator:

- Install mdgenerator from PyPI (recommended):

```
pip install mdgenerator
```

- Install mdgenerator from the Github source:

```
git clone https://github.com/nilansaha/mdgenerator.git
cd mdgenerator
pip install .
```

## Usage

- Generate File Tree Structure in Markdown
	- Using Python

	```
	from mdgenerator import generate_file_structure
	generate_file_structure(target_dir='/path/to/directory', output_dir='/output/directory')
	```
	- Using the terminal

	```
	mdgenerator --target_dir "/path/to/directory" --output_dir "/output/directory"
	```

- Generate Markdown Table using Python


