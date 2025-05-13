# The file cursor is necessary for reading or modifying specific parts of the file. Methods like .seek() move the cursor to a desired location within the file.
# Moving the file cursor using seek()
with open('example.txt', 'r') as file:
  file.seek(10)  # Move to the 10th byte
  content = file.read()

# The .truncate() method allows us to modify file size. This is useful when we want to remove or reset content beyond a certain point. We can trim or extend the file size as needed.
# Truncating a file
with open('example.txt', 'a') as file:
  file.truncate(20)  # Limit the file size to 20 bytes

# Note: r+ in the open() function is used to indicate both reading and writing are allowed in the file.
# Modify the message to simulate unsending
with open('sent_message.txt', 'r+') as file:
  # Read the sent message from the file
  original_message = file.read()
      
  # Move the cursor to the beginning of the file
  file.seek(0)