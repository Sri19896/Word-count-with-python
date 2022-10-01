Mood = input('what is on your mind today?')
Mood = Mood.rstrip()
Mood = Mood.lstrip()
count = 0
Mood = Mood.split()
for i in Mood:
    count = count + 1
print(count)
