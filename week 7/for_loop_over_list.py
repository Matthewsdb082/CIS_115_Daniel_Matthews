my_list={10,20,30,40,50,60}
count =0
def getMyList(my_list):
    count =0
    for x in my_list:
        print(x)
        count +=1
    return count


total= getMyList(my_list)

print("total for loops ran was:", total)
