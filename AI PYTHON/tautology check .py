A = [True,False,True,False];
B = [False,False,True,True];

p1=[False,True,True,False]
p2=[False,True,True,False]
p3=[False,True,True,False]
p4=[False,True,True,False]

leng = len(A)

for i in range (leng):
    p1[i]=A[i] or not A[i]
for i in range (leng):
    p2[i]=A[i] and not A[i]
for i in range (leng):
    p3[i]=A[i] and B[i]
for i in range (leng):

    p4[i]=A[i] or B[i]

print("A=",A)
print("B=",B)
print("Press 1 for A or not B")
print("Press 2 for A and not B")
print("Press 3 for A and B")
print("Press 4 for A or B")
a=int(input("Enter your choice:"))
if a ==1:
    print(p1)
    print("Tautology")
elif a==2:
    print(p2)
    print("contradicion")
elif a==3:
    print(p3)
    print("Satisfiable")
elif a==4:
    print(p4)
    print("Satisfiable")