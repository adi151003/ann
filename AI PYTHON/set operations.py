A = {0, 2, 4, 6, 8};
B = {1, 2, 3, 4, 5};

print("Enter 1 for Union")
print("Enter 2 for Intersection")
print("Enter 3 for Difference")
print("Enter 4 for Symetric Differnce")
a= int(input("ENTER YOUR CHOICE :"))
if a ==1:
    print("Union :", A | B)
elif a==2:
    print("Intersection :", A & B)
  
elif a==3:
    print("Difference :", A - B)
else:
    print("Incorrect input")