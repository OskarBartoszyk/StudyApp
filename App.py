import time
from datetime import datetime
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

input_data = input("Podaj liczby oddzielone spacją: ")
numbers = list(map(int, input_data.split()))


# Utworzenie dat dla osi x (obecne daty)
current_date = datetime.now().strftime('%d-%m-%Y')
dates = [current_date for i in range(len(numbers))]



#dataset

dataset= {
'x_aces' : [],
'y_aces' : []
}


df = pd.DataFrame(dataset)
new_row = {'x_aces':dates , 'y_aces': numbers}
df = df.append(new_row, ignore_index=True)
print(df)
print(df['x_aces'])


collecting_data = pd.read_excel(r'C:\Users\User\Desktop\StudyApp\dane.xlsx')
updated_data = collecting_data.append(pd.DataFrame(df), ignore_index=True)
updated_data.to_excel(r'C:\Users\User\Desktop\StudyApp\dane.xlsx', index=False)
print("Nowe dane zostały zapisane do pliku dane.xlsx.")

# x - dates
forgraph = pd.read_excel(r'C:\Users\User\Desktop\StudyApp\dane.xlsx')
first_row = forgraph['x_aces']
print(first_row)

# y - hours
second_row = forgraph['y_aces']
print(second_row)




# Tworzenie wykresu
plt.plot(first_row, second_row, marker='o')


# Konfiguracja osi y (liczby z inputu)
plt.ylim(0, 24)
plt.ylabel("Hours")
plt.xlabel("Days")

# Wyświetlenie wykresu
plt.tight_layout()
plt.grid()
plt.show()


