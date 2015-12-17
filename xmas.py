from random import shuffle
family = ["McClark", "Sir Adrian", "Laurz", "Pathe", "King Jamis", "K-Town"]
shuffle(family)
family.append(family[0]) # presents circular behavior better
print " -> ".join(family)
