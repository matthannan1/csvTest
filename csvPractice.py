import csv
import Tkinter as tk
import tkFileDialog

file_path = tkFileDialog.askopenfilename()
with open(file_path) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(type(row))
