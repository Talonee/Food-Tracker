# Food-Tracker
Track food intake using bar codes


## Project Description
This project will track down food item using the product's bar code, find its nutrition values, and evaluate the user's daily nutrition intake. 


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
