#Ma. Angeline Tipa|BSCPE 1-5|Vigenère Cipher Program|Before 04-08-23

print("*" * 55)
# a variable for alphabetical letters
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# input for the plaintext and keyword, remove space and change to uppercase
message = input("\n\033[3m\033[1m" "Message: \n> " "\033[0m").strip().upper()
keyword = input("\n\033[3m\033[1m" "Key: \n> " "\033[0m").strip().upper()
# list for message indices
message_indices = []
# find the index of each letter in message then add to list
for j in range(len(message)):
    message_indices.append(alphabet.find(message[j]))
# list for keyword indices
keyword_indices = []
# find the index of each letter in message then add to list
for i in range(len(keyword)):
    keyword_indices.append(alphabet.find(keyword[i]))

index1 = 0
index2 = 0
# list for mod of sum of message's and keyword's indices
mod_message_keyword = []
# for every message indices a keyword indices will add
for k in range(len(message_indices)):
    sum = message_indices[index1] + keyword_indices[index2]
    # if sum less than the len of alphabet, add to list, otherwise take mod then add to list
    if sum < len(alphabet):
        mod_message_keyword.append(sum)
    elif sum >= len(alphabet):
        mod_message_keyword.append(sum % len(alphabet))
    index1 += 1
    # if index2 on last index of keyword, bring it back to zero
    index2 += 1
    if index2 == len(keyword_indices):
        index2 -= len(keyword_indices)
print("\n\033[3m\033[1m" "Ciphertext: " "\033[0m")     
#take the index from list mod message keyword to the variable alphabet
for p in range(len(mod_message_keyword)):
    mod_indices = alphabet[mod_message_keyword[p]]
# output for ciphertext/print the result
    print("\033[4m", mod_indices, end="") 
print("\033[0m" "\n\n", end="*" * 55)

