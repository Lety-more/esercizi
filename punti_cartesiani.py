#dato un inzieme di 20 piunti su un piano cartesiamo,
#random compresi nell'intervallo 0,10. Calcolare il
#punto con ascissa massima e il punto con ordinata minima
import random

x=[]
y=[]

for i in range(0,20):
    y.append(random.randint(0,10))
    x.append(random.randint(0,10))

punti_cartesiano=[]
for i in range(0,20):
    punto=(random.randint(0,10),random.randint(0,10))
    punti_cartesiano.append(punto)
    
# come accedere alla x del primo numero
print(punti_cartesiano[0][0])
# come accedere alla y del primo numero
print(punti_cartesiano[0][1])