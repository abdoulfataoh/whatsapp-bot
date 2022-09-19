# coding: utf-8

from environs import Env


env = Env()


API_URL = env.url('API_URL', 'https://graph.facebook.com/v14.0')
PHONE_NUMBER_ID = env.str('PHONE_NUMBER_ID', '102703642606293')