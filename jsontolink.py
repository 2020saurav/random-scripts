import json

for i in range(1,36):
	f = open(str(i)+".json",'r')
	parsed = json.loads(f.read())
	for j in range(0,25):
		out = open('links','a')
		out.write(parsed['data'][j]['images'][0]['source']+"\n")
		out.close()