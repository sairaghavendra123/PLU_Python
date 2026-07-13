roll_numbers = [1,2,3,4,5,6,7,8,9,10]
key = int(input("Enter roll number to search: "))
found = False
for i in range(len(roll_numbers)):
    if roll_numbers[i] == key:
        print("Student Found")
        print("Position:", i)
        found = True
        break
if not found:
    print("Student Not Found")
    
    
    