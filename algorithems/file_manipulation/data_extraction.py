
number_of_records = 0
unique_students = {}
grades = {}


with open('data.txt', 'r') as data_file:
  
  for line in data_file:
    number_of_records += 1
    parts = line.split(":")
    
    unique_students[parts[0]] = parts[2]
    print(unique_students)
    

    
    
  