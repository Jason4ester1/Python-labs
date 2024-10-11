import random

#example 1
print(random.randint(1, 100))
print(random.randrange(1, 10)) 
#example 2
print(random.randrange(1, 10, 2))
print(random.randrange(0, 101, 10))
#example 3
print(random.choice('computer'))  
print(random.choice([12,23,45,67,65,43]))
print(random.choice((12,23,45,67,65,43)))
aList = [20, 40, 80, 100, 120]
sampled_list = random.sample(aList, 3)
print(sampled_list)
#example 4
num_list = random.sample(range(100), 5)
print(num_list)