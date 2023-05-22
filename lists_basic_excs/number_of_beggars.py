string_of_nums = input().split(", ")
beggars = int(input())
list_integers = list(map(int, string_of_nums))

counter_beggars = 0
list_beggar_profit = []


while counter_beggars < beggars:
    sum_beggar = 0
    # the index % beggars == counter_beggars / that loop give us the oportunity to iterate over counter beggars and take the sums from the list with sums
    for index in range(len(list_integers)):
        if index % beggars == counter_beggars:
            sum_beggar += list_integers[index]
    list_beggar_profit.append(sum_beggar)
    counter_beggars += 1
print(list_beggar_profit)


# Task:
# You will receive 2 lines of input. On the first line, you will receive a single string of integers, separated by a comma and a space ", ".
# On the second line, you will receive a count of beggars. Your job is to print a list with the sum of what each beggar brings home, assuming they all take regular turns, from the first to the last number in the list.
# For example: [1, 2, 3, 4, 5] for 2 beggars will return a result of 9 and 6, as the first one takes [1, 3, 5], the second one collects [2, 4].
# The same list with 3 beggars would produce a better outcome for the second beggar: 5, 7 and 3, as they will respectively take [1, 4], [2, 5], and [3].
# Also, note that not all beggars have to take the same amount of "offers", meaning that the length of the list is not necessarily a multiple of n.
# The list length could be even shorter - i.e., the last beggars will take nothing (0).