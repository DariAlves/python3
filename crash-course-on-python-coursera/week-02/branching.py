def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long.")
    else: 
        print("Validate username")

def is_even(number):
    if number % 2 == 0:
        return True
    return False

# elif operator
def hint_username2(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long.")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long.")
    else: 
        print("Validate username")


# Modulo operator - This operator performs integer division, but only returns the remainder of this division operation