# DisplayRootDirectory
This short module has only one function to use: display a directory tree for a given directory. It displays a directory and its subdirectories and files in the following way:

...project/ <br />
...├── dev/ <br />
...│   ├── app.py <br />
...│   ├── config.yml <br />
...│   ├── Foo.py <br />
...│   └── requirements.txt <br />
...└── build/<br />

# Disclaimer
Main functionalities of this script have been described in a [StackOverFlow post](https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python)

# Prerequisits
The source code is written in [Python 3.8](https://www.python.org/). It use the two native library *pathlib* and *argparse*

# Installation
You can clone this repository by running:
	
	git clone https://github.com/dheinz0989/Directory_Structure_Displayer

# Usage
To display the tree of an example directory *user/project*, use the following

```
python display_dir_structure.py -d user/project
```

# To Do
This repository has several things which are not implemented yet. Amongs others, the following implementation are planned:
1. Add an option to hide hidden files
2. Add funtionality to overwrite the output text file
3. Change arguments to be mutually exclusived with regards to print to console and write to a file