import os
source = ('C:/Users/Н/Edu/python/seminars/8/phonebook.txt')

#READ FILE
def readData (fileName):
    with open (fileName) as f:
        phoneBook = []
        for line in f:
            phoneBook.append(line.split(','))
    return phoneBook

phoneBook = readData(source)

#WRITE FILE
def writeData (fileName, phoneBook):
    with open (fileName, 'w') as f:
        for i in phoneBook:
            f.write (','.join(i))
        print("Data saved")

# ALL SHOW DATABASE  
def selectAllReadPhoneNumber(source):
    phoneBook = readData(source)
    for i in phoneBook:
        print (i)

# ADD PERSON
def addPerson (phoneBook, source):
    print ("Enter data:")
    number = str(len(phoneBook) + 1)
    surname = str(input("Enter surname:"))
    nameFirst = str(input("Enter first name:"))
    nameSecond = str(input("Enter second name:"))
    phoneNumber = str(input("Enter telephone number:"))
    n = ' \n'
    phoneBook.append([number, surname, nameFirst, nameSecond, phoneNumber, n])
    writeData(source, phoneBook)
    print('jobs done')

#SEARCH
def Search(phoneBook):
    search_value = str(input('Enter search value: '))
    for i in phoneBook:
        for j in i:
            if search_value == j:
                print(i)
                return phoneBook.index(i)
        
#EDIT DATA
def Edit(phoneBook, source):
    print('You are editing data now')
    string_to_edit = Search(phoneBook)
    number = str(string_to_edit+1)
    surname = str(input("Enter surname:"))
    nameFirst = str(input("Enter first name:"))
    nameSecond = str(input("Enter second name:"))
    phoneNumber = str(input("Enter telephone number:"))
    n = ' \n'
    phoneBook.insert (string_to_edit, ([number, surname, nameFirst, nameSecond, phoneNumber, n]))
    writeData(source, phoneBook)
    print('jobs done')

#DELETE DATA
def Delete(phoneBook, source):
    print('You are deliting data now')
    string_to_delete = Search(phoneBook)
    phoneBook.pop(string_to_delete)
    writeData(source, phoneBook) 
    print('jobs done')
    

#Чистка консольки
clear = lambda: os.system('cls')
clear()

print ('''HELLO, USER 
        \n [1] -- press for SHOW ALL 
        \n [2] -- press for SEARCH
        \n [3] -- press for ADD DATA
        \n [4] -- press for EDIT DATA
        \n [5] -- press for DELETE DATA
        ''')
while True:
    enteredNum = int(input())
    try:
        if (enteredNum == 1):
            selectAllReadPhoneNumber(source)
        elif (enteredNum == 2):
            print('String No: ', Search(phoneBook))
        elif (enteredNum == 3):
            addPerson(phoneBook, source)
        elif (enteredNum == 4):
            Edit(phoneBook, source)
        elif (enteredNum == 5):
            Delete(phoneBook, source)
        else:
            print(3)
            break
    except:
        print("it's not a number")