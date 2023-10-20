def format_phone_number(func):
    def wrapper(*args, **kwargs):
        number = func(*args, **kwargs)
        return "+" + number if len(number) == 12 else "+38" + number
    return wrapper


@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


if __name__ == "__main__":
    phone_numbers = [
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   "
    ]

    formatted_numbers = map(sanitize_phone_number, phone_numbers)
    print(list(formatted_numbers))
