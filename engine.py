from bs4 import BeautifulSoup as bs
import requests
import re
from stackapi import StackAPI



def runStackSearchEngine(phrase):
	url = "https://google.com/search?q=stackoverflow+"
	words = phrase.split(" ")
	for w in words:
		url += w
		url += "+"
	url = url[:-1]
	page = requests.get(url)
	soup = bs(page.content, features="html.parser")
	blockElem = soup.find("div", class_= "ZINbbc xpd O9g5cc uUPGi")
	soupString = str(soup)
	link = blockElem.find("a", href=True)
	link = (link['href'])
	link = link.split("/")
	qid = 0
	for i,l in enumerate(link):
		if l == "questions":
			qid = link[i + 1]
			break
	SITE = StackAPI('stackoverflow')
	top_answer = SITE.fetch('questions/' + str(qid) + '/answers', sort='votes', filter='!*SU8CGYZitCB.D*(BDVIficKj7nFMLLDij64nVID)N9aK3GmR9kT4IzT*5iO_1y3iZ)6W.G*')
	for item in top_answer["items"]:
		body = item['body']
		starts = [m.start() for m in re.finditer('<code>', body)]
		ends = [m.start() for m in re.finditer('</code>', body)]

		combined = zip(starts, ends)
		for q in range(0, len(starts)):
			a = starts[q]
			b = ends[q]
			if (a != -1 and b != -1):
				print (body[a + 6 : b])
		break

while True:
	val = input("Enter search: ")
	runStackSearchEngine(val)
