import csv
import sys
import Tkinter
import tkFileDialog
import os


edgeList = []
#nodeDict = {}

def openFile(fileType):
    ## create a root Tk widget (so we can destroy it later)
    root = Tkinter.Tk()
    if fileType == 'm':
        select = "Match"
    elif fileType == 'i':
        select = "ICW"
    else:
        print "Incorrect input"
        return    
    initialDir = "C:\Users\hannamj\Dropbox\Public\genealogy\$FamilyTree_GED\Gephi"
    filePath = tkFileDialog.askopenfilename(initialdir = initialDir,
                                        title = ("Select ", select, " file"),
                                        filetypes = (("csv files","*.csv"),("all files","*.*")))

    # I really think this could be its own def, but whatevs...it works
    with open(filePath, 'rb') as fileFile:
        fileReader = csv.reader(fileFile)
        fileList = list(fileReader)
    print "fileList type: ", type(fileList)
    print "fileList length = ", len(fileList)
    return fileList

def nodeList2Dict(nodeList):
    #print "Read the column names from the first row of the nodeList"
    nodeFields = nodeList[0]
    #print "Pop off first row (the headers)"
    nodeList.pop(0)
    #print "Now we have Headers (nodeFields) and node's data (nodeList) objects"
    # Create new list, nodeData.
    nodeData = []
    for row in nodeList:
        nodeData.append(row)
        nodeID = row[11]
        print nodeID
        nodeDictEntry = {}
        #print "Grab each additional row"
        for nodeRow in nodeData:
            #print "Zip together the field names and values to create Dictionary nodeDictEntry"
            nodeDictEntry.update(dict(zip(nodeFields, nodeRow)))
            print nodeDictEntry
        #nodeDict.update(nodeDictEntry)
    #print nodeDict
    return nodeDict      


# open node file
userInput = raw_input("Open Match file or ICW file? m or i: ")
# create nodeList
nodeList = openFile(userInput)
print "nodeList Length = ", len(nodeList)
#print nodeList
# convert nodeList rows to nodeDictEntry and build nodeDict
nodeDict = nodeList2Dict(nodeList)
print "nodeDict length: ", len(nodeDict)


# add nodeDictEntry to nodeDict
# open edge file and create edgeList
#userInput = raw_input("Open Match file or ICW file? m or i: ")
#openFile(userInput)
#icw2List(filePath)
# copy Target entries to icwList
# add icwList to correct nodeDictEntry within nodeDict