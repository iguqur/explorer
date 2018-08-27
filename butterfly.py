import random

class Butterfly():
    def __init__(self):
        self.value = random.random()

    def multiply(self):
        pass

butterfly = Butterfly()

print(butterfly.value)
exp = 4
var = 1
x = random.normalvariate(exp, var)
print(x)