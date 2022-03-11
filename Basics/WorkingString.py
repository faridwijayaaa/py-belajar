
phrase = "Farid Wijaya";

# \n works for newlines
print("Farid\nWijaya");

# \" works for quote
print("Farid\"Wijaya");

# to Uppercase or Lowercase
print(phrase.upper()); # .lower()

# check if it is uppercase or lower case : True / False
print(phrase.upper().isupper()); # .islower()

# check how many characters in string 
print(len(phrase));

# get index value of string, in pyhton is work bro :)
print(phrase[4]);

# this function is to replace one of the words.
print(phrase.replace("Farid", "Linguard"));