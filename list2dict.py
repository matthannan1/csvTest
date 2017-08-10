import csv
import sys
import Tkinter
import tkFileDialog
import os

## create a root Tk widget (so we can destroy it later)
root = Tkinter.Tk()

print "GUI file picker"

nodePath = tkFileDialog.askopenfilename(initialdir = 
                                        "C:\Users\hannamj\Dropbox\Public\genealogy\$FamilyTree_GED\Gephi",
                                        title = "Select Match file",
                                        filetypes = (("csv files","*.csv"),("all files","*.*")))

edgePath = tkFileDialog.askopenfilename(initialdir = 
                                        "C:\Users\hannamj\Dropbox\Public\genealogy\$FamilyTree_GED\Gephi",
                                        title = "Select ICW file",
                                        filetypes = (("csv files","*.csv"),("all files","*.*")))

print "Create empty lists"
nodeData = []
edgeData = []
nodeDict = {}

print "Open the files"
with open(edgePath, 'rb') as edgeFile:
    edge = csv.reader(edgeFile)
    edgeData = list(edge)

with open(nodePath, 'rb') as nodeFile:
    node = csv.reader(nodeFile)
    

    print "Pump file contents into nodes list"
    for row in node:
        nodeData.append(row)
        nodeID = row[11]
        nodeDictEntry = {}
        
        print "Read the column names from the first line of the file"
        nodeFields = nodeData[0]
        print "Pop off first row (the headers)"
        nodeData.pop(0)
        print "Now we have Headers and nodes objects"

        print "Grab each additional row"
        for nodeRow in nodeData:
            print "Zip together the field names and values to create Dictionary nodeDictEntry"
            nodeDictEntry.update(dict(zip(nodeFields, nodeRow)))

            print "Build ICW list"
            icwList = []
            for edgeRow in edgeData:
                if edgeRow[5] == nodeRow[11]:
                    icwList.append(edgeRow[6])

            print "Add icwList to Dictionary nodeDictEntry"
            nodeDictEntry.update({'ICW':icwList})
            print nodeDictEntry
            input()
        # Add Dictionary nodeDictEntry to Dictionary nodeDict
        nodeDict[nodeID] = (nodeDictEntry)
print nodeDict
print len(nodeDict) 
