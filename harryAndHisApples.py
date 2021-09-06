n = int(input("Enter the number of apples Harry is been provided--"))
mn = int(input("Enter minimum number of students--"))
mx = int(input("Enter maximum number of students--"))
for i in range(mn, mx + 1):
    if n % i == 0:
        print(f"Yes, {n} apples can be divided into {i} students.")
    else:
        print(f"No ,{n} apples cannot be divided into {i} students.")
