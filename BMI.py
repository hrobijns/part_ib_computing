# ask the user for their weight, and the unit which this is in:

unit = input("Which unit system would you like to use for weight? (metric or imperial) ")
if unit != "metric" and unit != "imperial":
    unit = input("Not recognised, choose 'metric' or 'imperial': ")

if unit == "metric":
    weight = float(input("What is your weight, in kg: "))

# convert the weight to kg if it is given in stones
else:
    weight = float(input("What is your weight, in stones (using decimal places to represent the pounds): ")) * 6.35

# ask the user for their height, and the unit which this is in:
unit = input("Which unit system would you like to use for height? (metric or imperial) ")
if unit != "metric" and unit != "imperial":
    unit = input("Not recognised, choose 'metric' or 'imperial': ")

if unit == "metric":
    height = float(input("What is your height, in cm: "))

# convert the height to cm if it is given in stones
else:
    height = float(input("What is your height, in feet (using decimal places to represent the inches): "))
    height = height * 30.48                   

# adjust height to metres
height = height/100
                   
# calculate BMI, and round it to two decimal places
BMI = weight / (height**2)
BMI = round(BMI, 2)

# print it for the user, as well as what range they're in.
print("Your BMI is: " + str(BMI))

if BMI < 19:
    print("This is underweight")

elif BMI > 25:
    print("This is overweight")

else:
    print("This is a healthy weight")
