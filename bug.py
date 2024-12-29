def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage:
my_numbers = [10, 20, 30, 40, 50]
avg = calculate_average(my_numbers)
print(f"The average is: {avg}")

my_empty_list = []
result = calculate_average(my_empty_list)
print(f"The average of an empty list is: {result}") # this line will produce ZeroDivisionError