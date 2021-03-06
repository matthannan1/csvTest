#!/usr/bin/env python
"""This script takes in Match (node) and ICW (edge) files and smashes them
into a json format."""

#from __future__ import print_function
from tkinter import filedialog
from tkinter import *
import csv
import os
import json
import locale
import time
import pprint

# Create empty lists
nodeData = []
edgeData = []
cbData = []
nodeDict = {}

###############################################################################

def which_directory():
    # Ask for the directory to get the files from
    root = Tk().withdraw() # .withdraw() hides that second blank window
    # This should be set to C:\Users\%USERNAME%\Downloads or whatever
    init_dir = os.path.expanduser('~')
    # These options in .askdirectory seem to get the job done!
    filedirectory = filedialog.askdirectory(initialdir=init_dir, title='Please select a directory')
    return filedirectory

def csv2list(search_string):
    # This creates the three basic lists from the three files.
    for filename in os.listdir(file_directory):
        if search_string in filename:
            with open(os.path.join(file_directory, filename), 'r', encoding="UTF8") as ffile:
                freader = csv.reader(ffile)
                fdata = list(freader)
            return fdata

def make_nodeDict(nodeData):
    # Read the column names from the first line of the file
    nodeFields = nodeData[0]
    # Fix ID column header
    if nodeFields[11] == "ResultID2":
        nodeFields[11] = nodeFields[11].replace("ResultID2", "ID")
    # Fix Label column header
    if nodeFields[13] == "Name":
        nodeFields[13] = nodeFields[13].replace("Name", "Label")
    # Pop off first row (the headers)
    nodeData.pop(0) # Now we have Headers and nodes objects
    # Set counter to 0
    count = 0
    # Start to cycle through nodes list
    for nodeRow in nodeData:
        nodeDictEntry = {}
        nodeID = nodeRow[11]
        # Break Ancestral string into Ancestral list
        nodeRow[8] = nodeRow[8].split('| ')
        # Zip together the field names and values to create Dictionary nodeDictEntry
        nodeDictEntry.update(dict(zip(nodeFields, nodeRow)))
        nodeDict[nodeID] = nodeDictEntry
        os.system('cls')
        print("Nodes processed: ", count)
        count = count + 1
    return nodeDict



file_directory = which_directory()
edgeData = csv2list('ICW')
cdData = csv2list('Browser')
nodeData = csv2list('Matches')
nodeDict = make_nodeDict(nodeData)

# Start node processing
#for filename in os.listdir(file_directory):
    #if "Matches" in filename:
        #with open(os.path.join(file_directory,filename), 'r', encoding="UTF8") as nodeFile:
            #nodeReader = csv.reader(nodeFile)
            # Pump node file contents into nodes list
            #nodeData = list(nodeReader)
            # Read the column names from the first line of the file
            #nodeFields = nodeData[0]
            # Fix ID column header
            #if nodeFields[11] == "ResultID2":
                #nodeFields[11] = nodeFields[11].replace("ResultID2", "ID")
            # Fix Label column header
            #if nodeFields[13] == "Name":
                #nodeFields[13] = nodeFields[13].replace("Name", "Label")
            # Pop off first row (the headers)
            #nodeData.pop(0) # Now we have Headers and nodes objects
            # Set counter to 0
            #count = 0
            # Start to cycle through nodes list
            #for nodeRow in nodeData:
                #nodeDictEntry = {}
                #nodeID = nodeRow[11]
                # Break Ancestral string into Ancestral list
                #nodeRow[8] = nodeRow[8].split('| ')
                # Zip together the field names and values to create Dictionary nodeDictEntry
                #nodeDictEntry.update(dict(zip(nodeFields, nodeRow)))
                # Build ICW list
 ###               icwList = []
                # Cycle through edgeData, created above from ICW file
 ###               for edgeRow in edgeData:
                    # If Source column value = the nodeID...
 ###                   if edgeRow[5] == nodeID:
                        # ...add the Target column value to icwList
 ###                       icwList.append(edgeRow[6])
                # Add icwList to Dictionary nodeDictEntry
 ###               nodeDictEntry.update({'ICW':icwList})
                # Build the Chromosome Browser mess
 ###               cbList = []
                # Cycle through cbData, created above
 ###               for cbRow in cbData:
 ###                   if cbRow[7] == nodeID:
 ###                       cbList.append(cbRow[1], cbRow[2], cbRow[3], cbRow[4],
 ###                                     cbRow[5], cbRow[6], cbRow[7])
 ###               nodeDictEntry.update({'Chromosome Data':cbList})
                # Add Dictionary nodeDictEntry to Dictionary nodeDict
                #nodeDict[nodeID] = nodeDictEntry
                #os.system('cls')
                #print("Nodes processed: ", count)
                #count = count + 1

print()
#pprint.pprint(cbData)
print("nodeDict length: ", len(nodeDict))

# Check if nodes.json file exists
if os.path.exists(os.path.join(file_directory,'nodes.json')):
    # if it does, delete it
    os.remove(os.path.join(file_directory,'nodes.json'))
    print("Deleted old nodes.json file.")

# Writing JSON data
with open(os.path.join(file_directory,'nodes.json'), 'w') as f:
    json.dump(nodeDict, f)
    print("nodes.json file created.")