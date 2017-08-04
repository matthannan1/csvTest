import csv
import os

# open csv file
csvfile = open( "inputfile.csv", "rb" )

# read csv file according to dialect
reader = csv.reader( csvfile )

# read header
# header = reader.next()

# read data into memory
data = [row for row in reader]

# close input file
csvfile.close()

# print data
print(data)

#####################################################

# Writing CSV Files With Python.

# open output file
outfile = open( "output.csv", "a" )



# get a csv writer
writer = csv.writer( outfile )

# write header
#writer.writerow(header)

# write data
[ writer.writerow(x) for x in data ]

# close file
outfile.close()
