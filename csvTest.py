import csv
import pandas as pd
import numpy as np

# Create empty data list
data = []

# Open the file
with open('96185_Family_Finder_Matches.csv', 'rb') as infile:
    readdata = csv.reader(infile)

# Pump file contents into data list
    for row in readdata:
        data.append(row)

# Read the column names from the first line of the file
    Header = data[0]

# Fix ID column header
    if Header[11] == "ResultID2":
        Header[11] = Header[11].replace("ResultID2", "ID")

# Fix Label column header
    if Header[13] == "Name":
        Header[13] = Header[13].replace("Name", "Label")

    #print len(Header)

# Pop off first row (the headers)
    data.pop(0)
# Now we have Headers and data objects

    print pd.DataFrame(data, columns=Header)

