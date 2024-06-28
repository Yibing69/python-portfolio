customer = {
    "name": "John Smith",
    "age": 30,
    "gender": "M",
}

print(customer.get("birthdate"))  # Gets the value from "birthdate" // Output: "None" (no value "in birthdate)

customer["birthdate"] = "Jan 1 1980"  # Adds "birthdate into "costumer" dictionary
print(customer["birthdate"])  # Output: Jan 1 1980

# Example
phone = input("Phone")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for x in phone:
    output += digits_mapping.get(x, "!") + " "
print(output)
