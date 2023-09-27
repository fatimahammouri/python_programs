"""
Helper function to calculate temperature using conversion formulas
depending on the user-inputted units
"""
def choose_formula(from_unit, to_unit, temp):
    # case: if the user inpts same unit for FROM and TO units
    if from_unit.upper() == to_unit.upper():
        print(f"{temp:.2f}{from_unit.upper()} = {temp:.2f}{to_unit.upper()}")

    # case: if the user inputs from celsius to fahrenheit
    elif from_unit in ["c", "C"] and to_unit in ["f", "F"]:
        fahrenheit_temp = (temp * 9) / 5 + 32
        print(f"{temp:.2f}{from_unit.upper()} = {fahrenheit_temp:.2f}{to_unit.upper()}")

    # case: if the user inputs from celsius to kelvin 
    elif from_unit in ["c", "C"] and to_unit in ["K", "k"]:
        kelvin_temp =  temp + 273.15
        print(f"{temp:.2f}{from_unit.upper()} = {kelvin_temp:.2f}{to_unit.upper()}")

    # case: if the user inputs from fahrenheit to celsius 
    elif from_unit in ["F", "f"] and to_unit in ["c", "C"]:
        celsius_temp = (temp - 32) * 5 / 9
        print(f"{temp:.2f}{from_unit.upper()} = {celsius_temp:.2f}{to_unit.upper()}")

    # case: if the user inputs from fahrenheit to kelvin
    elif from_unit in ["F", "f"] and to_unit in ["K", "k"]:
        kelvin_temp = (temp + 459.67) * 5 / 9
        print(f"{temp:.2f}{from_unit.upper()} = {kelvin_temp:.2f}{to_unit.upper()}")

    # case: if the user inputs from kelvin to fahrenheit
    elif from_unit in ["K", "k"] and to_unit in ["F", "f"]:
        f_temp =  temp * 9 / 5 - 459.67
        print(f"{temp:.2f}{from_unit.upper()} = {f_temp:.2f}{to_unit.upper()}")

    # case: if the user inputs from kelvin to celsius   
    elif from_unit in ["K", "k"] and to_unit in ["c", "C"]:
        c_temp = temp - 273.15
        print(f"{temp:.2f}{from_unit.upper()} = {c_temp:.2f}{to_unit.upper()}")

# Exit program function to exit any time user inputs "E"
def exit_program():
    print("Exiting the temperature conversion calculator.")
    show_calculater = False
    exit()

def enter_calculater():
    print("This is a temperature unit conversion calculator.\nIt converts from/to Celsius, Fahrenheit, and Kelvin.\n \n")

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
        if from_unit in ["C", "c", "F", "f", "K", "k"]:
            first_move = False
            second_move = True
        else:
            print(f"[ERROR] Invalid temperature unit {from_unit}\nValid choices are:[Cc/Ff/Kk]")

    while second_move:
        to_unit = input("Enter TO temperature unit :[Cc/Ff/Kk]")
        if to_unit == "E":
            exit_program()
        if to_unit in ["C", "c", "F", "f", "K", "k"]:
            choose_formula(from_unit, to_unit, temp_number)
            second_move = False
        else:
            print(f"[ERROR] Invalid temperature unit {from_unit}\nValid choices are:[Cc/Ff/Kk]")
    
show_calculater = True
while show_calculater:
    enter_calculater()



