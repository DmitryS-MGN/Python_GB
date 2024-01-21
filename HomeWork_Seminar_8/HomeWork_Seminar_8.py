# Функция для чтения данных из файла
def read_contacts(file_name):
    contacts = []
    with open(file_name, 'r') as file:
        for line in file:
            contact = line.strip().split(',')
            contacts.append(contact)
    return contacts

# Функция для записи контактов в файл
def write_contacts(file_name, contacts):
    with open(file_name, 'w') as file:
        for contact in contacts:
            file.write(','.join(contact) + '\n')

# Функция для добавления нового контакта
def add_contact(file_name):
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    contact = [last_name, first_name, patronymic, phone_number]
    contacts = read_contacts(file_name)
    contacts.append(contact)
    write_contacts(file_name, contacts)
    print("Контакт успешно добавлен.")

# Функция для вывода всех контактов
def list_contacts(file_name):
    contacts = read_contacts(file_name)
    if not contacts:
        print("Телефонный справочник пуст.")
    else:
        for contact in contacts:
            print(f"Фамилия: {contact[0]}, Имя: {contact[1]}, Отчество: {contact[2]}, Номер телефона: {contact[3]}")

# Функция для поиска контакта по характеристике
def search_contact(file_name):
    search_key = input("Введите характеристику для поиска: ")
    contacts = read_contacts(file_name)
    found_contacts = []
    for contact in contacts:
        if search_key in contact:
            found_contacts.append(contact)
    if not found_contacts:
        print("Контакты не найдены.")
    else:
        for contact in found_contacts:
            print(f"Фамилия: {contact[0]} Имя: {contact[1]} Отчество: {contact[2]} Номер телефона: {contact[3]}")

# Функция для удаления контакта
def delete_contact(file_name):
    contacts = read_contacts(file_name)
    if not contacts:
        print("Телефонный справочник пуст.")
        return
    search_key = input("Введите характеристику для поиска: ")
    found_contacts = []
    for contact in contacts:
        if search_key in contact:
            found_contacts.append(contact)
    if not found_contacts:
        print("Контакты не найдены.")
    else:
        for contact in found_contacts:
            contacts.remove(contact)
        write_contacts(file_name, contacts)
        print("Контакт успешно удален.")

# Функция для изменения контакта
def edit_contact(file_name):
    contacts = read_contacts(file_name)
    if not contacts:
        print("Телефонный справочник пуст.")
        return
    search_key = input("Введите характеристику для поиска: ")
    found_contacts = []
    for contact in contacts:
        if search_key in contact:
            found_contacts.append(contact)
    if not found_contacts:
        print("Контакты не найдены.")
        return

    new_last_name = input("Введите новую фамилию (оставьте пустым для пропуска): ")
    new_first_name = input("Введите новое имя (оставьте пустым для пропуска): ")
    new_patronymic = input("Введите новое отчество (оставьте пустым для пропуска): ")
    new_phone_number = input("Введите новый номер телефона (оставьте пустым для пропуска): ")

    for contact in found_contacts:
        if new_last_name:
            contact[0] = new_last_name
        if new_first_name:
            contact[1] = new_first_name
        if new_patronymic:
            contact[2] = new_patronymic
        if new_phone_number:
            contact[3] = new_phone_number

    write_contacts(file_name, contacts)
    print("Контакт успешно изменен.")

# Функция для вывода меню
def print_menu():
    print("1. Вывести все контакты")
    print("2. Добавить контакт")
    print("3. Найти контакт")
    print("4. Удалить контакт")
    print("5. Изменить контакт")
    print("6. Выход")

# Основная функция программы
def main():
    file_name = "phonebook.txt"  # Имя файла для хранения контактов
    while True:
        print_menu()
        choice = input("Выберите пункт меню: ")
        if choice == "1":
            list_contacts(file_name)
        elif choice == "2":
            add_contact(file_name)
        elif choice == "3":
            search_contact(file_name)
        elif choice == "4":
            delete_contact(file_name)
        elif choice == "5":
            edit_contact(file_name)
        elif choice == "6":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()