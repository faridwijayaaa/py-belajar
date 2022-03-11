from food import Food
from drink import Drink

# create list foods
food1 = Food('Roti Lapis', 5, 330)
food2 = Food('Kue Coklat', 4, 450)
food3 = Food('Kue Sus', 2, 180)

foods = [food1, food2, food3]

# create list drinks
drink1 = Drink('Kopi', 3, 180)
drink2 = Drink('Jus Jeruk', 2, 350)
drink3 = Drink('Esporesso', 3, 30)

drinks = [drink1, drink2, drink3]

# Menampilkan menu Makanan menggunakan (for)
print('------Makanan------')
idx = 0
for food_item in foods:
    print(str(idx) + '. ' + food_item.info())
    idx += 1

# Menampilkan menu Minuman menggunakan (for)
print('------Minuman------')
idx = 0
for drink_item in drinks:
    print(str(idx) + '. ' + drink_item.info())
    idx += 1

# Memilih menu menggunakan nomor menu
print('----------------------------')
selected_food = int(input('Masukkan nomor makanan: '))
selected_drink = int(input('Masukan nomor minuman: '))

# proses pengampilan data list pemilihan menu makanan dan minuman
selected_food = foods[selected_food]
selected_drink = drinks[selected_drink]

count = int(input('Mau berapa paket hidangan? (Diskon 10%' + 'untuk 3 atau lebih: '))

# Menghitung total harga dari pake pemesanan
result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)

print('Total harga adalah $' + str(result))