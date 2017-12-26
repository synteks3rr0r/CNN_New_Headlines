#webScraper
import urllib2, os, sys

def clearScreen():
	os.system('cls' if os.name == 'nt' else 'clear')
	
def crawlCNN():
	file=open("Output.html","w")
	response = urllib2.urlopen('http://www.cnn.com/specials/last-50-stories')
	html = response.read()
	count = 0
	startPos = 0
	endPos = 0
	findLinkStartPos = 0
	findLinkEndPos = 0
	#print html
	print 'Cnn Headlines:'
	for articlefound in html:
		count = count+1
		#print startPos
		#print endPos
		
		findLinkStartPos = html.find('contentbox=',findLinkStartPos)
		findLinkEndPos = html.find(' ',findLinkStartPos)
		
		startPos=html.find('cd__headline-text">',startPos)+19
		endPos=html.find("<",startPos)
		
		link=html[findLinkStartPos+12:findLinkEndPos-1]
		article=html[startPos:endPos]
		
		print str(count ) + '. ' + article + '.'
		#print startPos
		#print endPos
		#print count 
		editedLink = "	- http://www.cnn.com" + link
		print editedLink
		
		startPos=endPos
		endPos= endPos + startPos
		
		findLinkStartPos=findLinkEndPos
		findLinkEndPos= findLinkEndPos + findLinkStartPos
		file.write(str(count) + ". " + article + "\r\n" + editedLink + "\r\n\r\n")
		if count >= 10:
			print '\r\n'
			break

clearScreen()
crawlCNN()