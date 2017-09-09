#Creating a calculator for addition, subtract, division, multiplication, module division, square root.

def addition(a,b):
	add = a+b
	print(add)
def subtract(a,b):
	sub = a-b
	print(sub)
def multiply(a,b):
	mul = a*b
	print(mul)
def division(a,b):
	div = a/b
	print(div)
def moduleDivision(a,b):
	mod = a%b
	print(mod)
def square(a):
	a=10
	sqr = a*a
	print(sqr)


#calling a function

# addition()
# subtract()
# multiply() 
# division()
# moduleDivision()
# square()

def user_input():
	a=int(input("Please enter first number:"))
	b=int(input("Please enter second number:"))
	return a,b
while True:
	user_choice = int(input("\nPlease select an option \n 1.Add\n 2.Sub\n 3.Multiplicaiton\n 4.Division\n"))

	if(user_choice==1):
		a,b=user_input()
		addition(a,b)

	elif (user_choice==2):
		a,b=user_input()
		subtract(a,b)

	elif(user_choice==3):
		a,b=user_input()
		multiply(a,b)
	elif(user_choice==4):
		a,b=user_input()
		division(a,b)
	else:
		print("Sorry, Please enter correct option!!")