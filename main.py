import requests
import json
import copy
from concurrent.futures import ThreadPoolExecutor

request_url = input[0][6:-2]
header_strings = [input[i].strip()[4:-3].split(":") for i in range(1, len(input) - 1)]
headers = {}
for s in header_strings:
  headers[s[0]] = s[1][1:]
keys = headers.keys()

def do_request(header):
  curr_headers = copy.deepcopy(headers)
  del curr_headers[header]
  response = requests.get(request_url, headers=curr_headers)
  return response, header

with ThreadPoolExecutor(max_workers=5) as executor:
  for response, header in executor.map(do_request, keys):
    if(response.status_code != 200):
      print(header, 'is necessary!')
