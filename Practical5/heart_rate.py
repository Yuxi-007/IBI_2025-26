import matplotlib.pyplot as plt
#Put the data in it
heart_rate=[72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]
#Calculate munber and mean
num_patient=len(heart_rate)
mean=sum(heart_rate)/num_patient
print("Number of patients:", num_patient)
print("Mean heart rate:", mean)
#Catogerize and calculate the number in each group
low=0
normal=0
high=0

for hr in heart_rate:
    if hr<60:
        low+=1
    elif 60<=hr<120:
        normal+=1
    else :
        high+=1
print("Low:",low)
print("Normal:",normal)
print("High:",high)

category={"Low":low,"Normal":normal,"High":high}
largest=max(category,  key=category.get)
print(largest)
#Create pie chart
labels = category.keys()
sizes = category.values()

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Heart Rate Categories")
plt.show()