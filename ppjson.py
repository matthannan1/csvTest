import pprint
import json

with open('nodes.json') as json_data:
    d = json.load(json_data)
    pprint.pprint(d)