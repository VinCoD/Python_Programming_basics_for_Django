# 30 and below - E
# 40 to 49 - D
# 50 to 59 - C
# 60 and above you get A

marks = 70

if marks >= 60:
    print("A")

elif marks > 49 and marks <60:
    print("C")

elif marks > 39 and marks <50:
    print("D")

elif marks <= 30:
    print("E")

else:
    print("Invalid Marks")