# import os
#
# from selenium import webdriver
# import codecs
# #set chromedriver.exe path
# driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
# driver.implicitly_wait(0.5)
# #maximize browser
# driver.maximize_window()
# #launch URL
# driver.get("https://finance.yahoo.com/portfolio/p_0/view/v1")
# #get file path to save page
# n=os.path.join("C:\\Users\\ghs6kor\\Downloads\\Test","Page.html")
# #open file in write mode with encoding
# f = codecs.open(n, "w", "utf−8")
# #obtain page source
# h = driver.page_source
# #write page source content to file
# file.write(h)
# #close browser
# driver.quit()

#_*_coding: utf-8_*_

# ========= good
import os
import sys
import tempfile

from h5py.h5t import cfg
from selenium import webdriver
# import time
#
# # start web browser
# browser=webdriver.Firefox()
#
# # get source code
# browser.get("https://finance.yahoo.com/portfolio/p_0/view/view_1")
# html = browser.page_source
# time.sleep(2)
# print(html)
#
# # close web browser
# browser.close()

# =================

def firefox(headless=True):
    """
    Context manager returning Selenium webdriver.
    Instance is reused and must be cleaned up on exit.
    """
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options
    if headless:
        driver_key = 'headless'
        firefox_options = Options()
        firefox_options.add_argument('-headless')
    else:
        driver_key = 'headed'
        firefox_options = None
    # Load profile, if it exists:
    if os.path.isdir(PROFILE_DIR):
        firefox_profile = webdriver.FirefoxProfile(PROFILE_DIR)
    else:
        firefox_profile = None
    if FIREFOX_INSTANCE[driver_key] is None:
        FIREFOX_INSTANCE[driver_key] = webdriver.Firefox(
            firefox_profile=firefox_profile,
            firefox_options=firefox_options,
        )
    yield FIREFOX_INSTANCE[driver_key]

oo = getWebDriver()
print(oo)