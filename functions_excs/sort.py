def sort(int_list):
    result = sorted(int_list)
    return result


sequence_nums = [int(i) for i in input().split()]
print(list(sort(sequence_nums)))
