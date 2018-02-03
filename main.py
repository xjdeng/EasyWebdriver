import os
from path import Path as path
from selenium.common.exceptions import WebDriverException
from selenium import webdriver

try:
    old_environ = os.environ["PATH"]
except KeyError:
    old_environ = ""
    
class EasyWebdriver(object):
    
    def __init__(self, webdriver_path = [], firefox_exe = ['firefox', \
                 'Firefox'], chrome_exe = ['chrome', 'Chrome']):
        self.webdriver_path = webdriver_path
        if isinstance(firefox_exe, str):
            self.firefox_exe = [firefox_exe]
        else:
            self.firefox_exe = firefox_exe
        if isinstance(chrome_exe, str):
            self.chrome_exe = [chrome_exe]
        else:
            self.chrome_exe = chrome_exe
    
    def add_chrome_exe(self, newexe):
        self.chrome_exe.append(newexe)
    
    def add_firefox_exe(self, newexe):
        self.firefox_exe.append(newexe)
    
    def add_webdriver_path(self, newpath):
        self.webdriver_path.append(path(newpath))
    
    def _prep(self):
        #https://stackoverflow.com/questions/1681208/python-platform-independent-way-to-modify-path-environment-variable
        os.environ["PATH"] = old_environ + os.pathsep + \
        os.pathsep.join(self.webdriver_path)
        
    def Firefox(self):
        self._prep()
        for f in self.firefox_exe:
            try:
                return webdriver.Firefox(f)
            except Exception:
                pass
        try:
            return webdriver.Firefox()
        except Exception as we:
            raise(we)
