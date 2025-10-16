#ინდენტაცია საჭიროა თუ არა და რატომ for loop ის დროს, მოიყვანეთ მაგალითები და ახსენით კომენტარით

#დიახ საჭიროა და აუცილებელიც კი

#for loop-ის მეშვეობით გამოიტანეთ რიცხვი 4, 7-ჯერ.

for i in range (7):
    print(4)

#for loop-ის მეშვეობით გამოიტანეთ "I love cats" 8-ჯერ.

for i in range (8):
    print("i love cats")

#Input()-ის გამოყენებით მომხმარებელს შემოატანინეთ მისი სახელი, შემდეგ for loop-ით კი დაპრინტეთ ("hello" + მომხმარებლის სახელი) 5 ჯერ.

name = input ("give me your name!: ")

for i in range (5):
    print("hello " + name)

#შევასწოროთ შეცდომები:

#for i in range5
#print("i")

for i in range (5):
    print(i)