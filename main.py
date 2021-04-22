import sys
import logging
def add(a, b, *args):
    return a + b + sum(args)

def sub(a, b, *args):
    return a - b - sum(args)

def div(a, b, *args):
    z = 1
    for i in args:
        z = i*z
    return a/b/z

def mlt(a, b, *args):
    z = 1
    for i in args:
        z = i * z
    return a * b * z


operations = {
    '+': add,
    '-': sub,
    '/': div,
    '*': mlt
}

def get_data():
    operation = input("Podaj jakie działanie wykonać +-/*: ")
    a = input('Podaj pierwszą liczbę do działaia: ')
    b = input('Podaj drugą liczbę do działania: ')
    args = []
    while True:
        x = input('Podaj kolejną liczbę (jeśli koniec naciśnij k): ')
        if x == "k":
            break
        args.append(int(x))

    return operation, int(a), int(b), args

operation, a, b, args = get_data()

print(operations[operation](a, b, *args))


