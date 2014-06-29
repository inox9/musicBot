# coding=utf8
import requests as req
import lxml.html

class Firedrive:
	def __init__(url):
		self.url = url

	def get_link():
		sess = req.Session()
		try:
			res = sess.get(url, timeout=10)
		except (req.exceptions.Timeout, req.exceptions.ConnectionError, req.exceptions.HTTPError):
			return False
		tree = lxml.html.document_fromstring(res.text)
		hash = tree.xpath('//input[@name="confirm"]/@value')
		if not hash:
			return False
		try:
			res = sess.post(url, data={'confirm': hash[0]}, timeout=10)
		except (req.exceptions.Timeout, req.exceptions.ConnectionError, req.exceptions.HTTPError):
			return False
		tree = lxml.html.document_fromstring(res.text)
		link = tree.xpath('//a[@id="archive_download_button"]/@href')
		if not link:
			return False
		return link[0]