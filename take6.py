#!/usr/bin/env python
"""This script takes in Match (node), ICW (edge), and ChromosomeBrowser (cb)
    files and smashes them all together into a json format, which is exported
    to nodes.json file."""

#from __future__ import print_function
from tkinter import filedialog, Tk
#from tkinter import Tk
import csv
import os
import json
#import locale
#import time
import pprint
#import timeit

# Create empty lists
nodeData = []
edgeData = []
cbData = []
nodeDict = {}

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

def make_nodeDict(node_Data):
    """(list) -> dict

    This function starts processing the match list and converts it into
    a dictionary of dictionaries."""
    # Read the column names from the first line of the file
    nodeFields = node_Data[0]
    # Fix ID column header
    if nodeFields[11] == "ResultID2":
        nodeFields[11] = nodeFields[11].replace("ResultID2", "ID")
    # Fix Label column header
    if nodeFields[13] == "Name":
        nodeFields[13] = nodeFields[13].replace("Name", "Label")
    # Pop off first row (the headers)
    node_Data.pop(0) # Now we have Headers and nodes objects
    
    # Set counter to 0
    count = 0
    node_Dict = {}
    # Start to cycle through nodes list
    for nodeRow in node_Data:
        nodeDictEntry = {}
        nodeID = nodeRow[11]
        # Break Ancestral string into Ancestral list
        nodeRow[8] = nodeRow[8].split('| ')
        # Zip together the field names and values to create Dictionary nodeDictEntry
        nodeDictEntry.update(dict(zip(nodeFields, nodeRow)))
        # Make icwList and append to nodeDictEntry
        nodeDictEntry.update({'ICW':makeICW(edgeData, nodeID)})
        # Make cbList and append to nodeDictEntry
        nodeDictEntry.update({'Chromosome Data':makeCB(cbData, nodeID)})
        node_Dict[nodeID] = nodeDictEntry
        os.system('cls')
        print("Nodes processed: ", count)
        count = count + 1
    return node_Dict

def makeICW(edge_Data, node_ID):
    """(list, string) -> smaller list
    
    Simple function to extract ICW data and convert to a List.
    This List is then added to the main nodeDict as a dictionary
    entry, ala {ICW:icwList} """
    icwList = []
    # Cycle through edgeData, created above from ICW file
    for edgeRow in edge_Data:
    # If Source column value = the nodeID...
        if edgeRow[5] == node_ID:
    # ...add the Target column value to icwList
            icwList.append(edgeRow[6])
    return icwList

def makeCB(cb_Data, node_ID):
    """(list, string) -> list of lists of dictionaries
    
    This function will get a little more complex than makeICW. Basically,
    it will take the cbData and create a list of lists of dictionary entries.
    This mess will then be appeneded to the main nodeDict as a dictionary entry,
    ala {ChromosomeData:cbList} """
    # Build the Chromosome Browser mess
    cbList = []
    # Cycle through cbData, created above
    for cbRow in cb_Data:
        if cbRow[7] == node_ID:
            cbList.append(cbRow[1], cbRow[2], cbRow[3], cbRow[4],
                          cbRow[5], cbRow[6], cbRow[7])
        pprint.pprint(cbList)
    return cbList

file_directory = which_directory()
edgeData = csv2list('ICW')
cdData = csv2list('Browser')
nodeData = csv2list('Matches')
nodeDict = make_nodeDict(nodeData)

print()
#pprint.pprint(node)
print("nodeDict length: ", len(nodeDict))

# Check if nodes.json file exists
if os.path.exists(os.path.join(file_directory, 'nodes.json')):
    # if it does, delete it
    os.remove(os.path.join(file_directory, 'nodes.json'))
    print("Deleted old nodes.json file.")

# Writing JSON data
with open(os.path.join(file_directory, 'nodes.json'), 'w') as f:
    json.dump(nodeDict, f)
    print("nodes.json file created.")
