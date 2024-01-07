stack = []

while(1):
    ask = input().split()

    if(ask == 'push'):
        stack.append(ask[1])
        print
    elif(ask == 'pop'):
        stack.remove[-1]
    elif(ask == 'size'):
        print(len(stack))
    elif(ask == 'empty'):
        if(len(stack) == 'null'):
            print('1')
        else:
            print("0")
    elif(ask == 'top'):
        print(stack[-1])
    else:
        break
