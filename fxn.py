# Bar code reader
from pyzbar.pyzbar import decode
from PIL import Image

# API interpreter
import urllib.request
import json
import pprint

barInfo = decode(Image.open('photos/quakerbarcode.png'))
barCode = str(barInfo[0].data)[2:-1]

# keyNum = 0 # line placement of api key
# api_key = open(".gitignore/api_keys.txt", "r").readlines()
# print(api_key[keyNum])
# keyNum += 1
# print(api_key[keyNum])

# url = "https://api.barcodelookup.com/v2/products?barcode=" + barCode + "&formatted=y&key=" + api_key

# with urllib.request.urlopen(url) as url:
#     data = json.loads(url.read().decode())

# barcode = data["products"][0]["barcode_number"]
# print ("Barcode Number: ", barcode, "\n")

# name = data["products"][0]["product_name"]
# print ("Product Name: ", name, "\n")

# print ("Entire Response:")
# pprint.pprint(data)


url = "https://developer.nrel.gov/api/alt-fuel-stations/v1/nearest.json?api_key=TehI0dSnyvPsNIBs8qWtWro29oghehy3LTkXDSIc&location=Denver+CO"

with urllib.request.urlopen(url) as url:
    data = json.loads(url.read().decode())

print(data)