from io import StringIO
import json
import os

os.system('cls')
print()
json1a = {'A':1, 'B':2, 'C':3.14}
print(json1a)
print("C is type: ", type(json1a['C']))
print()

#json.dump(json1a, fp)


"""
fileObj = StringIO()
json.dump(["Hello", "Geeks"], fileObj)
print("Using json.dump(): "+str(fileObj.getvalue()))
print()
"""
class TypeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, type):
            return str(obj)

print("Using json.dumps(): " + str(json.dumps(type(str), cls=TypeEncoder)))
print()

print("Using json.JSONEncoder().encode" + str(TypeEncoder().encode(type(list))))
print()

json1 = str(TypeEncoder().encode(type(list)))
print("json1 type: ", type(json1))
print(json1)
print()

json2 = str(json.dumps(type(str), cls=TypeEncoder))
print("json2 type: ", type(json2))
print(json2)
print()

print("Using json.JSONEncoder().iterencode" + str(list(TypeEncoder().iterencode(type(dict)))))

print()
print("################################################")
print()

fileObj = StringIO('["Geeks for Geeks"]')
print("Using json.load(): "+str(json.load(fileObj)))
print("Using json.loads(): "+str(json.loads('{"Geeks": 1, "for": 2, "Geeks": 3}')))
print("Using json.JSONDecoder().decode(): " +
    str(json.JSONDecoder().decode('{"Geeks": 1, "for": 2, "Geeks": 3}')))
print("Using json.JSONDecoder().raw_decode(): " +
    str(json.JSONDecoder().raw_decode('{"Geeks": 1, "for": 2, "Geeks": 3}')))

print()
geekDict = json.JSONDecoder().decode('{"Geeks": 1, "for": 2, "Geeks": 3}')
print(geekDict["Geeks"])
print(type(geekDict["Geeks"]))

# Check if nodes.json file exists
if os.path.exists('jsonTest.json'):
    # if it does, delete it
    os.remove('jsonTest.json')
    print("Deleted old jsonTest.json file.")
# Writing JSON data
with open('jsonTest.json', 'w') as f:
    json.dump(json1a, f)
    print("jsonTest.json file created.")
