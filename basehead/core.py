'''
    new_bc.core.py

    core api calls for new_bc api library
'''
import os
import requests 


API_URL = 'https://basecamp.com/{}/api/v1/'
MY_API_URL = API_URL.format('2361076')

def make_api_url(account_num='2361076',call=None,*args):
    if call is None:
        call = ''
    u = API_URL.format(account_num) + call 
    u = u + '.json' if not args else u + '/' + '/'.join(map(str,args)) + '.json'
    return u


def get_auth(username=None,passwd=None):
    if username and passwd:
        return (username,passwd)
    else:
        if os.path.exists('auth.txt'):
            return tuple([str(x[:-1]) for x in tuple(open('auth.txt').readlines())])


req = requests.session()
req.auth = get_auth()

def send_request(url=None,json=True):
    global req
    if url is None:
        raise IOError('need a url to send request to')
    if json:
        return req.get(url).json()
    else:
        return req.get(url)
