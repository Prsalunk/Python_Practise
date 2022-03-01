from math import *

# a = "Pratiksha"
# b = 27
# print("Hey " + a +" \nAre you "+ str(b) +"yrs old.?")
 
# print(2-1)
# print(pow(2,2))
# print(ceil(2.3))

# x = input("Enter no1 : ")
# y = input("Enter no2 : ")
# result = int(x) + int(y)
# print(result)

# friends = ['teju', 'Sara','Rupali']
# print(friends[0])
# print(friends[-1])
 
# lucky_num = [4,7]

# friends.extend(lucky_num)
# print(friends)

# friends.append('gotta')
# print(friends)

# friends.insert(0,'maroti')
# print(friends)

# print(friends.index('gotta'))
# friends.pop(6)
# print(friends)

# friends.clear()
# print(friends)

# friends.sort()
# print(friends)

# friends.reverse()
# print(friends)

# friends_cp = friends.copy()
# print(friends_cp)

##### TUPLE #####  --Immutable

# coordinates = (1,2,3)

# print(coordinates)
# print(coordinates[1])

 
##### FUNCTION #####

# def hi(name):
#     print('Hey hi ' + name)
# hi(input("Enter ur name - "))

# def hi(name, age):
#     print('Hey hi ' + name + "., You are " + str(age))
# hi('prati' , 27)

# def cube(a):
#     return a*a*a
# print(cube(3))

# def power(a,b):
#     return a^b
# aa = power(2,3)
# print(aa)


##### IF Condition #####        -- if-elif-else

# def if_else():
#     is_male = False

#     if is_male:
#         print("Pratiksha is male")
#     else:
#         print("Pratiksha is female")
# if_else()


##### DICTIONARY ######

# month_dic = { 1:"Jan", 2:"Feb" }
# print(month_dic[1])
# print(month_dic.get(2))
# print(month_dic.get(6,"Not a valid value"))             #we can give default value if value is missing it will pop up


##### WHILE LOOP #####

# i=1
# while i<=10:
#     print(i)
#     i += 1
    
# limit = 5
# count = 1
# guess_pwd = " "
# over_limit = False
# while guess_pwd != 'Prati' and not(over_limit):
#     if count<limit:
#         guess_pwd = input("Guess the password - ")  
#         count += 1
#     else:
#         over_limit=True
#         print("You failed...")
# print("You're Unlocked")


##### FOR Loop #####

# for i in 'Pratiksha':
#     print(i)

# frnds = ['Teju','Rupi','Sara']
# for i in frnds:
#     print(i)

# for i in range(1,5):
#     print(i)

# frnds = ['Teju','Rupi','Sara']
# for i in range(len(frnds)):
#     print(frnds[i])

# for i in range(2):          #it will not count 2, its n-1
#     if i==0:
#         print("Its start..")
#     else:
#         print("In middle..")


# def pow(num, pwr):
#     res = 1
#     for i in range(pwr):
#         res = res*num
#     return res
# print(pow(2,2))


# lst = [[1,2,3],[4,5,6],[7,8,9],[0]]
# for row in lst:
#     for col in row:
#         print(col)


# def translate(name):
#     translation = ''
#     for letter in name:
#         if letter.lower() in 'aeiou':
#             if letter.isupper():
#                 translation = translation + 'G'
#             else:
#                 translation = translation + 'g'
#         else:
#             translation = translation + letter
#     return translation
# print(translate(input('Enter a word - ')))


###### Exception Handling ######

# try:
#     a = 10/0
#     p = int(input("Enter a no - "))
#     print(p)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError:
#     print('Invalid Input.')


##### File Processing #####

#-Read a File
# a = open("Imp_tips.txt", 'r')
# # print(a.read())
# print(a.readline())
# print(a.readlines())
# a.close() 

#-Appending a File
# a = open("Imp_tips.txt", 'a')
# a.write("\n Hey There..")
# a.close() 

#-Reading a File
# a = open("Imp_tips.txt", 'w')
# a.write("\n Hey There..")
# a.close() 



