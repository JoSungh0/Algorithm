import sys
#spyder에서는 잘 안돌아감
size = int(sys.stdin.readline()) #input보다 시간이 더 빠름
stack = []

for i in range(size):
    command = sys.stdin.readline().split()
    #반복문으로 여러줄을 입력받는 상황에 시간을 줄여줌
    if command[0] == 'push': # 정수 X를 스택에 넣는 연산
        stack.append(int(command[1])) #append를 이용해 넣음
    elif command[0] == 'pop': # stack에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다
        if len(stack) == 0: # 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size': # stack에 들어있는 정수의 개수를 출력한다
        print(len(stack))
    elif command[0] == 'empty': # stack이 비어있으면 1, 아니면 0을 출력한다
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top': #스택의 가장 위에 있는 정수를 출력한다
        if len(stack) == 0: # 만약 stack에 들어있는 정수가 없는 경우에는 -1을 출력한다
            print(-1)
        else:
            print(stack[-1])

#https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline
