# Boolean sind zwei build-in constants "True" oder False"

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


print(is_even(4))  # Output: True
print(is_even(5))  # Output: False

# Oder


is_raining = True
is_sunny = False

if is_raining:
    print("Vergiss dein Regenschirm nicht!")
else:
    print("Die Sonne scheint")

# Output: Vergiss dein Regenschirm nicht!
