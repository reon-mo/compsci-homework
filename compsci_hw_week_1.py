numGrid = [
    [66, 28, 97, 28, 6, 16, 45, 7, 71, 47],
    [43, 13, 9, 43, 18, 5, 80, 32, 10, 86],
    [73, 20, 19, 72, 95, 70, 70, 61, 98, 96],
    [11, 45, 4, 45, 25, 45, 9, 99, 98, 90],
    [28, 48, 85, 26, 59, 46, 12, 66, 78, 47],
    [62, 47, 16, 77, 68, 31, 37, 96, 11, 59],
    [12, 53, 6, 61, 87, 80, 8, 48, 38, 15],
    [68, 82, 29, 95, 64, 76, 82, 88, 37, 90],
    [57, 18, 27, 15, 69, 79, 46, 83, 29, 80], 
    [10, 79, 75, 58, 26, 29, 88, 30, 91, 78]
]
 
max = numGrid [0][0]
min = numGrid [0][0]
sum = 0
average = 0
range = 0
 
for list in numGrid:
    for number in list:
        if number < min:
                min = number
 
for list in numGrid:
     for number in list:
          if number > max:
                max = number
 
sum += number
 
average = sum / (len(numGrid) * len(numGrid[0]))
range = max - min
 
print (min)
print (max)
print (average)
print (range)
print ("select the number you want to find the range, average, minimum, and maximum of")
 
menuChoice = input("Enter a list from 1 to 10: ")
 
 
if menuChoice == "1":
    print (numGrid[0])
    print ("1. Minimum")
    print ("2. Maximum")
    print ("3. Average")
    print ("4. Range")
    valueChoice = input("Enter a number from 1 to 4: ")
    if valueChoice == "1":
        print (min)
    elif valueChoice == "2":
        print (max)
    elif valueChoice == "3":
        print (average)
    elif valueChoice == "4":
        print (range)
elif menuChoice == "2":
    print (numGrid[1])
    print ("1. Minimum")
    print ("2. Maximum")
    print ("3. Average")
    print ("4. Range")
    valueChoice = input("Enter a number from 1 to 4: ")
    if valueChoice == "1":
        print (min)
    elif valueChoice == "2":
        print (max)
    elif valueChoice == "3":
        print (average)
    elif valueChoice == "4":
        print (range)
elif menuChoice == "3":
    print (numGrid[2])
    print ("1. Minimum")
    print ("2. Maximum")
    print ("3. Average")
    print ("4. Range")
    valueChoice = input("Enter a number from 1 to 4: ")
    if valueChoice == "1":
        print (min)
    elif valueChoice == "2":
        print (max)
    elif valueChoice == "3":
        print (average)
    elif valueChoice == "4":
        print (range)          
elif menuChoice == "4":
    print (numGrid[3])
    print ("1. Minimum")
    print ("2. Maximum")
    print ("3. Average")
    print ("4. Range")
    valueChoice = input("Enter a number from 1 to 4: ")
    if valueChoice == "1":
        print (min)
    elif valueChoice == "2":
        print (max)
    elif valueChoice == "3":
        print (average)
    elif valueChoice == "4":
        print (range)
elif menuChoice == "5":
    print (numGrid[4])
    print ("1. Minimum")
    print ("2. Maximum")
    print ("3. Average")
    print ("4. Range")
    valueChoice = input("Enter a number from 1 to 4: ")
    if valueChoice == "1":
        print (min)
    elif valueChoice == "2":
        print (max)
    elif valueChoice == "3":
        print (average)
    elif valueChoice == "4":
        print (range)    
elif menuChoice == "6":
    print (numGrid[5])
    print ("1. Minimum")
    print ("2. Maximum")
    print ("3. Average")
    print ("4. Range")
    valueChoice = input("Enter a number from 1 to 4: ")
    if valueChoice == "1":
        print (min)
    elif valueChoice == "2":
        print (max)
    elif valueChoice == "3":
        print (average)
    elif valueChoice == "4":
        print (range)
elif menuChoice == "7":
    print (numGrid[6])
    print ("1. Minimum")
    print ("2. Maximum")
    print ("3. Average")
    print ("4. Range")
    valueChoice = input("Enter a number from 1 to 4: ")
    if valueChoice == "1":
        print (min)
    elif valueChoice == "2":
        print (max)
    elif valueChoice == "3":
        print (average)
    elif valueChoice == "4":
        print (range)
elif menuChoice == "8":
    print (numGrid[7])
    print ("1. Minimum")
    print ("2. Maximum")
    print ("3. Average")
    print ("4. Range")
    valueChoice = input("Enter a number from 1 to 4: ")
    if valueChoice == "1":
        print (min)
    elif valueChoice == "2":
        print (max)
    elif valueChoice == "3":
        print (average)
    elif valueChoice == "4":
        print (range)
elif menuChoice == "9":
    print (numGrid[8])
    print ("1. Minimum")
    print ("2. Maximum")
    print ("3. Average")
    print ("4. Range")
    valueChoice = input("Enter a number from 1 to 4: ")
    if valueChoice == "1":
        print (min)
    elif valueChoice == "2":
        print (max)
    elif valueChoice == "3":
        print (average)
    elif valueChoice == "4":
        print (range)
elif menuChoice == "10":
    print (numGrid[9])    
    print ("1. Minimum")
    print ("2. Maximum")
    print ("3. Average")
    print ("4. Range")
    valueChoice = input("Enter a number from 1 to 4: ")
    if valueChoice == "1":
        print (min)
    elif valueChoice == "2":
        print (max)
    elif valueChoice == "3":
        print (average)
    elif valueChoice == "4":
        print (range)
