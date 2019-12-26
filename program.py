from fxn import Tracker
me = Tracker()

food = 'photos/oatmeal2.jpg'

me.checkItem(food)
me.measure(food)
me.consume(food)

food = 'photos/7upbarcode.png'
me.checkItem(food)
me.measure(food, 3)
me.consume(food)
me.viewStats()