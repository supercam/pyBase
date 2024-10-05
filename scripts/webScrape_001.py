



import requests
from bs4 import BeautifulSoup

"""
##HTTP requests is meant to either retrieve data form a specified URI -
or to push data to a server.  It works as request-repsonse protocol between client and server.
Get method is used to retrieve information fromt he given server using a given URI.
It sends the encoded user information appeneded to the page request.

"""

#make a get request
req = requests.get("https://www.geeksforgeeks.org/python-programming-language/")

##check status code for response
# success code - 200

print(req)

#print content of request
#print(req.content)

#parse the HTML
soup = BeautifulSoup(req.content, "html.parser")

s = soup.find("div", class_="entry-content")
content = s.find_all("in")


print(content)
