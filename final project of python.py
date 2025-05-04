
import pandas as pd
import os
from Student import Student
from Person import Person
from employee import Employee
from enumerate import choice
import library_functions as library
from exception_class import Invalid_Menu_Option

def save_new_entry(the_people_dictionary: dict, user_input: str):
        user_input = input("do you want to save a Person, Student, or Employee?:")
        if user_input == "Person":
            id_input = library.check_if_in_dict(library.check_if_digit(library.try_input("please enter an id: ")) , the_people_dictionary)
            the_people_dictionary[id_input] = Person()
            print(the_people_dictionary)
        elif user_input == "Student":
            id_input = library.check_if_in_dict(library.check_if_digit(library.try_input("please enter an id: ")) , the_people_dictionary)
            the_people_dictionary[id_input] = Student()
            print(the_people_dictionary)
        elif user_input == "Employee":
            id_input = library.check_if_in_dict(library.check_if_digit(library.try_input("please enter an id: ")) , the_people_dictionary)
            the_people_dictionary[id_input] = Employee()
            print(the_people_dictionary)
        else:
            print("invalid input please try again")
        return the_people_dictionary, user_input
    

def print_entries_polimyarizm(the_people_dicitionary: dict):
    for list_people in the_people_dicitionary.values():
            type_class = list_people.get_type() 
            print(f"the type of class is {type_class}")
            print(list_people.__str__())
            




def save_all_data(the_people_dictionary: dict):
    user_input = None      
    data_list = []
    user_input = library.check_if_alpha(library.try_input("Choose which class to export to CSV: Person, Student, or Employee: "))
    if user_input == "Person":
        columns = ["age", "name", "id"]
    elif user_input == "Student":
        columns = ["age", "name", "id", "field_study", "year_study", "score_average"]
    elif user_input == "Employee":
         columns = ["age", "name", "id", "field_work", "salary"]
    else:
        print("invalid input")


    for person in the_people_dictionary.values():
        if person.get_type_str() == user_input:
            print(person.get_type_str())
            if user_input == "Person":
                row = [person.get_age(), person.get_name(), person.get_id()]
            elif user_input == "Student":
                row = [person.get_age(), person.get_name(), person.get_id(), person.get_field_of_study(), person.get_year_study(), person.get_score_average()]
           
            elif user_input == "Employee":
                row = [person.get_age(), person.get_name(), person.get_id(), person.get_field_work(), person.get_salary()]
            data_list.append(row)

    df = pd.DataFrame(data_list ,columns = columns)
    file_name = input("What is your output file name? : ")
    output_path = os.path.join("C:\\Users\\edrik_cgifjkr\\Desktop\\Nadav gothait visual studio codes\\final project of python lesson 66\\", file_name + ".csv")
    df.to_csv(output_path, index = False)
    print("Data saved successfully to " + output_path)

        
def print_menu():
    print("1. save a new entry")
    print("2. print all entries using polymyarizm")
    print("3. Save all data")
    print("4. exit")


def run_main(people_dictionary, user_all_inputs):
    while True:
            try:
                print_menu() 
                choose_option = (library.try_input("please choose an option:"))
                if choose_option == str(choice.option_1.value):
                    people_dictionary, user_all_inputs = save_new_entry(people_dictionary, user_all_inputs)
                elif choose_option == str(choice.option_2.value):
                    print_entries_polimyarizm(people_dictionary)
                elif choose_option == str(choice.option_3.value):
                    save_all_data(people_dictionary)
                elif choose_option == str(choice.option_4.value):
                    new_option = input("Are you sure?(y/n)?:")
                    if new_option == 'y':
                        break
                    else:
                        continue

                raise  Invalid_Menu_Option(f"Invalid option: {choose_option}")
            
            except Invalid_Menu_Option as e:
                    print(e)
                    print("incorrect input please try again")
            input("Press Enter to continue...")
user_input_1 = None
people_dictionary_1 = {}
run_main(people_dictionary_1, user_input_1 )                                                                                                                                                                                                                                                                                                                                                                                                                                                           