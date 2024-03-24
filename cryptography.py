import string
CHAR_SET = string.printable[:-5]
SUBSTITUTION_CHARS =CHAR_SET[-3:]+CHAR_SET[:-3]
ENCRYPTION_DICT = {}
DECRYPTION_DICT = {}
for i,k in enumerate(CHAR_SET):
   v = SUBSTITUTION_CHARS[i]
   ENCRYPTION_DICT[k]=v
   DECRYPTION_DICT[v]=k

for c in string.printable[-5:]: 
   ENCRYPTION_DICT[c]=c
   DECRYPTION_DICT[c]=c
TEST_MESSAGE = "I like Monty Python. They are very funny."
INPUT_FILE_NAME = "cryptopy_input.txt"
OUTPUT_FILE_NAME = "cryptopy_output.txt"
def encrypt_msg(plaintext, encrypt_dict):
   ciphertext = []
   for k in plaintext:
       v = encrypt_dict[k]
       ciphertext.append(v)
   ciphertext.append(encrypt_dict[k])
   return ''.join(ciphertext)
def decrypt_msg(ciphertext, decrypt_dict):
   plaintext = []
   for k in ciphertext:
      v = decrypt_dict[k]
      plaintext.append(v)
   return ''.join(plaintext)
if __name__ == "__main__":
   ENCRYPT = False 
   with open(INPUT_FILE_NAME,'r') as input_file:
      message = input_file.read()
   if ENCRYPT:
      text_to_output =encrypt_msg(message, ENCRYPTION_DICT)
   else:
      text_to_output =decrypt_msg(message, DECRYPTION_DICT)
   print(text_to_output) 
   with open(OUTPUT_FILE_NAME,'w') as output_file:
      output_file.write(text_to_output)
