import matplotlib.pyplot as plt

# Create empty arrays
X = []
Y = []

# Open file in read mode
inFile = open("projectileData.txt", "r")
for line in inFile:
    t, x, y, v_x, v_y = line.split(" ")
    X.append(float(x))
    Y.append(float(y))
inFile.close()

# Create the x vs y plot
plt.xlabel("$x$ (m)")
plt.ylabel("$y$ (m)")
plt.plot(X, Y)
plt.savefig("projectileTrajectory.eps")