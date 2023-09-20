
def unique_elements(input_list):
  new_list = []
  for value in input_list:
    if value not in new_list:
      new_list.append(value)
  return new_list