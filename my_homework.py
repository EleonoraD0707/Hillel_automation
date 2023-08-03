# def my_arguments(arg1, arg2):
#     if isinstance(arg1, (int)) and isinstance(arg2, (int)):
#         return arg1 * arg2
# result = my_arguments(3, 4)
# print(result)

# def my_arguments(arg1, arg2):
#     if isinstance(arg1, (str)) and isinstance(arg2, (str)):
#         return arg1 + arg2
# result = my_arguments("Eliza", "beth")
# print(result)

def my_arguments(arg1, arg2):
    if isinstance(arg1, (int)) and isinstance(arg2, (int)):
        return arg1 * arg2
    elif isinstance(arg1, (str)) and isinstance(arg2, (str)):
        return arg1 + arg2
    else:
        return arg1, arg2

