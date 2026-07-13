marks = [75, 45, 90, 60, 85, 55]
for i in range(len(marks)):
    for j in range(len(marks) - i - 1):
        if marks[j] > marks[j + 1]:
            marks[j], marks[j + 1] = marks[j + 1], marks[j]
print("Sorted Marks:", marks)
key = int(input("Enter mark to search: "))
low = 0
high = len(marks) - 1
found = False
while low <= high:
    mid = (low + high) // 2
    if marks[mid] == key:
        print("Mark Found")
        print("Position:", mid)
        found = True
        break
    elif marks[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
if not found:
    print("Mark Not Found")