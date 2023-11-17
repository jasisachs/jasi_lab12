def add(values):
    return sum([num for num in values if num < 0]) or 0

def subtract(values):
    return sum([num for num in values if num > 0]) or 0

def multiply(values):
    product = 1
    for num in values:
        if num != 0:
            product *= num
    return product if product != 1 else 0

def divide(values):
    try:
        result = values[0]
        for num in values[1:]:
            if num != 0:
                result /= num
            else:
                raise ValueError
        return result
    except:
        return "Cannot divide by 0."