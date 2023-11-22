import os
def clear_console():
    os.system('cls')
clear_console()

def work_with_phonebook():
    def actions():
        print()        
        print('Выберите действие:',
            '1. Распечатать справочник',
            '2. Найти телефон по фамилии',
            '3. Изменить номер телефона',
            '4. Удалить запись',
            '5. Найти абонента по номеру телефона',
            '6. Добавить абонента в справочник',
            '7. Закончить работу', sep='\n')
        print()
        option = int(input())
        return option

    def read_txt(fileName):
        phone_book = []
        fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
        with open(fileName, 'r', encoding='utf-8') as phb:
            for line in phb:
                record = dict(zip(fields, line.split(',')))
                phone_book.append(record)
        return phone_book

    def write_txt(fileName, phone_book):
        with open(fileName, 'w', encoding = 'utf-8') as phout:
            for i in range(len(phone_book)):
                s=''
                for v in phone_book[i].values():
                    s+=v+','
                phout.write(f'{s[:-1]}\n')

    def find_by_lastename(phone_book, l_name):
        for i in range(len(phone_book)):
            if phone_book[i].get('Фамилия') == l_name:
                return phone_book[i].get('Телефон')
        return "не найден"

    def change_number(phone_book, l_name, n_number):
        for i in range(len(phone_book)):
            if phone_book[i].get('Фамилия') == l_name:
                phone_book[i]['Телефон'] = n_number
                return "изменен"
        return "с такой фамилией не найден"

    def del_record(phone_book, l_name):
        for i in range(len(phone_book)):
            if phone_book[i].get('Фамилия') == l_name:
                phone_book.pop(i)
                return "произведено"
        return 'не произведено, фамилия не найдена'

    def find_by_tel(phone_book, telephone):
        for i in range(len(phone_book)):
            if phone_book[i].get('Телефон') == telephone:
                return phone_book[i].get('Фамилия')
        return "не найдена"

    def add_record(phone_book, l_name, a_name, a_number, a_description):
        new_dictionary = {'Фамилия':l_name, 'Имя':a_name, 'Телефон':a_number, 'Описание':a_description}
        phone_book.append(new_dictionary)
        return "Абонент в справочник добавлен"

    phoneBook = read_txt('guide.txt')
    var = actions()

    while (var != 7):
        if var == 1:
            clear_console()
            with open('guide.txt', 'r', encoding='utf-8') as data:
                k = 15
                print()
                print('Фамилия        ', 'Имя   ', '         Телефон', '        Описание')
                for line in data:
                    string = line.replace(",",' ').split()
                    for i in range(len(string)):
                        if i < 3:
                            print(string[i].ljust(k), end=' ')
                        else: print(string[i], end=' ')
                    print()

        if var == 2:
            last_name = input('Введите фамилию: ')
            print('Телефон абонента: ', find_by_lastename(phoneBook, last_name))

        if var == 3:
            last_name = input('Введите фамилию: ')
            new_number = input('Введите новый номер телефона: ')
            print("Телефон абонента", change_number(phoneBook, last_name, new_number))
            write_txt('guide.txt', phoneBook)

        if var == 4:
            last_name = input('Введите фамилию, удаляемого абонента: ')
            print("Удаление записи абонента ",del_record(phoneBook, last_name))
            write_txt('guide.txt', phoneBook)

        if var == 5:
            tel = input('Введите телефон: ')
            print('Фамилия абонента: ', find_by_tel(phoneBook, tel))

        if var == 6:
            last_name = input('Введите фамилию: ')
            name = input('Введите имя: ')
            number = input('Введите номер телефона: ')
            description = input('Введите описание: ')
            print(add_record(phoneBook, last_name, name, number, description))
            write_txt('guide.txt', phoneBook)

        var = actions()
work_with_phonebook()
