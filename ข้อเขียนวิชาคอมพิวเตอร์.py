A = (input("โปรดกรอกคะแนนเก็บ : "))
B = (input("โปรดกรอกคะแนน : "))
C = (input("โปรดกรอกคะแนนสอบปลายภาค : "))

if (A,B,C) = ร :
    print('W')
else :
    score = (A+B+C)
    if score >= 100 :
        print('4')
    elif score >= 75 :
        print ('3.5')
    elif score >= 70 :
        print ('3')
    elif score >= 65 :
        print ('2.5')
    elif score >= 60 :
        print ('2')
    elif score >= 55 :
        print ('1.5')
    elif score >= 50 :
        print ('1')
    elif score <= 49 :
        print ('0')
    else :
        print('โปรดกรอกคะแนนอีกครั้ง') 
print("เกรดของคุณคือ",score)


