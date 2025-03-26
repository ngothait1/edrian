def check_if_digit(value):
    while not value.isdigit(): 
        print("The value: " + str(value) + " isn't a number please try again")
        value = input("Enter a valid value: ")  
    return int(value)   
  
def save_new_entry(the_people_dictionary: dict, total_ages: float, list_ids: list): 
    id = input("please enter a new id:") 
    id = check_if_digit(id)
    if id in the_people_dictionary:
        print(" Error id already exists: try input again ")
        return the_people_dictionary, total_ages, list_ids
    list_ids.append(id)
    age = input("please enter a new age:")
    age = check_if_digit(age)
    total_ages += age
    name = input("please enter name:")
    the_people_dictionary[id] = [name, age]
    print_people_data(age, name, id)
    print("Id " + str(id) + " saved successfully")
    return the_people_dictionary, total_ages, list_ids
    
   
def search_by_id(the_people_dictionary: dict):
    id = input("please enter the id:")
    id = check_if_digit(id)
    if id not in the_people_dictionary:
        print(str(id) + " id isn't in dictionary please try again:")
        return the_people_dictionary
    else:
        name, age = the_people_dictionary[id]
        print_people_data(age, name, id)
        return the_people_dictionary

def print_ages_average(the_people_dictionary: dict, total_ages: float):
    if len(the_people_dictionary) == 0:
        print("sorry we cant divide by Zero")
        return the_people_dictionary 
    else:
        average = total_ages / len(the_people_dictionary)
        print("The ages average is: " + str(average) )  
        return the_people_dictionary, total_ages
    
def print_all_names(the_people_dictionary: dict):
    for  id, (name, age) in the_people_dictionary.items():
        print_people_data(age, name, id)
    return the_people_dictionary
        

def print_all_ids(the_people_dictionary: dict,):
    count = 0
    for id, (name, age) in the_people_dictionary.items():
        print("the index is: " + str(count) )
        print_people_data(age, name, id)
        count = count + 1
    return the_people_dictionary

def print_all_entries(the_people_dictionary: dict ):
    count = 0
    for id, (name, age) in the_people_dictionary.items():
        print("the index is: " + str(count) )
        print_people_data(age, name, id)
        count = count + 1
    return the_people_dictionary

def print_entry_by_index(the_people_dictionary: dict, list_ids ):
    index = input("please enter the index  of value you want:")
    index = check_if_digit(index)
    if index > len(the_people_dictionary):
        print(index + " index is out of range  please try again")
        return the_people_dictionary, list_ids 
    elif index < 0:
        print(index + " is negative please try again:")
        return the_people_dictionary, list_ids  
    else:  
        id = list_ids[index]
        name, age = the_people_dictionary[id]
        print("the index is: " + str(index))
        print_people_data(age, name, list_ids[index])
    return the_people_dictionary, list_ids

def print_people_data(age: int, name: str, id: int):
    print("\n")
    print("the id is: " + str(id))
    print("the age is: " + str(age))
    print("the name is: " + name)
    print("\n")
def print_menu():
    print("1. save a new entry")
    print("2. search by id")
    print("3. print ages average")
    print("4. print all names")
    print("5. print all Ids")
    print("6. print all entries")
    print("7. print entry by index")
    print("8. exit")


def print_main(people_dictionary, ages_sum, list_ids):
    while True:
        print_menu() 
        choose_option = input("please choose an option:")
        if choose_option == "1":
            people_dictionary, ages_sum, list_ids = save_new_entry(people_dictionary, ages_sum, list_ids )
        elif choose_option == "2":
            search_by_id(people_dictionary)
        elif choose_option == "3":
            print_ages_average(people_dictionary, ages_sum)
        elif choose_option == "4":
            print_all_names(people_dictionary)
        elif choose_option == "5":
            print_all_ids(people_dictionary)
        elif choose_option == "6":
            print_all_entries(people_dictionary)
        elif choose_option == "7":
            print_entry_by_index(people_dictionary, list_ids)
        elif choose_option == "8":
            new_option = input("Are you sure?(y/n)?:")
            if new_option == 'y':
                break
            else:
                continue                                                                                   
        else:
            print("incorrect input the option isn't exists , please try again")
        input("Press Enter to continue...")
ages_sum_1 = 0
people_dictionary_1 = {}   
list_ids_1 = []
print_main(people_dictionary_1, ages_sum_1 , list_ids_1)


                                                                                                
                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                                                                                                                                         