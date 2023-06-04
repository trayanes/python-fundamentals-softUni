def find_palindrome(list_ints):
    for number in list_ints:
        if number == number[::-1]:
            return True
        return False


int_list = list(map(str, input().split(", ")))

for i in int_list:
    print(find_palindrome(int_list))