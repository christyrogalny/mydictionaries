import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}



print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)
print(type(phonebook))
phone = phonebook['Chris']
print(phone)

mydictionary = {}
print(mydictionary)


mydictionary = dict(m = 8, n=9) #allows you to create a dictionary m and n are the keys, 8 and 9 are the values == {'m': 8, 'n': 9}
print(mydictionary)



print()
print('*****  end section 1 ********')
print()





print()
print('*****  start section 2 - search dictionary ********')
print()


name = 'Chri'

if name in phonebook: #use if to search through keys in dictionary, use do you dont break your code
    print(phonebook[name]) 
else: #if the key is not in the dictionary
    print(name, 'not in the phonebook') 




print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()

###keys cannot be updated ... only values###
### keys are immutable ###
print(phonebook)
phonebook['Chris'] = '555-0123' #this will change chris phonenumber in the dictionary
phonebook['Joe'] = '555-4444' #Joe is not in dictionary, it adds ... if key doesn't exist it will add it
print(phonebook)



print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

#del phonebook['Chris'] #this removes chris from the dictionary
#print(phonebook)


print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()


for key in phonebook: #the default iteration is the keys... it iterates through the keys 
    print(key) #key is just a variable name
    print(phonebook[key]) #will print out keys and values


for value in phonebook.values(): #if you want to go through all values you have to use the values method
    print(value)


for k, v in phonebook.items(): #allows to go though keys and values
    print("key: ", k, "value: ", v)


for tuple in phonebook.items():
    print(tuple)


print()
print('*****  end section 5 ********')
print()





print()
print('*****  start section 6 - using get and clear ********')
print()


phone = phonebook.get("Chris", "key not found") #get method...chris is in phonebook so it displays his phonenumber
print(phone)                                    #if name is not found, will display 'key not found'

#phonebook.clear()
#print(phonebook)


print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()






print()
print('*****  end section 7 ********')
print()

'''

print()
print('*****  start section 8 - using popitem ********')
print()






print()
print('*****  end section 8 ********')
print()



print()
print('*****  start section 9 - using random and converting to list ********')
print()





print()
print('*****  end section 9 ********')
print()


'''





