#Warning: Under Construction!!!

try:
    from . import main
except ImportError:
    import main

from selenium import webdriver as oldwebdriver
    
class webdriver(object):
    
    def __init__(self, browser, retry_delay = 0.1, retries = 100, \
                 final_delay = 0, debug = True):
        self.browser = browser
        self.retry_delay = retry_delay
        self.retries = retries
        self.final_delay = final_delay
        self.debug = debug