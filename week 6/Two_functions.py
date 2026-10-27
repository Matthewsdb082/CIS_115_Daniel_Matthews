def print_message1():
    print("i was called first")
    print_message2()
    return
def print_message2():
    print("i was called from print_message1()")
    return 
print_message1()