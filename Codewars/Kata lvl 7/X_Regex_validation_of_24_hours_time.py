"""
Write a regex to validate a 24 hours time string. See examples to figure out what you should check for:

Accepted: 01:00, 1:00, 00:00

Not accepted: 24:00, 13:1, 12:60

You should check for correct length and no spaces.
"""

one = "5"
two = 5
three = "05: 20"
four = "40:13"
five = "23:59"
six = "00:00"
seven = "10000"
eight = "1:45"
nine = "13:1"


# First solution
def validate_time(time):
    if not time or len(str(time)) < 4 or ":" not in time:
        return False

    hours= []
    for i in range(0, 24):
        if i <= 9:
            hours.append(f"0{i}")
            hours.append(f"{i}")
        else:
            hours.append(f"{i}")

    minutes = []
    for i in range(0, 60):
        if i <= 9:
            minutes.append(f"0{i}")
        else:
            minutes.append(f"{i}")

    validation = False
    value_given = time.split(":")

    if value_given[0] in hours and value_given[1] in minutes:
        validation = True

    return validation

print(validate_time(six))


# Second solution, saw that it wasn't necessary to create a huge list to check if in or not
def validate_time(time):
    if not time or len(time) < 4 or len(time) > 5 or ":" not in time or " " in time:
        return False

    value_given = time.split(":");

    if int(value_given[0]) >= 0 and int(value_given[0]) < 24 and int(value_given[1]) >= 0 and int(
            value_given[1]) < 60 and len(value_given[1]) == 2:
        return True
    else:
        return False