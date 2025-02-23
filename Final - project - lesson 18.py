import time
name = input(" Please enter your name: ")
print("HI NICE TO MEET YOU " + name )
print("This is a special calculator I would need two integer numbers from you: ")
n1 = (input(" FIRST NUMBER: "))
n2 = (input(" SECOND NUMBER: "))
n1 = int(n1)
n2 = int(n2)
n1even = ""
n2even = ""
if(n1%2==0):
    n1even = "even"
else:
    n1even = "odd"
if(n2%2==0):
    n2even = "even"
else:
    n2even= "odd"
print(" Thank you for entering two numbers ")
print(" First number is: " +n1even)
print(" Seccond number is: " +n2even)
operator = input(" Please choose the operator: /,*,+,-,//,^:  ")
result = 0
##############################################################################
if(operator == "+"):
  result = n1+n2
  typeresult= input("which type of result you want integer or float? ")
  if(typeresult == "integer"):
    result = int(result)
    n1 = str(n1)
    n2 = str(n2)
    result = str(result)
    print(n1 + operator + n2 + " = " + result )
  elif(typeresult == "float"):
    result = float(result)
    n1 = str(n1)
    n2 = str(n2)
    result = str(result)
    print(n1 + operator + n2 + " = " + result )
  else:
    print("error - no legal option has been inputed")
###############################################################################
elif(operator == "-"):
  result = n1-n2
  typeresult = input("which type of result you want integer or float? ")
  if(typeresult == "integer"):
    result = int(result)
    n1 = str(n1)
    n2 = str(n2)
    result = str(result)
    print(n1 + operator + n2 + " = " + result )
  elif(typeresult == "float"):
    result = float(result)
    n1 = str(n1)
    n2 = str(n2)
    result = str(result)
    print(n1 + operator + n2 + " = " + result )
  else:
    print("error - no legal option has been inputed")
##################################################################################
elif(operator=="*"):
  result = n1*n2
  typeresult = input("which type of result you want integer or float? ")
  if(typeresult == "integer"):
    result = int(result)
    n1 = str(n1)
    n2 = str(n2)
    result = str(result)
    print(n1 + operator + n2 + " = " + result )
  elif(typeresult == "float"):
    result = float(result)
    n1 = str(n1)
    n2 = str(n2)
    result = str(result)
    print(n1 + operator + n2 + " = " + result )
  else:
    print("error - no legal option has been inputed")
#################################################################################################
elif(operator=="/"):
  result = n1/n2
  typeresult = input("which type of result you want integer or float? ")
  if(typeresult == "integer"):
    result = int(result)
    n1 = str(n1)
    n2 = str(n2)
    result = str(result)
    print(n1 + operator + n2 + " = " + result )
  elif(typeresult == "float"):
    result = float(result)
    n1 = str(n1)
    n2 = str(n2)
    result = str(result)
    print(n1 + operator + n2 + " = " + result )
  else:
    print("error - no legal option has been inputed")
############################################################################
elif(operator=="//"):
  result = n1//n2
  typeresult = input("which type of result you want integer or float? ")
  if(typeresult == "integer"):
    result = int(result)
    n1 = str(n1)
    n2 = str(n2)
    result = str(result)
    print(n1 + operator + n2 + " = " + result )
  elif(typeresult == "float"):
    result = float(result)
    n1 = str(n1)
    n2 = str(n2)
    result = str(result)
    print(n1 + operator + n2 + " = " + result )
  else:
    print("error - no legal option has been inputed")
####################################################################################
elif(operator=="^"):
  result = n1**n2
  typeresult = input("which type of result you want integer or float? ")
  if(typeresult == "integer"):
    result = int(result)
    n1 = str(n1)
    n2 = str(n2)
    result = str(result)
    print(n1 + operator + n2 + " = " + result )
  elif(typeresult == "float"):
    result = float(result)
    n1 = str(n1)
    n2 = str(n2)
    result = str(result)
    print(n1 + operator + n2 + " = " + result )
  else:
    print("error - no legal option has been inputed")
#############################################################################
else:
    t = time.ctime()
    print(" thanks " +name+ " for using our calculator at " +t )
    print("error - no legal option has been inputed")
#############################################################################
t = time.ctime()
print(" thanks " +name+ " for using  using our calculator at " +t )
    
