
import library_functions as library

class Person:
    _id = None
    _name = None
    _age = None


    def __init__(self):
        self._name = library.check_if_alpha(library.try_input("please enter person's name: "))
        self._age = library.check_if_int(library.check_if_digit(library.try_input("please enter person's age: ")))
        self._id = library.check_if_int(library.check_if_digit(library.try_input("please enter person's id: ")))


    def get_age(self):
        return self._age


    def get_name(self):
        return self._name


    def get_id(self):
        return self._id


    def set_age(self, new_age):
        self._age = new_age


    def set_id(self, new_id):
        self._id = new_id


    def set_name(self, new_name):
        self._name = new_name


    def return_str_print_people(self):
        return "the id of " + self.get_name() + " is : " + str(self.get_id()) + " and the age is " + str(self.get_age())

   
    def print_myself(self):
        #self.print_people() # we can to definate it like this or:
        #super().print_people() # or like this
        print(self.return_str_print_people()) 
    

    def get_type(self):
        return __class__.__name__
    
    
    def get_type_str(self):
        return self.__class__.__name__


    def __str__(self): 
        return f'the person`s name: {self._name}. the person`s age: {self._age}. the person`s id: {self._id}.'



if __name__ == "__main__":
    test_name = "edrian"
    test_id = 323232
    test_age = 32
    #people_1 = Person(test_name, test_age, test_id) 
    #print(people_1.get_type())
   # if test_name != people_1.get_name():
   #     print("invalid name the name should be " + test_name + " and not " + people_1.get_name())
   # if test_age != people_1.get_age():
    #    print("invalid age the age should be " + str(test_age) + " and not " + str(people_1.get_age()))
   # if test_id != people_1.get_id():
  #      print("invalid id the id should be: " + str(test_id) + " and not " + str(people_1.get_id())) 

elif __name__ == "lesson_56_hw_import_code":
    print("welcome you use the import module " + __name__ + " please enjoy")

