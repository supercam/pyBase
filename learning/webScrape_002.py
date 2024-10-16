



"""
Selenium tutorial follow
uses chrome browser
then download webdriver
#make sure to grab the webdriver and place it in a location that will be remembered.



"""

from selenium import webdriver


#base example
#PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome()
driver.get("https://www.bionicnrg.com")

#close the tab doesn't close browser
#driver.close()

#get the title
print(driver.title)

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
