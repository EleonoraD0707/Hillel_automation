lst = [1, 7, 45, 78, 99, 10, 12, 13, 66, 44]
sum_of_even_numbers = 0
for num in lst:
    if num % 2 == 0:
        sum_of_even_numbers += num
print(sum_of_even_numbers)