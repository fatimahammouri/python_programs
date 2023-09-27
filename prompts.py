"""
Helper function to calculate temperature using conversion formulas
depending on the user-inputted units
"""
def choose_formula(from_unit, to_unit, temp):
    if from_unit in ["c", "C"] and to_unit in ["f", "F"]:
        fahrenheit_temp = (temp * 9) / 5 + 32
        print(f"{temp:.2f}C = {fahrenheit_temp:.2f}F")

    elif from_unit in ["c", "C"] and to_unit in ["K", "k"]:
        kelvin_temp =  temp + 273.15
        print(f"{temp:.2f}C = {kelvin_temp:.2f}K")

    elif from_unit in ["F", "f"] and to_unit in ["c", "C"]:
        celsius_temp = (temp - 32) * 5 / 9
        print(f"{temp:.2f}F = {celsius_temp:.2f}C")

    elif from_unit in ["F", "f"] and to_unit in ["K", "k"]:
        kelvin_temp = (temp + 459.67) * 5 / 9
        print(f"{temp:.2f}F = {kelvin_temp:.2f}K")

    elif from_unit in ["K", "k"] and to_unit in ["F", "f"]:
        f_temp =  temp * 9 / 5 - 459.67
        print(f"{temp:.2f}K = {f_temp:.2f}F")
        
    elif from_unit in ["K", "k"] and to_unit in ["c", "C"]:
        c_temp = temp - 273.15
        print(f"{temp:.2f}K = {c_temp:.2f}C")

# Exit program function to exit any time user inputs "E"
def exit_program():
    print("Exiting the temperature conversion calculator.")
    show_calculater = False
    exit()

def enter_calculater():
    print("This is a temperature unit conversion calculator.\n It converts from/to Celsius, Fahrenheit, and Kelvin.")

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
            print("here in 1 move")
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



