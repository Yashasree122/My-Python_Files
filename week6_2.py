import json
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import ssl

serviceurl = "http://python-data.dr-chuck.net/json?"
sample_address = "South Federal University"
data_address = "Columbia University"
address_wanted = data_address

parameters = {"sensor": "false", "address": address_wanted}
paramsurl = urllib.parse.urlencode(parameters)

queryurl = serviceurl + paramsurl
print("DATA URL: ", queryurl)

data = urllib.request.urlopen(queryurl).read()


jsondata = json.loads(str(data))
place_id = jsondata["results"][0]["place_id"]
print("PLACE ID: ", place_id)
