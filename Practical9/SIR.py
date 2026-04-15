import numpy as np
import matplotlib.pyplot as plt
# Parameters
N =10000
beta = 0.3
gamma = 0.05
time_points = 1000

# Initial population counts
S = N - 1
I = 1
R = 0

# Store history
S_history = [S]
I_history = [I]
R_history = [R]

#time loop
for t in range(time_points):
    # Probability that a susceptible person meets an infected person
    infection_prob = beta * (I / N)
    # Deal with infection
    if S > 0:
        new_infections_array = np.random.choice(
            [0, 1],
            size=S,
            p=[1 - infection_prob, infection_prob]
        )
        new_infections = np.sum(new_infections_array)
    else:
        new_infections = 0

    # Deal with recovrery
    if I > 0:
        new_recoveries_array = np.random.choice(
            [0, 1],
            size=I,
            p=[1 - gamma, gamma]
        )
        new_recoveries = np.sum(new_recoveries_array)
    else:
        new_recoveries = 0

    # Update counts
    S -= new_infections
    I += new_infections - new_recoveries
    R += new_recoveries

    # Record results
    S_history.append(S)
    I_history.append(I)
    R_history.append(R)


# Plot
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S_history, label="susceptible")
plt.plot(I_history, label="infected")
plt.plot(R_history, label="recovered")

plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model")
plt.legend()
plt.tight_layout()
plt.show()