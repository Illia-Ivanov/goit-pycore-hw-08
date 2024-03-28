from Classes import PhoneNotPasst, PhoneNotFound


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except PhoneNotPasst:
            return "This phone has wrong format!"
        except PhoneNotFound:
            return "This phone is not found,try again!"
        except Exception as e:
            return f"{e}"

    return inner
