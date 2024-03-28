from datetime import *


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_greetings = []

    for user in users:
        converted_birthdays = user['greetings_date'].date()

        if converted_birthdays < today:
            converted_birthdays += timedelta(weeks=52)

        next_birthday = (converted_birthdays - today).days

        if converted_birthdays.weekday() == 5:
            converted_birthdays += timedelta(days=2)

        elif converted_birthdays.weekday() == 6:
            converted_birthdays += timedelta(days=1)

        if next_birthday <= 7:
            upcoming_greetings.append(
                {"name": user["name"], "greetings_date": converted_birthdays.strftime('%d.%m.%Y')})

    return upcoming_greetings






if __name__ == '__main__':
    users = [
        {"name": "John Doe", "greetings_date": "1999.01.22"},
        {"name": "Jane Smith", "greetings_date": "2023.01.29"}
    ]

    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)
