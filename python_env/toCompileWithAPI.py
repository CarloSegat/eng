#external list of words
import sys
sys.path.append('../text')
import words

import unirest
import requests
from random import *

print words
def random_word():
	key = choice(words.keys())
	return (key, words[key])
	


#URBAN dictionary api
response = unirest.get("https://mashape-community-urban-dictionary.p.mashape.com/define?term=runt",
  headers={
    "X-Mashape-Key": "dcmsmMirTFmshXiL2wf9uN3eMETWp1e85iZjsnsblI2hQ9t2Dg",
    "Accept": "text/plain"
  }
) 
definitions = {}
for response in response.body[u'list']:
	ratio = response[u'thumbs_up']/response[u'thumbs_down']
	definitions[ratio] = [response[u'definition'], response[u'example']];
winner = definitions[max(definitions)] 
print winner

def word_api(word):
		word = word.lower().strip()
		url = "https://wordsapiv1.p.mashape.com/words/" + word + "/definitions"
		response = unirest.get(url, headers={"X-Mashape-Key": "dcmsmMirTFmshXiL2wf9uN3eMETWp1e85iZjsnsblI2hQ9t2Dg",
    					  "Accept": "application/json"})
		if response.code == 404:
			return 404  

		body = response.body 
		definitions = body[u'definitions']
	
		building = ""
		for count, defin in enumerate(body[u'definitions']):
			building += str(count) + ": " + defin[u'definition'] + "\n\n"
			
		url = "https://wordsapiv1.p.mashape.com/words/" + word + "/examples"
	
		response = unirest.get(url, headers={"X-Mashape-Key": "dcmsmMirTFmshXiL2wf9uN3eMETWp1e85iZjsnsblI2hQ9t2Dg",
    					  "Accept": "application/json"})
		
		return { "definitions" : [ str(building).strip() ], "img" : [], 
						 "example" : response.body[u'examples']}

def urban(word):
		url = "https://mashape-community-urban-dictionary.p.mashape.com/define?term=" + word.lower().strip()
		response = unirest.get(url, headers={"X-Mashape-Key": "dcmsmMirTFmshXiL2wf9uN3eMETWp1e85iZjsnsblI2hQ9t2Dg", 
					"Accept": "text/plain"}) 
		if response.body["result_type"] == "no_results":
			return 404
			print "damn, I din't find " + word
		else:

			definitions = {}
			for user_response in response.body[u'list']:
				ratio = user_response[u'thumbs_up']/user_response[u'thumbs_down']
				definitions[ratio] = [user_response[u'definition'], user_response[u'example']];
			print word
			return { "definitions" : [ str(definitions[max(definitions)][0]) ], "img" : [], 
						 "example" : [ str(definitions[max(definitions)][1]) ] }

#for pronounciation use google:
def get_pronounce(word):
	word = word.strip().lower()
	url="https://ssl.gstatic.com/dictionary/static/sounds/de/0/" + word + ".mp3"
	data=requests.get(url).content
	filename= word + ".mp3"
	with open(filename, 'wb') as f:
        	f.write(data)#creates file


def random_word():
	DOIT = raw_input()
	if DOIT != None:
		print random_word()

eng_dictionary = {}
not_found =  []
#for word in words:
	
	
print urban("apple")
print word_api("apple")
print word_api("flow")
get_pronounce("apple")

	

