# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 21:46:40 2019

@author: Dipanjan Chowdhury
"""


def listFibonacci(num):
    fibonacciSeries = []
    first = 0
    second = 1
    fibonacciSeries.append(first)
    fibonacciSeries.append(second)
    nextItem = fibonacciSeries[-1]+fibonacciSeries[-2]
    while nextItem < num:
        fibonacciSeries.append(nextItem)    
        nextItem = fibonacciSeries[-1]+fibonacciSeries[-2]
    
    return fibonacciSeries


def sumOfEvenFibonacci(fibonacciSeries):
    sumEvenFibo = 0
    for i in fibonacciSeries:
        if i % 2 == 0:
            sumEvenFibo += i
        
    return sumEvenFibo


def main():
    limit = int(input("Enter upper Limit: "))
    print(listFibonacci(limit))
    sumOfEvenFibo = sumOfEvenFibonacci(listFibonacci(limit))
    print("SUM OF EVEN FIBONACCI: ", sumOfEvenFibo)


if __name__ == "__main__":
    main()
