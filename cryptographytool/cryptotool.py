def cryptosec():
 keys = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ !'
 value = keys[-1] + keys[0:-1]

 encryptDict = dict(zip(keys, value))
 decryptDict = dict(zip(value, keys))

 message= input("Enter your message : ")
 mode = input("Please select the mode : Encode (E) OR Decode (D) : ")

 if mode.upper()== "E":
     newMessage = ''.join([encryptDict[letter] for letter in message])

 elif mode.upper() == "D":
     newMessage = ''.join([decryptDict[letter] for letter in message])

 else:
     print("Please enter a valid mode ! ")
     
 return newMessage

print(cryptosec())
