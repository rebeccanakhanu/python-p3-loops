#!/usr/bin/env python3

def happy_new_year():
    num = 10
    while num > 0 :
        print (num)
        num -= 1
    print("Happy New Year!")
    
def square_integers(int_list):
    #use list comprehension
    squared_num =[num **2  for num in int_list]
    return squared_num
#or use append 
#def square_integers("int_list")
#squared_num =[]
#for num in int_list:
#squared_num.append(num **2)
#return squared_num

    


def fizzbuzz():
    for num in range (1, 101):
        if num % 3 == 0 and num % 5 ==0:
            print ("FizzBuzz")
        elif num % 3 == 0:
            print ("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
          
