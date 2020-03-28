# use of Idioms in Conditional Expressions:-


# x = input("Enter the value:")

def check(x):
    ''' instead using this....
    if x<5:
       return 10
     else:            
        return 20
    '''

# use....
    return 10 if x<5 else 20

print(check(4))