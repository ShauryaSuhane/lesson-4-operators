notes= int(input("enter the amount you want to withdraw"))
note1=notes//400
note2=(notes%400)//100
note3=((notes%400)%100)//50
print(note1,note2,note3)