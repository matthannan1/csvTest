import csv
import pandas as pd
import numpy as np
import tkFileDialog
import os


def makeNodes():
    # Cleanup Family Finder Matches file and create nodes.csv
    # GUI file picker
    print("Select Family Finder Matches file...")
    filePath = tkFileDialog.askopenfilename()

    # Create empty nodes list
    nodes = []

    # Open the file
    with open(filePath, 'rb') as infile:
        readnodes = csv.reader(infile)

    # Pump file contents into nodes list
        for row in readnodes:
            nodes.append(row)

    # Read the column names from the first line of the file
        nodeHeader = nodes[0]

    # Fix ID column header
        if nodeHeader[11] == "ResultID2":
            nodeHeader[11] = nodeHeader[11].replace("ResultID2", "ID")
            print("Fixed ID Header")
        else:
            print("ID Header OK")    

    # Fix Label column header
        if nodeHeader[13] == "Name":
            nodeHeader[13] = nodeHeader[13].replace("Name", "Label")
            print("Fixed Label Header")
        else:
            print("Label Header OK")           

    # Pop off first row (the headers)
        nodes.pop(0)
    # Now we have Headers and nodes objects

    # If nodes.csv exists, delete it
    if os.path.isfile('./nodes.csv'):
        try:
            os.unlink('./nodes.csv')
            print("Removed previous nodes.csv file.")
        except:
            none

    # Write the Header and nodes to file
    with open('nodes.csv', 'wb+') as outfile:
        writenodes = csv.writer(outfile)
        writenodes.writerow(nodeHeader)
        for row in nodes:
            writenodes.writerow(row)
    print("Created nodes.csv file")

def makeEdges():
    # Cleanup ICW file and create edges.csv
    # GUI file picker 
    print("Select ICW file...")
    filePath = tkFileDialog.askopenfilename()

    # Create empty edges list
    edges = []

    # Open the file
    with open(filePath, 'rb') as infile:
        readedges = csv.reader(infile)

    # Pump file contents into edges list
        for row in readedges:
            edges.append(row)

    # Read the column names from the first line of the file
        edgesHeader = edges[0]

    # Fix ID column header
        if edgesHeader[5] == "Profile KitID":
            edgesHeader[5] = edgesHeader[5].replace("Profile KitID", "Source")
            print("Fixed Source Header")
        else:
            print("Source Header OK")    

    # Fix Label column header
        if edgesHeader[6] == "Match KitID":
            edgesHeader[6] = edgesHeader[6].replace("Match KitID", "Target")
            print("Fixed Target Header")
        else:
            print("Target Header OK")

    # Pop off first row (the headers)
        edges.pop(0)
    # Now we have Headers and nodes objects

    # If edges.csv exists, delete it
    if os.path.isfile('./edges.csv'):
        try:
            os.unlink('./edges.csv')
            print("Removed previous edges.csv file.")
        except:
            none

    # Write the Header and nodes to file
    with open('edges.csv', 'wb+') as outfile:
        writeedges = csv.writer(outfile)
        writeedges.writerow([edgesHeader[5], edgesHeader[6]])
        for row in edges:
            writeedges.writerow([row[5], row[6]])
    print("Created edges.csv file")


print("Let's clean some data!")
print("We'll start with Family Finder Match data")
makeNodes()
print("Great! Now let's prep the ICW data")
makeEdges()
print("OK. That should do it.")


