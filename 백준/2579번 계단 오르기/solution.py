import sys

N = int(input())

step = [0]
for _ in range(N):
    step.append(int(sys.stdin.readline()))

dp = [0] * (N + 1) # dynamic programing 이용

dp[0] = step[0]
dp[1] = step[1]
for i in range(2, N+1):
    dp[i] = max(step[i] + step[i-1] + dp[i-3], step[i] + dp[i-2])
  '''
  bottom-up 방식으로 생각하기, 어떻게 내려갈지 말고 어떻게 올라올지를 생각하기

  연속 2개 계단을 오른거 vs 전의 계단을 건너뛰고 오른거
  점화식을 세워서 dp에 저장하고 계속 불러오기
  '''

print(dp[N])
