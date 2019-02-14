import datetime
import os
import imageprocessor
from PIL import Image 
import sys



#print("Hello!")

def hello1(a_name):
	print("Hello" + a_name)

def hello2(name_a, name_b):
	print("Hello " + name_a + " & " + name_b)

def sum_two(x,y):
	z = x + y
	return z

import math

def circle_area():
	radius = int(input("Please insert radius of circle"))
	y = radius * radius * math.pi
	print(y)
	

#circle_area()

def today():
	now = datetime.datetime.now()
	return now.day

def my_sum(a_list):
	total = 0
	for n in a_list:
		total = total + n
	return total

def my_prod(a_list):
	product = 1
	for n in a_list:
		product = product * n
	return product



def my_count(a_list):	
	count = 0
	for n in a_list:
		count = 1 + count
	return count

def my_count_less_5(a_list):
	count = 0
	for n in a_list:
		if n < 5:
			count = count + 1
	return count

def my_count_ones(a_list):
	count = 0
	count5 = 0
	for n in a_list:
		if n == 1:
			count = count + 1
		elif n == 5:
			count5 = count5 + 1
	return count, count5

# We use this function to make sure our max_value function works
# This is important so that if there are negative n° it doesn't give
# Zero instead of the actual max value..
def is_list_empty(a_list):
	if my_count(a_list) == 0:
		return True
	else: 
		return False

def max_value(a_list):
	if is_list_empty(a_list):
		return None 
	maximum = a_list[0]
	for n in a_list:
		if n > maximum:
			maximum = n
	return maximum

# -------------------------------------------

def get_filenames(a_dirname):
	files = os.listdir(a_dirname)
	all_files = []
	for n in files:
		full_path = os.path.join(a_dirname, n)
		all_files.append(full_path)
	return all_files


# ---------------------------------------------

def process_pictures(a_path):
	filelist = get_filenames(a_path)
	for p in filelist:
		extension = p.split(".")[-1]
		print(p.split("."))
		print(extension)
		if extension == "jpg" or extension == "png" :
			print(p)
			im = Image.open(p)		
			imageprocessor.rotate_box(im)

def grey_scale(a_path):
	filelist = get_filenames(a_path)
	


#process_pictures("C:\\Users\\DimHackademy\\Desktop\\pictures")	


#---------------------------------------------------------- #
#			-- PREPARATION FOR GOL --						#
#---------------------------------------------------------- #

#[12, 34, [56, 67]] --> into one single list

def flatten(a_list_with_lists):
	new_list = []
	for n in a_list_with_lists:
		if isinstance(n,list):
			for i in n:
				new.list.append(i)	

			else:
				new.list.append(n)	

def print_right(a_list_with_lists):
	for n in a_list_with_lists:
		if isinstance(n,list):
			for i in n:
				print(i, end='')
		else:
			print(n)
	return n	

def print_right(a_list_with_lists):
	for n in a_list_with_lists:
		if isinstance(n,list):
			for i in n:
				print(i, end='')
		else:
			print(n, end="")
		print()

def single_row_stars(number):
	for n in range(number):
		print("*", end= "")

def single_row_of(number, symbol):
	for n in range(number):
		print(symbol, end="")

def square_of_stars(num):
	for n in range(num):
		for m in range(num):
				print("*", end="")
		print()

def rect_of_stars(rows, cols):
	for n in range(rows):
		for m in range(cols):
				print("*", end="")
		print()


def list_by_two(a_list):
	n_list = []
	for n in a_list:
		bob = n * 2
		n_list.append(bob)
	print(n_list)

# inner forloop --> row
# outer forloop --> column
# want a list of lists 

def create_grid(size):
	n_list = []
	for row in range(size):
		n1_list = []
		for column in range(size):
			n1_list.append("-")
		n_list.append(n1_list)
	return n_list

def is_duplicate_there(list_a, list_b):
	if len(set(list_a).intersection(list_b)) == 0: 
		return print(False)
	else: 
		return print(True)

