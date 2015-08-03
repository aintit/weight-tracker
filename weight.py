from datetime import date
import os

if not os.path.exists("weight.txt"):
    open("weight.txt", "w").close()

weightfile = open("weight.txt")
weighttext = weightfile.read()
weightfile.close()
weightnow = raw_input("What is your weight today? ")
weightarray = weighttext.splitlines()

today = date.today()
todaystr = today.isoformat()

if len(weightarray) == 0:
    weightarray.append(todaystr + " " + weightnow)
elif weightarray[-1].find(todaystr) != -1:
    weightarray[-1] = todaystr + " " + weightnow
else:
    weightarray.append(todaystr + " " + weightnow)

weighttext2 = "\n".join(weightarray)
weightfile = open("weight.txt", "w")
weightfile.write(weighttext2)
weightfile.close()
