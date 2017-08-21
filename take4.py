import csv
import sys
import Tkinter
import tkFileDialog
import pprint
import os

edgeList = []
nodeDict = {}
edgeDict = {}


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
    print "fileList length = ", len(fileList)
    return fileList

def nodeList2Dict(nodeList):
    #print "Read the column names from the first row of the nodeList"
    nodeFields = nodeList[0]
    #print "Pop off first row (the headers)"
    nodeList.pop(0)
    #print "Now we have Headers (nodeFields) and node's data (nodeList) objects"
    # Fix ID column header
    if nodeFields[11] == "ResultID2":
        nodeFields[11] = nodeFields[11].replace("ResultID2", "ID")
        print("Fixed ID Header")
    else:
        print("ID Header OK")
    # Fix Label column header
    if nodeFields[13] == "Name":
        nodeFields[13] = nodeFields[13].replace("Name", "Label")
        print("Fixed Label Header")
    else:
        print("Label Header OK")
    nodeDictBind = {}
    for row in nodeList:
        nodeID = row[11]
        nodeDictEntry = {}
        #print "Zip together the field names and values to create 
        # Dictionary nodeDictEntry"
        nodeDictEntry.update(dict(zip(nodeFields, row)))
        nodeDictBind.update({nodeID:nodeDictEntry})
    return nodeDictBind

def edgeList2Dict(edgeList):
    print "Build ICW list"
    for k, v in nodeDict.items():
        entries = nodeDict[k]
        icwList = []
        for row in edgeDict:
            for edgeRow in edgeList:
                if edgeRow[5] == nodeRow[11]:
            # example of syntax from dictTestNest.py
            # print "Age:  ", details.get('age')
            # This GETS the va ue for a key from a sub-dictionary
            # I want to insert a new k:v in the sub-dictionary                
                    icwList.append(edgeRow[6])

#    print "Add icwList to Dictionary nodeDictEntry"
    nodeDictEntry.update({'ICW':icwList})
    print nodeDictEntry

# open node file
userInput = raw_input("Open Match file or ICW file? m or i: ")
# create nodeList
nodeList = openFile(userInput)
print "nodeList Length = ", len(nodeList)
# convert nodeList rows to nodeDictEntry and build nodeDict
# add nodeDictEntry to nodeDict
nodeDict = nodeList2Dict(nodeList)
print "nodeDict length (out) = ", len(nodeDict)
#pprint.pprint(nodeDict)

# open edge file and create edgeList
#userInput = raw_input("Open Match file or ICW file? m or i: ")
# create edgeList
#edgeList = openFile(userInput)
#print "edgeList Length = ", len(edgeList)




#icw2List(filePath)
# copy Target entries to icwList
# add icwList to correct nodeDictEntry within nodeDict