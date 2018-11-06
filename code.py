import requests

def do_something():
    url = 'https://news.google.com/'
	r = requests.get(url)
	print(r)