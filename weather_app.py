#install requests and bs4 packages
#the url below is a confirmation proof of the py output result
#https://www.google.com/search?q=weather+in+lagos&oq=Weather+in+Lagos&aqs=chrome.0.0i131i433i512j0i512l9.616j0j7&sourceid=chrome&ie=UTF-8
  
import requests

from bs4 import BeautifulSoup

# the search strings can be updated to any location
search = "Weather in Lagos"
url = f"https://google.com/search?&q={search}"

r = requests.get(url)
s = BeautifulSoup(r.text, "html.parser")

update = s.find("div", class_="BNeawe").text
print(update)
