#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    counter = 11
    while counter >= 1:
        counter -= 1
        print(counter)  
    pass
    print("Happy New Year!")
happy_new_year()

def square_integers(int_list):
    # code goes here!
    int_list = [1,2,3,4,5] and [-1, -2, -3, -4, -5]
    squared_integers = [num ** 2 for num in int_list]
    return squared_integers
int_list = [1,2,3,4,5] and [-1, -2, -3, -4, -5]
squared_results = square_integers(int_list)
print (squared_results)   

def fizzbuzz():
    # code goes here!
    for number in range(1, 100):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print('Buzz')
        else:
            print(number)
    pass
fizzbuzz()