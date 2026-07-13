patients = ["Darling","prabhas","rebel","kalki","spirit"]
priority = [2, 5, 3, 1, 4]
for i in range(len(priority)):
    for j in range(len(priority) - i - 1):
        if priority[j] < priority[j + 1]:
            priority[j], priority[j + 1] = priority[j + 1], priority[j]
            patients[j], patients[j + 1] = patients[j + 1], patients[j]
print("Hospital Emergency Queue:")
for i in range(len(patients)):
    print(patients[i], "-", priority[i])