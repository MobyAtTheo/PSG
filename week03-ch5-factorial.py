import time

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        print result #debugging statement (which should be deleted after debug)
        time.sleep(0.2) #so I can see each time it recurses easily
        return result

if __name__ == '__main__':
    start_value=10
    vtype=type('start_value')
    print vtype
    print "Start value ",start_value
    value = factorial(start_value) #Python still doing the right thing with str
    #print value
