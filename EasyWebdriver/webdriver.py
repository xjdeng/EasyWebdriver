#Warning: Under Construction!!!

try:
    from . import main
except ImportError:
    import main

from selenium import webdriver as oldwebdriver
from selenium.common.exceptions import ElementNotInteractableException, \
StaleElementReferenceException, ElementClickInterceptedException, \
NoSuchElementException, TimeoutException
import time

common_exceptions = (ElementNotInteractableException,\
                     StaleElementReferenceException,\
                     ElementClickInterceptedException,
                     NoSuchElementException,TimeoutException)
    
class webdriver(object):
    
    def __init__(self, browser, retry_delay = 0.1, retries = 100, \
                 final_delay = 0, debug = True):
        self.browser = browser
        self.retry_delay = retry_delay
        self.retries = retries
        self.final_delay = final_delay
        self.debug = debug
    
    def run(self, methodstr, *args, **kwargs):
        tries = 0
        e = Exception()
        while tries < self.retries:
            try:
                tmp = getattr(self.browser, methodstr)(*args, **kwargs)
                if self.debug == True:
                    print("Success! {}({}, {})").format(methodstr, args, kwargs)
                time.sleep(self.final_delay)
                return tmp
            except common_exceptions as e:
                if self.debug == True:
                    print("Exception! {}({}, {}) failed with {}".format(methodstr,\
                          args, kwargs, e))
                time.sleep(self.retry_delay)
                tries += 1
        if self.debug == True:
            print("Failed! {}({}, {}) failed with {}".format(methodstr, args,\
                  kwargs, e))
        raise(e)
                
        