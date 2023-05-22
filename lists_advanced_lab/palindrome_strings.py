strings = input().split()
searched_palindrome = input()

palindromes = [pali for pali in strings if pali == pali[::-1]]
result = [searched_pal for searched_pal in palindromes if searched_pal == searched_palindrome]
print(palindromes)
print(f"Found palindrome {len(result)} times")
