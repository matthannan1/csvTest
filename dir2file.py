"""Testing out how to work with files from simply selecting the folder that contains them.
This: https://automatetheboringstuff.com/chapter8/
and teh next chapter: https://automatetheboringstuff.com/chapter9/ 
look interesting, as does https://automatetheboringstuff.com/chapter7/ , which is regex."""


from  Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
root = Tk()
root.directory = tkFileDialog.askdirectory()
print (root.directory)

