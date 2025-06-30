amount=int(input("please write a number:"))
note1= amount//100
note2= (amount%100)//50
note3= ((amount%100)%50)//10

print("100 RS notes in your amount", note1)
print("50 RS notes in your amount", note2)
print("10 RS notes in your amount", note3)


