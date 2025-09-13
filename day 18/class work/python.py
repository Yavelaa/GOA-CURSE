number = int(input("enter the number: "))

if number < 10:
    print("10 ზე ნაკლებია")
elif number < 20:
    print("20 ზე ნაკლებია")




number = int(input("enter the number: "))

if number * 2 == 2:
    print("ლუწია")
else:
    print("კენტია")


weather = input("შეიყვანეთ ამინდი ")

if weather == "მზიანი":
    print("დღეს ვივარჯიშებ გარეთ")
elif weather == "წვიმიანი":
    print("დღეს ვივარჯიშებ გარეთ")
else:
    print("არ ვივარჯიშებ დღეს")


for i in range(3):
    name = input("შეიყვანე სახელი: ")
    print(name)
