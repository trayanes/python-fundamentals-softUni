sequence_nums = [int(i) for i in input().split(", ")]


def is_palindrome(list_ints):
    for number in list_ints:
        number_as_string = str(number)
        if number_as_string == number_as_string[::-1]:
            print("True")
        else:
            print("False")


is_palindrome(sequence_nums)
