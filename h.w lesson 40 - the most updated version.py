#1- save a new entry : key : id , values : age,name
#2 - search by id 
#3 - prints ages average
#4 - print all names
#5 - print all ids
#6 - print all entries
#7 - print entry by index
#8 - exit 
#number = input(" please enter a number: ")
#number.isdigit() 
def save_new_entry(dictionary: dict , dict_two : dict , total_ages : int   ): 
    id = input("please enter a new id:") 
    if not id.isdigit():
        print("invaild input: you should enter a number " + str(id) + " isn't number")
        return dictionary, dict_two, total_ages
    elif id in dictionary:
        print(" Error id already exists: try input again ")
        return dictionary, dict_two, total_ages
    id = int(id)
    age = input("please enter a new age:")
    if not age.isdigit():
        print("invaild input: you should enter a number " + str(id) + " isn't number")
        return dictionary, dict_two, total_ages
    age = int(age)
    total_ages += age
    name = input("please enter name: ")
    dict_two[id] = [name]
    dictionary[id] = [name,age]
    print("the id is: " + str(id))
    print("the name is: " + name)
    print("the age is: " + str(age))
    print("Id " + str(dictionary.keys()) + " saved successfully")
    print("the new dict is:" + str(dictionary) )
    return dictionary , dict_two , total_ages
    
   
def search_by_id(dictionary: dict):
    id = input("please enter the id:")
    if not id.isdigit():
       print(id + " isn't digit please try again: ")
       return id
    id = int(id)
    if id  not in dictionary:
       print(id + " id isn't in dictionary please try again: ")
       return id
    else:
         print("The whole entry  in this id is: (" + str(id) +  " , " + str(dictionary[id]) + ")")


def print_ages_average(dictionary: dict, total_ages : float   ):
    if len(dictionary) == 0:
        print("sorry we cant divide by Zero")
        return dictionary, total_ages
    else:
        avg = total_ages / len(dictionary)
        print(avg)  

def print_all_names(dict_two : dict):
    for count, name in enumerate(dict_two.values()):
        print("the name in position " + str(count) +  " is: " + str(name) )

def print_all_ids(dictionary : dict):
    count = 0
    for key in dictionary:
       print("the id in position " + str(count) + " is: " + str(key) )
       count = count + 1
def print_all_entries(dictionary : dict ):
    for i, values in enumerate(dictionary.items()):
       print("The index of this entry is: " + str(i) + " and the entry is: " + str(values)  )

def print_entry_by_index(dictionary : dict):
    new_list = list(dictionary.items())
    index = input(" please enter the index  of value you want: ")
    if not index.isdigit():
        print(index + " isn't a digit try again:")
        return index
    index = int(index)
    if index > len(dictionary):
        print(index + " index is out of range  please try again")
        return index
    elif index < 0:
        print(index + " is negative please try again:")
        return index 
    else:
        print("the entry in index " + str(index) + " is: " + str(new_list[index]))
 
def print_menu(new_dict  , second_dict , ages_sum   ):
 while True: 
     print(" 1. save a new entry")
     print(" 2. search by id ")
     print(" 3. print ages average")
     print(" 4. print all names")
     print(" 5. print all Ids")
     print(" 6. print all entries")
     print(" 7. print entry by index ")
     print(" 8. exit ")
     choose_option = input(" please choose an option:")
     if choose_option == "1":
        new_dict,second_dict,ages_sum = save_new_entry(new_dict, second_dict, ages_sum )
     elif choose_option == "2":
        search_by_id(new_dict)
     elif choose_option == "3":
        print_ages_average(new_dict, ages_sum)
     elif choose_option == "4":
        print_all_names(second_dict )
     elif choose_option == "5":
        print_all_ids(new_dict)
     elif choose_option == "6":
        print_all_entries(new_dict)
     elif choose_option == "7":
        print_entry_by_index(new_dict)
     elif choose_option == "8":
        new_option = input("Are you sure?(y/n)?:")
        if new_option == "y":
            break
        else:
            continue
     else:
        print("incorrect input the option isn't exists , please try again ")

ages_sum_1 = 0
second_dict_1 = {}
new_dict_1 = {}   

print_menu(new_dict_1, second_dict_1, ages_sum_1)


#user_input = input("please enter ")