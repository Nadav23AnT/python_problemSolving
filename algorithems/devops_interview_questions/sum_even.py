def sum_even_numbers(numbers):
    # Initialize a variable to store the sum of even numbers
    even_sum = 0
    
    # Loop through the numbers in the list
    for number in numbers:
        if number % 2 == 0:
          even_sum += number
    
    return even_sum

# Test your function with a list of integers
if __name__ == "__main__":
  numbers_list = [1, 2, 3, 4, 5, 6]
  result = sum_even_numbers(numbers_list)
  print("Sum of even numbers:", result)
