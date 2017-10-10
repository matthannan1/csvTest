#!/usr/bin/env python


from tkinter import filedialog, Tk
import csv
import os
import json
import pprint

# Create empty lists
#listOfSegments = []
#segmentDetailsList = []
chromosomeData = {}
nodeID = '107701'


################################################################################

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

def csv2list(search_string):
    """(string) -> list

    This creates a basic list from a csv file and returns it."""
    for filename in os.listdir(file_directory):
        if search_string in filename:
            with open(os.path.join(file_directory, filename), 'r', encoding="UTF8") as ffile:
                freader = csv.reader(ffile)
                fdata = list(freader)
            return fdata

def makeCB(cb_Data, nodeID):
    # create cbList
    cbList = []
    cb_List = []
    # Cycle through cb_Data, paring it down to just the data (remove names)
    for cbRow in cb_Data:
        cbList.append([cbRow[2], cbRow[3], cbRow[4],
                       cbRow[5], cbRow[6], cbRow[7]])
    # Read the column names from the first line of the file
    cbFields = cbList[0]
    # Pop off first row (the headers)
    cbList.pop(0) # Now we have Headers and cbs objects
    print("cbList created")
    cbDictEntry = {}
    # Start to cycle through cbs list
    for cbListRow in cbList:
        cbDictEntry = {}
        cbID = cbListRow[5]
        cbListRow.pop(5)
        # Make cbList and append to cbDictEntry
        if cbID == nodeID:
            # Zip together the field names and values to create Dictionary cbDictEntry
            cbDictEntry.update(dict(zip(cbFields, cbListRow)))
            cb_List.append(cbDictEntry)
    return cb_List


##########################################################


file_directory = which_directory()
listOfSegments = csv2list('Chromosome')
#pprint.pprint(listOfSegments)
segmentDetailsList = makeCB(listOfSegments, nodeID)
pprint.pprint(segmentDetailsList)
