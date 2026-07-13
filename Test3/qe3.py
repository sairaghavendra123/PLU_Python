marks = [99,89,79,69,29,39,49]
for i in range(len(marks)):
    for j in range(len(marks) - i - 1):
        if marks[j] > marks[j + 1]:
            marks[j], marks[j + 1] = marks[j + 1], marks[j]
print("Sorted Marks:", marks)


