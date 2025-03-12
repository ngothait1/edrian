def iterateWithid(input_dict : dict):
    for id in input_dict.items():
        print("The name is " + id[0] + " and the id is " + str(id[1]))

def return_index(input_dict : dict , name : str):
    keys_list = list(input_dict.keys())
    if name in keys_list:
        return keys_list.index(name)
    else:
        return -1


ids_dictionary = {}
for i in range(20):
    name = input(" please enter name: ")
    id = int(input(" please enter id: ")) 
    ids_dictionary[name] = id
print(" the index of edrian is: " + str(return_index(ids_dictionary,"edrian")) )

iterateWithid(ids_dictionary) 

new_dictionary = {}
for name, id_number in ids_dictionary.items():
    age = int(input("please enter age: "))
    new_dictionary[name] = {"id number": id_number, "age": age}

print("New dictionary with additional details:")
for name, details in new_dictionary.items():
    print("The key is: " + name + " and the values are: " + str(details))
