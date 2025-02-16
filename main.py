import calendar 
import keyboard 
import time
import os

def clear_terminal():
    # Check if the system is Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux (posix systems)
    else:
        os.system('clear')
        
year = 2025
mon = 2
print("This is a calender!")
print("Press left arrow to go backwards")
print("Press Right arrow to go forwards")
print("Press escape to escape")
time.sleep(1)
print(calendar.month(year, mon))
while True:
    if keyboard.is_pressed("left_arrow"):
        if mon == 1:
            year -= 1
            mon = 12
        else:
            mon -= 1
        clear_terminal()
        print(calendar.month(year,mon))
        time.sleep(0.5)
    elif keyboard.is_pressed("right_arrow"):
        if mon == 12:
            mon = 1
        else:
            mon += 1
        clear_terminal()
        print(calendar.month(year,mon))
        time.sleep(0.5)
    elif keyboard.is_pressed("esc"):
        print("exiting the calender...")
        exit()