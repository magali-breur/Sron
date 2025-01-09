import numpy as np
import matplotlib.pyplot as plt
import csv 
import matplotlib.dates as mdates
import pandas as pd
import seaborn as sns
from datetime import datetime

def airport_emission(location):   
    # Lijst om de density-waarden op te slaan
    densities_2020 = []
    date_density_list_2020 = []
    dates_2020 = []

    # Lees het CSV-bestand
    with open(f'{location}_2020_1.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            
            # Zorg ervoor dat je geen lege rijen hebt
            if len(row) > 0:
                date_and_density_2020 = row[0].strip()  # Verwijder eventuele extra spaties aan het begin of einde van de string
                if '""' in date_and_density_2020:
                    pass
                else:
                    # Als '""' niet in de string staat, splits dan op basis van de enkele dubbele aanhalingstekens
                    parts_2020 = date_and_density_2020.split('"')
                    if len(parts_2020) > 1:  # Zorg ervoor dat er een waarde na de datum is
                        #print(f"Parts after alternative split: {parts}")
                        date_2020 = parts_2020[0]
                        density_2020 = parts_2020[1].strip()  # De waarde na de datum
                        try:
                            densities_2020.append(float(density_2020))  # Zet de density om naar een float
                        except ValueError:
                            print(f"Fout bij het converteren van density: {density_2020}")
                        date_density_list_2020.append(parts_2020)
                        
                    if len(parts_2020) < 1:
                        pass

    print(date_density_list_2020)


    dates_2020 = [item[0] for item in date_density_list_2020]  # Haal de datum uit elk element
    densities_2020 = [float(item[1]) for item in date_density_list_2020 if item[1] != ""]  # Haal de density uit elk element en zet om naar float

    # Print de twee lijsten
    print("Dates:", dates_2020)
    print("densities_2020:", densities_2020)



    densities_2020_2  = []
    date_density_list_2020_2 = []
    dates_2020_2 = []
    with open(f'{location}_2020_2.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            
            # Zorg ervoor dat je geen lege rijen hebt
            if len(row) > 0:
                date_and_density_2020_2 = row[0].strip()  # Verwijder eventuele extra spaties aan het begin of einde van de string
                if '""' in date_and_density_2020_2:
                    pass
                else:
                    # Als '""' niet in de string staat, splits dan op basis van de enkele dubbele aanhalingstekens
                    parts_2020_2 = date_and_density_2020_2.split('"')
                    if len(parts_2020_2) > 1:  # Zorg ervoor dat er een waarde na de datum is
                        #print(f"Parts after alternative split: {parts}")
                        date_2020_2 = parts_2020_2[0]
                        density_2020_2 = parts_2020_2[1].strip()  # De waarde na de datum
                        try:
                            densities_2020_2.append(float(density_2020_2))  # Zet de density om naar een float
                        except ValueError:
                            print(f"Fout bij het converteren van density: {density_2020_2}")
                        date_density_list_2020_2.append(parts_2020_2)
                        
                    if len(parts_2020_2) < 1:
                        pass
    dates_2020_2 = [item[0] for item in date_density_list_2020_2]  # Haal de datum uit elk element
    densities_2020_2 = [float(item[1]) for item in date_density_list_2020_2 if item[1] != ""]  # Haal de density uit elk element en zet om naar float


    dates_2020.extend(dates_2020_2)
    densities_2020.extend(densities_2020_2)

    densities_calculated_2020 = []
    for x in densities_2020:
        x = x / 1000000000
        densities_calculated_2020.append(x)
    
    # Lijst om de density-waarden op te slaan
    densities_2024 = []
    date_density_list_2024 = []
    dates_2024 = []

    # Lees het CSV-bestand
    with open(f'{location}_2024_1.csv', mode='r') as file:
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
    with open(f'{location}_2024_2.csv', mode='r') as file:
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

    # # Maak pandas DataFrame's voor de jaren 2020 en 2024
    df_2020 = pd.DataFrame({'Date': dates_2020, 'Density': densities_calculated_2020})
    df_2024 = pd.DataFrame({'Date': dates_2024, 'Density': densities_calculated_2024})

    # # Zet de datumkolom als index
    df_2020['Date'] = pd.to_datetime(df_2020['Date'])
    df_2024['Date'] = pd.to_datetime(df_2024['Date'])

    #maanden aanmaken
    df_2020['month']= df_2020['Date'].dt.month
    df_2024['month']= df_2024['Date'].dt.month

    # # Groepeer per maand en bereken het maandgemiddelde
    df_2020.set_index('Date', inplace=True)
    df_2024.set_index('Date', inplace=True)

    #jaar dataframes aanmaken
    df_2020['year']= 2020
    df_2024['year']= 2024

    # # Bereken het maandgemiddelde van de NO₂-dichtheid
    monthly_avg_2020 = df_2020.resample('M').mean()
    monthly_avg_2024 = df_2024.resample('M').mean()


    months_axis = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    plt.plot(months_axis, monthly_avg_2020['Density'], 'o-',label='Average NO₂ 2020')
    plt.plot(months_axis, monthly_avg_2024['Density'], 'o-',label='Average NO₂ 2024')
    plt.xlabel('Date (Month-Year)')
    plt.ylabel('Average NO₂ Density (mol/m²)')
    plt.title(f'(Heathrow {location} average monthly NO₂ density)')

    # Voeg de legenda toe
    plt.legend(loc='upper left')

    plt.tight_layout()
    plt.show()


    df_big = pd.concat([df_2020, df_2024 ])
    sns.boxplot(df_big, x='month' , y="Density", hue="year")
    plt.show()

    print(df_big)

airport_emission(location="Paris")
