#!/usr/bin/env python
"""A simple file that reads a json file and prett prints the output."""


from tkinter import Tk, filedialog
import pprint
import json
import os


def which_directory():
    """This function provides an easy GUI for the user to select the
        working directory of the files."""
    # Ask for the directory to get the files from
    root = Tk().withdraw() # .withdraw() hides that second blank window
    # This sets to the users home directory
    init_dir = os.path.expanduser('~')
    # These options in .askdirectory seem to get the job done!
    filedirectory = filedialog.askdirectory(initialdir=init_dir,
                                            title='Please select a directory')
    return filedirectory

file_directory = which_directory()

with open(os.path.join(file_directory, 'nodes.json'), 'r', encoding="UTF8") as json_data:
    json_file = json.load(json_data)
    pprint.pprint(json_file)
