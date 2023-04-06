#Ma. Angeline T. Tipa|BSCPE 1-5|Descryption Program|Before 04-08-23

# ask user for input
print("*" * 70)
encrypted_str = input("\n\033[3m\033[1m" "Enter a text to decrypt: " "\033[0m" ) 
decrypted_str = ""
# check each character
for i in range(len(encrypted_str)):
#   if *, change to a
    if encrypted_str[i] == "*":
        decrypted_str += "\033[0;31m" "a" "\033[0m"
#   if &, change to e
    elif encrypted_str[i] == "&":
        decrypted_str += "\033[0;31m" "e" "\033[0m"
#   if #, change to i
    elif encrypted_str[i] == "#":
        decrypted_str += "\033[0;31m" "i" "\033[0m"
#   if +, change to o
    elif encrypted_str[i] == "+":
        decrypted_str += "\033[0;31m" "o" "\033[0m"
#   if !, change to u
    elif encrypted_str[i] == "!":
        decrypted_str += "\033[0;31m" "u" "\033[0m"
#   else, do not change 
    else:
        decrypted_str += encrypted_str[i]
# print output
print("\033[3m\033[1m" "The decrypted string is:""\033[0m", decrypted_str, "\n\n", end="*" * 70 )


