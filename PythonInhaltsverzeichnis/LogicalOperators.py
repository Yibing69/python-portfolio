# Beispiel

has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit: # and == Wenn 2 Bedingungen erfüllt sind
    print("Eligible for loan")

has_criminal_record = True
if has_good_credit and not has_criminal_record: # and not == Erste Bedingung soll erfüllt werden, zweite nicht
    print("Eligible for loan")
else:
    print("not eligible for loan")


# Beispiel 2

name = "J"
if len(name) < 3:
    print("Name must be at least 3 characters long")
elif len(name) > 30:
    print("Name must be at most 30 characters long")
else:
    print("Name looks good")