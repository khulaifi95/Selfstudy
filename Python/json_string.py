# JSON string parsing

# JSON    Python
# object  dict
# array   list
# string  str
# int     int
# real    float
# true    True
# false   False
# null    None


import json

people_string = '''
{
  "people": [
    {
      "name": "John Smith",
      "phone": "615-555-7164",
      "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
      "has_lisense": false
    },
    {
      "name": "Jane Doe",
      "phone": "560-555-5113",
      "emails": null,
      "has_license": true
    }
  ]
}
'''

# loads()
data = json.loads(people_string)

print(type(data))
print(type(data['people']))

for person in data['people']:
    del person['phone']
    print(person)

# dumps()
new_string = json.dumps(data, indent=2, sort_keys=True)

print(new_string)
