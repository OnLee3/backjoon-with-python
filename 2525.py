A, B = map(int, input().split())
C = int(input())
startTime = A * 60 + B
endtime = startTime + C

hour = endtime // 60
if hour >= 24:
    hour -= 24
minute = endtime % 60
print(hour, minute)
