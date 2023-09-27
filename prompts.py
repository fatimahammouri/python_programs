def choose_formula(from_unit, to_unit, temp_number):
    pass

def exit_program():
    print("Exiting the temperature conversion calculator.")
    exit()

print(
"""This is a temperature unit conversion calculator.
It converts from/to Celsius, Fahrenheit, and Kelvin.
      
""")

temp_prompt = input("Enter a temperature(number), or E to exit: ")

if temp_prompt == "E":
    exit_program()

temp_number = float(temp_prompt)

first_move = True
second_move = False

while first_move:
    from_unit = input("Enter FROM temperature unit :[Cc/Ff/Kk]")
    if from_unit == "E":
        exit_program()
    if from_unit in "CcFfKk":
        first_move = False
        second_move = True
    else:
        print(f"[ERROR] Invalid temperature unit {from_unit} /n Valid choices are:[Cc/Ff/Kk]")

while second_move:
    to_unit = input("Enter TO temperature unit :[Cc/Ff/Kk]")
    if from_unit == "E":
        exit_program()
    if to_unit in "CcFfKk":
        choose_formula(from_unit, to_unit, temp_number)
        second_move = False
    else:
        print(f"[ERROR] Invalid temperature unit {from_unit} /n Valid choices are:[Cc/Ff/Kk]")
 




