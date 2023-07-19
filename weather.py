from pathlib import Path
import matplotlib.pyplot as plt

"""
1. Datein einlesen ^
2. Dict erstellen 
3. int als key für neues dict und Liste mit numerischen Temperaturen als value)
4. Plotten
""" 

with open(Path(__file__).parent / "wetterdaten.txt", mode="r", encoding="utf-8") as f:
    data = f.readlines()

weather = {}

for el in data:
    weather.update({el[:2]: [el[4:-1]]})

for key, value in weather.items():
    data_new = []
    split_list = value[0].split(" ")

    for el in split_list:
        if el[-2].isdigit():
            data_new.append(el[-2:])

    weather.update({key: data_new})

print(weather)

for key, value in weather.items():
    x = [index +1 for index in range(len(value))]
    y = [value for value in value]
    plt.scatter(x, y, label=f"Woche {key}")

plt.xlabel("Tage")
plt.ylabel("Temperatur")
plt.title("Wetterdaten")
plt.grid(True)
plt.legend()
plt.show()
