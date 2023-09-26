# Helper functions for conversion formulas

def celsius_to_fahrenheit(c_temp):
    fahrenheit_temp = (c_temp * 9) / 5 + 32
    return fahrenheit_temp

def celsius_to_kelvin(c_temp):
    kelvin_temp =  c_temp + 273.15
    return kelvin_temp

def fahrenheit_to_celsius(f_temp):
    celsius_temp = (f_temp - 32) * 5 / 9
    return celsius_temp

def fahrenheit_to_kelvin(f_temp):
    kelvin_temp = (f_temp + 459.67) * 5 / 9
    return kelvin_temp

def kelvin_to_fahrenheit(k_temp):
    f_temp =  k_temp * 9 / 5 - 459.67
    return f_temp

def kelvin_to_celsius(k_temp):
    c_temp = k_temp - 273.15
