#The file_date function creates a new file in the current working directory,
#checks the date that the file was modified, and returns just the date
#portion of the timestamp in the format of yyyy-mm-dd.
#Fill in the gaps to create a file called "newfile.txt"
#and check the date that it was modified.

import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  os.mkdir(filename)
  timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  time = datetime.datetime.fromtimestamp(timestamp)
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{}".format(time.strftime("%Y-%m-%d")))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd
