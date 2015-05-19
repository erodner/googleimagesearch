import argparse
import urllib2

import string
import random

# http://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

parser = argparse.ArgumentParser()
parser.add_argument('-o', help='out directory', default='out/')
parser.add_argument('-j', help='json file with links')

args = parser.parse_args()

import json

with open(args.j, 'r') as jsonfile:
    results = json.load(jsonfile)

outfiles = {}
for r in results:
    url = r['unescapedUrl']
    print url
    try:
        response = urllib2.urlopen(url)
        outimgfn = args.o + '/' + id_generator(size=10) + '.jpg'
        with open(outimgfn, 'wb') as outf:
            outf.write(response.read())
        outfiles[outimgfn] = r
        
    except:
        print "Error downloading the file..."

with open(args.o + '/meta.json', 'w') as metaout:
    json.dump(outfiles, metaout)
