

age = int(input("Enter your age: "))

try:
   age = int(input("Enter your age: "))
   print(age)
except:
    print("Not a valid input, please try again!")

print(some_object)

my_list = [1,2] # name error
my_list[4] # index error
"a" + 5 # type error
int("Python") # value error
3/0 # zero division error

try:
   age = int(input("Enter your age: "))
   print(age)
except ValueError:
    print("Not a valid input, please try again!")


try:
   age = int(input("Enter your age: "))
   print(age)
except NameError:
    print("Not a valid input, please try again!")




try:
   age = int(input("Enter your age: "))
   print(age)
except ValueError as error_type:
    print(f"Not a valid input {error_type}, please try again!")































