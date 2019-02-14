import Code
import os

a_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,1]
b_list = []
another_list = ["Bob", "Philipp","Bender"]

yanother_list = [1, "Bob", 3.4,"Bender"]

Code.my_sum(a_list)
the_sum = Code.my_sum(a_list)
print("The sum of this list is: " + str(the_sum))

Code.my_prod(a_list)
the_prod = Code.my_prod(a_list)
print("The product of this list is: " + str(the_prod))

Code.my_count(a_list)
the_count = Code.my_count(a_list)
print("The number of elements in this list is: " + str(the_count))

Code.my_count(b_list)
the_count2 = Code.my_count(b_list)
print("The number of elements in list b is: " + str(the_count2))

#to know the n° of elements in a list you don't need to use 
# them directly...

#-----------------------------------------
#EXAMPLE
numbers = [1,2,4]

total = 0

for n in numbers:
    total = total + n  

print(total)  

for n in numbers:
    b = sum(numbers)
print(b)
#----------------------------------------

numbers = [1,2,3,4,5,6,7,8,9,10]
total = 0

for n in numbers:
    total = total + n

print(total)

people = [" Jeff,", " Billy,", " John,", " Samatha,", " and Olivia"]
all_the_people = "Please welcome" 
for p in people:
    all_the_people = all_the_people + p
print(all_the_people)

numbers1 = [12,3,12]

total = 1

for n in numbers1:
    total = total * n
print(total)
# ----------------------------------------------------
a = 23
b = 24
c = 55
if a > b:
    print("You were right !!!")
else:
    print("It was actually false, sorry...")

# ----------------------------------------------------
# "==" checks whether its "equal" and it returns you either true or false
# "=" transforms what is on the left into what is on the right

Code.my_count_less_5(a_list)
five_count = Code.my_count_less_5(a_list)
print("The amount of elements under five is: " + str(five_count))

Code.my_count_ones(a_list)
one_count, five_count = Code.my_count_ones(a_list)
print("Amount of ones: " + str(one_count))
print("Amount of fives: " + str(five_count))

#------------------------------------------------------

Code.max_value(a_list)
the_max = Code.max_value(a_list)
print("The highest value in this list is: " + str(the_max))

# -----------------------------------------

Code.get_filenames("C:\\Users\\DimHackademy\\Desktop\\pythoncode")

