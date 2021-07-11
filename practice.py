
def number():
    num = input("Type a number:")

    try:

        num = float(num)
        return float(num)

    except ValueError or TypeError or NameError:
            print("Use numbers!")
    return None

def infinitecheck():
    while_flag = True
    while while_flag:
        num1=number()
        if num1:
            while_flag = False

    return num1


def summ():
    n2 = infinitecheck()
    sum = n1 + n2
    print(sum)
    return sum

def extract():
    n2 = infinitecheck()
    extraction = n1 + n2
    print(extraction)
    return extraction

def mult():
    n2 = infinitecheck()
    mult = n1*n2
    print(mult)
    return(mult)

def division():
    n2 = infinitecheck()
    division = n1/n2
    print(division)
    return(division)

def symbolInput():
    symbol= input("Type mathematical action(+ or - or  * or /")
    try:
        if symbol == "+":
             result = summ()
        elif symbol == "-":
             result = extract()
        elif symbol == "*":
            result = mult()
        elif symbol == "/":

            try:
                result = division()
                return result
            except ZeroDivisionError:
                print ("You cannot divide by zero!")

            return None

        return result
    except: print("You have typed wrong symbol. Try again")



def symbolcheck():
    while_flag1 = True
    while while_flag1:
        res = symbolInput()
        if res:
            while_flag = False
            return res


n1 = infinitecheck()
resultfinal = symbolcheck()


while_flag2 = True
while while_flag2:
    d = input("If you want quit calculator, print d, if you want to continue calculating press any other button:")

    if d!="d":
        n1==0
        n1=+resultfinal
        resultfinal=symbolcheck()

    elif d == "d":
        while_flag2 = False

        break
print('exit')



