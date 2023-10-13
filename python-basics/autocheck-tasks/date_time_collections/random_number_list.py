from random import sample,randrange


def get_numbers_ticket(min, max, quantity):
    if (min < 1 or max > 1000 or not quantity > min or not quantity < max):
        print(f"Expecting a value min >= 1, max <= 1000, and min < quantity < max")
        return []
    return sorted(sample([i for i in range(min, max + 1)], k=quantity))

def get_numbers_ticket2(min, max, quantity):
    if (min < 1 or max > 1000 or not quantity > min or not quantity < max):
        print(f"Expecting a value min >= 1, max <= 1000, and min < quantity < max")
        return []
    print(f"{min}, {max}, {quantity}")
    s = set()
    while len(s) < quantity:
        s.add(randrange(min, max))
    result = sorted(s)
    return result
        
if __name__ == "__main__":
    print(get_numbers_ticket(1, 1000, 1000))
    print(get_numbers_ticket(1, 1000, 12))            
    print(get_numbers_ticket(1, 49, 6))            
    print(get_numbers_ticket2(1, 49, 6))            
            
            
    