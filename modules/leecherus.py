# coding=utf8
from selenium.webdriver import PhantomJS
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import WebDriverException, NoSuchElementException
import time
import re

class Leecherus(object):
	def __init__(url):
		self.url = url
		DesiredCapabilities.PHANTOMJS['phantomjs.page.settings.loadImages'] = False
		self.browser = PhantomJS()

	def get_link():
		try:
			self.browser.get('http://leecher.us')
			time.sleep(5)
			self.browser.find_element_by_name('links').send_keys(self.url)
			self.browser.find_element_by_id('get_link').click()
			self.browser.find_element_by_xpath('//button[@class="subscribe"]').click()
			self.browser.switch_to_window(self.browser.window_handles[1])
			onclick = self.browser.find_element_by_xpath('//button[@class="subscribe"]').get_attribute('onclick')
		except (WebDriverException, NoSuchElementException):
			return False
		m = re.search("'(http://[^']+)',", onclick)
		if not m:
			return False
		return m.group(1)