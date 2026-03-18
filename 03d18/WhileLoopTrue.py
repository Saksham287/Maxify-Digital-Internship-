# While loops: while true

while True:
    exit = input("Enter 'q' to quit: ")
    if exit == "q":
        break
print("done")
'''
Output:

Enter 'q' to quit: w
Enter 'q' to quit: e
Enter 'q' to quit: f
Enter 'q' to quit: w
Enter 'q' to quit: 
Enter 'q' to quit: f
Enter 'q' to quit: 1
Enter 'q' to quit: 34
Enter 'q' to quit: wq
Enter 'q' to quit: edsq
Enter 'q' to quit: q
done

'''

total = 0

while True:
    num = int(input("Enter a number (0 to stop): "))
    
    if num == 0:
        break
    else:
        total += num
print("Total Score:", total)
'''
Output:

Enter a number (0 to stop): 34
Enter a number (0 to stop): 23
Enter a number (0 to stop): 3
Enter a number (0 to stop): 23
Enter a number (0 to stop): 324
Enter a number (0 to stop): 1
Enter a number (0 to stop): 2
Enter a number (0 to stop): 0
Total Score: 443

'''