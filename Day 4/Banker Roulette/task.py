import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Option 1
print(random.choice(friends))

# Option 2

random_from_list = random.randint(0, 4)
print(friends[random_from_list])