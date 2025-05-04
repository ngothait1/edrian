from Person import Person
import library_functions as library

class Student(Person):
    def __init__(self):
        self._name = library.check_if_alpha(library.try_input("please enter student's name: "))
        self._age = library.check_if_int(library.check_if_digit(library.try_input("please enter student's age: ")))
        self._id = library.check_if_int(library.check_if_digit(library.try_input("please enter student's id: ")))
        self.field_study = library.check_if_alpha(library.try_input("please enter student's field of study: "))
        self.year_study = library.check_if_int(library.check_if_digit(library.try_input("please enter student's year of study: ")))
        self.score_average = library.check_if_int(library.check_if_digit(library.try_input("please enter student's score average: ")))


    def get_field_of_study(self):
        return self.field_study


    def get_year_study(self):
        return self.year_study


    def get_score_average(self):
        return self.score_average


    def set_field_study(self, new_field_study):
        self._field_study = new_field_study


    def set_year_study(self, new_year_study):
        self._year_study = new_year_study


    def set_score_average(self, new_score_average):
        self._score_average = new_score_average


    def print_myself(self):
        print(self.return_str_print_people() + "," + " the field of study is " + self.get_field_of_study() + " and year of study is " + str(self.get_year_study()) + " and the average score is " + str(self.get_score_average()))
    

    def get_type(self):
        return __class__.__name__

     
    def get_type_str(self):
        return self.__class__.__name__


    def __str__(self): 
        return f" The student's name: {self._name}. the Student's age: {self._age}. the Student's  id: {self._id}. Student's field of study: {self.field_study}. Student's year of study {self.year_study}. And finally Student's Average sccore {self.score_average}"