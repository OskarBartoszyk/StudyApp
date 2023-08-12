import time
import datetime
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

date_today = datetime.date.today()
print(date_today)
x= date_today
y = int(input("yeye nene: "))

plt.plot(x, y)
plt.ylabel("Hours")
plt.xlabel("Days")
plt.show()
