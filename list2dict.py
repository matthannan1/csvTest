import csv
import sys
import Tkinter
import tkFileDialog
import os

## create a root Tk widget (so we can destroy it later)
root = Tkinter.Tk()

# GUI file picker
filePath = tkFileDialog.askopenfilename(initialdir = "C:\Users\hannamj\Dropbox\Public\genealogy\$FamilyTree_GED\Gephi",
                                            title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))

# Create empty nodes list
nodes = []

# Open the file
with open(filePath, 'rb') as infile:
    data = csv.reader(infile)

    # Grab first row as headers    
    fields = data.next()

    # Grab each additional row
    for row in data:
        # Zip together the field names and values
        item = dict(zip(fields, row))   

    for k, v in item.items():
        print(k,v)
        