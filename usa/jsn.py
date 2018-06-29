from urllib.request import urlopen
import json
import ssl

context = ssl._create_unverified_context()
contacts = urlopen("https://api.androidhive.info/contacts/", context=context).read()
#print(str(contacts))
jsonToPython = json.loads(contacts)
output = jsonToPython['contacts']
print(output)
first = output[0]
print(first)
print(first['name'])