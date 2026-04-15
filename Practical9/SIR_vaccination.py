import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
# Parameters
N =10000
beta = 0.3
gamma = 0.05
time_points = 1000

# Initial population counts
S = N - 1
I = 1
R = 0

infected_history = [I]
def run_sir_with_vaccination(vaccination_rate):
    vaccinated = int(N * vaccination_rate)

    S = N - vaccinated - 1
    I = 1
    R = 0

    infected_history = [I]

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
        S = S - new_infections
        I = I + new_infections - new_recoveries
        R = R + new_recoveries

        infected_history.append(I)

    return infected_history



# Plot
plt.figure(figsize=(6, 4), dpi=150)
# 0%, 10%, 20%, ..., 100%
vaccination_rates = list(range(0, 101, 10))
colors = cm.viridis(np.linspace(0, 1, len(vaccination_rates)))

for i, v in enumerate(vaccination_rates):
    infected_curve = run_sir_with_vaccination(v / 100)

    if v == 0:
        label = "0"
    else:
        label = f"{v}%"

    plt.plot(infected_curve, color=colors[i], label=label)

plt.xlabel("time")
plt.ylabel("number of infected people")
plt.title("SIR model with different vaccination rates")
plt.legend()
plt.tight_layout()
plt.show()