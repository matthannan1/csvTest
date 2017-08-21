#!/usr/bin/env python
"""This script takes in Match (node) and ICW (edge) files and smashes them
into a json format."""

import csv
import Tkinter
import tkFileDialog
import os
import json

## create a root Tk widget (so we can destroy it later)
ROOT = Tkinter.Tk()

# print "GUI file picker"
initialDir = "C:\Users\hannamj\Dropbox\Public\genealogy\$FamilyTree_GED\Gephi"

nodeFilename = tkFileDialog.askopenfilename(initialdir = initialDir,
                                        title = "Select Match file",
                                        filetypes = (("csv files", "*.csv"), ("all files", "*.*")))

edgeFilename = tkFileDialog.askopenfilename(initialdir = initialDir,
                                        title = "Select ICW file",
                                        filetypes = (("csv files", "*.csv"), ("all files", "*.*")))

#print "Create empty lists"
nodeData = []
edgeData = []
nodeDict = {}

#print "Open the files"
with open(edgeFilename, 'rb') as edgeFile:
    edgeReader = csv.reader(edgeFile)
    edgeData = list(edgeReader)

with open(nodeFilename, 'rb') as nodeFile:
    nodeReader = csv.reader(nodeFile)
    #print "Pump node file contents into nodes list"
    nodeData = list(nodeReader)
    #print "Read the column names from the first line of the file"
    nodeFields = nodeData[0]
    #print "Pop off first row (the headers)"
    nodeData.pop(0)
    #print "Now we have Headers and nodes objects"
    count = 0
    for nodeRow in nodeData:
        nodeDictEntry = {}
        nodeID = nodeRow[11]
        # Zip together the field names and values to create Dictionary nodeDictEntry
        nodeDictEntry.update(dict(zip(nodeFields, nodeRow)))
        # Build ICW list
        icwList = []
        for edgeRow in edgeData:
            if edgeRow[5] == nodeID:
                icwList.append(edgeRow[6])
        # Add icwList to Dictionary nodeDictEntry
        nodeDictEntry.update({'ICW':icwList})
        # Add Dictionary nodeDictEntry to Dictionary nodeDict
        nodeDict[nodeID] = (nodeDictEntry)
        os.system('cls')
        print "Nodes processed: ", count
        count = count + 1

#pprint.pprint(nodeDict)
print
print "nodeDict length: ", len(nodeDict)

# Writing JSON data
with open('nodes.json', 'w') as f:
    json.dump(nodeDict, f)
