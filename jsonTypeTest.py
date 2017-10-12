from io import StringIO
import json
 
fileObj = StringIO()
json.dump(["Hello", "Geeks"], fileObj)
print("Using json.dump(): "+str(fileObj.getvalue()))
 
class TypeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, type):
            return str(obj)
 
print("Using json.dumps(): "+str(json.dumps(type(str), cls=TypeEncoder)))
print("Using json.JSONEncoder().encode"+
      str(TypeEncoder().encode(type(list))))
print("Using json.JSONEncoder().iterencode"+
      str(list(TypeEncoder().iterencode(type(dict)))))

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


geekDict = json.JSONDecoder().decode('{"Geeks": 1, "for": 2, "Geeks": 3}')
print(geekDict["Geeks"])
print(type(geekDict["Geeks"]))
