# coding=utf8
'''
	oboom.com download link fetcher, uses phantomjs/selenium
	version 0.1
'''

import os.path
import subprocess

class Oboom(object):
	def __init__(self, url):
		self.url = url
		
	def get_link(self):
		d = os.path.dirname(os.path.abspath(__file__))
		try:
			link = subprocess.check_output(['%s/oboom.js' % d, self.url])
		except subprocess.CalledProcessError:
			return False
		return link.strip() if len(link.strip()) > 0 else False