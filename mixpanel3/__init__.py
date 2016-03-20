import hashlib
import requests
import time
try:
    import json
except ImportError:
    import simplejson as json

"""
View more parameter at
https://mixpanel.com/docs/api-documentation/data-export-api
"""

class Mixpanel(object):

    ENDPOINT = 'http://mixpanel.com/api'
    VERSION = '2.0'
    METHOD_SEGMENTATION = "segmentation/"
    METHOD_SEGMENT_NUMERIC = METHOD_SEGMENTATION + "/" + 'numeric'

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def get_request(self, methods, params, format='json'):
        """
            methods - List of methods to be joined, e.g. ['events', 'properties', 'values']
            params - Extra parameters associated with method
        """
        params['api_key'] = self.api_key
        params['expire'] = int(time.time()) + 600   # Grant this request 10 minutes.
        params['format'] = format
        if 'sig' in params: del params['sig']
        params['sig'] = self.hash_args(params)

        request_url = '/'.join([self.ENDPOINT, str(self.VERSION),methods])
        print(request_url)

        response = requests.get(request_url, params=params)
        return response.json()


    def hash_args(self, args):
        # print(args)
        sig = ''.join(str(key)+"="+str(value) for key,value in sorted(args.items()))
        sig += self.api_secret
        print(sig)
        return   hashlib.md5(sig.encode('utf-8')).hexdigest()


    def get_numeric_segmentation(self,params):
        return self.get_request(methods=self.METHOD_SEGMENT_NUMERIC, params=params)

    def get_segmentation(self,params):
        return self.get_request(methods=self.METHOD_SEGMENTATION, params=params)


