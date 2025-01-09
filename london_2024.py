import numpy as np
import matplotlib.pyplot as plt
import csv 
import matplotlib.dates as mdates
import pandas as pd
from datetime import datetime



# Lijst om de density-waarden op te slaan
densities_2024 = []
date_density_list_2024 = []
dates_2024 = []

# Lees het CSV-bestand
with open('London_2024_1.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        
        # Zorg ervoor dat je geen lege rijen hebt
        if len(row) > 0:
            date_and_density_2024 = row[0].strip()  # Verwijder eventuele extra spaties aan het begin of einde van de string
            if '""' in date_and_density_2024:
                pass
            else:
                # Als '""' niet in de string staat, splits dan op basis van de enkele dubbele aanhalingstekens
                parts_2024 = date_and_density_2024.split('"')
                if len(parts_2024) > 1:  # Zorg ervoor dat er een waarde na de datum is
                    #print(f"Parts after alternative split: {parts}")
                    date_2024 = parts_2024[0]
                    density_2024 = parts_2024[1].strip()  # De waarde na de datum
                    try:
                        densities_2024.append(float(density_2024))  # Zet de density om naar een float
                    except ValueError:
                        print(f"Fout bij het converteren van density: {density_2024}")
                    date_density_list_2024.append(parts_2024)
                    
                if len(parts_2024) < 1:
                    pass

print(date_density_list_2024)
# Print de lijst met densities_2024
#print("densities_2024:", densities_2024, "Dates:", date)


dates_2024 = [item[0] for item in date_density_list_2024]  # Haal de datum uit elk element
densities_2024 = [float(item[1]) for item in date_density_list_2024 if item[1] != ""]  # Haal de density uit elk element en zet om naar float

# Print de twee lijsten
print("Dates:", dates_2024)
print("densities_2024:", densities_2024)



densities_2024_2  = []
date_density_list_2024_2 = []
dates_2024_2 = []
with open('London_2024_2.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        
        # Zorg ervoor dat je geen lege rijen hebt
        if len(row) > 0:
            date_and_density_2024_2 = row[0].strip()  # Verwijder eventuele extra spaties aan het begin of einde van de string
            if '""' in date_and_density_2024_2:
                pass
            else:
                # Als '""' niet in de string staat, splits dan op basis van de enkele dubbele aanhalingstekens
                parts_2024_2 = date_and_density_2024_2.split('"')
                if len(parts_2024_2) > 1:  # Zorg ervoor dat er een waarde na de datum is
                    #print(f"Parts after alternative split: {parts}")
                    date_2024_2 = parts_2024_2[0]
                    density_2024_2 = parts_2024_2[1].strip()  # De waarde na de datum
                    try:
                        densities_2024_2.append(float(density_2024_2))  # Zet de density om naar een float
                    except ValueError:
                        print(f"Fout bij het converteren van density: {density_2024_2}")
                    date_density_list_2024_2.append(parts_2024_2)
                    
                if len(parts_2024_2) < 1:
                    pass
dates_2024_2 = [item[0] for item in date_density_list_2024_2]  # Haal de datum uit elk element
densities_2024_2 = [float(item[1]) for item in date_density_list_2024_2 if item[1] != ""]  # Haal de density uit elk element en zet om naar float


dates_2024.extend(dates_2024_2)
densities_2024.extend(densities_2024_2)

densities_calculated_2024 = []
for x in densities_2024:
    x = x / 1000000000
    densities_calculated_2024.append(x)

print(dates_2024)

# Zet de datums om naar datetime-objecten voor het plotten
dates_2024 = [datetime.strptime(date, "%b %d %Y") for date in dates_2024]  # Zonder komma

# Zet de data om naar een pandas DataFrame
df = pd.DataFrame({
    'date': dates_2024,
    'density': densities_calculated_2024
})

# Zet de datum als index
df['date'] = pd.to_datetime(df['date'])  # Zet datum om naar datetime
df.set_index('date', inplace=True)

# Groepeer de data op maand en bereken het gemiddelde van de densiteit per maand
monthly_avg = df.resample('M').mean()  # 'M' staat voor maand

# Maak de grafiek
plt.figure(figsize=(10, 6))
plt.plot(monthly_avg.index, monthly_avg['density'], label='NO2 Density (Monthly Avg)', color='blue')
plt.xlabel('Date')
plt.ylabel('Concentration of NO2 in mol/m2')
plt.title('NO2 Density over Time (Monthly Average)')
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())  # Laat alleen maanden zien
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))  # Formatteer als "Maand Jaar"

plt.legend()
plt.tight_layout()
plt.show()







