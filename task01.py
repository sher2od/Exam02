def add(a:int,b:int):
    result = a + b
    return result
    return result


def subtract(a:int,b:int):
    result = a - b
    return result

    return result
    
def multiply(a:int,b:int):
    result = a * b
    return result

    


def divid(a:int,b:int):
    result = a / b
    return result

    
 
def main():
    a = int(input("a >> "))
    op = input("+,/,*,- ")
    b = int(input("b >> "))

    if op == "+":
        print(add(a,b))
    elif op == "-":
        print(subtract(a,b))
    elif op == "*":
        print(multiply(a,b))
    elif op == "/":
        print(divid(a,b))
    else:
        print("error")
        
main()
    