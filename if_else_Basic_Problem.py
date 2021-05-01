#1.Write a  program to find maximum between two numbers.

# number_1=int(input("Enter the First Number : "))
# number_2=int(input("Enter the Second Number : "))

# if number_1>number_2:
#     print(number_1,"is Grater than",number_1)

# else:
#     print(number_2,"is Grater than",number_1)






#2.Write a  program to find maximum between three numbers.

# number_1=int(input("Enter the First Number : "))
# number_2=int(input("Enter the Second Number : "))
# number_3=int(input("Enter the Third Number : "))

# if number_1>number_2 and number_1>number_3 :
#     print(number_1,"is Grater than ",number_2," and " ,number_3)
# elif number_2>number_1 and number_2>number_3:
#     print(number_2,"is Grater than ",number_1," and " ,number_3)
# else:
#     print(number_3,"is Grater than ",number_1," and " ,number_2)





#3.Write a program to check whether a number is negative, positive or zero.

# number=int(input("Enter the number for checking negative , posivite or zero :"))
# if number>0:
#     print(number ," is positive")
# elif number<0:
#     print(number ," is negative")
# else:
#     print(number ," is Zero")





#4.Write a program to check whether a number is divisible by 5 and 11 or not.
# number = int(input("Enter the number for checking is it divisible by 5 and 11 or not : "))

# if number% 5==0 and number %11==0:
#     print(number," is divisible by 5 and 11")
# else:
#     print(number," is not divisible by 5 and 11")





#5.Write a  program to check whether a number is even or odd.

# number =int(input("Enter the number for checking even or odd :"))
# if number %2==0:
#     print(number," is even")
# else:
#      print(number," is odd")



#6.Write a  program to check whether a year is leap year or not.
# year=int(input("Enter the Year : "))
# if (year%4==0 or year%400==0) and (year%100!=0):
#     print(year," is leap year ")

# else:
#     print(year," is not leap year")



#7.Write a  program to check whether a character is alphabet or not.

# character=str(input("Enter the Character : "))

# if character>="a" and character<="z" or character>="A" and character<="Z":
#     print(character+" is alphabet ")
# else:
#     print(character+" is symbol ")



#8.Write a  program to input any alphabet and check whether it is vowel or consonant.

# alphabet=str(input("Enter the Alphabet : "))
# if (alphabet=="a" or alphabet=="e" or alphabet=="i" or alphabet=="o" or alphabet=="u") or (alphabet=="A" or alphabet=="E" or alphabet=="I" or alphabet=="O" or alphabet=="U"):
#     print(alphabet+" is vowel ")
# else:
#      print(alphabet+" is consonent ")




#9.Write a  program to input any character and check whether it is alphabet, digit or special character.

# character=str(input("Enter the Character for checking : "))
# if (character>="a" and character<="z") or (character>="A" and character<='z'):
#     print(character+" is Alphabet ")

# elif character>="0" and character<="9":
#     print(character+" is Digit ")
# else:
#      print(character+" is Special character ")





#10.Write a program to check whether a character is uppercase or lowercase alphabet.

# character=str(input("Enter the Character for checking upper case or lower case : "))
# if character>="A" and character<="Z":
#     print(character+ " is upper case")
# else:
#      print(character+ " is lower case")





#11.Write a program to input week number and print week day.

# week_number=int(input("Enter the Week Number :"))

# if week_number==1:
#     print("Monday")
# elif week_number==2:
#     print("Tuesday")
# elif week_number==3:
#     print("Wednesday")
# elif week_number==4:
#     print("Thrusday")
# elif week_number==5:
#     print("Friday")
# elif week_number==6:
#     print("Saturday")
# elif week_number==7:
#     print("Sunday")
# else:
#     print("Please input 1-7 ")



#12.Write a program to input month number and print number of days in that month.

# month=int(input("Enter the Month Number : "))
# if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
#     print("31 days")
# elif month==4 or month==6 or month==9 or month==11:
#     print("30 days")
# elif month==2:
#     print("28/29 Days")
# else:
#     print("Enter 1-12 ")




#13.Write a program to count total number of notes in given amount.
# amount =int(input("Enter the amount : "))
# note_1000=0
# note_500=0
# note_100=0
# note_50=0
# note_20=0
# note_10=0
# note_5=0
# note_2=0
# note_1=0
# while amount!=0:
#     if amount>=1000:
#         note_1000=amount//1000
#         amount=amount-(note_1000*1000)
#     elif amount>=500:
#         note_500=amount//500
#         amount=amount-(note_500*500)
#     elif amount>=100:
#         note_100=amount//100
#         amount=amount-(note_100*100)
#     elif amount>=50:
#         note_50=amount//50
#         amount=amount-(note_50*50)
#     elif amount>=20:
#         note_20=amount//20
#         amount=amount-(note_20*20)
#     elif amount>=10:
#         note_10=amount//10
#         amount=amount-(note_10*10)
#     elif amount>=5:
#         note_5=amount//5
#         amount=amount-(note_5*5)
#     elif amount>=2:
#         note_2=amount//2
#         amount=amount-(note_2*2)
#     elif amount>=1:
#         note_1=amount/1
#         amount=amount-(note_1*1)
# print(" ----------------------------------------")
# print(" | Type of Note |"+" Amount of the Note |")
# print(" ----------------------------------------")
# print(" |  1000 -------|"+"    ",int(note_1000),"   |")
# print(" |  500  -------|"+"    ",int(note_500),"    |")
# print(" |  100  -------|"+"    ",int(note_100) ,"   |")
# print(" |  50   -------|"+"    ",int(note_50)  ,"   |")
# print(" |  20   -------|"+"    ",int(note_20)  ,"   |")
# print(" |  10   -------|"+"    ",int(note_10)  ,"   |")
# print(" |  5    -------|"+"    ",int(note_5)   ,"   |")
# print(" |  2    -------|"+"    ",int(note_2)   ,"   |")
# print(" |  1    -------|"+"    ",int(note_1)   ,"   |")
# print(" ----------------------------------------")






#14.Write a program to input angles of a triangle and check whether triangle is valid or not.

# angle_1=int(input("Enter the First Angle : "))
# angle_2=int(input("Enter the Second Angle : "))
# angle_3=int(input("Enter the Third Angle : "))

# sum=angle_1+angle_2+angle_3

# if sum==180 :
#     print("Triangle is Valid")
# else:
#     print("Triangle is not Valid")



#15.Write a  program to input all sides of a triangle and check whether triangle is valid or not.

# first_side=int(input("Enter the First Side : "))
# seocond_side=int(input("Enter the Second  Side : "))
# third_side=int(input("Enter the Third Side : "))

# if (first_side+seocond_side>third_side) and (first_side+third_side>seocond_side) and (seocond_side+third_side>first_side):
#     print("Triangle is Valid")
# else:
#      print("Triangle is not  Valid")


#16.Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.


# first_side=int(input("Enter the First Side : "))
# seocond_side=int(input("Enter the Second  Side : "))
# third_side=int(input("Enter the Third Side : "))

# if first_side==seocond_side and seocond_side==third_side:
#     print("Triangle is an equilateral")
# elif first_side==seocond_side or first_side==third_side or third_side==seocond_side:
#    print("Triangle is an isosceles") 
# else:
#     print("Triangle is an scalene") 

















