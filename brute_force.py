import time
from itertools import combinations
import random

start_time = time.time()


def brute_force(n, budget, HW):

    best_battery = None
    best_combination = []

    for way in range(n):

        for comb in combinations(HW, way + 1):
            harga = sum([wc[0] for wc in comb])
            waktu = sum([wc[1] for wc in comb])
            if (best_battery is None or best_battery < waktu) and harga <= budget:
                best_battery = waktu
                best_combination = [0] * n
                for wc in comb:
                    best_combination[HW.index(wc)] = 1
    return best_battery, best_combination


HW = [(100000, 6), (122000, 5), (127000, 7),
      (150000, 9), (200000, 10), (240000, 11)]


#HR = []

#for n in range(30):
#    harga = random.randrange(100000, 240000, 2000)
#    lama = random.randrange(6, 11)
#    r = (harga, lama)
#    HR.append(r)

best = brute_force(len(HR), 400000, HR)
print(best)
print("--- %s seconds ---" % (time.time() - start_time))
