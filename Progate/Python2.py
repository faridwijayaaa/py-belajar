# di Python 2 ini saya mengembangkan aplikasi belanja dari Python1 sebelumnya

money = 20
items = {'apel':2, 'Jeruk':4, 'Manggis':6}

for item in items:
    print('----------------------------')
    print('Anda memiliki ' + str(money) + ' dolar di Dompet Anda')
    print('Harga setiap ' + item + ' ' + str(items[item]) + ' dolar')

    item_count = int(input('Mau berapa ' + item + '?: '))
    total_price = item_count * items[item]

    print('Anda akan membeli ' + str(item_count) + ' ' + item)
    print('Harga total adalah ' + str(total_price) + ' dolar')

    if money > total_price:
        print('Anda telah membeli ' + str(item_count) + ' ' + item)
        money -= total_price
    elif money == total_price:
        print('Anda telah membeli ' + str(item_count) + ' ' + item)
        print('Dompet Anda Kosong')
        money -= total_price
        break;
    else:
        print('Uang Anda tidak mencukupi')
        print('Anda tidak dapat membeli ' + item + ' sebanyak itu')
        break;

print('Uang Anda tinggal ' + str(money))