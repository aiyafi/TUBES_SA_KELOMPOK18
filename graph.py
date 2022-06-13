import matplotlib.pyplot as plt

plt.figure('Analisis Kompleksitas')
plt.style.use('seaborn')

# x axis values
x = [0]
x2 = [0]
# corresponding y axis values
y = [0]
y2 = [0]

for (n) in range(64):
    x.append(n)
    y.append(n*n*n)

plt.plot(x, y, label="complexity of Exhaustive Search")

for n in range(64):
    x2.append(n)
    y2.append(n)

plt.plot(x2, y2, label="complexity of Dynamic Programing")

plt.xlabel('x - axis')

plt.ylabel('y - axis')

plt.title('Grafik Kompleksitas')


plt.legend()


plt.show()
