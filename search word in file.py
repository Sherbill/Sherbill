
file = open("C://Users/dell/Desktop/ZAIM PROGRAMS/zaim.txt.txt", "r")
def findInFile(word):
    count=0
    for line in file:
        list = line.split()
        print(list)
        for wordInFile in list:
            if wordInFile.index(word) >0:
                count += 1

    return count


print("enter the word to be searched : ")
sword = input()

counter = findInFile(sword)

if counter == 0:
        print("\n the word {} is {} not found".format(sword, counter))
else:
    print("\n the word {} is {} found".format(sword, counter))

file.flush()
file.close()
