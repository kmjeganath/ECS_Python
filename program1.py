print("Hi, please enter temperature in celsius")
cel = float(input())
#cel = int(input()) //Only work if the input is integer.
#cel = input() //default data type is string
fah = (32 + ((9/5)*cel))
print(fah)

