import time
timestamp1 =time.strftime("%H:%M:%S")
print(timestamp1)

timestamp2 = int(time.strftime("%H"))

if timestamp2 >= 00 and timestamp2 < 12:
    print("Good Morning sir")
elif timestamp2 >= 12 and timestamp2 < 16:
    print("Good Afternoon sir")
elif timestamp2 >= 16 and timestamp2 < 20:
    print("Good Evening Sir")
else:
    print("Good night sir")
