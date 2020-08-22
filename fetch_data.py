import requests
import json
from os import environ

# client id and secret key
client_id = environ.get("ghclient_id")
client_secret = environ.get("ghclient_secret")


def get_user(user):
	content = requests.get(f'https://api.github.com/users/{user}?client_id={client_id}&client_secret={client_secret}').content
	content_dict = json.loads(content)

	if content_dict.get('message'):
		return -1

	# data that will be displayed
	filtered_keys = ['avatar_url', 'name', 'public_repos', 'followers', 'following', 'created_at']
	cleaned_data = {key: content_dict[key] if content_dict[key] != None else 'Not given' for key in filtered_keys}
	
	return cleaned_data



def get_image(url):
	return requests.get(url, stream=True).raw
	

def get_repos(user):
	content = requests.get(f'https://api.github.com/users/{user}/repos?per_page=5&client_id={client_id}&client_secret={client_secret}').content
	content_dict = json.loads(content)
	filtered_keys = ['name', 'watchers', 'forks']
	data_list = []  # list of repos
	for repo in content_dict:
		cleaned_data = {key: repo[key] for key in filtered_keys}
		data_list.append(cleaned_data)

	return data_list
