from collections import namedtuple

# color(R, G, B)
color = (55,155,255)
print(color[0])

# One way
color = {'red': 55, 'green': 155, 'blue': 255}
print(color['red'])

#-----------------------#
#     NAMED TUPLE       #
#-----------------------#

Color = namedtuple('Color', ['red', 'green', 'blue'])
color = Color(55, 155, 255) # or
color = Color(red=55, green=155, blue=255)
print(color.red)