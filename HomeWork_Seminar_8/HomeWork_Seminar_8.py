import os
import shutil

#добавляет новый контакт в справочник.

def add_contact(contacts):
    фамилия = input("Введите фамилию: ")
    имя = input("Введите имя: ")
    отчество = input("Введите отчество: ")
    номер_телефона = input("Введите номер телефона: ")
    
    контакт = {
        "фамилия": фамилия,
        "имя": имя,
        "отчество": отчество,
        "номер телефона": номер_телефона
    }
    
    contacts.append(контакт)
    print("Контакт успешно добавлен!")

#выводит список контактов

def print_contacts(contacts):
    file_path = input("Введите путь к файлу с контактами: ")
    if not os.path.exists(file_path):
        print("Файл не существует!")
        return

    with open(file_path, 'r') as file:
        contact_data = file.readlines()

    print("Телефонный справочник:")
    for i, line in enumerate(contact_data, start=1):
        line = line.strip()
        if line:
            print(f"{i}. {line}")

#сохроняет контакты

def save_contacts(contacts):
    file_path = input("Введите путь к файлу для сохранения данных: ")
    with open(file_path, 'w') as file:
        for contact in contacts:
            line = f"Фамилия: {contact['фамилия']}, Имя: {contact['имя']}, Отчество: {contact['отчество']}, Номер телефона: {contact['номер телефона']}\n"
            file.write(line)
    print("Данные успешно сохранены!")

#копирует контакты

def copy_contact(src_file_path, dest_file_path, contact_number):
    if not os.path.exists(src_file_path):
        print("Файл-источник не существует!")
        return
    
    if not os.path.exists(dest_file_path):
        print("Файл-приемник не существует!")
        return

    with open(src_file_path, 'r') as src_file:
        contact_data = src_file.readlines()
    
    if contact_number < 1 or contact_number > len(contact_data):
        print("Неверный номер контакта!")
        return

    contact_to_copy = contact_data[contact_number-1].strip()
    with open(dest_file_path, 'a') as dest_file:
        dest_file.write(f"{contact_to_copy}\n")

    print("Контакт успешно скопирован!")

#Выводит файл

def process_file(file_path):
    with open(file_path, 'r') as file:
        contact_data = file.readlines()

    contacts = []
    for line in contact_data:
        line = line.strip()
        if line:
            contacts.append(line)

    return contacts

#Сохранение файла

def save_file(file_path, contacts):
    with open(file_path, 'w') as file:
        for contact in contacts:
            file.write(f"{contact}\n")

    print("Файл успешно сохранен!")

#Выгрузка контактов

def load_contacts(file_path):
    contacts = process_file(file_path)
    print("Контакты успешно загружены!")
    return contacts

#Главный код с меню

def menu():
    contacts = []

    while True:
        print("\nМеню:")
        print("1. Добавить контакт")
        print("2. Просмотреть контакты")
        print("3. Сохранить контакты")
        print("4. Скопировать контакт в другой файл")
        print("5. Выход")

        choice = input("Выберите пункт меню: ")
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            print_contacts(contacts)
        elif choice == "3":
            save_contacts(contacts)
        elif choice == "4":
            src_file_path = input("Введите путь к исходному файлу: ")
            dest_file_path = input("Введите путь к файлу-приемнику: ")
            contact_number = int(input("Введите порядковый номер контакта: "))
            copy_contact(src_file_path, dest_file_path, contact_number)
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

menu()