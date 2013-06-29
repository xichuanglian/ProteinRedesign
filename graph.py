import matplotlib.pyplot as plt  

x = []
y = []

a = 0
b = 1
for i in range(100):
    x.append(i)
    t = b
    b = a+b
    a = t
    y.append(t)

plt.xlabel('tiems')  
plt.ylabel('numbers')  
plt.plot(x, y, 'b')  
plt.show()
