#!/usr/bin/env python
"""This script takes in Match (node) and ICW (edge) files and smashes them
into a json format."""

from __future__ import print_function
from  Tkinter import *
import csv
import Tkinter
import Tkconstants
import tkFileDialog
import os
import json

# Create empty lists
nodeData = []
edgeData = []
chrData  = []
nodeDict = {}

# Ask for the directory to get the files from
# .withdraw() hides that second blank window
root = Tk().withdraw()
# This should be set to C:\Users\%USERNAME%\Downloads or whatever
initDir = "C:\Users\hannamj\Dropbox\Public\genealogy\$FamilyTree_GED\Gephi"
# These options in .askdirectory seem to get the job done!
filedirectory = tkFileDialog.askdirectory(initialdir=initDir, title='Please select a directory')
#filedirectory = "C:\Users\hannamj\Dropbox\Public\genealogy\$FamilyTree_GED\Gephi\Matt Hannan\20170817-FTDNA"

###############################################################################

# This forces the creation of the edgeData and chrData before
# the start of node processing.
#icwStr = str("ICW")
#chrStr = str("Browser")
#matchStr = str("Matches")
##filename = str()

for filename in os.listdir(filedirectory):
    if icwStr in filename:
        with open(filename, 'rb') as edgeFile:
            edgeReader = csv.reader(edgeFile)
            edgeData = list(edgeReader)

for filename in os.listdir(filedirectory):
    if "Browser" in filename:
        with open(filename, 'rb') as chrFile:
            chrReader = csv.reader(chrFile)
            chrData = list(chrReader)

# Start node processing
for filename in os.listdir(filedirectory):
    if "Matches" in filename:
        with open(filename, 'rb') as nodeFile:
            nodeReader = csv.reader(nodeFile)
            # Pump node file contents into nodes list
            nodeData = list(nodeReader)
            # Read the column names from the first line of the file
            nodeFields = nodeData[0]
            # Fix ID column header
            if nodeFields[11] == "ResultID2":
                nodeFields[11] = nodeFields[11].replace("ResultID2", "ID")
            # Fix Label column header
            if nodeFields[13] == "Name":
                nodeFields[13] = nodeFields[13].replace("Name", "Label")
            # Pop off first row (the headers)
            nodeData.pop(0)
            # Now we have Headers and nodes objects
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
                # Build ICW list
                icwList = []
                # Cycle through edgeData, created above from ICW file
                for edgeRow in edgeData:
                    # If Source column value = the nodeID...
                    if edgeRow[5] == nodeID:
                        #...add the Target column value to icwlist
                        icwList.append(edgeRow[6])
                # Add icwList to Dictionary nodeDictEntry
                nodeDictEntry.update({'ICW':icwList})
                # Add Dictionary nodeDictEntry to Dictionary nodeDict
                nodeDict[nodeID] = (nodeDictEntry)
                os.system('cls')
                print("Nodes processed: ", count)
                count = count + 1

print()
print("nodeDict length: ", len(nodeDict))

# Check if nodes.json file exists
if os.path.exists('nodes.json'):
    # if it does, delete it
    os.remove('nodes.json')
    print("Deleted old nodes.json file.")

# Writing JSON data
with open('nodes.json', 'w') as f:
    json.dump(nodeDict, f)

