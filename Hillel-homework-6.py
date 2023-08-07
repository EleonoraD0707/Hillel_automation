def fibonacci_number_recursive(n):
    if n < 0:
        return "Wrong input"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_number_recursive(n - 1) + fibonacci_number_recursive(n - 2)

result = fibonacci_number_recursive(int(input()))
print("Fibonacci number by given index:", result)