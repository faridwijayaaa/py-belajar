# di Python 3 ini saya akan membuat program permainan suit tangan yaitu (Batu, Gunting, Kertas)

import random # call module

def print_hand(hand, name):
    hands = ['Batu', 'Kertas', 'Gunting']

    print(name + ' memilih: ' + hands[hand]);

def validate(hand):
    if hand < 0 or hand > 2:
        return False
    return True

def judge(player, computer):
    if player == computer:
        return 'Seri'
    elif (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
        return 'Kalah'
    else:
        return 'Menang'

print('Memulai permainan Kertas Gunting!')
player_name = input('Masukkan nama Anda?: ')

print('Pilih tangan (0. Batu, 1. Kertas, 2. Gunting)')
player_hand = int(input('Masukkan nomor (0-2): '))

if validate(player_hand):
    komputer_hand = random.randint(0,2)

    print_hand(player_hand, player_name)
    print_hand(komputer_hand, 'Komputer')
    
    result = judge(player_hand, komputer_hand)
    print('Hasil: ' + result)
else:
    print('Harap masukkan nomor yang benar')
