#!/usr/bin/env python

import os
import bz2
import gzip
import json

bags_dir = "/Users/ed/Data/mith-bags"

bags = [
    "6DC120C7-8901-417B-B387-0C6AFECEE9E8",
    "AF330002-664C-4321-98D2-E753BE8DD025", 
    "D651C3F6-5619-4A42-A8BC-7C22B7A9A44A",
    "fe28a093-d3f4-42d7-83ba-f5ba1b1cc765"
]

def process(filename):
    print "reading %s" % filename

    if filename.endswith('bz2'):
        fh = bz2.BZ2File(filename)
    elif filename.endswith('gz'):
        fh = gzip.open(filename)
    else:
        print filename

    blm = open("blacklivesmatter.json", "a")
    alm = open("alllivesmatter.json", "a")

    for line in fh:
        try:
            tweet = json.loads(line)
        except:
            continue
        for e in tweet['entities']['hashtags']:
            tag = e['text'].lower()
            write_to = None
            if tag == "blacklivesmatter":
                found = True
                blm.write(line)
            if tag == "alllivesmatter":
                found = True
                alm.write(line)

for bag in bags:
    data_dir = os.path.join(bags_dir, bag, "data")
    for filename in os.listdir(data_dir):
        if 'json' in filename:
            process(os.path.join(data_dir, filename))
