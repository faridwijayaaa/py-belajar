# Membuat program yang dapat menghitung total belanja

apple_price = 2 # harga buah apel per biji
money = 10 # jumlah uang yang dipunya

print('Selamat datang di toko buah serbagini')
apple_count = int(input('Mau berapa apel?: '));
total_price = apple_count * apple_price;

print('Anda akan membeli ' + str(apple_count) + ' apel')
print('Harga total adalah ' + str(total_price) + ' dolar')

# control Flow
if money > total_price:
    print('Anda telah membeli ' + str(apple_count) + ' apel')
    print('Sisa uang Anda adalah ' + str(money - total_price) + ' dolar')
elif money == total_price:
    print('Anda telah membeli ' + str(apple_count) + ' apel')
    print('Dompet Anda sekarang kosong')
else:
    print('Uang Anda tidak mencukupi')
    print('Anda tidak dapat membeli apel sebanyak itu')