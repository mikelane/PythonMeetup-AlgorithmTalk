# PythonMeetup-AlgorithmTalk
### A walkthrough of various algorithms for calculating the nth fibonacci number to illustrate the imporance of algorithms.

The fibonacci sequence is defined recursively as follows, the first number is
 1, the second is 1, the third number is 1+1=2, the fourth is 1+2=3, the 
 fifth is 2+3=5, and so on. A recursive definition would be 
 
 fibonacci(n)
   if n < 1, undefined
   if n = 1 or n = 2 return 1
   return fibonacci(n-2) + fibonacci(n-1)
   
 The recursive solution can be made into a python function with very few 
 changes.