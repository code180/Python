from smartphone import Smartphone

catalog = [
    Smartphone("Xiaomi_1", "ProArt", "+79999999999"),
    Smartphone("Xiaomi_2", "Pro", "+79999999888"),
    Smartphone("Xiaomi_3", "Pro123", "+79999999111"),
]

for smartphone in catalog:
    print(f"{smartphone.mark} - {smartphone.model} - {smartphone.number}")
