n = int(input("Enter number of students: "))

total = 0

for i in range(n):
    print("Student", i + 1)
    sum = 0

    for j in range(5):
        score = float(input("Enter score: "))
        sum = sum + score

    average = sum / 5
    print("Average:", average)

    total = total + sum

overall = total / (n * 5)
print("Overall average:", overall)