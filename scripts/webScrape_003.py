



"""
Selenium tutorial follow
uses chrome browser
then download webdriver
#make sure to grab the webdriver and place it in a location that will be remembered.

#when checking for elements
order to check
id - check first
name - check 2nd
class - least favorable because not unique

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#base example
#PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome()
driver.get("https://www.techwithtim.net")

#close the tab doesn't close browser
#driver.close()

#get the title
print(driver.title)

#search manually for s
# this was deprecated in version 4.3
#use driver.find_element()
#search = driver.find_element_by_name("s")

search = driver.find_element("name", "s")

search.send_keys("test")
search.send_keys(Keys.RETURN)

time.sleep(5)

#closes the browser
driver.quit()


"""
alternative that did not work
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

urls = [ "https://www.bionicnrg.com" ]

s = Service(r"C:\Program Files (x86)\chromedriver.exe")

for url in urls:
    driver = webdriver.chrome(service=s)
    driver.get(url)
"""
