# 1) Luo luokka Restaurant. __init__() -metodin tulee saada luokan instanssia
# (eli oliota) luodessa kaksi attribuuttia: restaurant_name ja cuisine_type.
# Aseta attribuutit init:iin parametreiksi.
# 2) Luo luokasta instanssi (eli olio) nimeltään restaurant.
# 3) Luo metodi describe_restaurant() joka printtaa seuraavan:
# "Restaurant name:(parametrina saatu restaurant_name) :
# Cuisine type:(parametrina saatu cuisine_type)"
# 4) Printtaa instanssin restaurant_name -attribuutti (muuttuja)
# 5) Kutsu instanssin describe_restaurant()-metodia.
# 6) Luo 2 muutakin ravintola-instanssia haluamillasi nimillä.
# 7) Kutsu lisättyjen ravintoloiden describe_restaurant()-metodeita.

class Restaurant:
    # dunder-metodi (lyhenne down-underscore) / magic-metodi
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant name:" + self.restaurant_name +
              ",C..:" + self.cuisine_type)


restaurant = Restaurant("Pizzeria Pollo", "Pizzeria")
print(restaurant.restaurant_name)
restaurant.describe_restaurant()
restaurant2 = Restaurant("Olive Garden", "Fine-dining")
restaurant3 = Restaurant("MegaKebab", "Turkish")
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
