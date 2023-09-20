

# json_file : { }

from gettext import find


def create_json():
  json_file = {
    "userId": 1,
    "firstName": "yaron_r",
    "lastName": "basson_re",
    "phoneNumber": "+972546868728"
  }


  # any _re _r to _x
  for i in json_file:
    if(i == "firstName"):
      if json_file["firstName"].find("_r") != -1 :
        new_first_name = json_file["firstName"].split("_r")
        json_file["firstName"] = new_first_name[0] + "_x"
      if json_file["firstName"].find("_re") != -1:
        new_first_name = json_file["firstName"].split("_r")
        json_file["firstName"] = new_first_name[0] + "_x"
        
    if(i == "lastName"):
      if json_file["lastName"].find("_r") != -1 :
        new_first_name = json_file["lastName"].split("_r")
        json_file["lastName"] = new_first_name[0] + "_x"
      if json_file["lastName"].find("_re") != -1 :
        new_first_name = json_file["lastName"].split("_r")
        json_file["lastName"] = new_first_name[0] + "_x"      
      

      
  
  print(json_file)
  
create_json()