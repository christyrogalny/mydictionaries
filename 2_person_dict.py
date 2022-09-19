person = {} #creates an empty dictionary
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"] #list
person["pets"] = {"dog": "Fido", "cat": "Sox"} #dictionary

print(person)

print(person['children']) #only prints the list of the children thats within the dictionary

#if i put type in front of person...
print(type(person['children'])) #will tell me what type of object im working with -- this is a list object

#to print out just Betty's name...
print(person['children'][1]) #add the index value of betty's name in the children list

#want to print out name of cat...
print(person['pets']['cat']) #you would give it the key value because its a dictionary -- cant do index value because the dictionary is looking for a key


#use for loop to print out names of children
for child in person['children']: 
    print(child)

#another for loop to print out names of dog and cat
for p in person['pets']:
    print(person['pets'][p]) #dont need quote here because its a variable
