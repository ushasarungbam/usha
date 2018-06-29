try:
    a=10/0
    print (a)
except ArithmeticError:
        print ("This statement is raising an exception")
else:
    print ("Welcome")