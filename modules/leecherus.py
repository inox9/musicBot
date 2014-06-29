# coding=utf8
'''
	Leecher.us direct link fetcher, uses phantomjs/selenium
	version 0.1
'''

from selenium.webdriver import PhantomJS
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import WebDriverException, NoSuchElementException
import re

class Leecherus(object):
	def __init__(self, url):
		self.url = url
		DesiredCapabilities.PHANTOMJS['phantomjs.page.settings.loadImages'] = False
		self.browser = PhantomJS()
		self.browser.implicitly_wait(10)

	def get_link(self):
		try:
			self.browser.get('http://leecher.us')
			self.browser.find_element_by_name('links').send_keys(self.url)
			self.browser.find_element_by_id('get_link').click()
			self.browser.find_element_by_xpath('//button[@class="subscribe"]').click()
			self.browser.switch_to_window(self.browser.window_handles[1])
			onclick = self.browser.find_element_by_xpath('//button[@class="subscribe"]').get_attribute('onclick')
		except (WebDriverException, NoSuchElementException):
			return False
		finally:
			self.browser.quit()
		m = re.search("'(http://[^']+)',", onclick)
		if not m:
			return False
		return m.group(1)
