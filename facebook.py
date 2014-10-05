import requests
import json
import time

TOKEN = 'your-token-here'
TIME = '1388572687'
def get_posts():
	query = ("SELECT post_id, actor_id, message FROM stream WHERE source_id = me() AND created_time > "+TIME+" LIMIT 200")
	payload = {'q' : query, 'access_token' : TOKEN}
	r = requests.get('https://graph.facebook.com/fql',params=payload,verify=False)
	result = json.loads(r.text)
	return result['data']

def comment_thanks(posts):
	for post in posts:
		r = requests.get('https://graph.facebook.com/%s/' % post['actor_id'],verify=False)
		url = 'https://graph.facebook.com/%s/comments' % post['post_id']
		user = json.loads(r.text)
		message = 'Thanks %s! :)' % user['first_name']
		payload = {'access_token' : TOKEN, 'message': message}
		s = requests.post(url,data=payload,verify=False)

		print "Wall post %s done" % post['post_id']
		time.sleep(1)

def like_posts(posts):
	for post in posts:
		url = 'https://graph.facebook.com/%s/likes' % post['post_id']
		payload = {'access_token' : TOKEN}
		requests.post(url,data=payload,verify=False)
		print "Liked %s" % post['post_id']
		time.sleep(1)

def show_posts(posts):
	for post in posts:
		print post['message']



if __name__ == '__main__':
	posts = get_posts()
	#comment_thanks(posts)
	show_posts(posts)
	#like_posts(posts)
	
