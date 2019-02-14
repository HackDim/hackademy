import Code
import datetime
import gol

day_number = Code.today()
print("Today is the " + str(day_number))

print("Hello")
#a =input("What is your name ?")

#Code.hello1(a)


print("Hello")
#b =input("What is the first person's name ? ")
#c =input ("What about the second person's name? ")

#Code.hello2(b,c)

#d = input("What are your ages combined ?")
#print("You are " + d + " old")

#Code.circle_area

num = int(input("Give me a number: "))
#Code.single_row_stars(num)

string = str(input("Give me a string: "))

#Code.single_row_of(num,string)

Code.square_of_stars(num)

num = int(input("Give me a number of rows: "))
num1 = int(input("Give me a number of columns: "))

Code.rect_of_stars(num,num1)

the_list = [1,2,3,4,5,6,7,8,9,10]

Code.list_by_two(the_list)

the_size = 5
the_grid = Code.create_grid(the_size)

print(the_grid)

gol.fill_grid_random(5,5)

