import numpy as np

celsius=np.array([25,30,18,40,15,50,28])

fahrenheit=(celsius * 9/5) + 32

print("Celsius: \n",celsius)
print("\nFahrenheit: \n",fahrenheit)

hottest=np.argmax(celsius)
coldest=np.argmin(celsius)

print(f"\nHottest Day: Day {hottest+1} ({celsius[hottest]}°C)")
print(f"Coldest Day: Day{coldest+1} ({celsius[coldest]}°C)")

clipping=np.clip(celsius,20,40)
print("\nAfter Clipping: ")
print(clipping)


'''OUTPUT SHOULD BE-----

Celsius:
[25 30 18 40 15 50 28]

Fahrenheit:
[ 77.   86.   64.4 104.   59.  122.   82.4]

Hottest Day: Day 6 (50°C)
Coldest Day: Day 5 (15°C)

After Clipping:
[25 30 20 40 20 45 28]'''

