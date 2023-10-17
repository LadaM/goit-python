# In mathematics and computer science, currying is the technique of breaking down 
# the evaluation of a function that takes multiple arguments into evaluating 
# a sequence of single-argument functions. Currying is also used in theoretical computer
# science, because it is often easier to transform multiple argument models into single 
# argument models.

def taxer_simple(base_tax, money):
    if money >= 10_000:
        base_tax = 1.5 * base_tax
    
    return money - base_tax * money

def taxer(base_tax):
    def calculate(money):
        nonlocal base_tax
        if money >= 10_000:
            base_tax = 1.5 * base_tax
    
        return money - base_tax * money

ukrainian = taxer(0.1) # 10% tax
sweedish = taxer(0.4) # 40% tax
