import logging
logging.basicConfig(level=logging.DEBUG)

def calculator (operation, a, b):
    if operation == 1:
        logging.info(f"Dodaję {a} i {b}")
        result = a + b 
    elif operation == 2:
        logging.info(f"Odejmuję {a} od {b}")
        result = a - b
    elif operation == 3:
        logging.info(f"Mnożę {a} razy {b}")
        result = a * b
    elif operation == 4:
        logging.info(f"Dzielę {a} przez {b}")
        result = a / b 
    else:
        print("Nie ma takiego trybu")
        exit(1)
    return result

if __name__ == "__main__":
    operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    a = input("Podaj składnik 1. ")
    b = input("Podaj składnik 2. ")
    result = calculator(int(operation), float(a), float(b))
    print("Wynik to %s" % result)