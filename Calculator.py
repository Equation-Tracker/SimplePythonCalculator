a = input("Enter a number: ")
b = input("Enter another number: ")
c = None
op = input("Enter the operator [+,-,*,/]: ")
print('\n')


def is_int(num):
    num = float(num)
    if num - int(num) > 0:
        return False
    else:
        return True

try:
    if is_int(a):
        a = int(a)
    else:
        a = float(a)
    if is_int(b):
        b = int(b)
    else:
        b = float(b)
    if op == "+":
        c = a + b
    elif op == "-":
        c = a - b
    elif op == "*":
        c = a * b
    elif op == '/':
        c = a / b
    else:
        print("Invalid operator...")
    if c:
        if is_int(c):
            c = int(c)
        else:
            c = float(c)
        print(f"{a} {op} {b} = {c}")
    else:
        print('')
except:
    print("Invalid input...")

