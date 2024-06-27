# Pounds(lbs) in Kilogram(kg) // Converting

weight = int(input("Enter your weight: "))
unit = input("Enter your unit in Pounds(L/l) or Kilograms(KG/kg): ")

if unit == "L" or "l":
    converted = weight * 0.45
    print(f"Your weight in Kilo is {converted}")
else:
    converted = weight * 0.85
    print(f"your weight in pounds is {converted}")