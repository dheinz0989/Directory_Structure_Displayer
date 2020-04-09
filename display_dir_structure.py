from pathlib import Path
import argparse

# Text used from the following SO post:
#https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python
class DisplayablePath(object):
    display_filename_prefix_middle = "├──"
    display_filename_prefix_last = "└──"
    display_parent_prefix_middle = "    "
    display_parent_prefix_last = "│   "

    def __init__(self, path, parent_path, is_last):
        self.path = Path(str(path))
        self.parent = parent_path
        self.is_last = is_last
        if self.parent:
            self.depth = self.parent.depth + 1
        else:
            self.depth = 0

    @property
    def displayname(self):
        if self.path.is_dir():
            return self.path.name + "/"
        return self.path.name

    @classmethod
    def make_tree(cls, root, parent=None, is_last=False, criteria=None):
        root = Path(str(root))
        criteria = criteria or cls._default_criteria

        displayable_root = cls(root, parent, is_last)
        yield displayable_root

        children = sorted(
            list(path for path in root.iterdir() if criteria(path)),
            key=lambda s: str(s).lower(),
        )
        count = 1
        for path in children:
            is_last = count == len(children)
            if path.is_dir():
                yield from cls.make_tree(
                    path, parent=displayable_root, is_last=is_last, criteria=criteria
                )
            else:
                yield cls(path, displayable_root, is_last)
            count += 1

    @classmethod
    def _default_criteria(cls, path):
        return True

    @property
    def displayname(self):
        if self.path.is_dir():
            return self.path.name + "/"
        return self.path.name

    def displayable(self):
        if self.parent is None:
            return self.displayname

        _filename_prefix = (
            self.display_filename_prefix_last
            if self.is_last
            else self.display_filename_prefix_middle
        )

        parts = ["{!s} {!s}".format(_filename_prefix, self.displayname)]

        parent = self.parent
        while parent and parent.parent is not None:
            parts.append(
                self.display_parent_prefix_middle
                if parent.is_last
                else self.display_parent_prefix_last
            )
            parent = parent.parent

        return "".join(reversed(parts))


def display_tree(directory, write_file=True,print_console=True):
    paths = DisplayablePath.make_tree(Path(directory))
    if write_file:
        with open("directory_root.txt", "w+", encoding='utf-8') as my_file:
            for path in paths:
                my_file.write(path.displayable()+'\n')
    if print_console:
        for path in paths:
            print(path.displayable())

def str_to_bool(string):
    return string=='y'

if __name__ =="__main__":
    parser = argparse.ArgumentParser(description='Module for creating a Python-based Machine Learning directory.')
    parser.add_argument(
        "-d",
        "--directory",
        type=str,
        required=True,
        default='.',
        help='The directory whose root is to be displayed',
    )
    parser.add_argument(
        "-f",
        "--file",
        type=str,
        required=False,
        default='y',
        choices=['y','n'],
        help='Indicate if the directory structure shall be written to a file',
    )
    parser.add_argument(
        "-c",
        "--console",
        type=str,
        required=False,
        default='n',
        choices=['y','n'],
        help='Indicate if the dsirectory structure hall be printed on the console',
    )

    args = parser.parse_args()
    display_tree(args.directory,str_to_bool(args.file), str_to_bool(args.console))

