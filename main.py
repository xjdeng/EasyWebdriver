import os
from selenium import webdriver
    
try:
    chromepath = os.environ['CHROME']
except KeyError:
    chromepath = None

try:
    firefoxpath = os.environ['FIREFOX']
except KeyError:
    firefoxpath = None
    
def Chrome(*args, mypath = chromepath,  **kwargs):
    if chromepath is not None:
        opts = webdriver.ChromeOptions()
        opts.binary_location = chromepath
        return webdriver.Chrome(*args, options = opts, **kwargs)
    else:
        return webdriver.Chrome(*args, **kwargs)

def Firefox(*args, mypath = firefoxpath, **kwargs):
    if firefoxpath is not None:
        return webdriver.Firefox(*args, firefox_binary = firefoxpath, **kwargs)
    else:
        return webdriver.Firefox(*args, **kwargs)
    