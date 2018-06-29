import urllib
import json
contacts = urllib.urlopen("https://api.androidhive.info/contacts/").read()
#print(str(contacts))
jsonToPython = json.loads(contacts)
output = jsonToPython["contacts"]
#print(output)
first = output[0]
#print(first)
print("firs['name']")