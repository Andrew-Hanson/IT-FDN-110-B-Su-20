#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# Ahanson, 2020-aug-05, draft two started
# Ahanson, 2020-aug-05, load function added
# Ahanson, 2020-aug-05, added context manager to write function
# Ahanson, 2020-aug-05, fixed bug where list not emptied after file write
# Ahanson, 2020-aug-05, No CD Entries!
# AHanson, 2020-aug-08, Entry deletion added
# AHanson, 2020-aug-08, code commented and cleaned up
# AHanson, 2020-aug-08, added print of stored entries after addding an entry


#TO-DO
#1)change the display menu so it prints before or after other information
#printed by the program, contextually
#2)find a use for exception handling
#3)check for valid entries
#4)allow deleting entries from the file
#5)dont allow duplicate entries

#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
# TODO replace list of lists with list of dicts
lstRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

#create file if none exists
# with is a context manager
# in this context, it will create a variable objFile and reference the opened file,
# strFileName in append mode. Then, it will run the code in the indent block and close the file.
# with context managers you will never forget to close your file. pun intended.
# note strFileName is a variable referncing the string 'CDInventory.txt'
with open(strFileName, 'a') as objFile:
    pass #pass is useful when syntax requires code in the indent block but you
         #don't actually want your program to do anything

# Get user Input
print('The Magic CD Inventory\n')
while True:
        # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        print('ID, CD Title, Artist') #header for display
        with open(strFileName, 'r') as objFile:
            print(objFile.read()) #prints entire file
        pass
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        lstRow = {'ID':strID,'title':strTitle,'artist':strArtist}
        #chose to keep name lstRow for dictionary to avoid multiple replacements
        lstTbl.append(lstRow)
        #display current entries in memory efter each entry is added
        if lstTbl != []: #check table is not empty
            print('ID, CD Title, Artist') #header for display
            for row in lstTbl: #print the values of each dictionary seperated by a comma and space
                print(*row.values(), sep = ', ')
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        if lstTbl != []: #check table is not empty
            print('ID, CD Title, Artist') #header for display
            for row in lstTbl: #print the values of each dictionary seperated by a comma and space
                print(*row.values(), sep = ', ')
            print()
        else: #just in case
            print('No CD entries!')
    elif strChoice == 'd':
        if lstTbl != []:
            print('ID, CD Title, Artist')
            for row in lstTbl: #display options to be deleted
                print(*row.values(), sep = ', ')
            strChoice2 = input('enter the id number of the entry to be deleted :')
            for row in lstTbl:
                if str(row['ID']) == strChoice2: #allows choosing by id number
                    gone = lstTbl.pop(row) #pop returns the removed value allowing it to be printed after removal
                    print(gone['ID'],' ',gone['title'],' ',gone['artist'],' deleted!')
                    print()
        else:#just incase
            print('No CD entries!')
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        with open(strFileName, 'a') as objFile:
            for row in lstTbl:
                strRow = ''
                for item in row.values():
                    strRow += str(item) + ','
                strRow = strRow[:-1] + '\n'
                objFile.write(strRow)
        print('Entries saved!')
        lstTbl = []  # list of data row
        #empties table in memory after written to file to prevent double entries
    else:
        print('Please choose either l, a, i, d, s or x!')
