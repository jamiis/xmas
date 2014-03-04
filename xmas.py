from random import shuffle
family = ["Mom", "Clark", "Adrian", "Lauren", "Pace", "Jamey", "Ella"]
shuffle(family)
family.append(family[0]) # presents circular behavior better
print " -> ".join(family)
