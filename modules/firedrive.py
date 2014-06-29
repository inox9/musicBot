# coding=utf8
'''
	FireDrive.com direct link fetcher
	version 0.1
'''

import requests as req
import lxml.html

class Firedrive(object):
	def __init__(self, url):
		self.url = url

	def get_link(self):
		sess = req.Session()
		try:
			res = sess.get(self.url, timeout=10)
		except (req.exceptions.Timeout, req.exceptions.ConnectionError, req.exceptions.HTTPError):
			return False
		tree = lxml.html.document_fromstring(res.text)
		hash = tree.xpath('//input[@name="confirm"]/@value')
		if not hash:
			return False
		try:
			res = sess.post(self.url, data={'confirm': hash[0]}, timeout=10)
		except (req.exceptions.Timeout, req.exceptions.ConnectionError, req.exceptions.HTTPError):
			return False
		tree = lxml.html.document_fromstring(res.text)
		link = tree.xpath('//a[@id="archive_download_button"]/@href')
		if not link:
			return False
		return link[0]