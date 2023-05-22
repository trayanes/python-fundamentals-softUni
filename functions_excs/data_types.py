def data_type_func(first_line,second_line):
    result = 0
    if first_line == "int":
        result = int(second_line) * 2
    elif first_line == "real":
        result = f"{float(second_line) * 1.5:.2f}"
    elif first_line == "string":
        return f"${second_line}$"
    return result


line1 = input()
line2 = input()
print(data_type_func(line1, line2))
