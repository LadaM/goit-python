def is_valid_pin_codes(pin_codes):
    # check all unique
    # check len == 4
    # check numeric
    if len(pin_codes) == 0:
        return False
    
    pincode_set = set()
    for p in pin_codes:
        if isinstance(p, str) and len(p) == 4 and p.isnumeric():
            if p in pincode_set:
                return False
            else:
                pincode_set.add(p)
        else:
            return False
    return True

print(is_valid_pin_codes(['1101', '9034', '0011b']))