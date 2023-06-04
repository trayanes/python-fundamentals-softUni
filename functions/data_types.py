def find_data_type(data_type: str, string: str):
    if data_type == "int":
        return int(string) * 2
    elif data_type == "real":
        result = float(string) * 1.5
        return f"{result:.2f}"
    elif data_type == "string":
        return f"${string}$"


input_data = input()
input_string = input()
print(find_data_type(input_data, input_string))