import matplotlib.pyplot as plt  

x1 = [10, 11, 12, 13, 14, 15]
y1 = [388, 252, 1111, 1160, 7006, 7078]

x2 = [10, 11, 12, 13, 14, 15, 16]
y2 = [136, 116, 131, 104, 129, 146, 134]

plt.xlabel('number of residues')  
plt.ylabel('running time')  
plt.plot(x2, y2, 'r')
#plt.hold
plt.plot(x1, y1, 'b') 
plt.show()
