from fxn import *
me = Tracker()

from pyzbar.pyzbar import decode
from PIL import Image
food = 'photos/oatmeal2.jpg'

me.checkItem(food)
me.measure(food)
me.consume(food)
me.viewStats()

print()