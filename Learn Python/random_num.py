import random

#-------------------------------------------------
#   Random Floating Point Value between 0 and 1
#-------------------------------------------------
value = random.random()

#-------------------------------------------------
#   Random Floating Point Value between Range
#-------------------------------------------------
value = random.uniform(1,10)

#-------------------------------------------------
#   Random Whole Value between Range
#   randint(x, y)
#   x -> included
#   y -> included
#-------------------------------------------------
value = random.randint(1,6)

#-------------------------------------------------
#   Random value from a given List
#-------------------------------------------------
greeting = ['Hi', 'Hello', 'Howdy', 'Hey']
value = random.choice(greeting)
# print(value, 'Hasan')

#-------------------------------------------------
#   Random values from a given List
#   @param k: how many times to pick rand value
#   @param weights: chances to occur
#-------------------------------------------------
color = ['Red', 'Blue', 'Green']
results = random.choices(color, k=10, weights=[18, 18, 2])
# print(results)

#-------------------------------------------------
#   shuffle(): Shuffle the list in place.
#   sample():  Gives unique sample from a list.
#-------------------------------------------------
deck = list(range(1, 53))
random.shuffle(deck)
hand = random.sample(deck, k=5)
print(hand)