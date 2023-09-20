# file objects


with open('./file_manipulation/dragon_fantasy_art-wallpaper-3440x1440.jpg', 'rb') as rf:
  with open('./file_manipulation/dragon_fantasy_art_copy.jpg', 'wb') as wf:
    chunk_size = 4096
    rf_chunk = rf.read(chunk_size)
    while len(rf_chunk) > 0:
      wf.write(rf_chunk)
      rf_chunk = rf.read(chunk_size)
  
  
  # while len(f_contents) > 0:
  #   print(f_contents, end="*")
  #   f_contents = f.read(size_to_read)
  
