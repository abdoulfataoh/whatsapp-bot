# coding: utf-8

from environs import Env


env = Env()

API_URL = env.str('API_URL', 'https://graph.facebook.com/v14.0')
PHONE_NUMBER_ID = env.str('PHONE_NUMBER_ID', '107797488755439')
TOKEN = env.str('TOKEN', 'EAAHIGqFaZAoUBAB0EyPKAKebIpgfvypWeKK1XsGLU5UGJRRZChNgZAgtV0lHYYSnbEEm6UepwqjnWUfSKcgGsENFqhJYFzSCyKHYUQu3bm220GH4sekZBSNgFL2AB00iDHfwIYzVraIgQtvNZAQHvqLJGjwFAWlsWJYBZBeG9z0BK7OMcMmrnBrp1ZCP7paOgS4gNpwpjMSxQZDZD')
