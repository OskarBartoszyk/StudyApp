import time
import datetime
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

input_data = input("Podaj liczby oddzielone spacją: ")
numbers = list(map(int, input_data.split()))

# Utworzenie dat dla osi x (obecne daty)
current_date = datetime.datetime.now()
dates = [current_date for i in range(len(numbers))]

# Tworzenie wykresu
plt.plot(dates, numbers, marker='o')

# Konfiguracja osi x (daty)


# Konfiguracja osi y (liczby z inputu)
plt.ylim(0, 24)
plt.ylabel("Hours")
plt.xlabel("Days")

# Wyświetlenie wykresu
plt.tight_layout()
plt.show()
