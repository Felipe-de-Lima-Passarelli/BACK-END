T = str(input())
while len(T) < 1 or len(T) > 500:
    T = str(input())

if len(T) <= 140:
    print("TWEET")
else:
    print("MUTE")
