from collections import UserDict
from datetime import datetime


class PhoneNotPasst(Exception):
    pass


class PhoneNotFound(Exception):
    pass


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    # реалізація класу
    pass


class Phone(Field):
    def __init__(self, phone):
        if len(phone) == 10 and phone.isdigit():
            super().__init__(phone)
        else:
            raise PhoneNotPasst


class Birthday(Field):

    def __init__(self, user_date):
        try:
            formated_birthday = datetime.now().strptime(user_date, '%d.%m.%Y')
            super().__init__(formated_birthday)

        except ValueError:
            raise ValueError("Invalid date-format")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None



    def add_birthday(self,birthday):
        self.birthday = Birthday(birthday)






    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, before_phone, after_phone):
        for phone in self.phones:
            if before_phone == phone.value:
                self.phones[self.phones.index(phone)] = Phone(after_phone)
                return None
        raise PhoneNotFound

    def find_phone(self, phone):
        for numb in self.phones:
            if numb.value == phone:
                return numb

        raise PhoneNotFound

    def remove_phone(self, phone):
        for numb in self.phones:
            if numb.value == phone:
                return self.phones.remove(numb)

        raise PhoneNotFound

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data.update({record.name.value: record})

    def find(self, person_name):
        return self.data.get(person_name)

    def delete(self, person):
        del self.data[person]


if __name__ == '__main__':
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # john_record.remove_phone('5555555555') перевірка для видалення номера телефону

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for record in book.data.values():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
