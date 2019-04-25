# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 19:34:49 2019

@author: Dipanjan Chowdhury
"""
import time
start_time=time.time()


def multipleOfThree(upperLimit):
    mulThreeList=[]
    for num in range(1,upperLimit):
        if(num%3==0):
            mulThreeList.append(num)

    return mulThreeList


def multipleOfFive(upperLimit):
    mulFiveList=[]
    for num in range(1,upperLimit):
        if(num%5==0):
            mulFiveList.append(num)

    return mulFiveList


def main():
    upperLimit=input("whats the upper limit?")
    x=multipleOfThree(int(upperLimit))
    y=multipleOfFive(int(upperLimit))
    sum_of_multiples=0
    for i in y:
        if i not in x:
            x.append(i)

    for i in x:
        sum_of_multiples += i

    print(sum_of_multiples)
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()