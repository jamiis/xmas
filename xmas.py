from random import shuffle
family = ["Clark/Bethany", "Adrian", "Lauren/Brian", "Pace/Stacy", "Jamey", "Ella"]
shuffle(family)
family.append(family[0]) # presents circular behavior better
print " -> ".join(family)
