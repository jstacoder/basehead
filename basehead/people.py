# coding: utf-8
from core import send_request,make_api_url, get_auth
from MY_BC import BC

def get_all_people(account_num=BC):
    return send_request(make_api_url(account_num,'people'),get_auth())

def get_person(account_num=BC,person_id=None):
    if person_id is None:
        raise IOError('need a person to get')
    return send_request(make_api_url(account_num,'people',person_id),get_auth())

def get_me(account_num=BC):
    return send_request(make_api_url(account_num,'people','me'),get_auth())
