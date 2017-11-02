
def myFunction():

    aliens = {}

    aliens["name"] = input("Введите имя вашего инопланетянена:\n")
    aliens["color"] = input("Введите цвет вашего " + aliens["name"] + "\n")
    aliens["age"] = input("Сколько " + aliens["name"] + " лет?\n")
    aliens["age"] = int(aliens["age"])
    aliens["planets"] = str(input("Откуда " + aliens["name"] + " прилетел?\n"))
    
    aliens_list = list(aliens.items())
    
    print("\n", aliens_list, "\n")
    
    aliens["var"] = input("Хотите попробовать еще?(y/n или д/н)\n")

    i = aliens["var"]
    
    if i.lower() == "n" or i.lower() == "н":
        print("Хорошо! Сделаем перерыв, а потом продолжим :)")
    elif i.lower() == "y" or i.lower() == "д":
        return myFunction()
    else:
        print("Error 404")

myFunction()
