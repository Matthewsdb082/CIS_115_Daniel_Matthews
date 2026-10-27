
count=0

while True:
    x= int(input("please input number of grades to enter 10 or less."))
    if x <=10:

     while count < x:
      console =float( input(f"enter grade {count} :" ))
      print (console)
      count += 1
    break

