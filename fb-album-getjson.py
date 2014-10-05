import urllib2
import json
url = 'https://graph.facebook.com/v2.1/<album-id>/photos?access_token=yourAccessToken'
i=1
while (url):
	page = urllib2.urlopen(url)
	page = page.read()
	page = json.loads(page)
	file = open(str(i)+".json",'w')
	file.write(json.dumps(page, indent=2))
	file.close()
	i+=1
	try:
		url = page['paging']['next']
	except:
		url = None