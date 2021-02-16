sec = int(input("Enter seconds"))
hour = sec // 3600
min = (sec - hour * 3600) // 60
sec = sec - (hour * 3600 + min * 60)
print(f" {hour}hh: {min}mm: {sec}ss")
