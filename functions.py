'''
Created on May 18, 2018

@author: o_olasub
'''

def multiply(a,b):
    return a*b;

def add(a,b):
    return a+b;
def divide(a,b):
    return a/b;


n = float(input("Input the first number"));
m = float(input("Input the second number"));

action= input("what do you want to do with the two number \n a) Add \n b)multiply \n c) divide");

if action=="a":
   print( add(n,m));
elif action== "b":
   print( multiply(n,m));
elif action=="c":
    divide(n,m)
    
    
#fibonacci numbers

def fibonacci_number(max_sequence):
    fibo=[0,1,1]
    
    for i in range (1,max_sequence):
        if len(fibo)!=max_sequence:
            new= fibo[-1] +fibo[-2]
            fibo.append(new);
    return fibo

max=int(input("how many terms do you want in the sequence?"))
print(', '.join(str(v) for v in fibonacci_number(max)))