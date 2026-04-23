print("ramzi")  # this prints "ramzi"

X = "flan"  # variable string

S = "and ramzi"  # variable string

U = "go to school"  # variable string 

Y = 250  # variable integer

L = 10293  # variable integer

F = 2.50  # variable float

print(X + " " + S + " " + U)  # concatenation

K = {}  # dictionary

P = []  # list

Q = ()  # tuple

print(P)

# string methods

O = "abdelli mohemed 'ramzi'"

print(O)

H = """

"welcome "

'to my web site'
a
s
f
d
"""

print(H)

# string slicing

# X = a,b,d,e,l,l,i, ,m,o,h,e,m,e,d, ,r,a,m,z,i

#   0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20

X = "abdelli mohemed ramzi"

print(X[0:21])  # prints from index 0 to 20

# string methods #2

name9 = "ramzi"

print(name9.upper())  # this function converts lowercase to uppercase

name10 = "RAMZI"

print(name10.lower())  # this function converts uppercase to lowercase

print(name9.islower())  # checks if all letters are lowercase

print(name10.isupper())  # checks if all letters are uppercase

print(name9.isupper())  # checks if all letters are uppercase

print(name9.capitalize())  # converts first letter to uppercase

name12 = "abdelli mohemed ramzi"

print(name12.title())  # converts first letter of each word to uppercase

# string methods #3 - split()

lan = "work sleep eat happiends "

print(lan.split())  # ['work', 'sleep', 'eat', 'happiends']

lan2 = "work_sleep_eat_happiends"

print(lan2.split("_"))  # ['work', 'sleep', 'eat', 'happiends']

lan3 = "9raya busnis programinisart"

print(lan3.split("_", 2))  # no underscores -> whole string as one element

print(lan3.split())  # split on spaces -> ['9raya', 'busnis', 'programinisart']

print(lan3.split(" ", 2))  # split on space, max 2 times -> ['9raya', 'busnis', 'programinisart']
