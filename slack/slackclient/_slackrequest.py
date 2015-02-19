import time
import urllib
import urllib2

class SlackRequest(object):
    def __init__(self):
        pass

    def do(self, token, request="?", post_data=None, domain="slack.com"):
        t = time.time()
        post_data = post_data or {}
        post_data["ts"] = t
        post_data["token"] = token
        post_data = urllib.urlencode(post_data)
        url = 'https://{0}/api/{1}'.format(domain, request)
        return urllib2.urlopen(url, post_data)
