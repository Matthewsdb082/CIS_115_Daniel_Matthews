def search(month):
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    if month in months:
        print(f"We found {month} in the months list. Search successful!")
    else:
        print(f"We could not find {month} in the months list.")

user_month = input("Enter a Month name: ")
search(user_month)