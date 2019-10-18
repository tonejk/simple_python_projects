# MD5 Hash from string to hexadecimal

import hashlib 
  
# User input string 
userInput = input('Enter your password: ')

# Encode using encode()
# Send to md5() 
result = hashlib.md5(userInput.encode()) 
  
# Returns the encoded data in hexadecimal format. 
print("Result is: ", end ="") 
print(result.hexdigest()) 

input("Press Enter to continue...")
