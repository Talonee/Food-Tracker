# Food-Tracker
Track food intake using bar codes

_Disclaimer: The program runs but doesn't work properly 100% of the time due to difficulty with the USDA's API. Conversion between barcode and product isn't always accurate, so success rate is more like 20%..._

## Project Description
This project will track down food item using bar code, find its nutrition values, and evaluate the user's daily nutrition intake. 


## Technical Description

1. Scan and decode barcode images using the library pyzbar.
2. Look for product's name using the barcode API, provided by [Barcode Lookup](https://www.barcodelookup.com/).
3. Look for product's nutrition values using USDA API, provided by [USDA](https://ndb.nal.usda.gov/ndb/).
4. Determine recommended nutrition intake, provided by FDA.
    - [Vitamins + Minerals](https://www.accessdata.fda.gov/scripts/InteractiveNutritionFactsLabel/factsheets/Vitamin_and_Mineral_Chart.pdf) 
    - [Other nutrients](https://www.accessdata.fda.gov/scripts/InteractiveNutritionFactsLabel/pdv.html)
5. Tracks nutrition intake.

## File Description

* `program.py` - Create and run the Tracker class
* `fxn.py` - Manage the Tracker class
* `photos` - Folder containing barcode pictures.