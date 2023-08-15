def sum_numbers_from_file(file_name):
    total_sum = 0

    try:
        with open("test.txt", 'r') as file:
            for line in file:
                numbers = line.strip().split(',')
            for num_str in numbers:
                    try:
                        num = int(num_str)
                        total_sum += num
                    except ValueError:
                        pass  # Ignore non-numeric values

        print("Sum of numbers:", total_sum)

    except FileNotFoundError:
        print("File not found:", "test.txt")
    except Exception as e:
        print("An error occurred:", e)

file_name = 'test.txt'
sum_numbers_from_file(file_name)





