# import pyshortners package

import pyshorteners

url = input("Enter URL: \n")

the_shortner = pyshorteners.Shortener().tinyurl.short(url)

print("The shortened URL: ", the_shortner)
