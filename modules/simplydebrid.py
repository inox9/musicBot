# coding=utf8
'''
	Simply-debrid.com direct link fetcher, uses requests lib
	version 0.2
'''

import requests
import base64

class Simplydebrid(object):
	def __init__(self, url):
		self.url = url

	def get_link(self):
		b64url = base64.b64encode(self.url)
		link = requests.get('https://simply-debrid.com/inc/name.php?j=%s' % b64url, headers={'Referer': 'https://simply-debrid.com/generate'}).text
		return link if link.startswith('http://') else False
