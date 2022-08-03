global pol_swahili_dictionary
global i
i = 1
pol_swahili_dictionary = {
    "jumba": "castle",
    "maji": "water",
    "mchanga": "soil"
    }

def Printkeys(pol_swahili_dictionary):
    for item in pol_swahili_dictionary:
        print(i, ": ", item)
        i += 1

del pol_swahili_dictionary["maji"]    # remove an item
print("After using the del keyword :")    # outputs: 2
Printkeys(pol_swahili_dictionary ) 
    
pol_swahili_dictionary.clear()   # removes all the items
print("After using the clear() function")    # outputs: 0
Printkeys(pol_swahili_dictionary )

print("The length of the dictionary is :", len(pol_swahili_dictionary))
print(pol_swahili_dictionary)
Printkeys(pol_swahili_dictionary)
 
del pol_swahili_dictionary   # removes the dictionary
Printkeys(pol_swahili_dictionary) 
