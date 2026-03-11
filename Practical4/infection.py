#Set the initial number	of infected individuals
#Set the growth rate
#Set the total number of students
#For each day:
#     calculate the new infected individuals
#     print the number
#     stop when infected individuals>= total number of students
#Print the total number of days needed
a = 5
growth_rate = 0.4
total = 91
day = 1
print("Day:", day)
while a <= total:
    a=a+a*growth_rate
    day=day+1
    print("Day:", day)
    print("new infected:",a)
print("All students infected after", day, "days.")
