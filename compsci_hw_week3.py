import random

list = [random.randint(1, 100) for _ in range(6)]
print("Unsorted list:", list)
print("Choose a sorting algorithm:")
print("1. (B)ubble Sort")
print("2. (S)election Sort")
choice = input("Enter your choice (1 or 2): ")

if choice == "b" or choice == "1":
    print("You chose Bubble Sort.")
    comparisons = 0
    swaps = 0
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            comparisons += 1
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                swaps += 1
    print("Sorted list:", list)
    print("Total comparisons:", comparisons)
    print("Total swaps:", swaps)
elif choice == "s" or choice == "2":
    print("You chose Selection Sort.")
    comparisons = 0
    swaps = 0
    n = len(list)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            comparisons += 1
            if list[j] < list[min_index]:
                min_index = j
        if min_index != i:
            list[i], list[min_index] = list[min_index], list[i]
            swaps += 1
    print("Sorted list:", list)
    print("Total comparisons:", comparisons)
    print("Total swaps:", swaps)
else:
    print("Invalid choice. Please choose bubble or selection sort.")
