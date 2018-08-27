import random

class Butterfly():
    def __init__(self, value):
        self.value = value
        self.age = 0

    def updateTime(self):
        ++self.age

    def multiply(self):
        return Butterfly(random.normalvariate(self.value, 0.01))


nature = []
for i in range(100):
    value = random.random()
    nature.append(Butterfly(value))

virusRange = 0.01
virus = 0.2
step = (1-0.2) / (10000)

for times in range(1000 * 10000):
    virus += step
    print(len(nature), nature[0].value)
    i = 0
    while (i < len(nature)):
        butterfly = nature[i]
        if butterfly.value > virus + virusRange or butterfly.value < virus - virusRange:
            # print('remove')
            nature.remove(butterfly)
            continue
        butterfly.age += 1
        # print(butterfly.age)
        if butterfly.age > 27 and butterfly.age < 40 and butterfly.age % 3 == 0 and len(nature) < 10000:
            # print('add')
            nature.append(butterfly.multiply())
        elif butterfly.age == 78:
            # print('remove')
            nature.remove(butterfly)
            continue
        i += 1

# print(random.normalvariate(0.2, 0.01))
#
# a = [1, 2, 3]
# i = 0
# while (i < len(a)) :
#
#     if a[i] == 1:
#         a.append(4)
#     elif a[i] == 3:
#         del(a[i])
#     i += 1
#     print(a)