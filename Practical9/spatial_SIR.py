import numpy as np
import matplotlib.pyplot as plt
# create an all 0 group
population = np.zeros((100, 100))
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1
# add color
plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
# model parameters
beta = 0.3
gamma = 0.05
# store snapshots for selected times
snapshot_times = [0, 10, 50, 100]
snapshots = {0: population.copy()}

# time loop
for t in range(1, 100 + 1):

    # find infected points
    infectedIndex = np.where(population == 1)

    # loop through all infected points
    for i in range(len(infectedIndex[0])):
        # get x, y coordinates for each infected point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]

        # infect each neighbour with probability beta
        # infect all 8 neighbours
        for xNeighbour in range(x - 1, x + 2):
            for yNeighbour in range(y - 1, y + 2):
                # do not infect the cell itself
                if (xNeighbour, yNeighbour) != (x, y):
                    # make sure indices stay inside the grid
                    if 0 <= xNeighbour < 100 and 0 <= yNeighbour < 100:
                        # only infect neighbours that are susceptible
                        if population[xNeighbour, yNeighbour] == 0:
                            population[xNeighbour, yNeighbour] = np.random.choice(
                                range(2), 1, p=[1 - beta, beta]
                            )[0]

        # allow infected individual to recover with probability gamma
        recover = np.random.choice(range(2), 1, p=[1 - gamma, gamma])[0]
        if recover == 1:
            population[x, y] = 2

    # save selected snapshots
    if t in snapshot_times:
        snapshots[t] = population.copy()

# plot results
fig, axes = plt.subplots(2, 2, figsize=(8, 8), dpi=150)

for ax, time in zip(axes.ravel(), snapshot_times):
    ax.imshow(snapshots[time], cmap="viridis", interpolation="nearest")
    ax.set_title(f"time = {time}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

plt.suptitle("Spatial SIR model")
plt.tight_layout()
plt.show()