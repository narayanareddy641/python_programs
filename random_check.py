def rand_check(num,low,high):
    if num in range(low,high+1):
        print('{} is range between {} and {}'.format(num,low,high))
    else:
        print('The number is out of range')

        
        
        
        =====================================
        
        Boolean check 

def rand_bool(num,low,high):
    return num in range(low,high+1)
