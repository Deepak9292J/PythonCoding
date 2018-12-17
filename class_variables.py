class Pound:
    value = 1.00
    color = "gold"
    num_edges = 1
    diameter = 22.5
    thickness = 3.5
    heads = True

coin1 = Pound() #coin1 is the object of class Pound
print(coin1.value)
print(coin1.color)
print(coin1.num_edges)
coin1.color = "greenish"
print(coin1.color)
