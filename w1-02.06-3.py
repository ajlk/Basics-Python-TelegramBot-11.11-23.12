minutesTotal = int(input())
toBed_H = int(input())
toBed_M = int(input())

hoursForRest = minutesTotal // 60
minutesForRest = minutesTotal % 60

wakeUp_H = toBed_H + hoursForRest
wakeUp_M = toBed_M + minutesForRest

if wakeUp_M > 60:
    wakeUp_H = wakeUp_H + 1
    wakeUp_M = wakeUp_M - 60

print(wakeUp_H)
print(wakeUp_M)
