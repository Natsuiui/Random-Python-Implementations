import random
import matplotlib.pyplot as plt

# Radius of Circle = 1 unit
# Therefore, Side of Square = 1 unit
# Step 1 - Generate random 'n' numbers, here 50000

n = 50000

# Keeping track of how many points are inside the circle and how many are outside
# Also kept a track of what points we took before already, so we don't induce dupes

inside = 0
outside = 0
points = []

# Generate n random points
for _ in range(n):

    # Uniform Distribution
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)

    # Check for duplicates
    if [x, y] not in points:

        # If points inside or on the Curve, increase count of inside
        if x ** 2 + y ** 2 < 1:
            inside += 1

            # Add point to the list of points inside the circle
            points.append([x, y])

        # Else increase the count of points outside
        else:
            outside += 1

# Value of pi will be the ratio of points inside and the total number of points taken, times four
print("Value of pi = ", inside / n * 4)

# Plot graph of points inside the circle!
plt.figure(figsize=(10, 10))
plt.scatter(*zip(*points))
plt.show()

