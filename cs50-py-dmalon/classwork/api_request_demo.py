# Must install $pip install requests to make REST API calls

# See iTunes REST Examples
# https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/LookupExamples.html

import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=2))

# change the limit
response = requests.get("https://itunes.apple.com/search?entity=song&limit=7&term=" + sys.argv[1])
json_value = response.json()

for result in json_value["results"]:
    print(result['trackName'], "---", result['artistName'])

