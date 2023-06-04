def validate_pass(password):
    is_valid = True

    if not 6 <= len(password) <= 10:
        is_valid = False
        print("Password must be between 6 and 10 characters")
    if not password.isalnum():
        is_valid = False
        print("Password must consist only of letters and digits")
    digit_counter = [x for x in password if x.isdigit()]
    if len(digit_counter) < 2:
        is_valid = False
        print("Password must have at least 2 digits")
    if is_valid:
        print("Password is valid")


input_password = input()
validate_pass(input_password)