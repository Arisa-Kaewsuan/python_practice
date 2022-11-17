scoreList = []

numbers = int(input('How many score do you want to input : '))

for i in range(numbers):
    score = int(input("score" + str(i) + ":"))
    scoreList.append(score)
    
maxValue = scoreList[0]
minValue = scoreList[0]
sum = 0

for score in scoreList:
    if maxValue < score:
        maxValue = score
        
for score in scoreList:
    if minValue > score:
        minValue = score
        
for score in scoreList:
    sum = sum + score
averageValue = sum/numbers

print(maxValue)
print(minValue)
print(averageValue )