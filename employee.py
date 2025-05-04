
from Person import Person
import library_functions as library

class Employee(Person):
    def __init__(self):
        self._name = library.check_if_alpha(library.try_input("please enter employe's name: "))
        self._age = library.check_if_int(library.check_if_digit(library.try_input("please enter employe's age: ")))
        self._id = library.check_if_int(library.check_if_digit(library.try_input("please enter  employe's  id: ")))
        self.field_work = library.check_if_alpha(library.try_input("please enter employee's field_work: "))
        self.salary = library.check_if_int(library.check_if_digit(library.try_input("please enter employee's salary: ")))


    def get_salary(self):
        return self.salary
    

    def get_field_work(self):
        return self.field_work
    

    def set_salary(self, new_salary):
        self._salary = new_salary


    def set_field_work(self, new_field_work):
        self._field_work = new_field_work


    def print_myself(self):
        #self.print_people() # we can to definate it like this or:
        #super().print_people() # or like this
        print( self.return_str_print_people() + "," + " the field of work is  " + self.get_field_work() + " and the salary is " + str(self.get_salary())) 


    def get_type(self):
        return __class__.__name__

     
    def get_type_str(self):
        return self.__class__.__name__


    def __str__(self): 
        return f"the employe`s name: {self._name}. the employe's age: {self._age}. the employe's  id: {self._id}. the employe's salary is: {self.salary}. and finally the employe's field of work is: {self.field_work}"