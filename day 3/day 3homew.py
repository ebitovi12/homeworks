my_name= input("enter your name: ") #input ით ყოველთვის შემოდის სტრინგ
my_surname = input("enter your surname: ")
my_age = int(input("enter your age: "))
my_sentence=" your name {}  your surname{}  your age {}".format("name","surname","age")
print(my_sentence)
# three_year_later = my_age +3
# print(three_year_later)
#my_age += 3
new_age=int(my_age)+3
print("after 3 years i am now {} years old".format(new_age))