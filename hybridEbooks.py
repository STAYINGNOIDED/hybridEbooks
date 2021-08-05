# A bot that generates markov text from one or more .txt files
# and posts it to the fediverse
# by NOIDED

import requests, argparse, markovify
import sys, os
from random import choice as ch

parser = argparse.ArgumentParser(description="corpuses")
parser.add_argument("-u", metavar="users",               help="write the filename(s) of one or more corpuses here,, eg; <Noided.txt> or <Noided.txt Grumbulon.txt Sterence.txt>", nargs="+")
parser.add_argument("-i", metavar="instance",  type=str, help="instance url without https:// prefix,, eg; <sleepy.cafe>", nargs=1)
parser.add_argument("-t", metavar="token",     type=str, help="bearer token,, generate here: https://tinysubversions.com/notes/mastodon-bot/", nargs=1)
parser.add_argument("-v", metavar="visibility",          help="visibility", nargs="?", default="unlisted")
parser.add_argument("-s", metavar="signature", type=str, help="signature appended to end", nargs="?", default="")
args = parser.parse_args()
d = vars(args)

# Makes the post. Takes the text you want posted, the visibility of the post,
# the instance, and the bearer token of the account.
def doPostOAuth(txt, vis, inst, tok):
	headers = {
	"Authorization":"Bearer " + tok}
	data = {
	'status': txt,
	'visibility': vis}
	try:
		response = requests.post("https://" + inst + "/api/v1/statuses", headers=headers, data=data)
	except:
		print( "failed to post lol" )
	return
		

# Creates the corpus to generate text. Merges multiple txt files 
# if applicable.
def concatenateCorpuses(lst):
	corp = ""
	for i in lst:
		try:
			path = os.path.join(sys.path[0], i)
			with open(path, encoding="utf-8") as f:
				corp += f.read()
		except:
			print(i + " does not exist,, moving on")
	return corp

# Creates the sentence to be posted with Markovify.
def createSentence(corpus):
	text_model = markovify.NewlineText( corpus, state_size=ch( [1,2] ) )
	if ch( [0, 1] ):
		nigger = text_model.make_sentence()
	else:
		nigger = text_model.make_short_sentence(280)
	return nigger

corpuses   = d["u"]
visibility = d["v"]
instance   = d["i"][0]
token      = d["t"][0]
signature  = d["s"]

fullCorp = concatenateCorpuses( corpuses )
sentence = createSentence( fullCorp )
if len( signature) > 0:
	sentence += "\n\n-- " + signature
print( sentence )
doPostOAuth( sentence, visibility, instance, token )