def palindrome(word,rword): 
    if word == rword:
        return True
    
    else:
     return False
    


word = input("input a word | ")

rword = word[::-1]

palindrome(word,rword)

if palindrome(word,rword):
    print(f"The string {word} is a palindrome.")
else:
    print(f"The string {word} is NOT a palindrome.")
