# Bar code reader
from pyzbar.pyzbar import decode
from PIL import Image

# API interpreter
import urllib.request
import json
import pprint

# API Keys file
from api_keys import key

limitNutrient = {
    "Biotin": ("mcg", 300), "Folate/Folic Acid": ("mcg", 400),
    "Niacin": ("mg", 20), "Pantothenic Acid": ("mg", 10),
    "Riboflavin": ("mg", 1.7), "Thiamin": ("mg", 1.5),
    "Vitamin A, IU": ("IU", 5000), "Vitamin B-6": ("mg", 2),
    "Vitamin B-12": ("mcg", 6), "Vitamin C, total ascorbic acid": ("mg", 60),
    "Vitamin D": ("IU", 400), "Vitamin E": ("IU", 30),
    "Vitamin K": ("mcg", 80), "Calcium": ("mg", 1000),
    "Chloride": ("mg", 3400), "Chromium": ("mcg", 120),
    "Copper": ("mg", 2), "Iodine": ("mcg", 150),
    "Iron": ("mg", 18), "Magnesium": ("mg", 400),
    "Manganese": ("mg", 2), "Molybdenum": ("mcg", 75),
    "Phosphorus": ("mg", 1000), "Potassium": ("mg", 3500),
    "Selenium": ("mcg", 70), "Sodium": ("mg", 2400),
    "Zinc": ("mg", 15), "Total lipid (fat)": ("g", 65, 80),
    "Fatty acids, total saturated": ("g", 20, 25),
    "Carbohydrate, by difference": ("g", 300, 375),
    "Fiber, total dietary": ("g", 25, 30), "Sugar": ("g", 50),
    "Cholesterol": ("mg", 300), "Caffeine": ("mg", 400)
}

intakeNutrient = {
    "Biotin": [0, 0, 0], "Folate/Folic Acid": [0, 0, 0],
    "Niacin": [0, 0, 0], "Pantothenic Acid": [0, 0, 0],
    "Riboflavin": [0, 0, 0], "Thiamin": [0, 0, 0],
    "Vitamin A, IU": [0, 0, 0], "Vitamin B-6": [0, 0, 0],
    "Vitamin B-12": [0, 0, 0], "Vitamin C, total ascorbic acid": [0, 0, 0],
    "Vitamin D": [0, 0, 0], "Vitamin E": [0, 0, 0],
    "Vitamin K": [0, 0, 0], "Calcium": [0, 0, 0],
    "Chloride": [0, 0, 0], "Chromium": [0, 0, 0],
    "Copper": [0, 0, 0], "Iodine": [0, 0, 0],
    "Iron": [0, 0, 0], "Magnesium": [0, 0, 0],
    "Manganese": [0, 0, 0], "Molybdenum": [0, 0, 0],
    "Phosphorus": [0, 0, 0], "Potassium": [0, 0, 0],
    "Selenium": [0, 0, 0], "Sodium": [0, 0, 0],
    "Zinc": [0, 0, 0], "Total lipid (fat)": [0, 0, 0],
    "Fatty acids, total saturated": [0, 0, 0],
    "Carbohydrate, by difference": [0, 0, 0],
    "Fiber, total dietary": [0, 0, 0], "Sugar": [0, 0, 0],
    "Cholesterol": [0, 0, 0], "Caffeine": [0, 0, 0]
}


def checkItem(food):
    barInfo = decode(Image.open(food))
    barCode = str(barInfo[0].data)[2:-1]
    
    uri = "https://api.barcodelookup.com/v2/products?"
    query = "barcode=" + barCode + "&formatted=y&key=" + key["barcode"]
    urlBar = uri + query

    # with urllib.request.urlopen(urlBar) as url:
    #     data = json.loads(url.read().decode())

    # barcode = data["products"][0]["barcode_number"]
    # print ("Barcode Number: ", barcode, "\n")

    # name = data["products"][0]["product_name"]
    # print ("Product Name: ", name, "\n")

    # print ("Entire Response:")
    # pprint.pprint(data)
    name = "Quaker Instant Oatmeal, Apples & Cinnamon, Breakfast Cereal, 10 Packets Per Box (Pack of 4)"
    name = name.replace(" ", "")

    return name


def measure(food, quantity):
    uri = "https://api.nal.usda.gov/ndb/search/?"
    query = "format=json&q=" + checkItem(food) + "&max=25&api_key=" + key["product"]
    urlFood = uri + query

    with urllib.request.urlopen(urlFood) as url:
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
    # print(json.dumps(filter, indent=4, sort_keys=True))

    eqv = str(filter[0]["measures"][0]["eqv"])
    unit = filter[0]["unit"]

    print("Showing results for one serving of " + eqv + unit)
    print("--------------------------")
    for i in filter:
        name = i["name"]
        value = str(i["measures"][0]["value"])
        # eqv = str(i["measures"][0]["eqv"])
        # unit = i["unit"]
        
        result = name + ": " + value + unit
        print(result)

    # return smth


def consume(food, quantity):
    nutrients = measure(food, quantity)


def viewStats():
    pass


# if vitamin in limitNutrient:
#     raise NameError

food = 'photos/quakerbarcode.png'

# checkItem(food)
# measure(food, 1)