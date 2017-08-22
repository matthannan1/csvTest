"""Testing out how to work with files from simply selecting the folder that contains them.
This: https://automatetheboringstuff.com/chapter8/
and teh next chapter: https://automatetheboringstuff.com/chapter9/ 
look interesting, as does https://automatetheboringstuff.com/chapter7/ , which is regex."""

from __future__ import print_function
from  Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

import os


root = Tk()
filedirectory = tkFileDialog.askdirectory()
print(filedirectory)
for filename in os.listdir(filedirectory):
    count = 0
    if "Matches" in filename:
            count = count + 1

    if count == 0:
        print("No Match files found.")
    if count == 1:
        print(filename)
    if count > 1:
        print("More than one Match file detected.")
        print("Please delete the unneccessary file(s).")

for filename in os.listdir(filedirectory):
    count = 0
    if "ICW" in filename:
            count = count + 1

    if count == 0:
        print("No ICW files found.")
    if count == 1:
        print(filename)    
    if count > 1:
        print("More than one ICW file detected.")
        print("Please delete the unneccessary file(s).")
   


