celsius = int(input("Enter an integer value for Celsius temperature: "))

def fahrenheit(parameter):
    return 1.8 * parameter + 32

print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(fahrenheit(celsius)))