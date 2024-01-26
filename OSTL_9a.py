import numpy as np

# Creating arrays: from lists and using built-in functions
# arrays from lists
distances = [10, 15, 17, 26, 20]
times = [0.3, 0.47, 0.55, 1.20, 1.0]
distances = np.array(distances)
times = np.array(times)

# speeds can be calculated as :
print(distances/times)

r1=distances/times
print(np.round(r1,2))

