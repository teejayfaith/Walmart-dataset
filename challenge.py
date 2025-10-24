# deeply-nested JSON (string)
import json
from tkinter import Y

nested_json = '''
{
  "user": {
    "id": 101,
    "name": "Ada Lovelace",
    "roles": ["admin", "developer"],
    "address": {
      "street": "12 Computing Way",
      "city": "London",
      "geo": { "lat": 51.5074, "lng": -0.1278 }
    },
    "projects": [
      {
        "title": "Analytical Engine",
        "year": 1843,
        "tags": ["mechanical", "math"]
      },
      {
        "title": "Note G",
        "year": 1843,
        "tags": ["algorithm", "loop"]
      }
    ]
  }
}
'''

# Question
# Convert the JSON string to a Python dictionary and print the tags of the first projects?
# print the full details of user with ID of 101 in text format (in a sentence)

convert = json.loads(nested_json)
convert

# print the tags of the first projects
project_tags = convert['user']['projects'][0]['tags']
print(project_tags)

# print the full details of user with ID of 101 in text format (in a sentence)
user101 = convert['user']
print(f"The User with ID of {user101['id']} is {user101['name']}, lives at No {user101['address']['street']} street, in the city of {user101['address']['city']}.")
print(f"With a geo-political map of ({user101['address']['geo']['lat']}) latitude ({user101['address']['geo']['lng']}) and longitude." )
print(F"Has the roles of: {user101['roles'][0]}, {user101['roles'][1]} and currently working on {len(user101['projects'])} projects,")
print(f"With the first title of {user101['projects'][0]['title']} in the year {user101['projects'][0]['year']} with {len(user101['projects'][0]['tags'])} tags.")