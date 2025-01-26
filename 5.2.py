from functools import reduce

numbers = [2, 4, 6, 3, 7, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

sum_even_numbers = reduce(lambda x, y: x + y, even_numbers)

# Output the result
print(f"Sum of even numbers: {sum_even_numbers}")