# EasyWebdriver

If you've installed Firefox or Chrome in non-standard locations on your system and you need to use the Selenium Webdriver, then this is the module for you!  Here are the steps:



1) Download and install Easywebdriver:

`git clone https://github.com/xjdeng/EasyWebdriver`

`cd EasyWebdriver`

`pip install .`



2) Download the webdrivers for Chrome and/or Firefox:

For Chrome: https://sites.google.com/a/chromium.org/chromedriver/downloads

For Firefox: https://github.com/mozilla/geckodriver/releases



3) Set your system variables:

- PATH: add to the path the location where you installed the webdrivers from Step 2
- CHROME: if you're using Chrome and it isn't installed at the default location on your system, set this variable to the new location.  Include the Chrome binary in this path!
- FIREFOX: same for Firefox - if it isn't installed at the standard location, set this to the location of the Firefox binary (including the binary itself in the path.)



4) Run the webdriver:

`import EasyWebdriver`

`Chrome = EasyWebdriver.Chrome()`

`Firefox = EasyWebdriver.Firefox()`

You can also pass keyword arguments for the Chrome and Firefox webdrivers in Selenium, e.g.:

`Firefox = EasyWebdriver.Firefox(timeout = 60)`