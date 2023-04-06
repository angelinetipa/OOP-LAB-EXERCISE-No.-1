alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

message = input("Message: ").strip().upper()
keyword = input("Key: ").strip().upper()

keyword_indices = []
for i in range(len(keyword)):
    letter = keyword[i]
    keyword_index = (alphabet.find(letter))
    keyword_indices.append(keyword_index)
print(keyword_indices)

message_indices = []
for j in range(len(message)):
    letter = message[j]
    message_index = (alphabet.find(letter))
    message_indices.append(message_index)

#for every 1 character of message add to every 1 character of keyword

    if index2 == len(str(keyword_index)) + 1:
        index2 = index2 - (len(str(keyword_index))) + 1
   
