import csv

matches = {}

with open('96185_Family_Finder_Matches.csv', 'rb') as f:
    data = csv.reader(f)
    # Read the column names from the first line of the file
    fields = data.next()
# what is it? It is a list
    print type(fields)

# Fix ID column header
    if fields[11] == "ResultID2":
        print "Fixed ID"
        fields[11] = "ID"
        print fields[11]

# Fix Label column header
    if fields[13] == "Name":
        print "Fixed Label"
        fields[13] = "Label"
        print fields[13]     

# Add Empty Segment item
    fields[14] = Segments{}
    
    for row in data:
        # zip together the field names and values
        items = zip(fields, row)
        item = {}
        # Add value to dictionary
        for (name, value) in items:
            item[name] = value.strip()

print items
