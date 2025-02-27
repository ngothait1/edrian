import time

name = input("Please enter your name:")
print("hi nice to meet you " + name )
print("This is a special calculator I would need two integer numbers from you: ")
number1 = int(input("FIRST NUMBER: "))
number2 = int(input("SECOND NUMBER: "))
n1_even = ""
n2_even = ""
isgood = True

if number1 % 2 == 0 and number2 %2 ==0:
    n1_even = "even"
    n2_even = "even"
    print("so both of them are even")
elif number1 % 2 !=0 and number2 %2 ==0:
    n1_even = "odd"
    n2_even = "even"
    print("so one of them are odd , and second are even")
elif number1 %2 == 0 and number2 %2 !=0:
    n1_even ="even"
    n2_even = "odd"
    print("so one of them are even , and second are odd")

else:
    n1_even = n2_even = "odd"
    print("so both of them are odd")


print("Thank you for entering two numbers " + str(number1) + " and " + str(number2))
print("First number is: " +n1_even)
print("Seccond number is: " +n2_even)



operator = input("Please choose the operator: /,*,+,-,:  ")
result = 0

if operator == "+":
  result = number1 + number2

elif operator == "-":
   result = number1 - number2
   

elif operator == "*":
  result = number1 * number2

elif operator == "/":
  if number2 == 0:
   print("incorrect input we cant divide numbers by zero")
   isgood = False
  if number2 != 0:
   typeresult = input("which type of result you want integer or float? ")
   if typeresult == "integer":
      result = number1 // number2
   elif typeresult == "float":
     result = number1 / number2
   else:
     isgood = False
else:
    isgood = False

if isgood == False:
    print("Error: Operator " + operator +  " is not supported An error had occured, please try again")

else:
    print(str(number1) + str(operator) + str(number2) + " = " + str(result) )

print("thanks " + name + " for using  using our calculator at " + time.ctime() )
