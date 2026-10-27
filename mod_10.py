
def validator():
 card_number = input("enter credit card number ")
 multiplied_numbers=[]
 re_card_number = card_number[::-1]
 total = 0 
 eventot = 0
 even_indexed = re_card_number[::2]
 odd_indexed = re_card_number[1::2]

 for char in odd_indexed:
    odd = int(char) * 2
    
    if odd <= 9:
        multiplied_numbers.append(odd)
    else:
        multiplied_numbers.append(odd - 9)

 for char in even_indexed:
    eventot += int(char)
 total = sum(multiplied_numbers)+ eventot

 check = total %10
 if check == 0:
    print(f"The credit card number {card_number} is valid!")
 else :
    print("Invalid credit card entered. Please try again.")
    validator()
 return
    
validator()