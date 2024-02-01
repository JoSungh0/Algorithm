import sys

size = int(sys.stdin.readline()) #input보다 시간이 더 빠름
stack = []

for i in range(size):
    command = sys.stdin.readline().split()
    #반복문으로 여러줄을 입력받는 상황에 시간을 줄여줌
    if command[0] == 'push': # 정수 X를 스택에 넣는 연산
        stack.append(int(command[1]))
    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

#https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline
