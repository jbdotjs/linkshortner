import requests, pyperclip

# API: https://api.shrtco.de/v2/

def link_shortner(link):
	url=f'https://api.shrtco.de/v2/shorten?url={link}'
	response=requests.get(url)
	response_json=response.json()

	short_link=response_json['result']['full_short_link']
	original_link=response_json['result']['original_link']

	pyperclip.copy(short_link)
	print('Short Link:', short_link)
	print('Original Link:',original_link)
	print('Short Link copied to clipboard :)')

link=input('Enter the url you want to shorten:')
link_shortner(link)
