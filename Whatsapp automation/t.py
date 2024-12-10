# importing the json module
import json

# opening the file and reading data from it
fp = open('groups.json', 'r')
data = fp.read()
fp.close()

# converting data to python dict
data = json.loads(data)

# accessing the data associated with wa_groups key
grps = data['wa_groups']
print(grps, len(grps), type(grps))