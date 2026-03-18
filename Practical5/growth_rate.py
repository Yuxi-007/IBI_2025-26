import matplotlib.pyplot as plt
#Set a dictionary contains the data
population={
    "UK":{"2020":66.7,"2024":69.2},
    "China":{"2020":1426,"2024":1410},
    "Italy":{"2020":59.4,"2024":58.9},
    "Brazil":{"2020":208.6,"2024":212.0},
    "USA":{"2020":331.6,"2024":340.1}
}
#Get ready for put the rate in
changes = {}
#Calculate the rate
for country in population:
    pop2020 = population[country]["2020"]
    pop2024 = population[country]["2024"]

    change = (pop2024 - pop2020) / pop2020 * 100
    changes[country] = change

    print(country, "change:", change)
#Sort changes from large to small
sorted_changes = sorted(changes.items(), key=lambda x: x[1], reverse=True)

print("Sorted population changes:")
for country, change in sorted_changes:
    print(country, change)
#Identify largest
largest_increase = sorted_changes[0]
largest_decrease = sorted_changes[-1]

print("Largest increase:", largest_increase)
print("Largest decrease:", largest_decrease)
#Create the bar chart
countries = list(changes.keys())
values = list(changes.values())

plt.bar(countries, values)
plt.xlabel("Country")
plt.ylabel("Population change (%)")
plt.title("Population Growth (2020-2024)")
plt.show()