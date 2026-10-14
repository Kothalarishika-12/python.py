marks=int(input("Enter your marks:"))
if marks>=35 and marks<=55:
    print("C grade",marks)
elif marks>=56 and marks<=74:
    print("B grade", marks)
elif marks>=75 and marks<=100:
    print("A grade",marks)
else:
    print("Invalid")