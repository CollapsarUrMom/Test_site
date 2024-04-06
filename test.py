import ast


qwe = "{'a': 1, 'b': 2}"
dictionary = ast.literal_eval(qwe)
print (type(dictionary))
print (dictionary)


string_l = "{'a': 1, 'b': 2}"
list_object = ast.literal_eval(string_l)
print(list_object)  
print(type(list_object))