def range_generator(start, end):
    current = start
    while current <= end:
        yield current
        current += 1

# Usage
start_number = 17
end_number = 34

for num in range_generator(start_number, end_number):
    print(num)