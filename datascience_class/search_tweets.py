import urllib
import json

def print_tweets(url):
	response = urllib.urlopen(url)
	a = json.load(response)
	#for i in a['results']:
	#	print i['text'].encode('utf-8')
	print a

num_pages = 10
for n in range(1,num_pages+1):
	url = 'http://search.twitter.com/search.json?q=microsoft&page=' + str(n)
	print_tweets(url)