import random
import math
from tracemalloc import start

obj = 'ABCDE'
data = []
temp_data = []
data_nilai = []
fact_obj = math.factorial(len(obj))
lane = {}

# Menghitung jalur atau rute yang dilewati
def rute(r):
    j = 0
    k = 0
    while (j < len(r)):
        value = 0
        for k in range (4):
            if (r[k] == 'A' and r[k + 1] == 'B') or (r[k] == 'B' and r[k + 1] == 'A'):
                value = value + 7
            elif (r[k] == 'A' and r[k + 1] == 'C') or (r[k] == 'C' and r[k + 1] == 'A'):
                value = value + 10
            elif (r[k] == 'A' and r[k + 1] == 'D') or (r[k] == 'D' and r[k + 1] == 'A'):
                value = value + 9
            elif (r[k] == 'A' and r[k + 1] == 'E') or (r[k] == 'E' and r[k + 1] == 'A'):
                value = value + 6
            elif (r[k] == 'B' and r[k + 1] == 'C') or (r[k] == 'C' and r[k + 1] == 'B'):
                value = value + 5
            elif (r[k] == 'B' and r[k + 1] == 'D') or (r[k] == 'D' and r[k + 1] == 'B'):
                value = value + 3
            elif (r[k] == 'B' and r[k + 1] == 'E') or (r[k] == 'E' and r[k + 1] == 'B'):
                value = value + 8
            elif (r[k] == 'C' and r[k + 1] == 'D') or (r[k] == 'D' and r[k + 1] == 'C'):
                value = value + 6
            elif (r[k] == 'C' and r[k + 1] == 'E') or (r[k] == 'E' and r[k + 1] == 'C'):
                value = value + 4
            elif (r[k] == 'D' and r[k + 1] == 'E') or (r[k] == 'E' and r[k + 1] == 'D'):
                value = value + 7
        j = j + 1
    return value

# Membuat titik rute atau titik jalur
i = 0
while (i < fact_obj):
    #merandom jalur dari variable obj
    n = random.sample(obj, len(obj))
    j = 0
    boolean = False
    # Mencari jalur yang sama dan apabila sama maka akan dirandom ulang
    while (j < len(data) and boolean == False):
        if (data[j] == n):
                boolean = True
        else:
                j = j + 1

    if (boolean == True):
        continue
    else:
        # Menambahkan data rute
        data.append(n)
    i = i + 1

# Convert data List to data String  dan menambahkan panjang rute
data.sort(reverse=True)
print('------ Ascending Jalur ------')
print('No\t Lintasan\t Panjang')
for i in range (len(data)):
    data_nilai.append(rute(data[i]))
    temp_data.append("".join(data[i]))
    print(i+1,'\t ', temp_data[i], '\t ', data_nilai[i])

# Combine rute dengan panjangnya    
for i in range (len(temp_data)):
    lane[temp_data[i]] = [data_nilai[i]] 
    

# Sorting untuk mencari jalur terpendek 
print('')
sort_lane = sorted(lane.items(), key=lambda x:x[1])
x = 1
print("Jalur terpendek: ", sort_lane[0])
