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
    "Vitamin D": ("IU", 400), "Vitamin E (alpha-tocopherol)": ("IU", 30),
    "Vitamin K": ("mcg", 80), "Calcium, Ca": ("mg", 1000),
    "Chloride": ("mg", 3400), "Chromium": ("mcg", 120),
    "Copper": ("mg", 2), "Iodine": ("mcg", 150),
    "Iron, Fe": ("mg", 18), "Magnesium, Mg": ("mg", 400),
    "Manganese": ("mg", 2), "Molybdenum": ("mcg", 75),
    "Phosphorus, P": ("mg", 1000), "Potassium, K": ("mg", 3500),
    "Selenium": ("mcg", 70), "Sodium, Na": ("mg", 2400),
    "Zinc, Zn": ("mg", 15), "Total lipid (fat)": ("g", 65, 80),
    "Fatty acids, total saturated": ("g", 20, 25),
    "Carbohydrate, by difference": ("g", 300, 375),
    "Fiber, total dietary": ("g", 25, 30), "Sugars, total": ("g", 50),
    "Cholesterol": ("mg", 300), "Caffeine": ("mg", 400)
}

intakeNutrient = {
    "Biotin": [0, 0, 0], "Folate/Folic Acid": [0, 0, 0],
    "Niacin": [0, 0, 0], "Pantothenic Acid": [0, 0, 0],
    "Riboflavin": [0, 0, 0], "Thiamin": [0, 0, 0],
    "Vitamin A, IU": [0, 0, 0], "Vitamin B-6": [0, 0, 0],
    "Vitamin B-12": [0, 0, 0], "Vitamin C, total ascorbic acid": [0, 0, 0],
    "Vitamin D": [0, 0, 0], "Vitamin E (alpha-tocopherol)": [0, 0, 0],
    "Vitamin K": [0, 0, 0], "Calcium, Ca": [0, 0, 0],
    "Chloride": [0, 0, 0], "Chromium": [0, 0, 0],
    "Copper": [0, 0, 0], "Iodine": [0, 0, 0],
    "Iron, Fe": [0, 0, 0], "Magnesium, Mg": [0, 0, 0],
    "Manganese": [0, 0, 0], "Molybdenum": [0, 0, 0],
    "Phosphorus, P": [0, 0, 0], "Potassium, K": [0, 0, 0],
    "Selenium": [0, 0, 0], "Sodium, Na": [0, 0, 0],
    "Zinc, Zn": [0, 0, 0], "Total lipid (fat)": [0, 0, 0],
    "Fatty acids, total saturated": [0, 0, 0],
    "Carbohydrate, by difference": [0, 0, 0],
    "Fiber, total dietary": [0, 0, 0], "Sugars, total": [0, 0, 0],
    "Cholesterol": [0, 0, 0], "Caffeine": [0, 0, 0],
    "Fatty acids, total monounsaturated": [0, 0, 0],
    "Fatty acids, total polyunsaturated": [0, 0, 0],
    "Fatty acids, total trans": [0, 0, 0]
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


def measure(food, quantity = 1, show = True):
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

    eqv = str(filter[0]["measures"][0]["eqv"] * quantity)
    unit = filter[0]["unit"]

    nutrition = {}

    if show:
        print("Showing results for", str(quantity), "serving(s) (" + eqv + unit + ")")
        print("--------------------------")

    for i in filter:
        name = i["name"]
        value = float(i["measures"][0]["value"]) * quantity

        nutrition[name] = [unit, value]
        
        if show:
            result = name + ": " + str(value) + unit
            print(result)

    return nutrition


def consume(food, quantity = 1):
    nutrition = measure(food, show = False)
    
    for i in nutrition:
        if i != "Water" and i != "Energy" and i != "Protein":
            if nutrition[i][0] == "g" or nutrition[i][0] == "IU":
                intakeNutrient[i][0] += nutrition[i][1] * quantity
            elif nutrition[i][0] == "mg":
                intakeNutrient[i][1] += nutrition[i][1] * quantity
            elif nutrition[i][0] == "mcg":
                intakeNutrient[i][2] += nutrition[i][1] * quantity



def viewStats():
    for i in intakeNutrient:
        intakeNutrient[i] = [round(num, 3) for num in intakeNutrient[i]]
        # print(i + ": " + str([round(num, 3) for num in intakeNutrient[i]]))
    
    print(intakeNutrient)





# if vitamin in limitNutrient:
#     raise NameError

food = 'photos/quakerbarcode.png'

checkItem(food)
# measure(food)
consume(food, 3)
# consume(food)
# consume(food)
viewStats()