# coding=utf8
'''
	Leecher.us direct link fetcher, uses phantomjs/selenium
	version 0.1
'''

from selenium.webdriver import PhantomJS
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException, NoSuchElementException, TimeoutException

class Leecherus(object):
	def __init__(self, url):
		self.url = url
		self.browser = PhantomJS()

	def get_link(self):
		try:
			self.browser.get('http://leecher.us')
			wdw = WebDriverWait(self.browser, 10)
			wdw.until(EC.visibility_of_element_located((By.NAME, 'link'))).send_keys(self.url)
			wdw.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="subscribe"]'))).click()
			wdw.until(EC.element_to_be_clickable((By.ID, 'get_link'))).click()
			self.browser.switch_to_window(self.browser.window_handles[1])
			url = wdw.until(EC.presence_of_element_located((By.XPATH, '//a[@title="click here to download"]'))).get_attribute('href')
		except (WebDriverException, NoSuchElementException, TimeoutException):
			return False
		finally:
			self.browser.quit()
		return url
