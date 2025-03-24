
def save_new_entry(dictionary_all: dict, total_ages : int   ): 
    id = input("please enter a new id:") 
    if not id.isdigit():
        print("invaild input: you should enter a number " + str(id) + " isn't number")
        return dictionary_all, total_ages
    if id in dictionary_all:
        print(" Error id already exists: try input again ")
        return dictionary_all, total_ages
    id = int(id)
    age = input("please enter a new age:")
    if not age.isdigit():
        print("invaild input: you should enter a number " + str(id) + " isn't number")
        return dictionary_all, total_ages
    age = int(age)
    total_ages += age
    name = input("please enter name:")
    dictionary_all[id] = [name,age]
    print("the id is: " + str(id))
    print("the name is: " + name)
    print("the age is: " + str(age))
    print("Id " + str(id) + " saved successfully")
    print("the new dictionary is:" + str(dictionary_all) )
    return dictionary_all, total_ages
    
   
def search_by_id(dictionary_all: dict):
    id = input("please enter the id:")
    if not id.isdigit():
       print(str(id) + " isn't digit please try again:")
       return id
    id = int(id)
    if id not in dictionary_all:
       print(str(id) + " id isn't in dictionary please try again:")
       return id
    else:
          print("the id is :" + str(id))
          print("and the name and age is:" + str(dictionary_all[id]))


def print_ages_average(dictionary_all: dict, total_ages : float   ):
    if len(dictionary_all) == 0:
        print("sorry we cant divide by Zero")
        return dictionary_all, total_ages
    else:
        avg = total_ages / len(dictionary_all)
        print("The ages average is: " + str(avg) )  

def print_all_names(dictionary_all : dict):
    for i,(name, age) in enumerate(dictionary_all.values()):
        print("the name in position " + str(i) +  " is: " + str(name) )
        

def print_all_ids(dictionary_all : dict):
    count = 0
    for key in dictionary_all:
       print("the id in position " + str(count) + " is: " + str(key) )
       count += 1 
    
def print_all_entries(dictionary_all : dict ):
    for i, values in enumerate(dictionary_all.items()):
       print("The index of this entry is: " + str(i) + " and the entry is: " + str(values)  )

def print_entry_by_index(dictionary_all : dict):
    new_list = list(dictionary_all)
    index = input("please enter the index  of value you want:")
    if not index.isdigit():
        print(index + " isn't a digit try again:")
        return index
    index = int(index)
    if index > len(dictionary_all):
        print(index + " index is out of range  please try again")
        return index
    elif index < 0:
        print(index + " is negative please try again:")
        return index 
    else:  
        id_value = new_list[index] 
        print("the id is :" + str(id_value))
        print("and the name and age is:" + str(dictionary_all[id_value]))
 
def print_menu(new_dict, ages_sum):
 while True: 
     print("1. save a new entry")
     print("2. search by id")
     print("3. print ages average")
     print("4. print all names")
     print("5. print all Ids")
     print("6. print all entries")
     print("7. print entry by index")
     print("8. exit")
     choose_option = input("please choose an option:")
     if choose_option == "1":
        new_dict,ages_sum = save_new_entry(new_dict, ages_sum )
        input("Press Enter to continue...")
     elif choose_option == "2":
        search_by_id(new_dict)
        input("Press Enter to continue...")
     elif choose_option == "3":
        print_ages_average(new_dict, ages_sum)
        input("Press Enter to continue...")
     elif choose_option == "4":
        print_all_names(new_dict)
        input("Press Enter to continue...")
     elif choose_option == "5":
        print_all_ids(new_dict)
        input("Press Enter to continue...")
     elif choose_option == "6":
        print_all_entries(new_dict)
        input("Press Enter to continue...")
     elif choose_option == "7":
        print_entry_by_index(new_dict)
        input("Press Enter to continue...")
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
new_dict_1 = {}   

print_menu(new_dict_1, ages_sum_1)


                                                                                                
                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                                                                                                                                         