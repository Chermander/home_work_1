import shutil
from csv import DictReader, DictWriter
from os.path import exists
class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt


filename = "phone.csv"
fileout = "migration.csv"

def get_data():
    flag = False
    while not flag:
        try:
            first_name = input("Введите имя: ")
            if len(first_name) < 2:
                raise NameError("Слишком короткое имя ")
            last_name = input("Введите фамилию: ")
            if len(last_name) < 2:
                raise NameError("Слишком короткая фамилия ")
            phone_num = input("Введите номер телефона: ")
            if len(phone_num) < 11:
                raise NameError("Введён некорреткный номер (слишком короткий) ")
            elif len(phone_num)>12:
                raise NameError("Введён некорреткный номер (слишком длинный) ")
        except NameError as err:
            print(err)
        else:
            flag = True

    return (first_name, last_name, phone_num)

def create_file(filename):
    with open(filename, 'w', encoding="utf-8") as data:
        f_w = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()

def read_file(filename):
    with open(filename, 'r', encoding="utf-8") as data:
        f_r = DictReader(data)
        return list(f_r)

def write_file(filename, lst):
    res = read_file(filename)
    obj = {'Имя':lst[0], 'Фамилия':lst[1], 'Телефон':lst[2] }
    res.append(obj)
    standart_write(filename, res)


def row_search(filename):
    last_name = input("Введите фамилию: ")
    res = read_file(filename)
    for row in res:
        if last_name == row["Фамилия"]:
            return row
    return "Запись не найдена"

def delete_row(filename):
    row_number = int(input("Введите номер строки: "))
    res = read_file(filename)
    res.pop(row_number-1)
    standart_write(filename, res)


def standart_write(filename, res):
    with open(filename, 'w', encoding="utf-8") as data:
        f_w = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()
        f_w.writerows(res)

def change_row(filename):
    row_number = int(input("Введите номер строки: "))
    res = read_file(filename)
    data = get_data()
    res[row_number - 1]["Имя"] = data[0]
    res[row_number - 1]["Фамилия"] = data[1]
    res[row_number - 1]["Телефон"] = data[2]
    standart_write(filename, res)

def copy_to_file(filename, fileout):
    row_number = int(input("Введите номер строки: "))
    res = read_file(filename)
    if row_number > len(res):
        print("Выход за пределы строк")
    else:
        with open(fileout, 'a') as file:
            file.write(f"{(res[row_number - 1]["Имя"])}, {(res[row_number - 1]["Фамилия"])}, {(res[row_number - 1]["Телефон"])}{"\n"}")
        standart_write(filename, res)
def main():
    while True:
        command = input("Введите команду: ")
        if command == "q":
            break
        elif command == "w":
            if not exists(filename):
                create_file(filename)
            write_file(filename, get_data())
        elif command == "r":
            if not exists(filename):
                print("Файл не существует. Создайте его")
                continue
            print(read_file(filename))
        elif command == "f":
            if not exists(filename):
                print("Файл не существует. Создайте его")
                continue
            print(row_search(filename))
        elif command == "d":
            if not exists(filename):
                print("Файл не существует. Создайте его")
                continue
            print(delete_row(filename))
        elif command == "c":
            if not exists(filename):
                print("Файл не существует. Создайте его")
                continue
            print(change_row(filename))
        elif command == "copy":
            if not exists(filename):
                print("Файл не существует. Создайте его вручную")
                continue
            print(copy_to_file(filename, fileout))

main()



