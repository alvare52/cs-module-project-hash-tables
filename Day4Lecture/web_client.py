# Understanding
# Let's make a web client
# it will fetch URLs
# but it will cache the web page that's returned

# Plan
# How to use hash tables to make a web cache?
# Key: url, Value: webpage data

# could make the value store more info
# webpage data
# when we looked it up

import urllib.request
import datetime
import time

class CacheEntry:
    def __init__(self, url, data):
        self.url = url
        self.data = data
        self.time_fetched = datetime.datetime.now().timestamp()

# Execute
cache = {}

url = "https://www.google.com"

TIMEOUT = 10

def get_page(url):

    time_now = datetime.datetime.now().timestamp()
    # given a url, check to see if it's in the same cache
    if url in cache and time_now - cache[url].time_fetched < TIMEOUT:
        # if less than 10 seconds since our last request
        # if so, return that
        return cache[url]
    # if not, go get it
    else:
        print("going out into the webs to get the page")
        resp = urllib.request.urlopen(url)
        data = resp.read()
        resp.close()

        # put in cache
        cache[url] = CacheEntry(url, data)
    
    return cache[url]

page = get_page(url)
# print("After this, we get from cache")

print("now we wait")
time.sleep(10)
page = get_page(url)
