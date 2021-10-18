
operater= input("write operater(*,-,+,/,) :")
calculator = int(input("FIRST VALUE : "))
calculator2 = int(input("SECOND VALUE : "))
result = print(calculator ,operater, calculator2 ,"=")
print(result)
try:
    if operater == "+":
        print( calculator + calculator2)

    if operater == "*" and calculator == 45 and calculator2 == 3:
        print(125)

    elif operater == "-":
        print(calculator - calculator2)
    elif operater == "*":
        print(calculator * calculator2)
    elif operater == "/":
        print(calculator / calculator2)

    else:
        print(operater ," is invaild operater")
except Exception as e:

    e =( "remember :  dont use alphabets")
    print(e)


