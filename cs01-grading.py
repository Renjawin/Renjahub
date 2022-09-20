a = int(input("โปรดป้อนคะแนนเก็บของนักเรียน : "))
b = int(input("โปรดป้อนคะแนนสอบกลางภาค : "))
c = int(input("โปรดป้อนคะแนนสอบปลายภาค : "))
d = (a+b+c)
if d >= 80 :
    print('A')
elif d > 75 :
    print('B')
elif d > 70 :
    print('B+')
elif d > 65 :
    print('C+')
elif d > 60 :
    print('C')
elif d > 55 :
    print("D+")
elif d > 50 :
    print("D")
else:
    print("F")