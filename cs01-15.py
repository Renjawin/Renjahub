num = int(input('Enter your loop : '))
numtotal = []
for i in range(num):
    data = int(input("Enter your data : "))
    numtotal += [data]
numtotal.sort()
print(numtotal[0])
print(numtotal[-1])

