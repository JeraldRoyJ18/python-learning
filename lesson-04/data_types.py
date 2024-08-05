#string data type

#literal assignment
first  = "jerald"
last = "Roy"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first , str ))

#constructor function
pizza = str("Pepperoni")


# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza , str ))


#Concatenation
fullname = first + " " + last
print("hello " + fullname)

fullname += "!"
print("hello " + fullname )

#Casting a number to a string
decade = str(2003)
print(type(decade))

decade2 = 2003
print(type(decade2))

statement = "I was born in the year " + decade + "s."
# statement = "I was born in the year " + decade2 + "s." does not work because of imcompatoble types

# print(statement)

#Multiple lines
multiline = '''
hey , how are you ?

I was just checking in.

                            All good!


'''

# print(multiline)

#Escaping special characters

sentence = 'I\'m back at work ! \t hey! \n\nwhere\'s this at \\ located' 

# print(sentence)