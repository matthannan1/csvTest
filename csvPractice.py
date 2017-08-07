import csv
# import Tkinter as tk
import tkFileDialog

# GUI file picker
filePath = tkFileDialog.askopenfilename()

# open file and assign to "csvfile" variable
with open(filePath) as csvfile:
    # read csv file to variable "reader"
    reader = csv.reader(csvfile)
    for row in reader:
        print("In loop")
        print row
        if row[2] == "D":
            row.insert(2, "C")
        if row[11] == "ResultID2":
            row[11] = "ID"
        print row
        input()
