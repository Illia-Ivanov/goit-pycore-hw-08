from decorator import input_error
from Classes import Record
from upcoming_birthdays import get_upcoming_birthdays


@input_error
def add_contact(args, book):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def change_contact(args, book):
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    record.edit_phone(old_phone, new_phone)

    return "Number is changed!"


@input_error
def phone(args, book):
    name, *_ = args
    record = book.find(name)
    result = [person_phone.value for person_phone in record.phones]

    return f'Person phone : \n{"\n".join(result)}'


def show_all(book):
    return f'Your contacts : \n{'\n'.join(book.keys())}'


@input_error
def add_birthday(args, book):
    name, birthday, *_ = args
    record = book.find(name)
    record.add_birthday(birthday)
    return 'Birthday added'


@input_error
def show_birthday(args, book):
    name, *_ = args
    record = book.find(name)
    birthday = record.birthday
    if birthday:
        return f'Person Birthday : {birthday.value.strftime('%d.%m.%Y')}'
    else:
        return 'I don\'t find a birthday'


def birthdays(book):
    soon_birthdays = []
    for name in book:
        soon_birthdays.append({"name": name, "greetings_date": book.find(name).birthday.value})

    soon_birthdays = get_upcoming_birthdays(soon_birthdays)
    return f"Congretulation dates: \n{'\n'.join([f'{my_dict['name']} : {my_dict['greetings_date']}' for my_dict in soon_birthdays])}"
