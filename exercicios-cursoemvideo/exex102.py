def fatorial(num, show):
    print(f'{num}! = ',end='')
    var = 1
    if show == True:
        for i in range(num, 0, -1):
            var *= i
            if i >=2:
                print(i, 'x', end=' ')
            else:
                print(i, '=', end=' ')
        print(var)  
    
    elif show == False:
        for i in range(num, 0, -1):
            var *= i
        print(var)


fatorial(4, True)
fatorial(4, False)
fatorial(8, True)
fatorial(8, False)
fatorial(7, False)
fatorial(11, True)
fatorial(11, False)
