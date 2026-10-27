def months_of_year(startMonth,endMonth):
    months = ["Jan", "Feb", "March", "April", "May", "June","July", "Aug", "Sept", "Oct", "Nov", "Dec"]
    return months[startMonth:endMonth]


startMonth = int(input("enter the start month index 0-11: "))
endMonth = int(input ("enter the start month index 1-12: "))

results =  months_of_year(startMonth,endMonth)

print (f"The selected months are : {results}")
