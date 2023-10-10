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


def get_phone_numbers_for_countries(list_phones):
    phone_numbers_by_country = {
        "UA": [],
        "JP": [],
        "TW": [],
        "SG": [],
    }

    phone_code_by_country = {
        "JP": "81",
        "SG": "65",
        "TW": "886",
        "UA": "380",
    }
    
    for ph in list_phones:
        phone = sanitize_phone_number(ph)
        matched = False # for not matching  numbers that have to be added to UA
        
        for country, code in phone_code_by_country.items():
            if phone.startswith(code):
                phone_numbers_by_country.get(country).append(phone)
                matched = True
                break

        if not matched:
            phone_numbers_by_country.get("UA").append(phone)
    
    return phone_numbers_by_country  

get_phone_numbers_for_countries(['380998759405', '818765347', '8867658976', '657658976'])