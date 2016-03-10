import urllib, urllib2
import json


def list(handle, starttime, endtime):
    parameters = { 'starttime': starttime, 'endtime': endtime, 'apiKey': handle.apikey }
    url = handle.server + '/api/2.0/recording?' + urllib.urlencode(parameters)
    req = urllib2.Request(url)
    response = urllib2.urlopen(req, context=handle.ctx)
    items = json.load(response)
    return items['data']

