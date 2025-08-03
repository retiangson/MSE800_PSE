import numpy as np

c = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])

max = np.max(c)
min = np.min(c)

average = np.average(c)
print("The average teperature is :", average)

print("The max record temperature is", max, "and the minimum temperature is", min)


i= 0
for item in c:
    toF = item * 9/5 + 32
    print("The", c[i], "°C in Fahrenheit (°F) is:", np.round(toF, 2))
    i+=1

day = 1
for temp in c:
    if temp > 20:
        print("The day", day, "is above 20°C")
    day +=1