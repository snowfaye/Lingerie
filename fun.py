import requests 
import json
import pandas as pd

# github.com/dword4/nhlapi

def not_found(error):
	return make_response(jsonify( { 'status': 'Bad request' }), 400)

def not_found(error):
	return make_response(jsonify( { 'status': 'Bad request' }), 404)

# call the api
def call_api(request_link):
	response = requests.get(request_link)
	json_data = response.json()

	return json_data


api_url = "https://statsapi.web.nhl.com/api/v1/people/"
# response = requests.get(api_url)

# json_data = response.json()

json_response = call_api(api_url)

print(json_response)

# print(json_response['teams'][2]['teamName'])

# team_name = input("Enter team name: ")



# print(json.dumps(json_data))
