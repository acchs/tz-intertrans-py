from datetime import datetime, timezone, tzinfo
import time
from zoneinfo import ZoneInfo
#from tomlkit import parse, dumps


# Verify timezone is valid
def check_timezone(check_tz):
    try:
        ZoneInfo(check_tz)
        return "pass"
    except:
        print("Timezone does not exist: " + str(check_tz))
        return "error"


def convert_timezone(time_changed, to_timezone, from_timezone):
    if check_timezone(to_timezone) == "pass" and check_timezone(from_timezone) == "pass":
        to_timezone = ZoneInfo(to_timezone)
        from_timezone = ZoneInfo(from_timezone)
        from_time = time_changed.astimezone(from_timezone)
        converted_time = from_time.astimezone(to_timezone)
        return converted_time


def print_menu():
    print("""Possible actions: 
    conv TIME - outputs conversions of time 
    TIME - HH:MM format 
    add TIMEZONE - adds TIMEZONE to output 
    rm TIMEZONE - removes TIMEZONE from output 
    TIMEZONE - IANA time zone 
    ls - lists added timezones 
    exit - exits the program""")



timezones = [
    ]


# Process config file
configfile = open("config")
for lines in configfile:
    if len(lines.strip()) == 0 or lines[0] == "#":
        pass
    else:
        parsedline = lines.strip().split()
        zonename = parsedline[0]
        try:
            parsedline[1]
            comment = parsedline[1]
        except:
            comment = ""
        timezones.append([zonename, comment])


running = True
while running:
    print_menu()
    currentaction = input(" >> ")
    print("")
    currentaction = currentaction.strip().split()


    if currentaction[0] == "exit":
        running = False


    elif currentaction[0] == "add":
        # Verifying input
        try:
            currentaction[1]
            has_input = True
            try:
                currentaction[2]
                has_additional = True
            except:
                has_additional = False
        except:
            print("Please input a timezone.")
            has_input = False
        
        # Adding timezone and location name
        if has_input == True and check_timezone(currentaction[1]) == "pass":
            zonename = currentaction[1]
            if has_additional == False:
                comment = ""
            else:
                comment = currentaction[2]
            timezones.append([zonename, comment])
            print("Success!")


    elif currentaction[0] == "rm":
        # Verifying input
        try:
            currentaction[1]
            has_input = True
        except:
            print("Please input a timezone or location.")
            has_input = False

        if has_input:
            for zones in timezones:
                removeterm = currentaction[1]
                if zones[0] == removeterm or zones[1] == removeterm:
                    timezones.remove(zones)
                    print("Success!")


    elif currentaction[0] == "ls":
        for zones in timezones:
            if zones[1] == "":
                print(zones[0])
            else:
                print(zones[1] + " (" + zones[0] + ")")

    elif currentaction[0] == "conv":
        # Verifying output
        try:
            currentaction[1]
            has_input = True
        except:
            has_input = False

        # Process time or now time
        if has_input == True:
            # Recombine input
            try:
                input_time = datetime.strptime(currentaction[1], "%H:%M")
            except:
                print("Format not right")

        else:
            # If no additional input is given
            input_time = datetime.now(timezone.utc)
            input_timezone = "UTC"

        # Convert time
        for zones in timezones:
            converted = convert_timezone(input_time, zones[0].strip(), input_timezone)
            if zones[1] == "":
                print(zones[0] + ": " + str(converted.strftime("%Y-%m-%d %H:%M %z")))
            else:
                print(zones[1] + " (" + zones[0] + "): " + str(converted.strftime("%Y-%m-%d %H:%M %z")))

    else:
        print("Command not found")
    print("")


print("Thank you for using this program...")

