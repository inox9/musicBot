# coding=utf8
'''
	premiumgeneratorlink.com direct link fetcher, uses phantomjs/selenium
	version 0.1
'''

import re
from selenium.webdriver import PhantomJS
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException, NoSuchElementException, TimeoutException

class Premiumgeneratorlink(object):
	def __init__(self, url):
		self.url = url
		self.browser = PhantomJS()

	def get_link(self):
		try:
			self.browser.get('http://premiumgeneratorlink.com/')
			self.browser.find_element_by_name('link').send_keys(self.url)
			self.browser.find_element_by_xpath('//a[@class="input"]').click()
			wdw = WebDriverWait(self.browser, 10)
			wdw.until(EC.element_to_be_clickable((By.ID, 'check'))).click()
			wdw.until(EC.element_to_be_clickable((By.ID, 'generate'))).click()
			link = wdw.until(EC.visibility_of_element_located((By.XPATH, '//form[@class="center"]'))).get_attribute('action')
		except (WebDriverException, NoSuchElementException, TimeoutException):
			return False
		finally:
			self.browser.quit()
		return link