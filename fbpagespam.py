import requests
import time
import urllib2
import json
# Replace line 6 with actual token and put spam comment in line 16
TOKEN = 'put-your-access-token-here'
def get_posts():
	url = 'https://graph.facebook.com/v2.2/891971000853462/posts?access_token='+ TOKEN
	page = urllib2.urlopen(url)
	page = page.read()
	page = json.loads(page)
	return page["data"]

def comment(postId):
	url = 'https://graph.facebook.com/v2.2/'+postId+'/comments'
	comment = 'SPAM'
	payload = {'access_token' : TOKEN, 'message': comment}
	s = requests.post(url,data=payload,verify=False)
	time.sleep(1)

if __name__ == '__main__':
	posts = get_posts()
	for post in posts:
		comment(post["id"])
		print "Done"
