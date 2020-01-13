def check_even(num):
    return num%2 == 0

---------------------
names = [1,2,3,4,5,6]
filter(check_even,names)
list(filter(check_even,names))
