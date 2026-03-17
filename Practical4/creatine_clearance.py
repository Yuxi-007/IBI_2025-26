# Enter age, weight, gender and creatine concentration
# Check if inputs are within the ranges
# If not, print which variable needs to be corrected
# If they are in the range, calculate CrCl using the Cockcroft-Gault equation
# If gender is female multiply result by 0.85
# Print the creatine clearance rate

age = int(input("Enter age: "))
weight = float(input("Enter weight: "))
gender = input("Enter gender: ")
Cr = float(input("Enter creatine: "))
if age >= 100:
    print("Age must be less than 100 years")
if weight <= 20 or weight >= 80:
    print("Weight must be between 20 and 80 kg")
if Cr <= 0 or Cr >= 100:
    print("Creatine concentration must be between 0 and 100 µmol/l")
if gender != "male" and gender != "female":
    print("Gender must be 'male' or 'female'")
else:
    CrCl = ((140 - age) * weight) / (72 * Cr)
    if gender == "female":
        CrCl = CrCl * 0.85
    print("Creatine clearance rate:", CrCl)