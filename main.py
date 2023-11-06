message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    if ord(ch) >= 65 and ord(ch) <= 90:
        encoded_message = encoded_message + chr((ord(ch) - ord('A') + offset) % 26 + ord('A'))
        continue
    elif ord(ch) >= 97 and ord(ch) <= 122 :
         encoded_message = encoded_message + chr((ord(ch) - ord('a') + offset) % 26 + ord('a'))
         continue
    else:
        encoded_message = encoded_message + ch

print(encoded_message)