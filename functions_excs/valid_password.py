def password_validation(password):
    counter_false = 0
    if not 6 <= len(password) <= 10:
        counter_false += 1
        print("Password must be between 6 and 10 characters")
    if not password.isalnum():
        counter_false += 1
        print("Password must consist only of letters and digits")
    counter_digits = 0
    for ele in password:
        if ele.isnumeric():
            counter_digits += 1
    if not counter_digits >= 2:
        counter_false += 1
        print("Password must have at least 2 digits")
    return counter_false


password_arg = input()
counter_false = password_validation(password_arg)
if counter_false == 0:
    print("Password is valid")

