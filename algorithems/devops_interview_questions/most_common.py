def most_common_character(input_string):
  char_count = {}
  
  for char in input_string:
    if char in char_count:
      print(f"adding new char {char} to {char_count}")
      char_count[char] += 1
    else:
      char_count[char] = 1
  return max(char_count, key=char_count.get)

input_str = "hello world"
result = most_common_character(input_str)
print("Most common character:", result)