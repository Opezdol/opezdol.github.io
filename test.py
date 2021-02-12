def decor (f):
    def wrapper(*args):
        print('*****DECORATED*******')
        f(*args)
        print ('__________________')
    return wrapper

@decor
def mained ():
    
    @decor
    def pr(i):
        print (i)
    for i in range(4):
        pr(i)


mained()