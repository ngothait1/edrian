

def check_if_digit(value):
    while not value.isdigit(): 
        print("The value: " + str(value) + " isn't a number please try again")
        value = input("Enter a valid value: ")  
    return int(value)   


def check_if_int(number):
    while type(number) != int:
        print("type of number isn't int  please try to input again")
        number = check_if_digit(try_input("please enter a normal int number: "))
    return number


def try_input(string):
    try:
        input_value = input(string)
        return input_value
    except KeyboardInterrupt:
        print("you have pressed ctrl + c we are now exiting")
        return None
    

def check_if_alpha(value):
    while not value.isalpha():
        print("the value isn't a string try to type again please")
        value = str(input("please enter again and please enter a correct string: "))
    return str(value)


def check_if_in_dict(value, dictionary):
    while value in dictionary:
        print("the value is in dictionary please type id again: ")
        value = check_if_digit(try_input("please enter a normal value: "))
    return value