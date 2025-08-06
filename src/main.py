from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import tomlkit


def check_timezone(check_tz):
    try:
        x = ZoneInfo(check_tz)
        return "Pass"
    except:
        print("Timezone does not exist: " + check_tz)
        return "Error"

def print_menu():
    print("""
    Possible actions: \n
    convert TIME - outputs conversions of time \n
    TIME - HH:MM format \n
    add TIMEZONE - adds TIMEZONE to output \n
    rm TIMEZONE - removes TIMEZONE from output \n
    TIMEZONE - IANA time zone \n
    exit - exits the program
    """)


running = True
while running:
    print_menu()
    currentaction = input(" >> ")

    if currentaction == "exit":
        running = False


