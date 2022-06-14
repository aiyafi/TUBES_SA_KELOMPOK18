import time
import random
start_time = time.time()


def dpcigarettesselector(n, budget, HW):

    def optimalsolution(i, j):
        if i == 0:
            return 0
        # memanggil solusi optimal dari subset sebelumnya
        harga, waktu = HW[i - 1]
        if harga > j:
            return optimalsolution(i - 1, j)
        else:
            # menentukan solusi optimal setiap subroblem
            return max(optimalsolution(i - 1, j), optimalsolution(i - 1, j - harga) + waktu)

    j = budget
    result = [0] * n
    for i in range(len(HW), 0, -1):
        if optimalsolution(i, j) != optimalsolution(i - 1, j):
            result[i - 1] = 1
            j -= HW[i - 1][0]
    return optimalsolution(len(HW), budget), result


HW = [(100000, 6), (122000, 5), (127000, 7),
      (150000, 9), (200000, 10), (240000, 11)]

# Untuk Melakukan Pengujian Effisiensi Algoritma
#HR = []

#for n in range(100):
#    harga = random.randrange(100000, 240000, 2000)
#    lama = random.randrange(6, 11)
#    r = (harga, lama)
#    HR.append(r)

best = dpcigarettesselector(len(HR), 400000, HR)

print(best)
print("--- %s seconds ---" % (time.time() - start_time))
