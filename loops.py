# for i in range (0,10):
#   print("hello zaid")
def list_update():
    abc = ["zaid", "ahmed", "apple", "carrot", "laptop", "sham"]
    count = 0
    print(abc)
    add = input("write anything to add in this list: ")
    abc.append(add)

    for i in abc:
        count = count + 1
        print(count, ": ", i)
    print("\nlist: ", abc)


list_update()