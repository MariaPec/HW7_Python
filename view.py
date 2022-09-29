import controller

def getdata():
    return str(input("=> "))

def getvalue(value):
    if value == "1":
        return init(), export()
    elif value == "2":
        return importNumbers()
    else: 
        print('Некорректный ввод')
        controller.button_push()

number = None
name = None
surname = None

def init ():
    global number
    global name
    global surname
    print("введите номер")
    number = getdata()
    print("введите имя")
    name = getdata()
    print("введите фамилию")
    surname = getdata()

def export():
    file = open('numbers.txt', 'a+')
    file.write(f"\n{number} {name} {surname}")
    file.close()

def importNumbers():
    with open("numbers.txt", "r") as file1:
        for line in file1:
            print(line.strip())

