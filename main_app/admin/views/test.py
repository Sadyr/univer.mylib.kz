def get_gpa(number):
    if number >= 95 and number <= 100:
        return 4
    elif number >= 90 and number <= 94:
        return 3.67
    elif number >= 85 and number <= 89:
        return 3.33
    elif number >= 80 and number <= 84:
        return 3
    elif number >= 75 and number <= 79:
        return 2.67
    elif number >= 70 and number <= 74:
        return 2.33
    elif number >= 65 and number <= 69:
        return 2
    elif number >= 60 and number <= 64:
        return 1.67
    elif number >= 55 and number <= 59:
        return 1.33
    elif number >= 50 and number <= 54:
        return 1
    elif number >= 0 and number <= 49:
        return 0
