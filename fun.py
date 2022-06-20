import requests 
import json
import pandas as pd

# github.com/dword4/nhlapi

api_url = "https://statsapi.web.nhl.com/api/v1/teams"
response = requests.get(api_url)

json_data = response.json()

print(json_data['teams'][2]['teamName'])

team_name = input("Enter team name: ")


# print(json_data)

if json_data['teams'][2]['teamName'] == team_name:
	print("true")
else:
	print("false")

# print(json.dumps(json_data))