import os
from selenium import webdriver

try:
    old_environ = os.environ["PATH"]
except KeyError:
    old_environ = ""
    
try:
    chromepath = os.environ['CHROME']
except KeyError:
    chromepath = None

try:
    firefoxpath = os.environ['FIREFOX']
except KeyError:
    firefoxpath = None
    
def Chrome(mypath = chromepath):
    if chromepath is not None:
        opts = webdriver.ChromeOptions()
        opts.binary_location = chromepath
        return webdriver.Chrome(options = opts)
    else:
        return webdriver.Chrome()

def Firefox(mypath = firefoxpath):
    if firefoxpath is not None:
        return webdriver.Firefox(firefox_binary = firefoxpath)
    else:
        return webdriver.Firefox()
    