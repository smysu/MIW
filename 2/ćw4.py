def funkcja(temperature_type):
    if temperature_type < 1 or temperature_type > 3:
        return "Podałeś zły numer"
    temp = input("Podaj wartość do przekonwertowania\n")
    temp = int(temp)
    if temperature_type == 1:
        temp = (temp * 1.8) + 32
        return temp
    elif temperature_type == 2:
        temp = (temp * 1.8) + 491.67
        return temp
    elif temperature_type == 3:
        temp = temp + 273.15
        return temp


x = input("Podaj na jaką temp chcesz przekonwertować.\n1-"
          "Farenheit\n2-Renkine\n3-Kelvin\n")
x = int(x)
print(funkcja(x))
