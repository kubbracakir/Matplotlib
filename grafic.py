import numpy as np
import matplotlib.pyplot as plt

gunler = [1,2,3,4,5]
uyku = [7,8,6,11,7]
yemek = [2,3,4,3,2]
calisma = [7,8,7,2,2]
eglenme = [8,5,7,8,13]
dilimler = [7,2,2,13]
aktiviteler = ['Uyku', 'Yemek', 'Çalışma', 'Eğlenme']
renkler = ['c', 'm', 'r', 'b']

plt.pie(dilimler,
        labels= aktiviteler,
        colors= renkler,
        startangle= 90,
        shadow= True,
        explode= (0,0.1,0,0),
        autopct= '%1.1f%%')

plt.title('Pasta Grafiği')
plt.show()