q=["1. In a common emitter amplifier, what is the phase difference between input and output signals?",
   "2. Which logic gate gives a HIGH output only when all of its inputs are LOW?",
   "3.What is the function of a Zener diode in a circuit?"]
a=["A.0 degree \nB.90 degree \nC.180 degree",
   "A.NOT \nB.AND \nC.OR",
   "A.Oscillation \nB.Voltage regulation \nC.Amplification",]
score=0
crt_ans=[2,0,1]
print("Quiz Started")
for i in range(len(q)):
    print(q[i])
    print(a[i])
    user_ans=input().upper()
    if(user_ans=="A" and crt_ans[i]==0):
        score+=1
    elif(user_ans=="B" and crt_ans[i]==1):
        score+=1
    elif(user_ans=="C" and crt_ans[i]==2):
        score+=1
    print()
print("Quiz completed")
print(f"your score={score} / {len(q)}")