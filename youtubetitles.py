import json
import requests
import pprint #make sure to do pprint.pprint("string") when printing

#https://www.googleapis.com/youtube/v3/search?part=snippet&key=[API_KEY]
#After getting stuff from API, turns into code and stuff

def getVids(link):
        result = requests.get(link)
        return result

def makeDict(result):
        #makes into a dict
        rdata = json.loads(result.text)
        return rdata

def printAllTitles(rdata):
        #how to print the titles
        for i in range(50):
                pprint.pprint(rdata['items'][i]['snippet']['title'])

