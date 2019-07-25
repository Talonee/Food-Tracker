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

urlLookUp = "https://api.nal.usda.gov/ndb/search/?format=json&q=QuakerInstantOatmeal,Apples&Cinnamon,BreakfastCereal,10PacketsPerBox(Packof4)&max=25&api_key=TehI0dSnyvPsNIBs8qWtWro29oghehy3LTkXDSIc"

with urllib.request.urlopen(urlLookUp) as url:
    data = json.loads(url.read().decode())

product = ""

result = data["list"]["item"]

for i in result:
    if i["ds"] == "SR" or i["ds"] == "BL":
        product = i["ndbno"]
        break

urlNutri = "https://api.nal.usda.gov/ndb/V2/reports?ndbno=" + product + "&type=b&format=json&api_key=TehI0dSnyvPsNIBs8qWtWro29oghehy3LTkXDSIc"

with urllib.request.urlopen(urlNutri) as url:
    data = json.loads(url.read().decode())


# print(json.dumps(data, indent=4, sort_keys=True))

filter = data["foods"][0]["food"]["nutrients"]
print(json.dumps(filter, indent=4, sort_keys=True))