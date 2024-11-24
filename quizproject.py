############ Quiz competition

import time
def miniproject():
    count=0
    timelimit=10
    startingtime=time.time()
    print('Quiz competition \nQuestion 1 \nWhen was Python first invented ? \n1.1990 \n2.1991 \n3.1992 \n4.1993')
    a=int(input('Enter the Q1 answer'))
    if time.time()-startingtime > timelimit:
        print('Time out')
    else:
        if a==2:
            print('correct answer')
            count+=1
        else:
            print('wrong answer')
    print(count)
    startingtime=time.time()
    print('Quiz competition \nQuestion 2 \nWho is the CEO of Python? \n1.Albert \n2.Thomson \n3.Edison \n4.Rossum')
    a=int(input('Enter the Q1 answer'))
    if time.time()-startingtime > timelimit:
        print('Time out')
    else:
        if a==4:
            print('correct answer')
            count+=1
        else:
            print('wrong answer')
    print(count)
    startingtime=time.time()
    print('Quiz competition \nQuestion 3 \nWhich of the following is the correc t extension of the python file? \n1..python \n2..pyp \n3..py \n4..pth')
    a=int(input('Enter the Q1 answer'))
    if time.time()-startingtime > timelimit:
        print('Time out')
    else:
        if a==3:
            print('correct answer')
            count+=1
        else:
            print('wrong answer')
    print(count)
    startingtime=time.time()
    print('Quiz competition \nQuestion 3 \nWhich key word is used for function python in language? \n1.fun \n2.def \n3.define \n4.function')
    a=int(input('Enter the Q1 answer'))
    if time.time()-startingtime > timelimit:
        print('Time out')
    else:
        if a==2:
            print('correct answer')
            count+=1
        else:
            print('wrong answer')
    print(count)
    print(f'you got {count}')
miniproject()