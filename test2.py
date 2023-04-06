alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

message = input("Message: ").strip().upper()
keyword = input("Key: ").strip().upper()

message_indices = []
for j in range(len(message)):
    letter = message[j]
    message_index = (alphabet.find(letter))
    message_indices.append(message_index)
print(message_indices)  

keyword_indices = []
for i in range(len(keyword)):
    letter = keyword[i]
    keyword_index = (alphabet.find(letter))
    keyword_indices.append(keyword_index)
print(keyword_indices)

index1 = 0
index2 = 0
mod_message_keyword = []
for k in range(len(message_indices)):
    sum = message_indices[index1] + keyword_indices[index2]
    if sum < len(alphabet):
        mod_message_keyword.append(sum)
    elif sum >= len(alphabet):
        mod = sum % len(alphabet)
        mod_message_keyword.append(mod)
    index1 += 1
    index2 += 1
    if index2 == len(keyword_indices):
        index2 -= len(keyword_indices)
print(mod_message_keyword)
    
mod_indices = []
for p in range(len(mod_message_keyword)):
    letter = mod_message_keyword[p]
    mod_index = (alphabet[letter])
    mod_indices.append(mod_index)
print(mod_indices) 



   

