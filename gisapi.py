import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', help='out file', default='out.json')
parser.add_argument('-q', help='query')
parser.add_argument('--cconly', help='creative commons images only', action='store_true')

args = parser.parse_args()

import urllib2
import simplejson
from pprint import pprint
import json
import time
import random

query = args.q.replace(' ', '%20')
url = ('https://ajax.googleapis.com/ajax/services/search/images?' + 
       'v=1.0&q=' + query + '&userip=INSERT-USER-IP')

if args.cconly:
    url += '&restrict=cc_attribute'

currentpage = "0"
k = 1
rlist = []

while True:
    request = urllib2.Request(url + '&start=' + currentpage, None, {'Referer': 'asp.uni-jena.de'})
    response = urllib2.urlopen(request)

    # Process the JSON string.
    results = simplejson.load(response)

    pages = results['responseData']['cursor']['pages']
    if k>=len(pages):
        break

    currentpage = pages[k]['start']
    print "Results so far: %d" % (len(rlist))
    print "Next start page is %s" % (currentpage)

    rlist = rlist + results['responseData']['results']
    time.sleep(random.randint(5,10))
    k += 1


with open(args.o, 'w') as f: 
    json.dump(rlist,f, indent=4)

#for r in rlist:
#    print rlist[r]['unesp
