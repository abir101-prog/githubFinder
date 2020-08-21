import requests
import json

# client id and secret key
client_id = ''
client_secret = ''


def parse(user):
	content = requests.get(f'https://api.github.com/users/{user}?client_id={client_id}&client_secret={client_secret}').content
	content_dict = json.loads(content)

	if content_dict.get('message'):
		return -1

	# data that will be displayed
	filtered_keys = ['avatar_url', 'name', 'public_repos', 'followers', 'following', 'created_at']
	cleaned_data = {key: content_dict[key] if content_dict[key] else 'Not given' for key in filtered_keys}
	
	return cleaned_data



def get_image(url):
	return requests.get(url, stream=True).raw
	


    