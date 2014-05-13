'''
    new_bc.core.py

    core api calls for new_bc api library
'''
import os
import requests as req

API_URL = 'https://basecamp.com/{}/api/v1/'
MY_API_URL = API_URL.format('2361076')

def make_api_url(account_num='2361076',call=None,*args):
    if call is None:
        call = ''
    u = API_URL.format(account_num) + call 
    u = u + '.json' if not args else u + '/' + '/'.join(map(str,args)) + '.json'
    return u

def send_request(url=None,auth=None,json=True):
    if auth is None:
        auth = get_auth()
    if url is None:
        raise IOError('need a url to send request to')
    if json:
        return req.get(url,auth=auth).json()
    else:
        return req.get(url,auth=auth)

def get_auth():
    if os.path.exists('auth.txt'):
        return tuple([str(x[:-1]) for x in tuple(open('auth.txt','r').readlines())])
