customer = {
    "name": "John Smith",
    "age": 30,
    "gender": "M",
}

print(customer.get("birthdate"))  # Gets the value from "birthdate" // Output: "None" (no value "in birthdate)

customer["birthdate"] = "Jan 1 1980"  # Adds "birthdate into "costumer" dictionary
print(customer["birthdate"])  # Output: Jan 1 1980
