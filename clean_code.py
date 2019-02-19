
### Universely Recognize Variables ###
# Bad variable's names
em = ""
pwd = ""
usr = []
# Readable variables
email_addres = ""
password = ""
users = []


### Meaningfull names ###
# Lets take as an example a dividing function
def div(x, y):
    res = x / y
    return res

# You can use more meaningfull names to make the function more readable
def divided(dividend, divisor):
    result = dividend / divisor
    return result


### Organizing for redability ###
# The most important stuff should come first
# First Functions and Classes
def check_state(state):
    if state == "on":
        print("It is on")
    else:
        print("It is off")

# Then Independent Variables
state = "off"
# Then some Action
check_state(state)


### Simplify your conditional expressions ###
# You can do a conditional block like this
def canPersonDrive(person_age):
    if person_age >= 16:
        return True
    else:
        return False

# To clean this function a bit you could remove the else
def canPersonDrive2(person_age):
    if person_age >=  16:
        return True
    # Removing the else
    return False

# But the best option would be to remove the entire conditional block
def canPersonDrive3(person_age):
    return person_age >= 16


### Smaller functions are more clean and readable ###
# Function example
def close(door):
    door.grab_door_handle()
    door.twist_door_handle()
    door.push_door()
    door.release_door_handle()
    door.put_key()
    door.lock_door()

# Cleaner Function
def close_door(door):
    door.grab_door_handle().twist_door_handle()
    door.push_door().release_door_handle()
    # Locking the door
    lock_door(door)

def lock_door(door):
    door.put_key().lock_door()


### Limit the number of parameters on your functions and methods ###
# One bad function with a lot of parameters
def create_user(email, username, password, name, age, status, ipAddress):
    pass

# Calling this kind of functions could also be confusing
# Some developer that eventually would check this code would not know what "active" means
create_user("example@gmail.com", "lerroyjenkings", "456", "Scott", "18", "active", "127.0.0.1")

# This is an alternative way to do the same thing
# Using only one argument and a dictionary with user info
def create_user_easily(user):
    pass

user = {
    'email': "example@gmail.com",
    'username': "lerroyjenkings",
    'password': "456",
    'name': "Scott",
    'age': 18,
    'status': "active",
    'ipAddress': "127.0.0.1"
}

create_user_easily(user)

