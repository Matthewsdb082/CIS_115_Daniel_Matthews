def append_to_list(item, target_list):
    target_list.append(item)
values = []

first_value = input("Enter a value to append to the list: ")
append_to_list(first_value, values)

while True:
    choice = input("Would you like to enter another value to append to the list? (y or n): ")

    if choice == "y":
        new_value = input("Enter a value to append to the list: ")
        append_to_list(new_value, values)

    elif choice == "n":
        break

    else:
        print("Sorry, you have entered an invalide value, please try again")

print("Here is your complete list:", values)