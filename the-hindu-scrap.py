#scrap the hindu for news
import urllib
import urllib2


response = urllib2.urlopen('http://thehindu.com')
html = response.read()

h1start = html.find('<h1>')
h1start = html.find('>',h1start)+1
h1start = html.find('>',h1start)+1


h1end = html.find('</a>',h1start)

h1 = html [h1start:h1end]
print "HEADLINE:",h1


brkstart = html.find('breakingNews_list">')
brkstart = html.find('<h3>',brkstart)

brkend = html.find('</div>',brkstart)
brk = html [brkstart:brkend]

print "OTHER NEWS:"

while(brk.find('<h3>')!=-1):
	brkstart=brk.find('<a')
	bnewsstart=brk.find('>',brkstart)+1
	bnewsend = brk.find('</a>',bnewsstart)
	bnews=brk[bnewsstart:bnewsend]
	print bnews
	print ""
	brkstart = brk.find('</h3>')+4
	brk = brk [brkstart:brkend]